const url = '/Clientes/Perfil/';
const agendamentosContainer = document.getElementById('agendamentosCliente');


const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json', 
  },
};

fetch(url, options)
  .then(response => {
    if (!response.ok) {
      throw new Error('Erro na requisição');
    }
    return response.json(); 
  })
  .then(data => {
    const nome = document.querySelector('h1.nome');
    nome.textContent = data[0][1]; // Supondo que o nome esteja na primeira posição de infoCliente

    const idade = document.querySelector('td.idade');
    idadeUsuario = calcularIdade(data[0][2]); // Supondo que a data de nascimento esteja na segunda posição de infoCliente
    idade.textContent = "Idade: " + idadeUsuario + ' anos';

    const cpf = document.querySelector('td.cpf');
    cpf.textContent = "CPF: " + data[0][4]; // Supondo que o CPF esteja na quarta posição de infoCliente

    const email = document.getElementById('mailValue')
    email.textContent = data[0][5]; // Supondo que o email esteja na quinta posição de infoCliente

    const telefone = document.getElementById('telValue')
    telefone.textContent = data[0][6]; // Supondo que o telefone esteja na sexta posição de infoCliente

    const cep = document.getElementById('cepValue')
    cep.textContent = data[0][7]; // Supondo que o CEP esteja na sétima posição de infoCliente

    const endereco = document.getElementById('endValue')
    endereco.textContent = data[0][11]; // Supondo que o endereço esteja na décima segunda posição de infoCliente

    const hoje = new Date(); // Obtém a data atual
    const hojeFormatado = formatDate(hoje); 

    data[1].forEach((agendamentoData, index) => {
      dataConvertida = convertToDate(agendamentoData[4])
      if (dataConvertida >= hojeFormatado) {
      const novoAgendamento = document.createElement('div');
      novoAgendamento.classList.add('section-1');
  
      const titulo = document.createElement('div');
      titulo.id = 'marcada';
      titulo.textContent = agendamentoData[3] + " - " +agendamentoData[4];
  
      const dataParagrafo = document.createElement('p');
      dataParagrafo.textContent = '';
  
      const botoesContainer = document.createElement('div');
      botoesContainer.classList.add('botoes-container');
  
      const detalhesBtn = document.createElement('button');
      detalhesBtn.classList.add('btn', 'btn-custom');
      detalhesBtn.textContent = 'Ver detalhes';
  
      const desmarcarBtn = document.createElement('button');
      desmarcarBtn.classList.add('btn-cancel');
      desmarcarBtn.textContent = 'Desmarcar';

      detalhesBtn.addEventListener('click', () => {
        var info = data[1][index];
        var jsonString = JSON.stringify(info);
        localStorage.setItem('detalhesAgendamento', jsonString);
        window.location.href = '/Detalhes/Consulta/';
        console.log(data[1][index]); 
    });

    desmarcarBtn.addEventListener('click', () => {
      var agendamentoDelete = data[1][index][0]; 
      window.location.href = `/Desmarcar/Consulta/${agendamentoDelete}`;
      
      console.log(data[1][index][0]); 
  });


      botoesContainer.appendChild(detalhesBtn);
      botoesContainer.appendChild(desmarcarBtn);
  
      novoAgendamento.appendChild(titulo);
      novoAgendamento.appendChild(dataParagrafo);
      novoAgendamento.appendChild(botoesContainer);
  
      agendamentosContainer.appendChild(novoAgendamento);
} 

else {
  const novoAgendamento = document.createElement('div');
  novoAgendamento.classList.add('section-1');

  const titulo = document.createElement('div');
  titulo.id = 'marcada';
  titulo.textContent = agendamentoData[3] + " - " + agendamentoData[4];

  const dataParagrafo = document.createElement('p');
  dataParagrafo.textContent = '';

  const botoesContainer = document.createElement('div');
  botoesContainer.classList.add('botoes-container');

  const detalhesBtn = document.createElement('button');
  detalhesBtn.classList.add('btn', 'btn-custom');
  detalhesBtn.textContent = 'Ver detalhes';

  const desmarcarBtn = document.createElement('button');
  desmarcarBtn.classList.add('btn-cancel');
  desmarcarBtn.textContent = 'Desmarcar';

  detalhesBtn.addEventListener('click', () => {
      var info = data[1][index];
      var jsonString = JSON.stringify(info);
      localStorage.setItem('detalhesAgendamento', jsonString);
      window.location.href = '/Detalhes/Consulta/';
  });

  desmarcarBtn.addEventListener('click', () => {
      var agendamentoDelete = data[1][index][0];
      window.location.href = `/Desmarcar/Consulta/${agendamentoDelete}`;

  });

  botoesContainer.appendChild(detalhesBtn);
  botoesContainer.appendChild(desmarcarBtn);

  novoAgendamento.appendChild(titulo);
  novoAgendamento.appendChild(dataParagrafo);
  novoAgendamento.appendChild(botoesContainer);

  const agendamentosContainerHistorico = document.getElementById('agendamentosClienteHistorico');
  agendamentosContainerHistorico.appendChild(novoAgendamento);
}

  });

  








  data[2].forEach((exameData, index) => {
    dataConvertida = convertToDate2(exameData[4])
    dataConvertida2 = convertToDate3(exameData[4])
      if (dataConvertida >= hojeFormatado) {
        console.log("exame - data agendada: ", dataConvertida)
        console.log("exame hoje: ", hojeFormatado)
          // Se a data do exame for igual ou superior a hoje, continuar com o processamento
          const novoAgendamento = document.createElement('div');
          novoAgendamento.classList.add('section-1');
  
          const titulo = document.createElement('div');
          titulo.id = 'marcada';
          titulo.textContent = exameData[3] + " - " + dataConvertida2;
  
          const dataParagrafo = document.createElement('p');
          dataParagrafo.textContent = '';
  
          const botoesContainer = document.createElement('div');
          botoesContainer.classList.add('botoes-container2');
  
          const detalhesBtn = document.createElement('button');
          detalhesBtn.classList.add('btn', 'btn-custom');
          detalhesBtn.textContent = 'Ver detalhes';
  
          const desmarcarBtn = document.createElement('button');
          desmarcarBtn.classList.add('btn-cancel');
          desmarcarBtn.textContent = 'Desmarcar';
  
          detalhesBtn.addEventListener('click', () => {
              var info = data[2][index];
              var jsonString = JSON.stringify(info);
              localStorage.setItem('detalhesExame', jsonString);
              window.location.href = '/Detalhes/Exame/';
          });
  
          desmarcarBtn.addEventListener('click', () => {
              var agendamentoDelete = data[2][index][0];
              window.location.href = `/Desmarcar/Exame/${agendamentoDelete}`;
          });
  
          botoesContainer.appendChild(detalhesBtn);
          botoesContainer.appendChild(desmarcarBtn);
  
          novoAgendamento.appendChild(titulo);
          novoAgendamento.appendChild(dataParagrafo);
          novoAgendamento.appendChild(botoesContainer);
  
          agendamentosContainer.appendChild(novoAgendamento);
      }

      else{
        console.log("exame - data agendada: ", exameData[4])
        console.log("exame hoje: ", hojeFormatado)
        const novoAgendamento = document.createElement('div');
        novoAgendamento.classList.add('section-1');
      
        const titulo = document.createElement('div');
        titulo.id = 'marcada';
        titulo.textContent = exameData[3] + " - " + dataConvertida2;
      
        const dataParagrafo = document.createElement('p');
        dataParagrafo.textContent = '';
      
        const botoesContainer = document.createElement('div');
        botoesContainer.classList.add('botoes-container');
      
        const detalhesBtn = document.createElement('button');
        detalhesBtn.classList.add('btn', 'btn-custom');
        detalhesBtn.textContent = 'Ver detalhes';
      
        const desmarcarBtn = document.createElement('button');
        desmarcarBtn.classList.add('btn-cancel');
        desmarcarBtn.textContent = 'Desmarcar';
      
        detalhesBtn.addEventListener('click', () => {
            var info = data[2][index];
            var jsonString = JSON.stringify(info);
            localStorage.setItem('detalhesExame', jsonString);
            window.location.href = '/Detalhes/Exame/';
        });
      
        desmarcarBtn.addEventListener('click', () => {
            var agendamentoDelete = data[2][index][0];
            window.location.href = `/Desmarcar/Consulta/${agendamentoDelete}`;
        });
      
        botoesContainer.appendChild(detalhesBtn);
        botoesContainer.appendChild(desmarcarBtn);
      
        novoAgendamento.appendChild(titulo);
        novoAgendamento.appendChild(dataParagrafo);
        novoAgendamento.appendChild(botoesContainer);
      
        const agendamentosContainerHistorico = document.getElementById('agendamentosClienteHistorico');
        agendamentosContainerHistorico.appendChild(novoAgendamento);
      }
  });








    
    console.log("Info Cliente:", data[0]);
    console.log("Agendamentos:", data[1]);
    console.log("Exames: data:", data[2]);
  })
  .catch(error => {
    console.error('Erro:', error);
  });





  





const navmenuItems = document.querySelectorAll('.navmenu > div');

const sections = document.querySelectorAll('.all > div');

let maxHeight = 0;
sections.forEach((section) => {
  const sectionHeight = section.offsetHeight;
  if (sectionHeight > maxHeight) {
    maxHeight = sectionHeight;
  }
});
sections.forEach((section) => {
  section.style.height = maxHeight + 'px';
});

// Adiciona um ouvinte de evento de clique a cada elemento da div navmenu
navmenuItems.forEach((item, index) => {
  item.addEventListener('click', () => {
    // Remove a classe ativa de todos os elementos da div navmenu
    navmenuItems.forEach((item) => {
      item.classList.remove('selected');
      item.style.backgroundColor = '#63A355'; // Define a cor padrão para itens não selecionados
    });

    // Adiciona a classe ativa ao elemento clicado
    item.classList.add('selected');
    item.style.backgroundColor = '#9CE38C'; // Define a cor para o item selecionado

    // Oculta todas as seções
    sections.forEach((section) => {
      section.style.display = 'none';
    });

    // Exibe a seção correspondente ao índice do elemento clicado
    sections[index].style.display = 'flex';
  });

  item.addEventListener('mouseover', () => {
    // Define a cor de hover para os itens não selecionados
    if (!item.classList.contains('selected')) {
      item.style.backgroundColor = '#407935';
    } else {
      // Define a cor de hover para os itens selecionados
      item.style.backgroundColor = '#81c27d';
    }
  });

  item.addEventListener('mouseout', () => {
    // Remove a cor de hover se não estiver selecionado
    if (!item.classList.contains('selected')) {
      item.style.backgroundColor = '#63A355';
    } else {
      // Remove a cor de hover se estiver selecionado
      item.style.backgroundColor = '#9CE38C';
    }
  });
});

// Função para remover a classe 'selected' de todos os elementos
function removeSelectedClass() {
  var elements = document.querySelectorAll('.menu nav .navmenu div');
  elements.forEach(function(element) {
    element.classList.remove('selected');
    element.style.backgroundColor = '#63A355'; // Define a cor padrão para itens não selecionados
  });
}

// Adicionando um evento de clique a cada elemento
document.getElementById("dadcontent").addEventListener("click", function() {
  if (this.classList.contains("selected")) {
    // Não faz nada se já estiver selecionado
    return;
  } else {
    // Removendo a classe 'selected' de todos os elementos
    removeSelectedClass();
    // Adicionando a classe 'selected' apenas ao elemento clicado
    this.classList.add("selected");
    // Mudando a cor do elemento dadocad
    this.style.backgroundColor = "#9CE38C";
  }
});

document.getElementById("recontent").addEventListener("click", function() {
  // Mudando a cor do elemento dadocad
  document.getElementById("dadcontent").style.backgroundColor = "#9CE38C";
  // Removendo a classe 'selected' de todos os elementos
  removeSelectedClass();
  // Adicionando a classe 'selected' apenas ao elemento clicado
  this.classList.add("selected");
});

document.getElementById("agencontent").addEventListener("click", function() {
  // Mudando a cor do elemento dadocad
  document.getElementById("dadcontent").style.backgroundColor = "#9CE38C";
  // Removendo a classe 'selected' de todos os elementos
  removeSelectedClass();
  // Adicionando a classe 'selected' apenas ao elemento clicado
  this.classList.add("selected");
});

document.getElementById("hiscontent").addEventListener("click", function() {
  // Mudando a cor do elemento dadocad
  document.getElementById("dadcontent").style.backgroundColor = "#9CE38C";
  // Removendo a classe 'selected' de todos os elementos
  removeSelectedClass();
  // Adicionando a classe 'selected' apenas ao elemento clicado
  this.classList.add("selected");
});



function calcularIdade(dataNascimento) {
  const dataAtual = new Date(); // Data atual
  const dataNasc = new Date(dataNascimento); // Data de nascimento
  
  // Calcular diferença em milissegundos entre as datas
  const diff = dataAtual.getTime() - dataNasc.getTime();
  
  // Converter diferença de milissegundos para anos
  const idade = Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25)); // Considerando anos bissextos
  
  return idade;
}



function formatDate(date) {
  const year = date.getFullYear();
  let month = date.getMonth() + 1;
  if (month < 10) {
      month = '0' + month;
  }
  let day = date.getDate();
  if (day < 10) {
      day = '0' + day;
  }
  const formattedDateString = `${year}-${month}-${day}`;
  return new Date(formattedDateString);
}

function convertToDate(dateString) {
  const [day, month, year] = dateString.split('-');
  const formattedDateString = `${year}-${month}-${day}`;
  return new Date(formattedDateString);
}


function convertToDate2(dateString) {
  const [year, month, day] = dateString.split('-');
  const formattedDateString = `${year}-${month}-${day}`;
  return new Date(formattedDateString);
}

function convertToDate3(dateString) {
  const [year, month, day] = dateString.split('-');
  const formattedDateString = `${day}-${month}-${year}`;
  return formattedDateString;
}