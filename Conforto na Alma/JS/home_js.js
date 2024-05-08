

function exibirLogin() {
  var container = document.querySelector('.caixa');
  var container2 = document.querySelector('.caixa2');
  var computedStyle = window.getComputedStyle(container);

  if (computedStyle.display === 'none') {
      container.style.display = 'block';
      console.log("O estado do display é: block");
  } else {
      container.style.display = 'none';
      console.log("O estado do display é: none");
  }

  // Verifica se o usuário está logado
  if (boolLogado) {
      container.style.display = 'none';  // Oculta caixa original
      container2.style.display = 'block';  // Exibe caixa2
      console.log("Usuário está logado. Exibindo caixa2.");
  }
}
const clicouDentro = document.querySelector('.BL img');
const clicouDentroCaixa = document.querySelector('.caixa');
document.addEventListener('mousedown', (event) => {
  if (clicouDentro.contains(event.target) || clicouDentroCaixa.contains(event.target)) {
  } else {
    var container = document.querySelector('.caixa');
    container.style.display = 'none';
  }
})
