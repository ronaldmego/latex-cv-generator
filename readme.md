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

### 1. Configuración Inicial

**IMPORTANTE**: Este repositorio incluye archivos de ejemplo. Para usar con tus propios datos:

1. Copia la carpeta de ejemplo:
```bash
cp -r Data-example/ Data/
```

2. Edita los archivos JSON en la carpeta `Data/` con tu información personal.

### 2. Estructura del Proyecto
```
latex-cv-generator/
│
├── Data-example/           # 📁 Datos de ejemplo (para referencia)
│   ├── education.json      # Información educativa de ejemplo
│   ├── languages.json      # Idiomas de ejemplo
│   ├── personal.json       # Datos personales de ejemplo
│   ├── profile.json        # Perfil profesional de ejemplo
│   ├── skills.json         # Habilidades de ejemplo
│   ├── work_experience.json # Experiencia laboral de ejemplo
│   └── optional_sections.json # Secciones opcionales de ejemplo
│
├── Data/                   # 📁 TUS DATOS PERSONALES (crear copiando Data-example/)
│   ├── education.json      # Tu información educativa
│   ├── languages.json      # Tus idiomas
│   ├── personal.json       # Tus datos personales
│   ├── profile.json        # Tu perfil profesional
│   ├── skills.json         # Tus habilidades
│   ├── work_experience.json # Tu experiencia laboral
│   └── optional_sections.json # Tus secciones opcionales
│
├── Dockerfile
├── compile_latex.py
├── cv_template.tex
└── generate_cv.py
```

### 3. Edición de Datos

Actualiza tus datos personales modificando los archivos JSON en la carpeta `Data/`. 

**Ejemplo de `personal.json`:**
```json
{
    "name": "Tu Nombre",
    "lastname": "Tu Apellido",
    "header": "Tu Título Profesional | Especialización | Industria",
    "linkedin_url": "https://www.linkedin.com/in/tu-perfil/",
    "github_url": "https://github.com/tu-usuario",
    "x_url": "https://tu-sitio-web.com/",
    "twitter_url": "https://x.com/tu-usuario",
    "mobile": "+1234567890",
    "email": "tu.email@ejemplo.com",
    "location": "Tu Ciudad, País"
}
```

### 4. Generación del CV

Para generar tu CV, ejecuta:
```bash
docker run -v ${PWD}:/app latex-cv-generator
```

El PDF resultante se guardará en el directorio actual como `cv.pdf`.

## 🔒 Privacidad y Seguridad

- **Archivos ignorados**: Los archivos `cv.pdf`, `cv.tex` y la carpeta `Data/` están en `.gitignore` para proteger tu privacidad
- **Datos de ejemplo**: La carpeta `Data-example/` contiene datos ficticios para mostrar la estructura
- **Tus datos**: Nunca se subirán al repositorio automáticamente

## 🔄 Flujo de Trabajo Recomendado

1. Copia `Data-example/` a `Data/`
2. Actualiza los archivos JSON en la carpeta `Data/` con tu información
3. Ejecuta el comando docker
4. Revisa el PDF generado (`cv.pdf`)
5. Repite según sea necesario

## 📝 Estructura de los Archivos JSON

### personal.json
Información de contacto y datos básicos.

### profile.json
Descripción profesional y resumen de carrera.

### education.json
Historial educativo con fechas, instituciones y detalles.

### work_experience.json
Experiencia laboral con fechas, empresas, títulos y logros.

### skills.json
Habilidades técnicas organizadas por categorías.

### languages.json
Idiomas con niveles de dominio.

### optional_sections.json
Certificaciones, proyectos, publicaciones, etc.

## ⚠️ Solución de Problemas

Si encuentras errores:

1. Asegúrate de que Docker Desktop esté ejecutándose
2. Verifica que los archivos JSON estén correctamente formateados
3. Confirma que la carpeta `Data/` existe y contiene todos los archivos necesarios
4. Para reconstruir la imagen desde cero:
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
- **Recuerda**: Nunca subas tu carpeta `Data/` personal al repositorio

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.