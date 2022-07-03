$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_com',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (con) {
        // percorrer a lista de con retornadas;
        l=true
        aux=0
        somador_aux = true
        while(l){
            if(somador_aux){
                for (var i in con){
                    if (con[i].idcomentario!="")
                        aux=con[i].idcomentario
                        somador_aux = false
                }
            }
            for (var i in con) { //i vale a posição no vetor
                if (con[i].idcomentario==aux){
                    aux1=aux-1
                    con[i].idcomentario=""
                    somador_aux = true
                    lin=
                    '<div class="card mb-3" style="margin-left:20%; margin-right:20%; margin-top:1%; max-width: 50rem;">'+
                        '<div class="row g-0">'+
                            '<div class="col-md-8">'+
                            '<div class="card-body">'+
                                '<h5 class="card-title">' + con[i].usuario +':</h5>'+
                                '<p class="card-text">' + con[i].comentario +'</p>'+
                                '<p class="card-text"><small class="text-muted">cadastrado no dia: ' + con[i].data +'</small></p>'+
                                '<br>'+
                                '<a href="#" class="listar_comentarios" id="editar_' + con[i].idmateriais +'"><img src="../../imagens/comentario.png" alt="..."></a>'+
                            '</div>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                    $('#listarcm').append(lin);
                    if (aux1==0){
                        l=false
                    }
            }
        }
        }
}});


$(function() { // quando o documento estiver pronto/carregado
    // percorrer a lista de mat retornadas;
    lin='<img src="http://localhost:5000/get_cont" class="img-fluid rounded-start" style="max-width: 550px; margin-left:20%; margin-right:20%; margin-top:3%; border-radius:15%"; alt="...">';
    $('#listarimg').append(lin);
}
);