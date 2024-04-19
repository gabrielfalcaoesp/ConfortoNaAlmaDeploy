
    // Verifica se há um nome armazenado no localStorage
    var nomeArmazenado = localStorage.getItem('unidade');

    if (nomeArmazenado) {
        // Se houver, exibe o nome na página
        document.getElementById('unidadeSalva').innerText = nomeArmazenado;
    } else {
        // Caso contrário, exibe uma mensagem padrão
        document.getElementById('unidadeSalva').innerText = 'Nenhum nome foi salvo.';
    }