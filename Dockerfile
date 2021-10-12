## Arquivo com as instruções necessárias para construção da imagem Docker ##

## Imagem Base ##

# Características da nossa imagem base:
# frolvlad -> autor dessa imagem
# alpine-miniconda3 -> é o nome dessa imagem (OS Alpine com Miniconda Python 3 já instalado)
# python3.7 -> é a tag dessa imagem (nos diz que a versão específica do Python em uso é 3.7)

# Alpine Linux é um OS desenvolvido em torno de musl, libc e busybox. Isso o torna menor e mais eficiente em termos de recursos do que as distribuições GNU/Linux tradicionais.
# O uso da tag é ótimo, pois permite criar diferentes versões de imagens semelhantes. Nesse caso, poderíamos ter essa mesma imagem com uma versão diferente do Python, como 3.5.
# poderíamos usar a imagem oficial do Python (python:3.7), mas ela é mito maior do que essa e não é necessária para o que estamos fazendo aqui

FROM frolvlad/alpine-miniconda3:python3.7

## Instalando as Dependências ##

# Vamos instalar os pacotes Python necessários em nosso servidor para realizar a predição
# O comando abaixo copia o arquivo local de requerimentos para dentro da nossa imagem

COPY requirements.txt .

# O comando RUN permite executar no terminal da nossa imagem.
# pip install -> instala os pacotes citados no arquivo anterior
# && -> indica que são dois comandos encadeados para execução no terminal
# rm -> remove esse arquivo após a conclusão da instalação, pois não precisamos mais dele

RUN pip install -r requirements.txt && \
    rm requirements.txt

## Expondo a Porta ##
# Nosso servidor irá atender as solicitações pela porta 80

EXPOSE 80

## Copiar nosso Servidor para a Imagem ##
# Copia o diretório do nosso aplicativo para a raiz do container

COPY ./app /app

## Ligando o Servidor ##
# Esse comando que será executado assim que um contêiner que usa essa imagem for iniciado. Ativará o servidor especificando o host e a porta.

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
