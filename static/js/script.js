let d = document;

// Función para que el botón de la página principal scrollee la vista hasta la parte del selector de especialidades.

function scrollToSection(event, id) {
    event.preventDefault();
    let seccion = d.getElementById(id);

    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth' });
    }
}

let boton_cliente = d.getElementById('boton-cliente');
let boton_profesional = d.getElementById('boton-profesional');

console.log(d.querySelector("#boton-cliente"));
