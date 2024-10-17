FROM python:3.13.0-slim-bookworm

# Expor a porta da aplicação
EXPOSE 5000

# Definir o diretório de trabalho
WORKDIR /app

# Copiar requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copiar o código da aplicação
COPY app.py .

# Comando para rodar a aplicação
CMD ["python3", "app.py"]
