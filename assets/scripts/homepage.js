// Evento para cargar la toast cada vez que se cargue la página
document.addEventListener('DOMContentLoaded', function () {
    let myToast = new bootstrap.Toast(document.querySelector('.toast'));
    myToast.show();
});
