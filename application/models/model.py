from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json
from flask_cors import CORS
from flask_login import UserMixin, LoginManager
import os
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="secret"
db= SQLAlchemy(app)
lm=LoginManager()
lm.init_app(app)
#importa as bibliotecas necessarias 


caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "banco.db") #recebe o caminho do arquivo banco.db





@lm.user_loader 
def load_user(user_id): 
    return usuario.query.filter(usuario.id == int(user_id)).first()

class usuario (db.Model, UserMixin):#cria a tabela usuario 
    #cria as colunas
    id = db.Column(db.Integer, primary_key=True)#chave primaria
    nome_usuario=db.Column(db.String(200), nullable=False)
    senha= db.Column(db.String(20), unique=True, nullable=False)
    #nullable significa que o campo não pode ser nulo
    def __str__(self):
        return f'{str(self.id)},{self.nome_usuario}, {self.senha}'
        #retorna em string as informaçoes
    def json(self):
        return{
            "id" : self.id,
            "nome_usuario" : self.nome_usuario,
            "senha" : self.senha,
            #retorna em join as informaçoes
        }
        
class materiais (db.Model):#cria a tabela materiais
    #cria as colunas
    idmateriais = db.Column(db.Integer, primary_key=True)#chave primaria
    materiais_nome=db.Column(db.String(200), nullable=False)
    imagem=db.Column(db.String(200), nullable=False)
    descricao=db.Column(db.String(200), nullable=False)
    ativo=db.Column(db.String(200), nullable=False)
    data= db.Column(db.String(400), nullable=False)
    
    def __str__(self):
        return f'{str(self.idmateriais)}, {self.materiais_nome}, {self.imagem}, {self.descricao}, {self.ativo}, {self.data}'
    #retorna em string as informaçoes
    def json(self):
        return{
            "idmateriais" : self.idmateriais,
            "materiais_nome" : self.materiais_nome,
            "imagem" : self.imagem,
            "descricao" : self.descricao,
            "ativo" : self.ativo,
            "data" : self.data,
            #retorna em join as informaçoes
        }


class comentarios(db.Model):#cria a tabela comentarios
    #cria as colunas
    idcomentario = db.Column(db.Integer, primary_key=True)#chave primaria
    comentario=db.Column(db.String(500), nullable=False)
    material = db.Column(db.Integer, db.ForeignKey(materiais.idmateriais), nullable= False)
    Material = db.relationship("materiais", foreign_keys =  material)#chave estrangeira
    user = db.Column(db.Integer, db.ForeignKey(usuario.id), nullable= False)
    User = db.relationship("usuario", foreign_keys =  user)#chave estrangeira
    data= db.Column(db.String, nullable=False)
    # relacionamento das clases
    #nullable significa que o campo não pode ser nulo
    def __str__(self):
        return f'{str(self.idcomentario)}, {self.comentario}, {self.material}, {self.user}, {self.data}'
    #retorna em string as informaçoes
    def json(self):
        return{
            "idcomentario" : self.idcomentario,
            "comentario" : self.comentario,
            "material" : self.material,
            "usuario" : self.user,
            "data" : self.data,
            #retorna em join as informaçoes
        }
def teste():
    
    
    db.drop_all()
    db.create_all()

    Inquilinos1 =usuario(nome_usuario="Rodri", senha="fgs")
    Inquilinos2 =usuario(nome_usuario="Ezequiel", senha="ags")
    Inquilinos3 =usuario(nome_usuario="Marcoss", senha="otio")
    Inquilinos4 =materiais(materiais_nome="sxcvbn", imagem="100_0490 - Copia - Copia.jpg", descricao="rhtebvae", ativo="Ativo", data="2022-07-02")
    Inquilinos5 =comentarios(comentario="Rodrigo wilbert", material="1", user="1", data="2202")
    Inquilinos6 =comentarios(comentario="Rodrigo wilberltunkyht", material="1", user="1", data=2202)
    Inquilinos7 =comentarios(comentario="Rodrigo wilberltunkyht", material="1", user="1", data=2202)
    Inquilinos8 =comentarios(comentario="Voce não é para aparecer", material="2", user="1", data=2202)
    Inquilinos9 =comentarios(comentario="Seu nome é diferente", material="1", user="3", data="qwef")
    db.session.add_all([Inquilinos1, Inquilinos2, Inquilinos3, Inquilinos4, Inquilinos5, Inquilinos6, Inquilinos7, Inquilinos8, Inquilinos9])
    db.session.commit()       
if __name__=="__main__":#testa as classes
    if os.path.exists(arquivobd):
        os.remove(arquivobd)#remove o banco de dados se existir
        print("foi")
    db.create_all()#cria o banco de dados
    teste()
    

