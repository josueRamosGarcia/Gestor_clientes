// Variables para almacenar los datos temporales
let telefonos = [];
let archivos = [];
let prestamos = [];

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

// Función para agregar préstamo
document.getElementById('agregar-prestamo').addEventListener('click', function() {
  const financiera = document.getElementById('prestamo-financiera').value;
  const tipo = document.getElementById('prestamo-tipo').value;
  const cat = document.getElementById('prestamo-cat').value;
  const monto = document.getElementById('prestamo-monto').value;
  const descuento = document.getElementById('prestamo-descuento').value;
  const plazo = document.getElementById('prestamo-plazo').value;
  const importe = document.getElementById('prestamo-importe').value;
  const fecha = document.getElementById('prestamo-fecha').value;
  const estatus = document.getElementById('prestamo-estatus').value;
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

// Función para actualizar la lista de préstamos en la UI
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
            <th>Estatus</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
  `;
  
  prestamos.forEach((prestamo, index) => {
    const tipoNombre = document.getElementById('prestamo-tipo').options[prestamo.tipo-1].text;
    const estatusNombre = document.getElementById('prestamo-estatus').options[prestamo.estatus-1].text;
    
    html += `
      <tr>
        <td>${prestamo.financiera}</td>
        <td>${tipoNombre}</td>
        <td>$${parseFloat(prestamo.monto).toLocaleString('es-MX', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
        <td>${prestamo.cat}%</td>
        <td>${prestamo.plazo} meses</td>
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
  prestamos.forEach((prestamo, index) => {
    html += `
      <input type="hidden" name="prestamos[${index}][prst_financiera]" value="${prestamo.financiera}">
      <input type="hidden" name="prestamos[${index}][tp_id]" value="${prestamo.tipo}">
      <input type="hidden" name="prestamos[${index}][prst_cat]" value="${prestamo.cat}">
      <input type="hidden" name="prestamos[${index}][prst_monto]" value="${prestamo.monto}">
      <input type="hidden" name="prestamos[${index}][prst_descuento]" value="${prestamo.descuento}">
      <input type="hidden" name="prestamos[${index}][prst_plazo]" value="${prestamo.plazo}">
      <input type="hidden" name="prestamos[${index}][prst_imp_pagar]" value="${prestamo.importe}">
      <input type="hidden" name="prestamos[${index}][prst_f_p_desc]" value="${prestamo.fecha}">
      <input type="hidden" name="prestamos[${index}][ep_id]" value="${prestamo.estatus}">
      ${prestamo.liquida ? `<input type="hidden" name="prestamos[${index}][prst_id_liq]" value="${prestamo.liquida}">` : ''}
    `;
  });
  
  container.innerHTML = html;
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

// Funciones para editar/eliminar préstamos
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

function eliminarPrestamo(index) {
  if (confirm('¿Estás seguro de eliminar este préstamo?')) {
    prestamos.splice(index, 1);
    actualizarListaPrestamos();
  }
}