document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.cc-num');

    inputs.forEach((input, index) => {
        input.addEventListener('input', (e) => {
            if (input.value.length >= input.maxLength) {
                if (index < inputs.length - 1) {
                    inputs[index + 1].focus();
                }
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const confirmButton = document.querySelector('.confirmButton');

    confirmButton.addEventListener('click', function() {
        // Redireciona para a página desejada
        window.location.href = 'clienteAgendado.html';
    });
});