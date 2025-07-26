// Función para resaltar las filas de la tabla al hacer hover
document.addEventListener('DOMContentLoaded', function () {
    const rows = document.querySelectorAll('.table tbody tr');
    rows.forEach(row => {
    row.addEventListener('mouseenter', function () {
        this.style.backgroundColor = 'rgba(102, 126, 234, 0.1)';
    });
    row.addEventListener('mouseleave', function () {
        this.style.backgroundColor = '';
    });
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