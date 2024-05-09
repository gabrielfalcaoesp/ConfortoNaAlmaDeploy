function buscarEndereco() {
    var cep = document.getElementById("cep").value;
    if (cep.length === 8) { // Verifica se o CEP possui 8 dígitos
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.getElementById("estado").value = data.uf;
                    document.getElementById("cidade").value = data.localidade;
                    document.getElementById("bairro").value = data.bairro;
                    document.getElementById("endereco").value = data.logradouro;
                } else {
                    alert("CEP não encontrado.");
                }
            })
            .catch(error => console.error('Erro ao buscar endereço:', error));
    }
}