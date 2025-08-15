import * as vscode from 'vscode';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';
import { spawn } from 'child_process';

interface AnalysisServerResult {
    success: boolean;
    symbols?: any[];
    ast?: any;
    error?: string;
    details?: string;
}

interface PythonScriptExecutionResult {
    stdout: string;
    stderr: string;
    code: number;
}

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

    async createDebugAdapterDescriptor(session: vscode.DebugSession, executable: vscode.DebugAdapterExecutable | undefined): Promise<vscode.ProviderResult<vscode.DebugAdapterDescriptor>> {
        const compilerBridgePath = vscode.Uri.joinPath(session.workspace.uri, 'espanoloo_compiler', 'compiler_bridge.py').fsPath;
        const programPath = session.configuration.program;

        if (!fs.existsSync(compilerBridgePath)) {
            vscode.window.showErrorMessage('No se encontró el archivo compiler_bridge.py. Asegúrate de que el compilador EspañolOO esté en la raíz del workspace.');
            return undefined;
        }

        if (!fs.existsSync(programPath)) {
            vscode.window.showErrorMessage(`No se encontró el archivo de programa: ${programPath}`);
            return undefined;
        }

        try {
            // Step 1: Compile the EspañolOO program to Python
            const compileRawResult = await this.runPythonScript(compilerBridgePath, programPath);

            if (compileRawResult.code !== 0) {
                vscode.window.showErrorMessage(`Error de compilación de EspañolOO: Proceso Python terminó con código ${compileRawResult.code}. Stderr: ${compileRawResult.stderr}`);
                return undefined;
            }

            const analysisResult: AnalysisServerResult = JSON.parse(compileRawResult.stdout);

            if (analysisResult.error) {
                vscode.window.showErrorMessage(`Error de compilación de EspañolOO: ${analysisResult.error}. Detalles: ${analysisResult.details}`);
                return undefined;
            }

            // Step 2: Execute the generated Python code
            const generatedPythonRawResult = await this.runPythonScript(compilerBridgePath, JSON.stringify(analysisResult.ast));

            if (generatedPythonRawResult.code !== 0) {
                vscode.window.showErrorMessage(`Error de ejecución del código Python generado: Proceso Python terminó con código ${generatedPythonRawResult.code}. Stderr: ${generatedPythonRawResult.stderr}`);
                return undefined;
            }

            const pythonCode = generatedPythonRawResult.stdout;

            // For now, just show the output in the debug console
            vscode.debug.activeDebugConsole.appendLine(pythonCode);

            // In a real scenario, you would launch a Python debugger here
            // For simplicity, we're just showing output.
            return new vscode.DebugAdapterInlineImplementation({
                type: 'python',
                request: 'launch',
                program: pythonCode, // This would be the path to the generated .py file
                console: 'integratedTerminal'
            });

        } catch (error: any) {
            vscode.window.showErrorMessage(`Error durante la preparación de la depuración: ${error.message}`);
            return undefined;
        }
    }

    private runPythonScript(scriptPath: string, input: string): Promise<PythonScriptExecutionResult> {
        return new Promise((resolve, reject) => {
            const pythonPath = vscode.workspace.getConfiguration('python').get<string>('defaultInterpreterPath') || 'python';
            const pythonProcess = spawn(pythonPath, [scriptPath]);
            
            let stdout = '';
            let stderr = '';

            pythonProcess.stdout.on('data', (data: string) => {
                stdout += data.toString();
            });

            pythonProcess.stderr.on('data', (data: string) => {
                stderr += data.toString();
            });

            pythonProcess.on('close', (code: number) => {
                resolve({ stdout, stderr, code });
            });

            pythonProcess.on('error', (err: Error) => {
                reject(err); // Reject with the actual error
            });

            pythonProcess.stdin.write(input);
            pythonProcess.stdin.end();
        });
    }
}