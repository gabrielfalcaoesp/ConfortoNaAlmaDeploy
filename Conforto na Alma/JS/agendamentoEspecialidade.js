var verificacao = 0; 

const selectElement = document.getElementById('especialidadeSelect');
        selectElement.addEventListener('change', function() {
            const selectedValue = selectElement.value;
            console.log(selectedValue); 
        });

const botaoAvancar = document.querySelector('.botaoAvancar');

selectElement.addEventListener('change', function() {
    const selectedValue = selectElement.value;

    if (selectedValue) {  
        botaoAvancar.style.cursor = 'pointer';
        verificacao = 1;
    } else {
        botaoAvancar.style.cursor = 'none';
    }
});

function redirectToPage() {

    var especialidade = document.getElementById('especialidadeSelect').value;
    localStorage.setItem('especialidade', especialidade);

    if (verificacao==1) {  
    window.location.href = "/Agendamento/Data";
    }
  }