$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão de login
    $(document).on("click", "#btLoginusuario", function () {
        //pegar dados da tela
        Vid = $("#campoVid").val();
        VSenha = $("#campoVSenha").val();
        // preparar dados no formato json
        var dados = JSON.stringify({Vid: Vid, VSenha: VSenha});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/login_usuario',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: login_usuario, // chama a função login_usuario para processar o resultado
            error: erroAoIncluir
        });
        function login_usuario (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // redireciona a guia
                window.location.href = 'material.html';
                // limpar os campos
                $("#campoVid").val();
                $("#campoVSenha").val();
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