
    // Verifica se há um nome armazenado no localStorage
    var nomeArmazenado = localStorage.getItem('unidade');

    if (nomeArmazenado) {
        // Se houver, exibe o nome na página
        document.getElementById('unidadeSalva').innerText = nomeArmazenado;
    } else {
        // Caso contrário, exibe uma mensagem padrão
        document.getElementById('unidadeSalva').innerText = 'Nenhum nome foi salvo.';
    }

       // Verifica se há uuma especilade armazenado no localStorage
       var especialidadeArmazenado = localStorage.getItem('especialidade');

       if (especialidadeArmazenado) {
           // Se houver, exibe o nome na página
           document.getElementById('especialidadeSalva').innerText = especialidadeArmazenado;
       } else {
           // Caso contrário, exibe uma mensagem padrão
           document.getElementById('especialidadeSalva').innerText = 'Nenhum nome foi salvo.';
       }

    // Recupera a data selecionada do localStorage
    var dataSelecionada = localStorage.getItem("dataSelecionada");

    if (dataSelecionada) {
        // Se houver, exibe o nome na página
        document.getElementById('dataSalva').innerText = dataSelecionada;
    } else {
        // Caso contrário, exibe uma mensagem padrão
        document.getElementById('dataSalva').innerText = 'Nenhum nome foi salvo.';
    }