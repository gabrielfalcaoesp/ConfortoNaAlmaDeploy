

function exibirLogin() {
    fetch('http://localhost:8000/verificarLogin')
      .then(response => response.json())
      .then(data => {
        console.log('Estado da variável:', data);
        // Aqui você pode fazer o que precisar com o estado da variável (data)
        
        var container = document.querySelector('.caixa');
        var container2 = document.querySelector('.caixa2');
        
        if (data != "") {
          localStorage.setItem('id_usuario', data);
          container2.style.display = 'block';
          console.log("O estado do display é: block");
        } else {
          container.style.display = 'block';
          console.log("O estado do display é: block");
          // Certifique-se de ocultar a caixa2 apenas quando o usuário não estiver logado
          container2.style.display = 'none';
        }
      })
      .catch(error => console.error('Erro ao verificar estado da variável:', error));
  }
  
  const clicouDentro = document.querySelector('.BL img');
  const clicouDentroCaixa = document.querySelector('.caixa');
  const clicouDentroCaixa2 = document.querySelector('.caixa2');
  document.addEventListener('mousedown', (event) => {
    if (clicouDentro.contains(event.target) || clicouDentroCaixa.contains(event.target) || clicouDentroCaixa2.contains(event.target)) {
    } else {
      var container = document.querySelector('.caixa');
      var container2 = document.querySelector('.caixa2');
      container.style.display = 'none';
      container2.style.display = 'none';
    }
  });
  
  function loginFailed() {
    alert("Login falhou. Por favor, verifique seu email e senha.");
}