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
    senha= db.Column(db.String(20), nullable=False)
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
    materiais_nome=db.Column(db.String, nullable=False)
    imagem=db.Column(db.String, nullable=False)
    descricao=db.Column(db.String, nullable=False)
    ativo=db.Column(db.Integer, nullable=False)
    data= db.Column(db.String, nullable=False)
    
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
    Material = db.relationship("materiais")#chave estrangeira
    user = db.Column(db.Integer, db.ForeignKey(usuario.id), nullable= False)
    User = db.relationship("usuario")#chave estrangeira
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
#função para colocar no banco de dados as informaçoes necessarias
def teste():
    
    
    db.drop_all()
    db.create_all()

    Us1 =usuario(nome_usuario="Rodri", senha="111111")
    Us2 =usuario(nome_usuario="Ezequiel", senha="212121")
    Us3 =usuario(nome_usuario="Marcos", senha="414141")
    Us4 =usuario(nome_usuario="Igor", senha="313131")
    Mt1 =materiais(materiais_nome="Processador Intel Core i9-7920X Skylake, Cache 16.5MB, 2.9GHz (4.3GHz Max Turbo), LGA 2066 - BX80673I97920X", imagem="Intel_Core_i9.png", descricao="Com esse processador inovador e incrível você desfruta ao máximo o verdadeiro potencial do seu computador e desfruta da mais pura velocidade. Maximize o seu desempenho seja trabalhando, jogando, navegando ou assistindo o seu filme preferido, com esse processador você pode tudo!", ativo=1, data="2021-11-25 14:00:00.01")
    Mt2 =materiais(materiais_nome="Monitor, Dell, U2518D, UltraSharp, Preto e Suporte em Alumínio, 25", imagem="Monitor_Dell.png", descricao="Dê vida ao seu trabalho com uma tela de 25 polegadas quase sem bordas que conta com detalhes em cores vívidas e consistentes graças a tecnologia hdr, resolução qhd e ângulo de visão ultra-amplo. Aumente sua performance com os recursos dell display manager, dell easy arrange e trabalhe confortavelmente graça a um suporte totalmente ajustável e recurso confortview.", ativo=0, data="2021-11-12 15:30:00.02")
    Mt3 =materiais(materiais_nome="Mouse Gamer Razer Deathadder Essential Óptico 5 Botões 4G 6.400 DPI", imagem="Mouse_Razer.png", descricao="Nada melhor do que um mouse gamer com tecnologia de ponta para qualificar seus comandos e aprimorar suas jogadas nos games. Com este Mouse Gamer Razer, sua atuação nas batalhas gamers serão ainda mais bem-sucedidas, com desempenho acima da média e desenvoltura arrasadora, que vai deixar seus oponentes impressionados. O mouse Razer Deathadder Essential tem sensor óptico de 6400 DPI de 4G, 5 botões, design moderno e ergonômico, especialmente projetado para jogadores destros, e uma empunhadura lateral emborrachada que garante mais firmeza ao manuseio do equipamento, melhorando as respostas obtidas pelos players. O mouse Razer ainda oferece ajuste de sensibilidade, pezinhos Ultraslick silenciosos, cabo ultra resistente de fibra trançada e Modo Always-On, que mantém o mouse ligado mesmo quando o equipamento estiver inativo. É um mouse gamer Razer para ninguém botar defeito, com todas as funções e especificações técnicas que você precisa para ter mais produtividade nos jogos. O Razer Deathadder Essential é realmente essencial e ainda tem o diferencial de estar habilitado para Razer Synapse 3 e de ser compatível com PC e Mac, com porta USB. Conheça o modelo e faça um investimento seguro!", ativo=1, data="2021-11-07 16:00:00.03")
    Mt4 =materiais(materiais_nome="All-in-One Media Keyboard", imagem="Teclado_Microsoft.png", descricao="O All-in-One Media Keyboard é o dispositivo ideal para sua sala ou home office. Com teclado em tamanho natural e trackpad multitoque integrado, é possível digitar, passar o dedo, arrastar, fazer zoom e clicar facilmente. O teclado com teclas de atalho de mídia personalizáveis permite que a Web e suas músicas, fotos e filmes favoritos estejam a seu alcance. O teclado também tem um design resistente, portanto, não é necessário se preocupar com esbarrões, quedas ou derramamentos comuns. O All-in-One Media Keyboard é tudo o que você precisa para digitar confortavelmente e navegar sem esforço.", ativo=0, data="2021-11-11 17:54:00.04")
    Con1 =comentarios(comentario="Deverá fazer o download do aplicativo da razer para alterar a cor do mouse.", material="2", user="4", data="2021-11-07 18:00:00.000")
    Con2 =comentarios(comentario="Problema de aquecimento no processador após 1 ano de uso.", material="2", user="2", data="2021-11-04 07:30:00.000")
    db.session.add_all([Us1, Us2, Us3, Us4, Mt1, Mt2, Mt3, Mt4, Con1, Con2])#adiciona as infomaçoes no banco de dados
    db.session.commit() #confimar a operação   
if __name__=="__main__":#testa as classes
    if os.path.exists(arquivobd):
        os.remove(arquivobd)#remove o banco de dados se existir
        print("foi")
    db.create_all()#cria o banco de dados
    teste()#chama a função teste
    

