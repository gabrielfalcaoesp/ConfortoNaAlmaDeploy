
    var nomeArmazenado = localStorage.getItem('unidade');
    var id_usuario = localStorage.getItem('id_usuario');
    var id_medico = 1
    const dataDeHoje = pegarDataDeHoje();
    var dataSelecionada = localStorage.getItem("dataEscolhida");
    var newData = exibirData(dataSelecionada);

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
        return dataSelecionada
    }

    document.addEventListener('DOMContentLoaded', function () {
        const botaoAvancar = document.querySelector('.botaoAvancar');
        const formaPagamento = document.querySelector('.formaPagamento');

        botaoAvancar.addEventListener('click', function () {
            // Verifica qual opção de pagamento está selecionada
            const pixSelecionado = document.getElementById('pix').checked;
            const cartaoSelecionado = document.getElementById('cartao').checked;
            const pagamentoConsultaSelecionado = document.getElementById('pagamento-consulta').checked;

            if (pixSelecionado) {
                window.location.href = 'pagamento/pix';
            } else if (cartaoSelecionado) {
                window.location.href = 'pagamento/cartao';
            } else if (pagamentoConsultaSelecionado) {
                window.location.href = 'pagamento/consulta';
            } else {
                // Tratamento para quando nenhuma opção é selecionada
                alert('Selecione uma opção de pagamento.');
            }
        });
    });







    function pegarDataDeHoje() {
        return new Date().toISOString().split('T')[0];
    }






    function enviarAgendamento() {
        const agendamento = {
            id_cliente: id_usuario,
            id_medico: id_medico,
            tipo_consulta: especialidadeArmazenado,
            data_agendada: newData,
            data_agendamento: dataDeHoje,
            horario_consulta: horaSelecionada,
            unidade: nomeArmazenado
        };

        console.log('Agendamento:', agendamento);
    
        fetch('/Agendamento/Enviar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(agendamento)
        })
        .then(response => {
            return "message: enviou para o banco"
        })
        .catch(error => {
            console.error('Erro ao enviar o agendamento:', error);
        });
    }

    console.log(
        `id_usuario: ${id_usuario}\n
        id_medico: ${id_medico}\n
        tipo_consulta: ${especialidadeArmazenado}\n
        data_agendada: ${newData}\n
        data_agendamento: ${dataDeHoje}\n
        horario_consulta: ${horaSelecionada}\n
        unidade: ${nomeArmazenado}` 
    )