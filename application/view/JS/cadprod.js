$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir produto
    $(document).on("click", "#btIncluirProduto", function () {
        var form_data = new FormData($('#meuform')[0]);

        $.ajax({
            url: 'http://localhost:5000/salvar_imagem',
            type: 'POST',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                alert("Imagem salva");//informa se a mensagem foi salva
            },
            error: function(data) {
                alert(data);
            }
        });
        //pegar dados da tela
        materiais_nome = $("#campoNome").val();
        imagem =$("#campoImg").val().substr(12); 
        descricao = $("#campoDes").val();
        ativo = $("#campoStatus").val();
        data = "";
        // preparar dados no formato json
        var dados = JSON.stringify({ materiais_nome: materiais_nome, imagem: imagem, descricao: descricao, ativo:ativo, data:data });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_produto',
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
                alert("Cadastrado");
                location.reload();//recarrega a pagina
                // limpar os campos
                $("#campoNome").val();
                $("#campoImg").val();
                $("#campoDes").val();
                $("#campoStatus").val();
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