import * as vscode from 'vscode';
import { EspanolOOCompletionProvider } from './completion';
import { EspanolOODebugConfigurationProvider } from './debug';

export function activate(context: vscode.ExtensionContext) {
    console.log('La extensión "EspañolOO" está activa.');

    // Registrar el proveedor de autocompletado
    const selector = { scheme: 'file', language: 'espanoloo' };
    context.subscriptions.push(
        vscode.languages.registerCompletionItemProvider(
            selector,
            new EspanolOOCompletionProvider(context), // Pass context here
            '.' // Caracteres que disparan el autocompletado
        )
    );

    // Registrar el proveedor de configuración de depuración
    context.subscriptions.push(
        vscode.debug.registerDebugAdapterDescriptorFactory('espanoloo', new EspanolOODebugAdapterDescriptorFactory(context))
    );
}

export function deactivate() {
    console.log('La extensión "EspañolOO" ha sido desactivada.');
}