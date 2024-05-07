function associarHorario(elementoClicado) {
    // Remove a classe "selecionada" de todas as caixas
    var todasCaixas = document.querySelectorAll('.caixa');
    todasCaixas.forEach(function(caixa) {
        caixa.classList.remove('selecionada');
    });

    // Adiciona a classe "selecionada" à caixa clicada
    elementoClicado.classList.add('selecionada');

    // Obtém o valor do horário selecionado
    var horarioSelecionado = elementoClicado.querySelector('p').innerText;

    // Obtém o nome do médico
    var nomeMedico = elementoClicado.closest('.parent').querySelector('.nome p').innerText;

    // Armazena o valor do horário selecionado e o nome do médico no localStorage
    localStorage.setItem('horarioSelecionado', horarioSelecionado);
    localStorage.setItem('nomeMedico', nomeMedico);

    console.log(horarioSelecionado)
    console.log(nomeMedico)
}