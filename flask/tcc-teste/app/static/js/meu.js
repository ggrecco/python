$(function (){

  var intervalo = setInterval(function (){
    clearInterval(intervalo);

    document.getElementById("carregando").style.display = "none";
    document.getElementById("corpo").style.display = "block";
  },500);
});

function clickLoad(){
  document.getElementById("corpo").style.display = "none";
  document.getElementById("carregando").style.display = "block";
}

// criei uma função css que deixa sempre a tela de load e esconte o conteudo da pagina.
// criei função javaScript que retira essa tela e carrega o conteúdo.
// criei uma outra função para que a cada click seja carregada a tela de laod;
