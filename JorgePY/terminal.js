let pyodideReadyPromise = null;
const promptHTML = '<span class="terminal-user">jorge@python-dev</span>:<span class="terminal-path">~/proyecto</span>$ ';

// Estructura de archivos
const ARCHIVOS = {
    'especiales': {
        titulo: 'Parámetros Especiales',
        path: './parametros_especiales/',
        files: ['especiales.py', 'especiales2.py', 'especiales3.py']
    }
};

let archivoActual = {
    nombre: 'especiales.py',
    ruta: './parametros_especiales/especiales.py',
    categoria: 'Parámetros Especiales'
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
        editor.style.display = 'block';
    } catch (err) {
        editor.value = "# Error al cargar el archivo: " + err.message;
        editor.style.display = 'block';
    }
}

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
    cmdSpan.innerHTML = promptHTML + `python3 JorgePY/${archivoActual.ruta.replace('./', '')}`;
    
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
        
        let finalOutput = stdout;
        if (stderr) finalOutput += "\n[Error]\n" + stderr;
        
        resSpan.innerHTML = finalOutput ? finalOutput.replace(/\n/g, '<br>') : '<em>(Sin salida)</em>';

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
};

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
        // Cargar archivo por defecto
        archivoActual = { 
            nombre: 'especiales.py', 
            ruta: './parametros_especiales/especiales.py', 
            categoria: 'Parámetros Especiales' 
        };
        seleccionarArchivo(archivoActual.nombre, archivoActual.ruta, archivoActual.categoria);
    }
});
