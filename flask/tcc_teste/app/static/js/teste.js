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
