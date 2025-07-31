document.addEventListener('DOMContentLoaded', function () {
    // Variables de estado
    let currentTelefonoId = null;
    let currentPrestamoId = null;

    // Elementos del DOM
    const btnAddTelefono = document.getElementById('btn-add-telefono');
    const btnAddArchivo = document.getElementById('btn-add-archivo');
    const btnAddPrestamo = document.getElementById('btn-add-prestamo');

    // Modal de teléfono
    const telefonoModal = new bootstrap.Modal(document.getElementById('telefonoModal'));
    const telefonoForm = document.getElementById('telefono-form');

    // Modal de archivo
    const archivoModal = new bootstrap.Modal(document.getElementById('archivoModal'));
    const archivoForm = document.getElementById('archivo-form');

    // Modal de préstamo
    const prestamoModal = new bootstrap.Modal(document.getElementById('prestamoModal'));
    const prestamoForm = document.getElementById('prestamo-form');

    // Eventos para teléfonos
    btnAddTelefono.addEventListener('click', function () {
        currentTelefonoId = null;
        telefonoForm.reset();
        document.getElementById('telefonoModalLabel').textContent = 'Agregar Teléfono';
        telefonoModal.show();
    });

    // Eventos para archivos (similar a teléfonos)
    btnAddArchivo.addEventListener('click', function () {
        currentArchivoId = null;
        archivoForm.reset();
        document.getElementById('archivoModalLabel').textContent = 'Subir Documento';
        archivoModal.show();
    });

    // Eventos para préstamos (similar a teléfonos)
    btnAddPrestamo.addEventListener('click', function () {
        currentPrestamoId = null;
        prestamoForm.reset();
        document.getElementById('prestamoModalLabel').textContent = 'Agregar Préstamo';
        prestamoModal.show();
    });
    
    const textarea = document.getElementById('observaciones-textarea');
    const btnEditar = document.getElementById('editar-observaciones');
    const btnGuardar = document.getElementById('guardar-observaciones');
    const btnCancelar = document.getElementById('cancelar-observaciones');
    let valorOriginal = textarea.value;  // Guarda el valor inicial
    
    // Al hacer clic en "Editar"
    btnEditar.addEventListener('click', function() {
        textarea.readOnly = false;
        textarea.focus();
        btnEditar.classList.add('d-none');
        btnGuardar.classList.remove('d-none');
        btnCancelar.classList.remove('d-none');
    });
    
    // Al hacer clic en "Cancelar"
    btnCancelar.addEventListener('click', function() {
        textarea.value = valorOriginal;
        textarea.readOnly = true;
        btnEditar.classList.remove('d-none');
        btnGuardar.classList.add('d-none');
        btnCancelar.classList.add('d-none');
    });

    document.querySelector('textarea[name="observaciones"]').addEventListener('input', function(e) {
        const charCount = e.target.value.length;
        document.getElementById('char-count').textContent = charCount;
    }); 
})

function togglePassword() {
    const passwordField = document.getElementById('correo-password');
    const toggleIcon = document.querySelector('.password-toggle i');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleIcon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordField.type = 'password';
        toggleIcon.classList.replace('fa-eye-slash', 'fa-eye');
    }
}

