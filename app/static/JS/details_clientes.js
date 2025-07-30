document.addEventListener('DOMContentLoaded', function () {
    // Variables de estado
    let currentTelefonoId = null;
    let currentPrestamoId = null;

    // Elementos del DOM
    const form = document.getElementById('cliente-form');
    const inputs = form.querySelectorAll('input, select, textarea');
    const btnAddTelefono = document.getElementById('btn-add-telefono');
    const btnAddArchivo = document.getElementById('btn-add-archivo');
    const btnAddPrestamo = document.getElementById('btn-add-prestamo');

    // Modal de teléfono
    const telefonoModal = new bootstrap.Modal(document.getElementById('telefonoModal'));
    const telefonoForm = document.getElementById('telefono-form');
    const guardarTelefonoBtn = document.getElementById('guardar-telefono');

    // Modal de archivo
    const archivoModal = new bootstrap.Modal(document.getElementById('archivoModal'));
    const archivoForm = document.getElementById('archivo-form');
    const guardarArchivoBtn = document.getElementById('guardar-archivo');

    // Modal de préstamo
    const prestamoModal = new bootstrap.Modal(document.getElementById('prestamoModal'));
    const prestamoForm = document.getElementById('prestamo-form');
    const guardarPrestamoBtn = document.getElementById('guardar-prestamo');

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
})