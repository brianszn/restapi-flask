FROM python:3.13.0-slim-bookworm

# expor a porta
EXPOSE 5000

# diretório do meu app
WORKDIR /app

# copiar o requirements.txt e instalar
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copiar o código da aplicação
COPY app.py .

# rodar a minha aplicação que ja inicia o server automático
CMD ["python3", "app.py"]
