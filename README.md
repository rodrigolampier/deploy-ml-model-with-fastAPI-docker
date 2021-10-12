# deploy-ml-model-with-fastAPI-docker
Vamos implantar um servidor Web que hospeda um modelo preditivo para classificação de vinhos, usando FastApi e Docker.

## Por que não usar o Tensorflow Serving?
Nem todos os modelos com os quais você trabalhará serão escritos no Tensorflow, eles podem nem mesmo ser modelos de Deep Learning. O TFS é uma ótima opção ao trabalhar com o Tensorflow, mas na maioria das vezes você precisará da flexibilidade extra que vem com a codificação do servidor da Web por conta própria.


## Docker - Construção da imagem
Na pasta do projeto execute o comando abaixo em um terminal para construção da imagem Docker.

docker build -t img-classificador-vinho:versao-1 .


## Docker - Executando o Container
No mesmo terminal da etapa anterior, execute o comando abaixo para inicializar um container com a imagem criada acima. Note que estamos passando o parametro "--rm", que vai eliminar esse container no momento que o mesmo for desligado e também estamos mapeando a porta 8080 do host local para a porta 80 do container.

docker run --rm -p 8080:80 img-classificador-vinho:versao-1


## Cliente Embutido
O FastAPI tem um cliente embutido para interagir com o servidor. Podemos usá-lo acessando o link abaixo e passar os casos de exemplo que temos no campo "Request body".

http://localhost:8080/docs

