# Usar uma imagem base do Python
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    openjdk-11-jdk

# Instalar dependências Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Configurar Java para Spark
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/"
ENV PATH="$JAVA_HOME/bin:$PATH"
