let originalValues = {};
let editMode = false;

function toggleEditMode() {
    editMode = !editMode;
    const inputs = document.querySelectorAll('#cliente-form input, #cliente-form select');
    const editText = document.getElementById('edit-text');
    const editActions = document.getElementById('edit-actions');
    
    if (editMode) {
    // Guardar valores originales
    inputs.forEach(input => {
        originalValues[input.id] = input.value;
        input.disabled = false;
    });
    editText.textContent = 'Cancelar edición';
    editActions.style.display = 'block';
    } else {
    // Cancelar edición
    cancelEdit();
    }
}

function cancelEdit() {
    editMode = false;
    const inputs = document.querySelectorAll('#cliente-form input, #cliente-form select');
    const editText = document.getElementById('edit-text');
    const editActions = document.getElementById('edit-actions');
    
    inputs.forEach(input => {
    input.value = originalValues[input.id] || '';
    input.disabled = true;
    });
    
    editText.textContent = 'Actualizar información';
    editActions.style.display = 'none';
    originalValues = {};
}

function editPrestamo(prestamoId) {
    // Aquí deberías obtener los datos del préstamo específico
    // Por ahora, solo mostraremos el modal
    document.getElementById('prestamo-id').value = prestamoId;
    document.getElementById('prestamo-form').action = `/actualizar_prestamo/${prestamoId}`;
    
    // Mostrar el modal
    const modal = new bootstrap.Modal(document.getElementById('editPrestamoModal'));
    modal.show();
}

// Resaltar filas de la tabla
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('.table tbody tr');
    rows.forEach(row => {
    row.addEventListener('mouseenter', function() {
        this.style.backgroundColor = 'rgba(102, 126, 234, 0.1)';
    });
    row.addEventListener('mouseleave', function() {
        this.style.backgroundColor = '';
    });
    });
});

function togglePassword() {
  const passwordField = document.getElementById('passwordField');
  const toggleIcon = document.querySelector('.password-toggle i');
  
  if (passwordField.type === 'password') {
    passwordField.type = 'text';
    toggleIcon.classList.replace('fa-eye', 'fa-eye-slash');
  } else {
    passwordField.type = 'password';
    toggleIcon.classList.replace('fa-eye-slash', 'fa-eye');
  }
}