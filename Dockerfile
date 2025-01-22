FROM texlive/texlive:latest

# Instalar Python y otras dependencias
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && apt-get clean

# Establecer el directorio de trabajo
WORKDIR /app

# Crear un entorno virtual
RUN python3 -m venv /app/venv

# Activar el entorno virtual e instalar las dependencias
COPY requirements.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Agregar el entorno virtual al PATH
ENV PATH="/app/venv/bin:$PATH"

# Copiar el resto de los archivos al contenedor
COPY . .

# Configurar el script de entrada
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
