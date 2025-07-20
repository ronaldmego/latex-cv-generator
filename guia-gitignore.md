# 🔄 Guía de Migración

Esta guía te ayudará a migrar desde la estructura actual del proyecto a la nueva estructura con datos de ejemplo.

## 📋 Cambios Realizados

### 1. Archivos Agregados al .gitignore
- `cv.pdf` - Tu CV generado
- `cv.tex` - Archivo LaTeX generado
- `Data/` - Carpeta con tus datos personales

### 2. Nueva Carpeta de Ejemplo
- `Data-example/` - Contiene datos ficticios para mostrar la estructura

## 🚀 Pasos para Migrar

### Opción 1: Mantener tus datos actuales (Recomendado)

1. **Hacer backup de tus datos actuales:**
```bash
cp -r Data/ Data-backup/
```

2. **Crear la carpeta de ejemplo:**
```bash
cp -r Data-example/ Data-example-backup/
```

3. **Verificar que tus datos están protegidos:**
```bash
git status
```
No deberías ver `Data/`, `cv.pdf`, o `cv.tex` en los archivos a commitear.

### Opción 2: Usar datos de ejemplo

1. **Eliminar tus datos actuales:**
```bash
rm -rf Data/
```

2. **Copiar datos de ejemplo:**
```bash
cp -r Data-example/ Data/
```

3. **Editar con tu información:**
Edita los archivos en `Data/` con tu información personal.

## 🔍 Verificación

Para verificar que todo está configurado correctamente:

1. **Verificar .gitignore:**
```bash
cat .gitignore | grep -E "(cv\.pdf|cv\.tex|Data/)"
```

2. **Verificar que tus datos no se subirán:**
```bash
git status
```

3. **Probar la generación:**
```bash
docker run -v ${PWD}:/app latex-cv-generator
```

## ⚠️ Notas Importantes

- **Nunca hagas commit de la carpeta `Data/`** - contiene tu información personal
- **Siempre haz backup** antes de hacer cambios importantes
- **Los datos de ejemplo** están diseñados para mostrar la estructura, no para uso real
- **El archivo `cv.pdf`** se regenera cada vez que ejecutas el generador

## 🆘 Si algo sale mal

Si accidentalmente subiste datos personales:

1. **Eliminar del historial de Git:**
```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch Data/*' --prune-empty --tag-name-filter cat -- --all
```

2. **Forzar push:**
```bash
git push origin --force
```

3. **Regenerar .gitignore:**
Verifica que el archivo `.gitignore` contenga las reglas correctas.

## 📞 Soporte

Si tienes problemas con la migración, puedes:
1. Revisar el README.md actualizado
2. Abrir un issue en el repositorio
3. Usar los datos de ejemplo como punto de partida 