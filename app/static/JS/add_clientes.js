// Variables para almacenar los datos temporales
let correos = [];
let telefonos = [];
let archivos = [];

// Función para agregar correo
document.getElementById('agregar-correo').addEventListener('click', function() {
    const email = document.getElementById('correo-email').value;
    const password = document.getElementById('correo-password').value;
    const localizacion = document.getElementById('correo-localizacion').value;
    
    if (!email) {
    alert('El correo electrónico es obligatorio');
    return;
    }
    
    correos.push({
    email: email,
    password: password,
    localizacion: localizacion
    });
    
    actualizarListaCorreos();
    document.getElementById('correo-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('correoModal')).hide();
});

// Función para agregar teléfono
document.getElementById('agregar-telefono').addEventListener('click', function() {
    const numero = document.getElementById('telefono-numero').value;
    const nombre = document.getElementById('telefono-nombre').value;
    const parentesco = document.getElementById('telefono-parentesco').value;
    
    if (!numero || !nombre || !parentesco) {
    alert('Todos los campos son obligatorios');
    return;
    }
    
    telefonos.push({
    numero: numero,
    nombre: nombre,
    parentesco: parentesco
    });
    
    actualizarListaTelefonos();
    document.getElementById('telefono-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('telefonoModal')).hide();
});

// Función para subir archivo
document.getElementById('subir-archivo').addEventListener('click', function() {
    const tipo = document.getElementById('archivo-tipo').value;
    const nombre = document.getElementById('archivo-nombre').value;
    const fileInput = document.getElementById('archivo-file');
    
    if (!tipo || !nombre || !fileInput.files.length) {
    alert('Todos los campos son obligatorios');
    return;
    }
    
    // Aquí iría la lógica para subir a Cloudinary
    // Por ahora solo almacenamos la información básica
    archivos.push({
    tipo: tipo,
    nombre: nombre,
    archivo: fileInput.files[0].name,
    file: fileInput.files[0] // Para el envío real del formulario
    });
    
    actualizarListaArchivos();
    document.getElementById('archivo-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('archivoModal')).hide();
});

// Función para actualizar la lista de correos en la UI
function actualizarListaCorreos() {
    const container = document.getElementById('correos-container');
    
    if (correos.length === 0) {
    container.innerHTML = '<div class="alert alert-info">No se han agregado correos electrónicos aún.</div>';
    return;
    }
    
    let html = '<div class="table-responsive"><table class="table"><thead><tr><th>Correo</th><th>Localización</th><th>Acciones</th></tr></thead><tbody>';
    
    correos.forEach((correo, index) => {
    html += `
        <tr>
        <td>${correo.email}</td>
        <td>${correo.localizacion || 'N/A'}</td>
        <td>
            <button class="btn btn-edit-small" onclick="editarCorreo(${index})">
            <i class="fas fa-edit"></i>
            </button>
            <button class="btn btn-cancel-small" onclick="eliminarCorreo(${index})">
            <i class="fas fa-trash"></i>
            </button>
        </td>
        </tr>
    `;
    });
    
    html += '</tbody></table></div>';
    
    // Agregar campos ocultos para cada correo
    correos.forEach((correo, index) => {
    html += `
        <input type="hidden" name="correos[${index}][corr_nombre]" value="${correo.email}">
        <input type="hidden" name="correos[${index}][corr_contraseña]" value="${correo.password || ''}">
        <input type="hidden" name="correos[${index}][corr_localizacion]" value="${correo.localizacion || ''}">
    `;
    });
    
    container.innerHTML = html;
}

// Función para actualizar la lista de teléfonos en la UI
function actualizarListaTelefonos() {
    const container = document.getElementById('telefonos-container');
    
    if (telefonos.length === 0) {
    container.innerHTML = '<div class="alert alert-info">No se han agregado teléfonos aún.</div>';
    return;
    }
    
    let html = '<div class="table-responsive"><table class="table"><thead><tr><th>Número</th><th>Nombre</th><th>Parentesco</th><th>Acciones</th></tr></thead><tbody>';
    
    telefonos.forEach((telefono, index) => {
    html += `
        <tr>
        <td>${telefono.numero}</td>
        <td>${telefono.nombre}</td>
        <td>${telefono.parentesco}</td>
        <td>
            <button class="btn btn-edit-small" onclick="editarTelefono(${index})">
            <i class="fas fa-edit"></i>
            </button>
            <button class="btn btn-cancel-small" onclick="eliminarTelefono(${index})">
            <i class="fas fa-trash"></i>
            </button>
        </td>
        </tr>
    `;
    });
    
    html += '</tbody></table></div>';
    
    // Agregar campos ocultos para cada teléfono
    telefonos.forEach((telefono, index) => {
    html += `
        <input type="hidden" name="telefonos[${index}][tel_telefono]" value="${telefono.numero}">
        <input type="hidden" name="telefonos[${index}][tel_nombre]" value="${telefono.nombre}">
        <input type="hidden" name="telefonos[${index}][tel_parentesco]" value="${telefono.parentesco}">
    `;
    });
    
    container.innerHTML = html;
}

// Función para actualizar la lista de archivos en la UI
function actualizarListaArchivos() {
    const container = document.getElementById('archivos-container');
    
    if (archivos.length === 0) {
    container.innerHTML = '<div class="alert alert-info">No se han subido documentos aún.</div>';
    return;
    }
    
    let html = '<div class="table-responsive"><table class="table"><thead><tr><th>Tipo</th><th>Nombre</th><th>Archivo</th><th>Acciones</th></tr></thead><tbody>';
    
    archivos.forEach((archivo, index) => {
    html += `
        <tr>
        <td>${document.getElementById('archivo-tipo').options[archivo.tipo-1].text}</td>
        <td>${archivo.nombre}</td>
        <td>${archivo.archivo}</td>
        <td>
            <button class="btn btn-edit-small" onclick="editarArchivo(${index})">
            <i class="fas fa-edit"></i>
            </button>
            <button class="btn btn-cancel-small" onclick="eliminarArchivo(${index})">
            <i class="fas fa-trash"></i>
            </button>
        </td>
        </tr>
    `;
    });
    
    html += '</tbody></table></div>';
    
    // Agregar campos ocultos para cada archivo
    archivos.forEach((archivo, index) => {
    html += `
        <input type="hidden" name="archivos[${index}][ta_id]" value="${archivo.tipo}">
        <input type="hidden" name="archivos[${index}][arch_nombre]" value="${archivo.nombre}">
    `;
    });
    
    container.innerHTML = html;
}

// Funciones para editar/eliminar elementos (simplificadas)
function editarCorreo(index) {
    const correo = correos[index];
    document.getElementById('correo-email').value = correo.email;
    document.getElementById('correo-password').value = correo.password || '';
    document.getElementById('correo-localizacion').value = correo.localizacion || '';
    
    correos.splice(index, 1);
    actualizarListaCorreos();
    
    const modal = new bootstrap.Modal(document.getElementById('correoModal'));
    modal.show();
}

function eliminarCorreo(index) {
    if (confirm('¿Estás seguro de eliminar este correo?')) {
    correos.splice(index, 1);
    actualizarListaCorreos();
    }
}

function editarTelefono(index) {
    const telefono = telefonos[index];
    document.getElementById('telefono-numero').value = telefono.numero;
    document.getElementById('telefono-nombre').value = telefono.nombre;
    document.getElementById('telefono-parentesco').value = telefono.parentesco;
    
    telefonos.splice(index, 1);
    actualizarListaTelefonos();
    
    const modal = new bootstrap.Modal(document.getElementById('telefonoModal'));
    modal.show();
}

function eliminarTelefono(index) {
    if (confirm('¿Estás seguro de eliminar este teléfono?')) {
    telefonos.splice(index, 1);
    actualizarListaTelefonos();
    }
}

function editarArchivo(index) {
    const archivo = archivos[index];
    document.getElementById('archivo-tipo').value = archivo.tipo;
    document.getElementById('archivo-nombre').value = archivo.nombre;
    
    archivos.splice(index, 1);
    actualizarListaArchivos();
    
    const modal = new bootstrap.Modal(document.getElementById('archivoModal'));
    modal.show();
}

function eliminarArchivo(index) {
    if (confirm('¿Estás seguro de eliminar este archivo?')) {
    archivos.splice(index, 1);
    actualizarListaArchivos();
    }
}
