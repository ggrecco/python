var vals;

$('#bt-ok').click(function() {
    vals = [];
    $("input[type='checkbox']:checked").each(function(){
        vals.push($(this).prop('name'));
    });
    $("#text").val(vals.join(', '));
});


$('#area').click(function(){
    vals = [];
    vals = $('#text').text();
    $.ajax({
    type: "POST",
    url: '/listar',
    data: vals
    });
});

$('.value-plus').on('click', function() {
    // var valores = document.querySelector(" table tr td span ");
    var valores = document.querySelectorAll("table tr td span#nota");
    for (i = 0; i < valores.length; i++) {
        // console.log(valores[i].innerHTML);
        n = valores[i].innerHTML;
        console.log('n');
        console.log(n);
        if (n > 8.0) {
            n.style.color = "red";
        } else {
            n.style.color = "blue";
        }
    }
})

// usando jquery
$("#exibir").click(function(event){
    alert("Funciona!");
})
