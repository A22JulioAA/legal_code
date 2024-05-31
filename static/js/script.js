let d = document;

// Función para que el botón de la página principal scrollee la vista hasta la parte del selector de especialidades.

function scrollToSection(event, id) {
    event.preventDefault();
    let seccion = d.getElementById(id);

    if (seccion) {
        seccion.scrollIntoView({ behavior: 'smooth' });
    }
}

// Con este evento se crea la animación de las estrellas en la sección de comentarios.

document.addEventListener('DOMContentLoaded', (e) => {
    const stars = document.querySelectorAll('.star-rating i');
        const ratingInput = document.getElementById('rating');
        
        stars.forEach(star => {
            star.addEventListener('mouseover', (e) => {
                const value = e.target.getAttribute('data-value');
                highlightStars(value);
            });
            
            star.addEventListener('mouseout', (e) => {
                resetStars();
            });
            
            star.addEventListener('click', (e) => {
                const value = e.target.getAttribute('data-value');
                ratingInput.value = value;
                setSelectedStars(value);
            });
        });
        
        function highlightStars(value) {
            stars.forEach(star => {
                star.classList.remove('hovered');
                if (star.getAttribute('data-value') <= value) {
                    star.classList.add('hovered');
                }
            });
        }
        
        function resetStars() {
            stars.forEach(star => {
                star.classList.remove('hovered');
            });
        }
        
        function setSelectedStars(value) {
            stars.forEach(star => {
                star.classList.remove('selected');
                if (star.getAttribute('data-value') <= value) {
                    star.classList.add('selected');
                }
            });
        }
    });



