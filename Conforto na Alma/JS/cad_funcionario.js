function mostrarCNR() {
    var cargoSelecionado = document.getElementById("cargo").value;
    var cnrDiv = document.getElementById("cnrDiv");

    if (cargoSelecionado === "2") { // Se o cargo selecionado for "Médico"
        cnrDiv.style.display = "block"; // Mostra o campo CNR
    } else {
        cnrDiv.style.display = "none"; // Oculta o campo CNR
    }
}               