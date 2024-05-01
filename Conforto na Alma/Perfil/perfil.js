// Obtém todos os elementos da div navmenu
const navmenuItems = document.querySelectorAll('.navmenu > div');

// Obtém todas as seções
const sections = document.querySelectorAll('.all > div');

// Define uma altura fixa para todas as seções
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