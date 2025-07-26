document.addEventListener('DOMContentLoaded', function () {
    // Variables de estado
    let editMode = false;
    let currentTelefonoId = null;
    let currentArchivoId = null;
    let currentPrestamoId = null;

    // Elementos del DOM
    const btnEdit = document.getElementById('btn-edit');
    const btnSave = document.getElementById('btn-save');
    const btnCancel = document.getElementById('btn-cancel');
    const form = document.getElementById('cliente-form');
    const inputs = form.querySelectorAll('input, select, textarea');
    const btnAddTelefono = document.getElementById('btn-add-telefono');
    const btnAddArchivo = document.getElementById('btn-add-archivo');
    const btnAddPrestamo = document.getElementById('btn-add-prestamo');
    const btnEditTelefonos = document.querySelectorAll('.btn-edit-telefono');
    const btnDeleteTelefonos = document.querySelectorAll('.btn-delete-telefono');
    const btnDeleteArchivos = document.querySelectorAll('.btn-delete-archivo');
    const btnEditPrestamos = document.querySelectorAll('.btn-edit-prestamo');
    const btnDeletePrestamos = document.querySelectorAll('.btn-delete-prestamo');

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

    // Habilitar/deshabilitar edición
    btnEdit.addEventListener('click', function () {
        editMode = true;
        btnEdit.classList.add('d-none');
        btnSave.classList.remove('d-none');
        btnCancel.classList.remove('d-none');

        // Habilitar inputs del formulario principal
        /* inputs.forEach(input => {
            input.disabled = false;
        }); */

        // Habilitar botones de agregar
        btnAddTelefono.disabled = false;
        btnAddArchivo.disabled = false;
        btnAddPrestamo.disabled = false;

        // Habilitar botones de edición/eliminación
        btnEditTelefonos.forEach(btn => {
            btn.disabled = false;
        });
        btnDeleteTelefonos.forEach(btn => {
            btn.disabled = false;
        });
        btnDeleteArchivos.forEach(btn => {
            btn.disabled = false;
        });
        btnEditPrestamos.forEach(btn => {
            btn.disabled = false;
        });
        btnDeletePrestamos.forEach(btn => {
            btn.disabled = false;
        });
    });

    // Cancelar edición
    btnCancel.addEventListener('click', function () {
        editMode = false;
        btnEdit.classList.remove('d-none');
        btnSave.classList.add('d-none');
        btnCancel.classList.add('d-none');

        // Deshabilitar inputs del formulario principal
        inputs.forEach(input => {
            input.disabled = true;
        });

        // Deshabilitar botones de agregar
        btnAddTelefono.disabled = true;
        btnAddArchivo.disabled = true;
        btnAddPrestamo.disabled = true;

        // Deshabilitar botones de edición/eliminación
        btnEditTelefonos.forEach(btn => {
            btn.disabled = true;
        });
        btnDeleteTelefonos.forEach(btn => {
            btn.disabled = true;
        });
        btnDeleteArchivos.forEach(btn => {
            btn.disabled = true;
        });
        btnEditPrestamos.forEach(btn => {
            btn.disabled = true;
        });
        btnDeletePrestamos.forEach(btn => {
            btn.disabled = true;
        });

        // Recargar la página para descartar cambios
        location.reload();
    });

    // Guardar cambios del formulario principal
    btnSave.addEventListener('click', function () {
        form.submit();
    });

    // Eventos para teléfonos
    btnAddTelefono.addEventListener('click', function () {
        currentTelefonoId = null;
        telefonoForm.reset();
        document.getElementById('telefonoModalLabel').textContent = 'Agregar Teléfono';
        telefonoModal.show();
    });

    // Eventos para editar teléfono
    document.querySelectorAll('.btn-edit-telefono').forEach(btn => {
        btn.addEventListener('click', function () {
            const telefonoId = this.getAttribute('data-id');
            // Aquí deberías hacer una petición AJAX para obtener los datos del teléfono
            // y llenar el formulario del modal
            // Por ahora, solo simulamos que estamos en modo edición
            currentTelefonoId = telefonoId;
            document.getElementById('telefonoModalLabel').textContent = 'Editar Teléfono';
            telefonoModal.show();
        });
    });

    // Eventos para eliminar teléfono
    document.querySelectorAll('.btn-delete-telefono').forEach(btn => {
        btn.addEventListener('click', function () {
            const telefonoId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar este teléfono?')) {
                // Aquí deberías hacer una petición AJAX para eliminar el teléfono
                // y luego actualizar la tabla
                fetch(`/eliminar_telefono/${telefonoId}`, {
                    method: 'DELETE'
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            document.getElementById(`telefono-${telefonoId}`).remove();
                        }
                    });
            }
        });
    });

    // Guardar teléfono
    guardarTelefonoBtn.addEventListener('click', function () {
        if (telefonoForm.checkValidity()) {
            const telefonoData = {
                numero: document.getElementById('telefono-numero').value,
                nombre: document.getElementById('telefono-nombre').value,
                parentesco: document.getElementById('telefono-parentesco').value
            };

            // Determinar la URL y método según si es nuevo o edición
            const url = currentTelefonoId ?
                `/actualizar_telefono/${currentTelefonoId}` :
                `/agregar_telefono/{{ cliente.cte_id }}`;
            const method = currentTelefonoId ? 'PUT' : 'POST';

            // Aquí deberías hacer una petición AJAX para guardar el teléfono
            fetch(url, {
                method: method,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(telefonoData)
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        telefonoModal.hide();
                        location.reload(); // Recargar para ver los cambios
                    }
                });
        } else {
            telefonoForm.reportValidity();
        }
    });

    // Eventos para archivos (similar a teléfonos)
    btnAddArchivo.addEventListener('click', function () {
        currentArchivoId = null;
        archivoForm.reset();
        document.getElementById('archivoModalLabel').textContent = 'Subir Documento';
        archivoModal.show();
    });

    // Eventos para eliminar archivo
    document.querySelectorAll('.btn-delete-archivo').forEach(btn => {
        btn.addEventListener('click', function () {
            const archivoId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar este documento?')) {
                // Petición AJAX para eliminar el archivo
                fetch(`/eliminar_archivo/${archivoId}`, {
                    method: 'DELETE'
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            document.getElementById(`archivo-${archivoId}`).remove();
                        }
                    });
            }
        });
    });

    // Guardar archivo
    guardarArchivoBtn.addEventListener('click', function () {
        if (archivoForm.checkValidity()) {
            const formData = new FormData();
            formData.append('tipo', document.getElementById('archivo-tipo').value);
            formData.append('nombre', document.getElementById('archivo-nombre').value);
            formData.append('archivo', document.getElementById('archivo-file').files[0]);

            // Petición AJAX para subir el archivo
            fetch(`/subir_archivo/{{ cliente.cte_id }}`, {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        archivoModal.hide();
                        location.reload(); // Recargar para ver los cambios
                    }
                });
        } else {
            archivoForm.reportValidity();
        }
    });

    // Eventos para préstamos (similar a teléfonos)
    btnAddPrestamo.addEventListener('click', function () {
        currentPrestamoId = null;
        prestamoForm.reset();
        document.getElementById('prestamoModalLabel').textContent = 'Agregar Préstamo';
        prestamoModal.show();
    });

    // Eventos para editar préstamo
    document.querySelectorAll('.btn-edit-prestamo').forEach(btn => {
        btn.addEventListener('click', function () {
            const prestamoId = this.getAttribute('data-id');
            // Aquí deberías hacer una petición AJAX para obtener los datos del préstamo
            // y llenar el formulario del modal
            // Por ahora, solo simulamos que estamos en modo edición
            currentPrestamoId = prestamoId;
            document.getElementById('prestamoModalLabel').textContent = 'Editar Préstamo';
            prestamoModal.show();
        });
    });

    // Eventos para eliminar préstamo
    document.querySelectorAll('.btn-delete-prestamo').forEach(btn => {
        btn.addEventListener('click', function () {
            const prestamoId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar este préstamo?')) {
                // Petición AJAX para eliminar el préstamo
                fetch(`/eliminar_prestamo/${prestamoId}`, {
                    method: 'DELETE'
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            document.getElementById(`prestamo-${prestamoId}`).remove();
                        }
                    });
            }
        });
    });

    // Guardar préstamo
    guardarPrestamoBtn.addEventListener('click', function () {
        if (prestamoForm.checkValidity()) {
            const prestamoData = {
                financiera: document.getElementById('prestamo-financiera').value,
                tipo: document.getElementById('prestamo-tipo').value,
                cat: document.getElementById('prestamo-cat').value,
                monto: document.getElementById('prestamo-monto').value,
                descuento: document.getElementById('prestamo-descuento').value,
                plazo: document.getElementById('prestamo-plazo').value,
                importe: document.getElementById('prestamo-importe').value,
                fecha: document.getElementById('prestamo-fecha').value,
                estatus: document.getElementById('prestamo-estatus').value,
                liquida: document.getElementById('prestamo-liquida').value
            };

            // Determinar la URL y método según si es nuevo o edición
            const url = currentPrestamoId ?
                `/actualizar_prestamo/${currentPrestamoId}` :
                `/agregar_prestamo/{{ cliente.cte_id }}`;
            const method = currentPrestamoId ? 'PUT' : 'POST';

            // Petición AJAX para guardar el préstamo
            fetch(url, {
                method: method,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(prestamoData)
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        prestamoModal.hide();
                        location.reload(); // Recargar para ver los cambios
                    }
                });
        } else {
            prestamoForm.reportValidity();
        }
    });
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