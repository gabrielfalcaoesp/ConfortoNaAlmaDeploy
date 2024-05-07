document.addEventListener('DOMContentLoaded', function() {
    const confirmButton = document.querySelector('.confirmButton');

    confirmButton.addEventListener('click', function() {
        // Redireciona para a página desejada
        window.location.href = 'clienteAgendado.html';
    });
});