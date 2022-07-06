from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, jsonify, request, send_file
from flask_cors import CORS
from flask_login import login_user, current_user
from models.model import *
import datetime
import os
#importa as bibliotecas


path = os.path.dirname(os.path.abspath(__file__))
np=[] #Lista para guardar o id do usuario quando logado
Lista_mat=[] #Lista para guardar o id do material quando solicitado

@app.route("/login_usuario", methods=["GET", "POST"])
def login_usuario():#função para o usuario logar
    dados = request.get_json() # receber as informações 
    np.clear() #limpa a lista
    userlogin = db.session.query(usuario)\
        .filter(usuario.id==dados['Vid'], usuario.senha==dados['VSenha'])\
        .first() #busca no banco de dados as informaçoes
    if userlogin:
        login_user(userlogin, remember=True)
        if userlogin.is_authenticated==True:#se o login foi feito
            np.append(current_user.id)#coloca na lista o valor da id do usuario, valor necessario para operar as outras rotas
            resposta=jsonify({"resultado":"ok", "detalhes":np})#mensagem de Ok
        else:
            resposta=jsonify({"resultado":"erro", "detalhes":"erro"})#informa a mensagem de erro
    else:
        # informar mensagem de erro
        resposta=jsonify({"resultado":"erro", "detalhes":"erro"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_produto", methods=["post"])
def incluir_produto():
    # preparar uma resposta otimista
    resposta_cad = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    Cadados = request.get_json() 
    data=datetime.datetime.now()#recebe a data e a hora atual
    Cadados["data"]=data
    try:  # tentar executar a operação
        novaCad = materiais(**Cadados)  # criar a nova pessoa
        db.session.add(novaCad)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta_cad = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta_cad.headers.add("Access-Control-Allow-Origin", "*")
    return resposta_cad  # responder!
#Rota para salvar a imagem
@app.route("/salvar_imagem", methods=['POST'])
def salvar_imagem():
    r = jsonify({"mensagem":"tentando..."})
    if request.method == 'POST':
        file_val = request.files['capa']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(path, '../Imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"mensagem":"ok", "arquivo": file_val.filename})
    r.headers.add("Access-Control-Allow-Origin", "*")
    return r
#rota para buscar a imagem salva
@app.route('/get_image/<int:id_img>')
def get_image(id_img):
    if id_img==9999999999999:
        id_img=Lista_mat[0]
    mat = db.session.query(materiais).get(id_img)   
    arquivoimg = os.path.join(path, '../Imagens/'+ mat.imagem)
    return send_file(arquivoimg, mimetype='image/gif', cache_timeout=0)

@app.route("/listar_material")
def listar_material():
    Lista_mat.clear()
    # obter as material do cadastro
    material = db.session.query(materiais).all()
    # aplicar o método json que a classe material possui a cada elemento da lista
    material_em_json = [ x.json() for x in material ]
    # converter a lista do python para json
    resposta = jsonify(material_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_comentarios/<int:id_material>", methods=["GET", "POST"]) 
def listar_comentarios(id_material):
    Lista_mat.clear()#limpa a lisa de material, para evitar erros
    Lista_mat.append(id_material)#adiciona a id do material solicitado na lsta
    if Lista_mat!="" and Lista_mat!=None:#Para verificar se a lista não ficou vazia
        resposta = jsonify({"mensagem":"ok", "resultado":"Foi"})
    else:
        resposta = jsonify({"mensagem":"erro", "resultado":"erro"})
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/listar_com")
def listar_com():
    valor=Lista_mat[0]
    com = db.session.query(comentarios).filter_by(material=valor).all()
    # aplicar o método json que a classe material possui a cada elemento da lista
    comentarios_em_json = [ x.json() for x in com]
    for i in comentarios_em_json:
        nomes = db.session.query(usuario).filter_by(id=i['usuario']).all()
        nomes_em_json = [ x.json() for x in nomes]
        for j in nomes_em_json:
            #troca o id do usuario pelo seu nome, para operar a listagem
            i['usuario']=j['nome_usuario']
    # converter a lista do python para json
    res = jsonify(comentarios_em_json)
    # PERMITIR res para outras pedidos oriundos de outras tecnologias
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res # retornar...

@app.route("/incluir_Comentario", methods=["POST"])
def incluir_Comentario():
    # preparar uma resposta otimista
    resposta_com = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações
    Cadados = request.get_json() 
    data=datetime.datetime.now()
    Cadados["data"]=data
    Cadados["material"]=Lista_mat[0]
    Cadados["user"]=np[0]
    try:  # tentar executar a operação
        novaCad = comentarios(**Cadados)  # criar o novo comentario
        db.session.add(novaCad)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta_com = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta_com.headers.add("Access-Control-Allow-Origin", "*")
    return resposta_com  # responder!

#rota para apagar o material, recebe o id do material 
@app.route("/cont_del/<int:id_mat>", methods=["DELETE"]) 
def cont_del(id_mat):
    Lista_mat.clear()#limpa a lista para evitar erros
    try:
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        comentarios.query.filter(comentarios.material == id_mat).delete() # excluir os comentario do ID informado
        materiais.query.filter(materiais.idmateriais == id_mat).delete() # excluir o material do ID informado
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
        # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!


