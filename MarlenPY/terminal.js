let pyodideReadyPromise = null;
const promptHTML = '<span class="terminal-user">marlen@python-dev</span>:<span class="terminal-path">~/proyecto</span>$ ';

// Estructura de archivos
const ARCHIVOS = {
    'parametros': {
        titulo: 'Parámetros y Argumentos',
        path: './parametros_argumentos/',
        files: ['paso_por_referencia.py', 'paso_por_valor.py', 'por_defecto.py', 'por_posicion.py']
    },
    'retorno': {
        titulo: 'Retorno de Valores',
        path: './retorno_de_valores/',
        files: ['retorno_de_colecciones.py', 'retorno_implicito.py', 'retorno_multiple.py', 'retorno_unico.py']
    }
};

let archivoActual = {
    nombre: 'paso_por_referencia.py',
    ruta: './parametros_argumentos/paso_por_referencia.py',
    categoria: 'Parámetros y Argumentos'
};

async function initPyodide() {
    if (!pyodideReadyPromise) {
        try {
            pyodideReadyPromise = loadPyodide();
            await pyodideReadyPromise;
        } catch (err) {
            console.error("Error al cargar Pyodide", err);
        }
    }
}

async function cargarArchivo(ruta) {
    const editor = document.getElementById('python-editor');
    if (!editor) return;
    try {
        const response = await fetch(ruta);
        if (!response.ok) throw new Error('No se pudo leer el archivo: ' + ruta);
        const code = await response.text();
        editor.value = code;
        updateEditorHighlight();
    } catch (err) {
        editor.value = "# Error al cargar el archivo: " + err.message;
        updateEditorHighlight();
    }
}

window.updateEditorHighlight = function() {
    const editor = document.getElementById('python-editor');
    const highlight = document.getElementById('editor-highlight');
    if (!editor || !highlight) return;

    let code = editor.value;
    
    let highlighted = code
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/(#.*)/g, '<span class="code-comment">$1</span>');
    
    highlight.innerHTML = highlighted + (code.endsWith('\n') ? '\n ' : ' ');
    
    highlight.scrollTop = editor.scrollTop;
    highlight.scrollLeft = editor.scrollLeft;
};

document.addEventListener('DOMContentLoaded', () => {
    const editor = document.getElementById('python-editor');
    const highlight = document.getElementById('editor-highlight');
    if (editor && highlight) {
        editor.onscroll = () => {
            highlight.scrollTop = editor.scrollTop;
            highlight.scrollLeft = editor.scrollLeft;
        };
    }
});

// Funciones globales para el HTML
window.toggleFiles = function(categoria, btn) {
    const container = document.getElementById('file-list-container');
    const items = document.getElementById('file-items');
    
    // Si ya está abierto para esta categoría, lo cerramos
    if (container.style.display === 'block' && btn.classList.contains('active')) {
        closeFileSelector();
        return;
    }

    if (!ARCHIVOS[categoria]) return;

    // Actualizar botones activos
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // Llenar archivos
    items.innerHTML = '';
    ARCHIVOS[categoria].files.forEach(file => {
        const div = document.createElement('div');
        div.className = 'file-item';
        if (file === archivoActual.nombre) div.classList.add('active');
        div.innerText = file;
        div.onclick = (e) => {
            e.stopPropagation();
            seleccionarArchivo(file, ARCHIVOS[categoria].path + file, ARCHIVOS[categoria].titulo);
        };
        items.appendChild(div);
    });

    // Posicionar el dropdown justo debajo del botón
    const btnRect = btn.getBoundingClientRect();
    const navRect = btn.parentElement.getBoundingClientRect();
    
    // Offset relativo al contenedor parent (category-nav)
    container.style.left = (btnRect.left - navRect.left) + "px";
    container.style.top = (btnRect.bottom - navRect.top + 2) + "px";
    container.style.display = 'block';
};

window.closeFileSelector = function() {
    document.getElementById('file-list-container').style.display = 'none';
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
};

function seleccionarArchivo(nombre, ruta, catNombre) {
    archivoActual = { nombre, ruta, categoria: catNombre };
    
    // Actualizar UI
    document.querySelector('.terminal-container h2').innerText = catNombre;
    document.querySelector('.terminal-container h3').innerHTML = `Archivo: <code>${nombre}</code>`;
    
    cargarArchivo(ruta);
    closeFileSelector();
    limpiarTerminal();
}

// Cerrar dropdown al hacer click fuera
document.addEventListener('click', (e) => {
    const container = document.getElementById('file-list-container');
    if (container && container.style.display === 'block') {
        if (!e.target.closest('.category-nav')) {
            closeFileSelector();
        }
    }
});

window.recargarCodigo = function() {
    cargarArchivo(archivoActual.ruta);
};

window.ejecutarTerminal = async function() {
    const output = document.getElementById('terminal-output');
    const promptStart = document.getElementById('prompt-start');
    const btnRun = document.getElementById('btn-run');
    const editor = document.getElementById('python-editor');
    
    if (!editor || !output) return;

    if (promptStart) promptStart.style.display = 'none';
    
    const block = document.createElement('div');
    const cmdSpan = document.createElement('span');
    cmdSpan.className = 'terminal-cmd';
    cmdSpan.innerHTML = promptHTML + `python3 MarlenPY/${archivoActual.ruta.replace('./', '')}`;
    
    const resSpan = document.createElement('span');
    resSpan.className = 'terminal-res';
    resSpan.innerHTML = '<span class="terminal-running">(Ejecutando...)</span>';
    
    block.appendChild(cmdSpan);
    block.appendChild(resSpan);
    output.appendChild(block);
    output.scrollTop = output.scrollHeight;
    
    if (btnRun) {
        btnRun.style.pointerEvents = 'none';
        btnRun.style.opacity = '0.5';
    }

    try {
        let pyodide = await pyodideReadyPromise;
        const codeToRun = editor.value;
        
        pyodide.runPython(`
import sys
import io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
        `);
        
        pyodide.runPython(codeToRun);
        
        let stdout = pyodide.runPython("sys.stdout.getvalue()");
        let stderr = pyodide.runPython("sys.stderr.getvalue()");
        
        if (stderr) {
            resSpan.innerHTML = '<span style="color: #ef4444;">Error de Python:<br>' + stderr.replace(/\n/g, '<br>') + '</span>';
        } else if (stdout) {
            resSpan.innerHTML = '';
            const lines = stdout.split('\n');
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].trim() === '' && i === lines.length - 1) continue;
                const lineDiv = document.createElement('div');
                lineDiv.innerText = lines[i];
                resSpan.appendChild(lineDiv);
                output.scrollTop = output.scrollHeight;
                await new Promise(resolve => setTimeout(resolve, 500));
            }
        } else {
            resSpan.innerHTML = '<em>(Sin salida)</em>';
        }

    } catch (err) {
        resSpan.innerHTML = '<span style="color: #ef4444;">Error de Python:<br>' + err.toString().replace(/\n/g, '<br>') + '</span>';
    } finally {
        if (btnRun) {
            btnRun.style.pointerEvents = 'auto';
            btnRun.style.opacity = '1';
        }
        
        const newPrompt = document.createElement('span');
        newPrompt.innerHTML = promptHTML + '<span class="terminal-cursor"></span>';
        output.appendChild(newPrompt);
        output.scrollTop = output.scrollHeight;
    }
}

window.limpiarTerminal = function() {
    const output = document.getElementById('terminal-output');
    if (output) {
        output.innerHTML = '<span id="prompt-start">' + promptHTML + '<span class="terminal-cursor"></span></span>';
    }
};

// Inicialización
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById('python-editor')) {
        initPyodide();
        // Cargar archivo por defecto sin abrir el selector
        archivoActual = { 
            nombre: 'paso_por_referencia.py', 
            ruta: './parametros_argumentos/paso_por_referencia.py', 
            categoria: 'Parámetros y Argumentos' 
        };
        cargarArchivo(archivoActual.ruta);
    }
});
