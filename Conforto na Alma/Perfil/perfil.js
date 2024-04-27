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
      item.classList.remove('active');
    });

    // Adiciona a classe ativa ao elemento clicado
    item.classList.add('active');

    // Oculta todas as seções
    sections.forEach((section) => {
      section.style.display = 'none';
    });

    // Exibe a seção correspondente ao índice do elemento clicado
    sections[index].style.display = 'flex';
  });
});


    // Função para remover a classe 'selected' de todos os elementos
    function removeSelectedClass() {
      var elements = document.querySelectorAll('.menu nav .navmenu div');
      elements.forEach(function(element) {
          element.classList.remove('selected');
      });
  }

  // Adicionando um evento de clique a cada elemento
  document.getElementById("dadcontent").addEventListener("click", function() {
      if (this.classList.contains("selected")) {
          this.classList.remove("selected");
          this.style.backgroundColor = "#9CE38C"; // restaura a cor original
      } else {
          // Removendo a classe 'selected' de todos os elementos
          removeSelectedClass();
          // Adicionando a classe 'selected' apenas ao elemento clicado
          this.classList.add("selected");
          // Mudando a cor do elemento dadocad
          this.style.backgroundColor = "#63A355";
      }
  });

  document.getElementById("recontent").addEventListener("click", function() {
      // Mudando a cor do elemento dadocad
      document.getElementById("dadcontent").style.backgroundColor = "#63A355";
      // Removendo a classe 'selected' de todos os elementos
      removeSelectedClass();
      // Adicionando a classe 'selected' apenas ao elemento clicado
      this.classList.add("selected");
  });

  document.getElementById("agencontent").addEventListener("click", function() {
      // Mudando a cor do elemento dadocad
      document.getElementById("dadcontent").style.backgroundColor = "#63A355";
      // Removendo a classe 'selected' de todos os elementos
      removeSelectedClass();
      // Adicionando a classe 'selected' apenas ao elemento clicado
      this.classList.add("selected");
  });

  document.getElementById("hiscontent").addEventListener("click", function() {
      // Mudando a cor do elemento dadocad
      document.getElementById("dadcontent").style.backgroundColor = "#63A355";
      // Removendo a classe 'selected' de todos os elementos
      removeSelectedClass();
      // Adicionando a classe 'selected' apenas ao elemento clicado
      this.classList.add("selected");
  });