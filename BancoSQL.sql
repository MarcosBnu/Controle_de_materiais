CREATE TABLE usuario(
id int not NULL,
nome_usuario VARCHAR(200),
senha VARCHAR(20),
PRIMARY key(id)
);

CREATE TABLE materiais(
idmateriais int not NULL,
materiais_nome VARCHAR not NULL,
imagem VARCHAR not NULL,
descricao VARCHAR not NULL,
ativo int not NULL,
data VARCHAR not NULL, 
PRIMARY key(idmateriais)
);

CREATE TABLE comentarios(

idcomentario int NOT NULL,
comentario VARCHAR(500) NOT NULL,
material int NOT NULL,
user int NOT NULL,
data VARCHAR NOT NULL,
PRIMARY key(idcomentario),
FOREIGN key (material) references materiais (idmateriais),
FOREIGN key (user) references usario (id)
);

INSERT INTO usuario VALUES(1, 'Rodri', '111111');
INSERT INTO usuario VALUES(2, 'Ezequiel', '212121');
INSERT INTO usuario VALUES(3, 'Marcos', '414141');
INSERT INTO usuario VALUES(4, 'Igor', '313131');
INSERT INTO materiais VALUES(1, 'Processador Intel Core i9-7920X Skylake, Cache 16.5MB, 2.9GHz (4.3GHz Max Turbo), LGA 2066 - BX80673I97920X', 'Intel_Core_i9.png', 'Com esse processador inovador e incrível você desfruta ao máximo o verdadeiro potencial do seu computador e desfruta da mais pura velocidade. Maximize o seu desempenho seja trabalhando, jogando, navegando ou assistindo o seu filme preferido, com esse processador você pode tudo!', 1, '2021-11-25 14:00:00.01');
INSERT INTO materiais VALUES(2, 'Monitor, Dell, U2518D, UltraSharp, Preto e Suporte em Alumínio, 25', 'Monitor_Dell.png', 'Dê vida ao seu trabalho com uma tela de 25 polegadas quase sem bordas que conta com detalhes em cores vívidas e consistentes graças a tecnologia hdr, resolução qhd e ângulo de visão ultra-amplo. Aumente sua performance com os recursos dell display manager, dell easy arrange e trabalhe confortavelmente graça a um suporte totalmente ajustável e recurso confortview.', 0, '2021-11-12 15:30:00.02');
INSERT INTO materiais VALUES(3, 'Mouse Gamer Razer Deathadder Essential Óptico 5 Botões 4G 6.400 DPI', 'Mouse_Razer.png', 'Nada melhor do que um mouse gamer com tecnologia de ponta para qualificar seus comandos e aprimorar suas jogadas nos games. Com este Mouse Gamer Razer, sua atuação nas batalhas gamers serão ainda mais bem-sucedidas, com desempenho acima da média e desenvoltura arrasadora, que vai deixar seus oponentes impressionados. O mouse Razer Deathadder Essential tem sensor óptico de 6400 DPI de 4G, 5 botões, design moderno e ergonômico, especialmente projetado para jogadores destros, e uma empunhadura lateral emborrachada que garante mais firmeza ao manuseio do equipamento, melhorando as respostas obtidas pelos players. O mouse Razer ainda oferece ajuste de sensibilidade, pezinhos Ultraslick silenciosos, cabo ultra resistente de fibra trançada e Modo Always-On, que mantém o mouse ligado mesmo quando o equipamento estiver inativo. É um mouse gamer Razer para ninguém botar defeito, com todas as funções e especificações técnicas que você precisa para ter mais produtividade nos jogos. O Razer Deathadder Essential é realmente essencial e ainda tem o diferencial de estar habilitado para Razer Synapse 3 e de ser compatível com PC e Mac, com porta USB. Conheça o modelo e faça um investimento seguro!', 1, '2021-11-07 16:00:00.03');
INSERT INTO materiais VALUES(4, 'All-in-One Media Keyboard', 'Teclado_Microsoft.png', 'O All-in-One Media Keyboard é o dispositivo ideal para sua sala ou home office. Com teclado em tamanho natural e trackpad multitoque integrado, é possível digitar, passar o dedo, arrastar, fazer zoom e clicar facilmente. O teclado com teclas de atalho de mídia personalizáveis permite que a Web e suas músicas, fotos e filmes favoritos estejam a seu alcance. O teclado também tem um design resistente, portanto, não é necessário se preocupar com esbarrões, quedas ou derramamentos comuns. O All-in-One Media Keyboard é tudo o que você precisa para digitar confortavelmente e navegar sem esforço.', 0, '2021-11-11 17:54:00.04');
INSERT INTO comentarios VALUES(1, 'Deverá fazer o download do aplicativo da razer para alterar a cor do mouse.', 2, 4, "2021-11-04 07:30:00.000");
INSERT INTO comentarios VALUES(2, 'Problema de aquecimento no processador após 1 ano de uso.', 2, 2, "2021-11-04 07:30:00.000");