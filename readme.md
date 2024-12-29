# 📄 LaTeX CV Generator

Un generador de CV automatizado que convierte datos JSON en un PDF profesional usando LaTeX.

## 📋 Requisitos Previos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git (opcional, para clonar el repositorio)

## 🚀 Instalación

1. Clonar el repositorio (o descargar como ZIP):
```bash
git clone https://github.com/yourusername/latex-cv-generator.git
cd latex-cv-generator
```

2. Construir la imagen Docker:
```bash
docker build -t latex-cv-generator .
```

## 💻 Uso

### 1. Estructura del Proyecto
```
latex-cv-generator/
│
├── Data/
│   ├── education.json       # Información educativa
│   ├── languages.json      # Idiomas
│   ├── personal.json       # Datos personales
│   ├── profile.json        # Perfil profesional
│   ├── skills.json         # Habilidades
│   └── work_experience.json # Experiencia laboral
├── Dockerfile
├── compile_latex.py
├── cv_template.tex
└── generate_cv.py
```

### 2. Edición de Datos
Actualiza tus datos personales modificando los archivos JSON en la carpeta `Data/`. Por ejemplo:

```json
// personal.json
{
    "name": "Tu Nombre",
    "email": "tu.email@ejemplo.com",
    "phone": "+1234567890"
}
```

### 3. Generación del CV
Para generar tu CV, ejecuta:
```bash
docker run -v ${PWD}:/app latex-cv-generator
```

El PDF resultante se guardará en el directorio actual como `cv.pdf`.

## 🔄 Flujo de Trabajo Recomendado

1. Actualiza los archivos JSON en la carpeta `Data/` según necesites
2. Ejecuta el comando docker
3. Revisa el PDF generado
4. Repite según sea necesario

## ⚠️ Solución de Problemas

Si encuentras errores:

1. Asegúrate de que Docker Desktop esté ejecutándose
2. Verifica que los archivos JSON estén correctamente formateados
3. Para reconstruir la imagen desde cero:
```bash
docker rmi latex-cv-generator
docker build -t latex-cv-generator . --no-cache
```

## 🛠️ Personalización

El template LaTeX (`cv_template.tex`) puede ser modificado para cambiar el estilo del CV. Los cambios comunes incluyen:
- Fuentes
- Colores
- Espaciado
- Diseño general

## 📝 Notas

- La primera construcción puede tomar varios minutos debido a la instalación de TeXLive
- Los archivos JSON deben mantener su estructura aunque cambies el contenido
- El sistema está diseñado para ser completamente reproducible en cualquier ambiente que tenga Docker instalado

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.