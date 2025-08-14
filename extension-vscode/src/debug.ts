import * as vscode from 'vscode';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';
import { spawn } from 'child_process';

/**
 * Resuelve la configuración de depuración para EspañolOO.
 * Esta clase actúa como un paso de "pre-lanzamiento".
 * 1. Toma el código EspañolOO del archivo activo.
 * 2. Llama a los scripts del compilador para producir código Python.
 * 3. Guarda el código Python en un archivo temporal.
 * 4. Modifica la configuración de lanzamiento para que VS Code inicie el depurador de Python estándar sobre ese archivo temporal.
 */
export class EspanolOODebugConfigurationProvider implements vscode.DebugConfigurationProvider {

    constructor(private context: vscode.ExtensionContext) { }

    async resolveDebugConfiguration(folder: vscode.WorkspaceFolder | undefined, config: vscode.DebugConfiguration, token?: vscode.CancellationToken): Promise<vscode.DebugConfiguration | undefined> {

        // Si no hay un programa definido, no podemos continuar.
        if (!config.program) {
            return vscode.window.showInformationMessage("No se puede iniciar el depurador: el atributo 'program' no está definido en launch.json.").then(() => {
                return undefined;
            });
        }

        const activeEditor = vscode.window.activeTextEditor;
        if (!activeEditor || activeEditor.document.uri.toString() !== config.program) {
             await vscode.window.showErrorMessage('Por favor, abra el archivo EspañolOO que desea depurar y asegúrese de que coincida con el atributo "program" en su launch.json.');
             return undefined;
        }
        
        const espanolooCode = activeEditor.document.getText();
        const baseName = path.basename(activeEditor.document.fileName, '.eoo');
        const tempDir = path.join(os.tmpdir(), 'espanoloo_debug');

        try {
            // Asegurarse de que el directorio temporal exista
            if (!fs.existsSync(tempDir)) {
                fs.mkdirSync(tempDir);
            }

            // 1. Llamar a analysis_server.py para obtener el AST en formato JSON
            const analysisServerPath = path.join(this.context.extensionPath, 'espanoloo_compiler', 'analysis_server.py');
            const analysisResult = await this.runPythonScript(analysisServerPath, espanolooCode);

            if (analysisResult.error) {
                vscode.window.showErrorMessage(`Error en el análisis del código EspañolOO: ${analysisResult.error} - ${analysisResult.details || ''}`);
                return undefined;
            }

            // 2. Llamar a compiler_bridge.py para generar código Python desde el AST JSON
            const compilerBridgePath = path.join(this.context.extensionPath, 'espanoloo_compiler', 'compiler_bridge.py');
            // Pasamos el AST completo, no solo los símbolos
            const generatedPythonResult = await this.runPythonScript(compilerBridgePath, JSON.stringify(analysisResult.ast));

            if (generatedPythonResult.error) {
                vscode.window.showErrorMessage(`Error en la generación de código Python: ${generatedPythonResult.error} - ${generatedPythonResult.details || ''}`);
                return undefined;
            }
            
            const pythonCode = generatedPythonResult.output;

            // 3. Guardar el código Python generado en un archivo temporal
            const tempPythonFile = path.join(tempDir, `${baseName}_debug.py`);
            fs.writeFileSync(tempPythonFile, pythonCode);

            // 4. Modificar la configuración de lanzamiento para usar el depurador de Python
            config.type = 'python';
            config.request = 'launch';
            config.program = tempPythonFile; // Apuntar al archivo temporal
            config.justMyCode = config.justMyCode !== undefined ? config.justMyCode : false; // Permitir entrar en código que no es del usuario
            config.name = `Depurar (EspañolOO: ${baseName})`; // Nombre dinámico para la sesión de depuración

            return config;

        } catch (error: any) {
            vscode.window.showErrorMessage(`Error durante la preparación de la depuración: ${error.message}`);
            return undefined;
        }
    }

    private runPythonScript(scriptPath: string, input: string): Promise<{output: string, error?: string, details?: string}> {
        return new Promise((resolve, reject) => {
            const pythonPath = vscode.workspace.getConfiguration('python').get<string>('defaultInterpreterPath') || 'python';
            const pythonProcess = spawn(pythonPath, [scriptPath]);
            
            let stdout = '';
            let stderr = '';

            pythonProcess.stdout.on('data', (data) => {
                stdout += data.toString();
            });

            pythonProcess.stderr.on('data', (data) => {
                stderr += data.toString();
            });

            pythonProcess.on('close', (code) => {
                if (code === 0) {
                    // Intentar parsear como JSON, si falla, es salida de texto plano (código generado)
                    try {
                        resolve(JSON.parse(stdout));
                    } catch (e) {
                        resolve({ output: stdout });
                    }
                } else {
                    // Si hay un error, el stderr es el mensaje principal
                    reject(new Error(`El script de Python (${path.basename(scriptPath)}) finalizó con el código ${code}. Error: ${stderr}`));
                }
            });

            pythonProcess.on('error', (err) => {
                reject(new Error(`No se pudo iniciar el proceso de Python. Asegúrese de que '${pythonPath}' sea correcto. Error: ${err.message}`));
            });

            pythonProcess.stdin.write(input);
            pythonProcess.stdin.end();
        });
    }
}