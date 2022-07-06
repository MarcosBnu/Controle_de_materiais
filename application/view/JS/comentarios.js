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
        // Desenvolvi toda essa função para order a lista pelas datas
        l=true
        n=0
        t=0
        var datas = []
        r_aux=true
        while(l){
            n=0
            if(r_aux){
                for (var i in con){
                    n=n+1
                    xxn=con[i].data
                    xxn.substr(0,23)
                    xxn=xxn.replace("-","900000000000009")
                    xxn=xxn.replace("-","900000000000009")
                    xxn=xxn.replace(" ","911111111111119")
                    xxn=xxn.replace(":","922222222222229")
                    xxn=xxn.replace(":","922222222222229")
                    xxn=xxn.replace(".","933333333333339")
                    datas.push(xxn)
                    datas.sort()
                    r_aux=false
                }
            }
            dodo=datas.at(-1)
            for (var i in con) { //i vale a posição no vetor
                dodo=dodo.replace("900000000000009","-")
                dodo=dodo.replace("900000000000009","-")
                dodo=dodo.replace("911111111111119"," ")
                dodo=dodo.replace("922222222222229",":")
                dodo=dodo.replace("922222222222229",":")
                dodo=dodo.replace("933333333333339",".")
                //manipulei as stings para ordenalas na lista, depois coloquei de novo os pontos e caracteres para comparar a lsita com o json
                decisor=con[i].data
                if (decisor==dodo){
                    t=t+1
                    datas.pop()
                    lin=
                    '<div class="card mb-3" style="margin-left:20%; margin-right:20%; margin-top:1%; max-width: 50rem;">'+
                        '<div class="row g-0">'+
                            '<div class="col-md-8">'+
                            '<div class="card-body">'+
                                '<h5 class="card-title">' + con[i].usuario +':</h5>'+
                                '<p class="card-text">' + con[i].comentario +'</p>'+
                                '<p class="card-text"><small class="text-muted">cadastrado no dia: ' + decisor +'</small></p>'+
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
        if (n==t){
            l=false
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
        // solicitar a exclusao do material
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
    // código para mapear click do botão incluir comentario
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
                alert("Sucesso! Comentário cadastrado para o material.");
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