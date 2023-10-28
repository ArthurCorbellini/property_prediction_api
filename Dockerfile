FROM tensorflow/tensorflow
LABEL maintainer="propertyprediction.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN \
    # Cria um ambiente virtual Python na pasta /py
    python -m venv /py && \
    # O Python pip é atualizado para a versão mais recente dentro do ambiente 
    # virtual.
    /py/bin/pip install --upgrade pip && \
    # pip dentro do ambiente virtual para instalar as dependências Python 
    # listadas no arquivo /tmp/requirements.txt.
    /py/bin/pip install -r /tmp/requirements.txt && \
    # Inicia-se uma estrutura condicional em que o código a seguir será 
    # executado apenas se a variável de ambiente $DEV for igual a "true".
    #   Dentro da estrutura condicional, se $DEV for igual a "true", ele 
    #   usa o pip dentro do ambiente virtual para instalar as dependências
    #   de desenvolvimento listadas no arquivo /tmp/requirements.dev.txt.
    if [ $DEV = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    # Remove recursivamente o diretório /tmp e seu conteúdo. Isso é feito 
    # para limpar os arquivos temporários que foram usados durante a 
    # instalação de dependências.
    rm -rf /tmp && \
    # Cria um usuário chamado django-user no sistema, com senha desabilitada 
    # (--disabled-password) e sem a criação de diretório home (--no-create-home). 
    # Esse usuário pode ser usado para executar o aplicativo Python de forma 
    # mais segura, limitando as permissões.
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user
