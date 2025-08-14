import * as vscode from 'vscode';
import { spawn } from 'child_process'; // Import child_process

export class EspanolOOCompletionProvider implements vscode.CompletionItemProvider {
    async provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken, context: vscode.CompletionContext): Promise<vscode.ProviderResult<vscode.CompletionItem[] | vscode.CompletionList>> {
        const keywords = [
            "clase", "funcion", "si", "sino", "mientras", "para", "retornar",
            "publico", "privado", "protegido", "nuevo", "este", "super",
            "hereda", "implementa", "abstracto", "interfaz", "intentar",
            "atrapar", "finalmente", "lanzar", "afirmar", "nulo",
            "verdadero", "falso", "entero", "decimal", "cadena", "booleano",
            "y", "o", "no", "constante", "en"
        ];

        let completionItems: vscode.CompletionItem[] = keywords.map(keyword => {
            const item = new vscode.CompletionItem(keyword, vscode.CompletionItemKind.Keyword);
            item.detail = "Palabra reservada de EspañolOO";
            return item;
        });

        // Get the full document text
        const codeText = document.getText();

        try {
            // Call the Python analysis server
            const pythonProcess = spawn('python', [
                vscode.Uri.joinPath(context.extensionUri, 'espanoloo_compiler', 'analysis_server.py').fsPath
            ]);

            let stdout = '';
            let stderr = '';

            pythonProcess.stdout.on('data', (data) => {
                stdout += data.toString();
            });

            pythonProcess.stderr.on('data', (data) => {
                stderr += data.toString();
            });

            await new Promise<void>((resolve, reject) => {
                pythonProcess.stdin.write(codeText);
                pythonProcess.stdin.end(); // Close stdin to signal end of input

                pythonProcess.on('close', (code) => {
                    if (code === 0) {
                        resolve();
                    } else {
                        reject(new Error(`Python process exited with code ${code}. Stderr: ${stderr}`));
                    }
                });

                pythonProcess.on('error', (err) => {
                    reject(err);
                });
            });

            const analysisResult = JSON.parse(stdout);

            if (analysisResult.success && analysisResult.symbols) {
                analysisResult.symbols.forEach((symbol: any) => {
                    let kind: vscode.CompletionItemKind;
                    switch (symbol.type) {
                        case 'clase':
                            kind = vscode.CompletionItemKind.Class;
                            break;
                        case 'funcion':
                            kind = vscode.CompletionItemKind.Function;
                            break;
                        case 'metodo': // Assuming 'metodo' type will be returned for class methods
                            kind = vscode.CompletionItemKind.Method;
                            break;
                        case 'entero':
                        case 'decimal':
                        case 'cadena':
                        case 'booleano':
                        case 'nulo':
                            kind = vscode.CompletionItemKind.TypeParameter; // Or appropriate type
                            break;
                        default:
                            kind = vscode.CompletionItemKind.Variable; // Default for other types like 'variable'
                            break;
                    }
                    const item = new vscode.CompletionItem(symbol.name, kind);
                    item.detail = `Símbolo de EspañolOO (${symbol.type})`;
                    completionItems.push(item);
                });
            } else if (analysisResult.error) {
                console.error("Error from analysis server:", analysisResult.error, analysisResult.details);
                // Optionally, show a message to the user
            }

        } catch (error: any) {
            console.error("Failed to run analysis server:", error.message);
            // Optionally, show an error message to the user
        }

        return new vscode.CompletionList(completionItems, true);
    }
}
