
    var nomeArmazenado = localStorage.getItem('unidade');

    if (nomeArmazenado) {
        document.getElementById('unidadeSalva').innerText = nomeArmazenado;
    } else {
        document.getElementById('unidadeSalva').innerText = 'Nenhum nome foi salvo.';
    }


    var especialidadeArmazenado = localStorage.getItem('especialidade');

       if (especialidadeArmazenado) {
           document.getElementById('especialidadeSalva').innerText = especialidadeArmazenado;
       } else {
           document.getElementById('especialidadeSalva').innerText = 'Nenhum nome foi salvo.';
       }


    var dataSelecionada = localStorage.getItem("dataEscolhida");

    if (dataSelecionada) {
        exibirData(dataSelecionada);
    } else {
        document.getElementById('dataSalva').innerText = 'Nenhum nome foi salvo.';
    }


    var profissionalSelecionado = localStorage.getItem("nomeMedico");

    if (profissionalSelecionado) {
        document.getElementById('nomeProfissionalSalvo').innerText = profissionalSelecionado;
    } else {
        document.getElementById('nomeProfissionalSalvo').innerText = 'Nenhum nome foi salvo.';
    }


    var horaSelecionada = localStorage.getItem("horarioSelecionado");

    if (horaSelecionada) {
        document.getElementById('horaSalva').innerText = horaSelecionada;
    } else {
        document.getElementById('horaSalva').innerText = 'Nenhum nome foi salvo.';
    }


    function exibirData(dataSelecionada) {
        var partesData = dataSelecionada.split('-');
        if (partesData.length === 1) {
            var hoje = new Date();
            var dia = parseInt(partesData[0], 10);
            hoje.setDate(dia);
            var ano = hoje.getFullYear();
            var mes = hoje.getMonth() + 1; 
            dataSelecionada = `${dia < 10 ? '0' + dia : dia}-${mes < 10 ? '0' + mes : mes}-${ano}`;
        } else {
            var dia = parseInt(partesData[2], 10);
            var mes = parseInt(partesData[1], 10);
            var ano = parseInt(partesData[0], 10);
            dataSelecionada = `${dia < 10 ? '0' + dia : dia}-${mes < 10 ? '0' + mes : mes}-${ano}`;
        }
        document.getElementById('dataSalva').innerText = dataSelecionada;
    }