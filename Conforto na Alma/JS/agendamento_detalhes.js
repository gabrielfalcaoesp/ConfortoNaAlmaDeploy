
    var id_medico = 1
    var detalhesAgendamentoString = localStorage.getItem("detalhesAgendamento");
    var detalhesAgendamento = JSON.parse(detalhesAgendamentoString);

    if (detalhesAgendamento[7]) {
        document.getElementById('unidadeSalva').innerText = detalhesAgendamento[7];
    } else {
        document.getElementById('unidadeSalva').innerText = 'Nenhum nome foi salvo.';
    }

    if (detalhesAgendamento[3]) {
        document.getElementById('especialidadeSalva').innerText = detalhesAgendamento[3];
    } else {
        document.getElementById('especialidadeSalva').innerText = 'Nenhum nome foi salvo.';
    }

    if (detalhesAgendamento[4]) {
        document.getElementById('dataSalva').innerText = detalhesAgendamento[4];
    } else {
        document.getElementById('dataSalva').innerText = 'Nenhum nome foi salvo.';
    }


    var profissionalSelecionado = localStorage.getItem("nomeMedico");

    if (profissionalSelecionado) {
        document.getElementById('nomeProfissionalSalvo').innerText = profissionalSelecionado;
    } else {
        document.getElementById('nomeProfissionalSalvo').innerText = 'Nenhum nome foi salvo.';
    }


    var hora = detalhesAgendamento[6]
    var novaHoraFormatada = formatarHora(hora)

    if (detalhesAgendamento[6]) {
        document.getElementById('horaSalva').innerText = novaHoraFormatada;
    } else {
        document.getElementById('horaSalva').innerText = 'Nenhum nome foi salvo.';
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
        detalhesAgendamento
    )

    function formatarHora(segundos) {
        var horas = Math.floor(segundos / 3600);
        var minutosRestantes = Math.floor((segundos % 3600) / 60);
        var minutosFormatados = minutosRestantes < 10 ? '0' + minutosRestantes : minutosRestantes;
        var horaFormatada = horas + ':' + minutosFormatados;
    
        return horaFormatada;
    }