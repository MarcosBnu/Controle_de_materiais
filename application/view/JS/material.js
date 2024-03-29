$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_material',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (mat) {
        // percorrer a lista de mat retornadas;
        for (var i in mat) { //i vale a posição no vetor   
            lin=
            '<div class="card mb-3" style="margin-left:20%; margin-right:20%; margin-top:5%; max-width: 50rem;">'+
                '<div class="row g-0">'+
                    '<div class="col-md-4">'+
                        '<img src="http://localhost:5000/get_image/'+mat[i].idmateriais+'" class="img-fluid rounded-start" alt="...">'+
                    '</div>'+
                    '<div class="col-md-8">'+
                    '<div class="card-body">'+
                        '<h5 class="card-title">' + mat[i].materiais_nome +'</h5>'+
                        '<p class="card-text">' + mat[i].descricao +'</p>'+
                        '<p class="card-text"><small class="text-muted">cadastrado no dia: ' + mat[i].data +'</small></p>'+
                        '<br>'+
                        '<a href="#" class="listar_comentarios" id="editar_' + mat[i].idmateriais +'"><img src="../../imagens/comentario.png" alt="..."></a>'+
                        '<a href="#" class="deletar_comentario" id="deletar_' + mat[i].idmateriais +'"><img src="../../imagens/deletar.png" alt="..."></a>'+
                    '</div>'+
                    '</div>'+
                '</div>'+
            '</div>';
            // adiciona a linha no corpo da tabela se for ativo
            if (mat[i].ativo== 0 || mat[i].ativo== "0")
             $('#listarmat').append(lin);
        }
    }

});

$(function() { // quando o documento estiver pronto/carregado
    $(document).on("click", ".deletar_comentario", function() {
        // obter o ID do ícone que foi clicado
        var componente_clicado = $(this).attr('id'); 
        // no id do ícone
        var nome_icone = "deletar_";
        var id_mat = componente_clicado.substring(nome_icone.length);
        // solicitar a exclusao da despesa
        $.ajax({
            url: 'http://localhost:5000/cont_del/'+id_mat,
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

$(function() { // quando o documento estiver pronto/carregado
    $(document).on("click", ".listar_comentarios", function() {
        // obter o ID do ícone que foi clicado
        var componente_clicado = $(this).attr('id'); 
        // no id do ícone
        var nome_icone = "editar_";
        var id_material = componente_clicado.substring(nome_icone.length);
        // solicitar a edição da despesa
        $.ajax({
            url: 'http://localhost:5000/listar_comentarios/'+id_material,
            type: 'POST', // método da requisição
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: pessoasalva, // chama a função pessoasalva para processar o resultado
            error: erroAosalvar
        });
        function pessoasalva (retorno) {
            if (retorno.resultado == "Foi") { // a operação deu certo?
                // redireciona a guia
                window.location.href = 'comentarios.html';
                // limpar os campos
        }}
        function erroAosalvar (retorno) {
            // informar mensagem de erro
            alert("erro");
        }
    });
});