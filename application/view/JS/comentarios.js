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
        n=0
        t=0
        somador_aux = true  
        while(l){
            n=0
            if(somador_aux){
                somador_aux = false
                for (var i in con){
                    n=n+1
                    if (con[i].idcomentario!="")
                        aux=con[i].idcomentario
                        somador_aux = false
                }
            }
            else {
                l=false
            }
            for (var i in con) { //i vale a posição no vetor
                if (con[i].idcomentario==aux){
                    t=t+1
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
                            '</div>'+
                            '</div>'+
                        '</div>'+
                    '</div>';
                    $('#listarcm').append(lin);
                    if (n==t){
                        l=false
                    }
            }
        }
        }
}});


$(function() { // quando o documento estiver pronto/carregado
    $(document).on("click", ".deletar_comentario", function() {
        // obter o ID do ícone que foi clicado
        var componente_clicado = $(this).attr('id'); 
        // no id do ícone
        var nome_icone = "deletar_";
        var id_comen = componente_clicado.substring(nome_icone.length);
        alert(id_comen)
        // solicitar a edição da despesa
        $.ajax({
            url: 'http://localhost:5000/cont_del/'+id_comen,
            type: 'DELETE', // método da requisição
            dataType: 'json', // os dados são recebidos no formato json
            success: pessoasalva, // chama a função pessoasalva para processar o resultado
            error: erroAosalvar
        });
        function pessoasalva (retorno) {
            location.reload();//recarrega a pagina
        }
        function erroAosalvar (retorno) {
            // informar mensagem de erro
            alert("erro");
        }
    });
});


$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirComentarios", function () {
        //pegar dados da tela
        comentario = $("#textCom").val();
        material = ""
        user= ""
        data= ""
        // preparar dados no formato json
        var dados = JSON.stringify({ comentario: comentario, material: material, user: user, data: data});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_Comentario',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: incluir_livro, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function incluir_livro (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Comentario cadastrado com sucesso!");
                window.location.href = 'material.html';//redireciona a pagina
                // limpar os campos
                $("#textCom").val();

            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});