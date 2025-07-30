// Variables para almacenar los datos temporales
let phone_numbers = [];
let files = [];
let prestamos = [];

// ---------- Eventos telefonos ----------
// Agregar telefono
document.getElementById('add_phone_number').addEventListener('click', function () {
    const ph_number = document.getElementById('ph_number').value;
    const ph_name = document.getElementById('ph_name').value;
    const ph_rel = document.getElementById('ph_rel').value;

    if (!ph_number || !ph_name || !ph_rel) {
        alert('Todos los campos son obligatorios');
        return;
    }

    phone_numbers.push({
        ph_number: ph_number,
        ph_name: ph_name,
        ph_rel: ph_rel
    });

    updatePhoneList();
    document.getElementById('ph-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('ph-modal')).hide();
});

// Actualizar la lista telefonos
function updatePhoneList() {
    const container = document.getElementById('ph-container');

    if (phone_numbers.length === 0) {
        container.innerHTML = '<div class="alert alert-info">No se han agregado teléfonos aún.</div>';
        return;
    }

    let html = '<div class="table-responsive"><table class="table"><thead><tr><th>Número</th><th>Nombre</th><th>Parentesco</th><th>Acciones</th></tr></thead><tbody>';

    phone_numbers.forEach((phone, i) => {
        html += `
        <tr>
        <td>${phone.ph_number}</td>
        <td>${phone.ph_name}</td>
        <td>${phone.ph_rel}</td>
        <td>
            <button class="btn btn-edit-small" onclick="editPhone(${i})">
            <i class="fas fa-edit"></i>
            </button>
            <button class="btn btn-cancel-small" onclick="deletePhone(${i})">
            <i class="fas fa-trash"></i>
            </button>
        </td>
        </tr>
    `;
    });

    html += '</tbody></table></div>';

    // Agregar campos ocultos para cada teléfono
    phone_numbers.forEach((phone, i) => {
        html += `
        <input type="hidden" name="ph_number[${i}]" value="${phone.ph_number}">
        <input type="hidden" name="ph_name[${i}]" value="${phone.ph_name}">
        <input type="hidden" name="ph_rel[${i}]" value="${phone.ph_rel}">
    `;
    });

    container.innerHTML = html;
}

// Editar telefono
function editPhone(i) {
    const phone = phone_numbers[i];
    document.getElementById('ph_number').value = phone.ph_number;
    document.getElementById('ph_name').value = phone.ph_name;
    document.getElementById('ph_rel').value = phone.ph_rel;

    phone_numbers.splice(i, 1);
    updatePhoneList();

    const modal = new bootstrap.Modal(document.getElementById('ph-modal'));
    modal.show();
}

// Eliminar telefono
function deletePhone(i) {
    if (confirm('¿Estás seguro de eliminar este teléfono?')) {
        phone_numbers.splice(i, 1);
        updatePhoneList();
    }
}

// ---------- Eventos para archivos ----------
// Agregar archivo
document.getElementById('add_file').addEventListener('click', function () {
    const fil_ft_id = document.getElementById('fil_ft_id').value;
    const fil_name = document.getElementById('fil_name').value;
    const fileInput = document.getElementById('fil-file');
    const multiInput = document.getElementById('fil-multifile');
    const metadatosDiv = document.getElementById('fil-metadatos');

    if (!fil_ft_id || !fil_name || !fileInput.files.length) {
        alert('Todos los campos son obligatorios');
        return;
    }

    // Agregar archivo al input multiple oculto
    // Creamos un nuevo DataTransfer para combinar los archivos existentes + el nuevo
    const dt = new DataTransfer();
    // Agrega los archivos ya existentes
    for (let i = 0; i < multiInput.files.length; i++) {
        dt.items.add(multiInput.files[i]);
    }
    // Agrega el nuevo archivo
    dt.items.add(fileInput.files[0]);
    multiInput.files = dt.files;

    // Guardar metadatos en campos ocultos
    const i = multiInput.files.length - 1;
    const taInput = document.createElement('input');
    taInput.type = 'hidden';
    taInput.name = `fil_ft[${i}]`;
    taInput.value = fil_ft_id;
    const nombreInput = document.createElement('input');
    nombreInput.type = 'hidden';
    nombreInput.name = `fil_name[${i}]`;
    nombreInput.value = fil_name;
    metadatosDiv.appendChild(taInput);
    metadatosDiv.appendChild(nombreInput);

    // Actualizar la lista visual
    updateFileList();
    document.getElementById('fil-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('fil-modal')).hide();
});

// Actualizar la lista archivos
function updateFileList() {
    const container = document.getElementById('fil-container');
    const multiInput = document.getElementById('fil-multifile');
    const metadatosDiv = document.getElementById('fil-metadatos');

    if (multiInput.files.length === 0) {
        container.innerHTML = '<div class="alert alert-info">No se han subido documentos aún.</div>';
        metadatosDiv.innerHTML = '';
        return;
    }
    let html = '<div class="table-responsive"><table class="table"><thead><tr><th>Tipo</th><th>Nombre</th><th>Archivo</th><th>Acciones</th></tr></thead><tbody>';
    for (let i = 0; i < multiInput.files.length; i++) {
        const fil_ft = document.querySelector(`input[name='fil_ft[${i}]']`)?.value || '';
        const fil_name = document.querySelector(`input[name='fil_name[${i}]']`)?.value || '';
        html += `
            <tr>
                <td>${fil_ft}</td>
                <td>${fil_name}</td>
                <td>${multiInput.files[i].name}</td>
                <td>
                    <button class="btn btn-cancel-small" onclick="deleteFile(${i})">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            </tr>
        `;
    }
    html += '</tbody></table></div>';
    container.innerHTML = html;
}

// Eliminar archivo
function deleteFile(i) {
    if (confirm('¿Estás seguro de eliminar este archivo?')) {
        const multiInput = document.getElementById('fil-multifile');
        const metadatosDiv = document.getElementById('fil-metadatos');
        const dt = new DataTransfer();
        
        
        // Agrega los archivos ya existentes
        for (let j = 0; j < multiInput.files.length; j++) {
            if(i != j){
                dt.items.add(multiInput.files[j]);
            }
        }
        multiInput.files = dt.files;
        
        const fil_ft = document.querySelector(`input[name='fil_ft[${i}]']`);
        const fil_name = document.querySelector(`input[name='fil_name[${i}]']`);
        
        fil_ft.remove();
        fil_name.remove();

        reindexMetadata();
        updateFileList();
    }
}

function reindexMetadata() {
    const metadatosDiv = document.getElementById('fil-metadatos');
    const inputsFt = metadatosDiv.querySelectorAll('input[name^="fil_ft["]');
    const inputsName = metadatosDiv.querySelectorAll('input[name^="fil_name["]');

    inputsFt.forEach((input, index) => {
        input.name = `fil_ft[${index}]`;  // Reindexa fil_ft[0], fil_ft[1], etc.
    });

    inputsName.forEach((input, index) => {
        input.name = `fil_name[${index}]`; // Reindexa fil_name[0], fil_name[1], etc.
    });
}

// ---------- Eventos de prestamos ----------
// Agregar préstamo
document.getElementById('agregar-prestamo').addEventListener('click', function () {
    const financiera = document.getElementById('prestamo-financiera').value;
    const tipo = document.getElementById('prestamo-tipo').value;
    const estatus = document.getElementById('prestamo-estatus').value;
    const cat = document.getElementById('prestamo-cat').value;
    const monto = document.getElementById('prestamo-monto').value;
    const descuento = document.getElementById('prestamo-descuento').value;
    const plazo = document.getElementById('prestamo-plazo').value;
    const importe = document.getElementById('prestamo-importe').value;
    const fecha = document.getElementById('prestamo-fecha').value;
    const liquida = document.getElementById('prestamo-liquida').value;

    // Validar campos obligatorios
    if (!financiera || !tipo || !cat || !monto || !descuento || !plazo || !importe || !fecha || !estatus) {
        alert('Todos los campos marcados como obligatorios (*) deben ser completados');
        return;
    }

    prestamos.push({
        financiera: financiera,
        tipo: tipo,
        cat: cat,
        monto: monto,
        descuento: descuento,
        plazo: plazo,
        importe: importe,
        fecha: fecha,
        estatus: estatus,
        liquida: liquida || null
    });

    actualizarListaPrestamos();
    document.getElementById('prestamo-form').reset();
    bootstrap.Modal.getInstance(document.getElementById('prestamoModal')).hide();
});

// Actualizar la lista prestamos
function actualizarListaPrestamos() {
    const container = document.getElementById('prestamos-container');

    if (prestamos.length === 0) {
        container.innerHTML = '<div class="alert alert-info">No se han agregado préstamos aún.</div>';
        return;
    }

    let html = `
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th>Financiera</th>
            <th>Tipo</th>
            <th>Monto</th>
            <th>CAT</th>
            <th>Plazo</th>
            <th>Monto a pagar</th>
            <th>Primer descuento</th>
            <th>Estatus</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
  `;

    prestamos.forEach((prestamo, index) => {
        const tipoNombre = document.getElementById('prestamo-tipo').options[prestamo.tipo].text;
        const estatusNombre = document.getElementById('prestamo-estatus').options[prestamo.estatus].text;
        const financieraNombre = document.getElementById('prestamo-financiera').options[prestamo.financiera].text;

        html += `
      <tr>
        <td>${financieraNombre}</td>
        <td>${tipoNombre}</td>
        <td>$${parseFloat(prestamo.monto).toLocaleString('es-MX', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
        <td>${prestamo.cat}%</td>
        <td>${prestamo.plazo} meses</td>
        <td>$${prestamo.importe}</td>
        <td>${prestamo.fecha}</td>
        <td>${estatusNombre}</td>
        <td>
          <button class="btn btn-edit-small" onclick="editarPrestamo(${index})">
            <i class="fas fa-edit"></i>
          </button>
          <button class="btn btn-cancel-small" onclick="eliminarPrestamo(${index})">
            <i class="fas fa-trash"></i>
          </button>
        </td>
      </tr>
    `;
    });

    html += '</tbody></table></div>';

    // Agregar campos ocultos para cada préstamo
    prestamos.forEach((prestamo, i) => {
        html += `
        <input type="hidden" name="ln_cat[${i}]" value="${prestamo.cat}">
        <input type="hidden" name="ln_monto[${i}]" value="${prestamo.monto}">
        <input type="hidden" name="ln_descuento[${i}]" value="${prestamo.descuento}">
        <input type="hidden" name="ln_plazo[${i}]" value="${prestamo.plazo}">
        <input type="hidden" name="ln_imp_pagar[${i}]" value="${prestamo.importe}">
        <input type="hidden" name="ln_f_p_desc[${i}]" value="${prestamo.fecha}">
        <input type="hidden" name="ln_fi_id[${i}]" value="${prestamo.financiera}">
        <input type="hidden" name="ln_tp_id[${i}]" value="${prestamo.tipo}">
        <input type="hidden" name="ln_ep_id[${i}]" value="${prestamo.estatus}">
        ${prestamo.liquida ? `<input type="hidden" name="ln_id_liq[${i}]" value="${prestamo.liquida}">` : ''}
    `;
    });

    container.innerHTML = html;
}

// Editar prestamo
function editarPrestamo(index) {
    const prestamo = prestamos[index];

    document.getElementById('prestamo-financiera').value = prestamo.financiera;
    document.getElementById('prestamo-tipo').value = prestamo.tipo;
    document.getElementById('prestamo-cat').value = prestamo.cat;
    document.getElementById('prestamo-monto').value = prestamo.monto;
    document.getElementById('prestamo-descuento').value = prestamo.descuento;
    document.getElementById('prestamo-plazo').value = prestamo.plazo;
    document.getElementById('prestamo-importe').value = prestamo.importe;
    document.getElementById('prestamo-fecha').value = prestamo.fecha;
    document.getElementById('prestamo-estatus').value = prestamo.estatus;
    document.getElementById('prestamo-liquida').value = prestamo.liquida || '';

    prestamos.splice(index, 1);
    actualizarListaPrestamos();

    const modal = new bootstrap.Modal(document.getElementById('prestamoModal'));
    modal.show();
}

// Eliminar prestamo
function eliminarPrestamo(index) {
    if (confirm('¿Estás seguro de eliminar este préstamo?')) {
        prestamos.splice(index, 1);
        actualizarListaPrestamos();
    }
}

// ---------- Otros metodos ----------
// Metodo para ver/ocultar contraseña
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

// Selecciona todos los inputs de texto y hace toUpperCase()
const inputsTexto = document.querySelectorAll('input[type="text"]');

inputsTexto.forEach(input => {
    input.addEventListener('input', function () {
        const start = this.selectionStart; // Guarda posición del cursor
        const end = this.selectionEnd;
        this.value = this.value.toUpperCase();
        this.setSelectionRange(start, end); // Restaura posición del cursor
    });
});