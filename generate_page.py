# generate_index.py - Actualizado para generar background.md con el nuevo formato
import os
import json

def escape_markdown_special_chars(text):
    """Escape Markdown special characters, except for parentheses."""
    if text is None:
        return ""
    special_chars = {
        "_": "\\_",
        "*": "\\*",
        "[": "\\[",
        "]": "\\]"
    }
    for char, escape in special_chars.items():
        text = text.replace(char, escape)
    return text

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON from {file_path}: {e}")
        raise

# Directorios y rutas de archivos
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'Data')

# Rutas de los archivos JSON de entrada
profile_path = os.path.join(data_dir, 'profile.json')
personal_path = os.path.join(data_dir, 'personal.json')
work_experience_path = os.path.join(data_dir, 'work_experience.json')
education_path = os.path.join(data_dir, 'education.json')
skills_path = os.path.join(data_dir, 'skills.json')
languages_path = os.path.join(data_dir, 'languages.json')
optional_sections_path = os.path.join(data_dir, 'optional_sections.json')

# Ruta del archivo de salida
output_file_path = os.path.join(base_dir, 'background.md')

# Cargar datos JSON
profile_data = load_json(profile_path)
personal_data = load_json(personal_path)
work_experience_data = load_json(work_experience_path)
education_data = load_json(education_path)
skills_data = load_json(skills_path)
languages_data = load_json(languages_path)
optional_sections_data = load_json(optional_sections_path)

# Crear el header del nuevo formato
header = f"""---
layout: default
title: {personal_data['name']} {personal_data['lastname']} - Professional Background
---

<div class="professional-banner smaller">
  <div class="banner-content">
    <h1>{personal_data['name']} {personal_data['lastname']}</h1>
    <p class="tagline">{escape_markdown_special_chars(personal_data['header'])}</p>
  </div>
</div>

<div class="profile-section">
  <div class="container">
    <div class="profile-card">
      <div class="download-cv-button-container">
        <a href="/assets/docs/RonaldMego_CV.pdf" class="download-cv-button" style="cursor: pointer; z-index: 5; position: relative;">
          <i class="fas fa-download"></i> Download CV
        </a>
      </div>
      <h2>Profile</h2>
      <p class="summary-text">{escape_markdown_special_chars(profile_data['profile'].split('. ', 1)[0] + '.')}</p>
      <p class="summary-text">{escape_markdown_special_chars('. '.join(profile_data['profile'].split('. ')[1:]))}</p>
    </div>
  </div>
</div>
"""

# Función para crear la sección de experiencia profesional
def create_work_experience_section():
    # Primeras 4 experiencias (visibles inicialmente)
    visible_experiences = work_experience_data['experiences'][:4]
    # Experiencias restantes (ocultas inicialmente)
    hidden_experiences = work_experience_data['experiences'][4:] if len(work_experience_data['experiences']) > 4 else []
    
    # Crear la sección de timeline
    timeline_section = """
<div class="timeline-section">
  <div class="container">
    <h2>Professional Experience</h2>
    
    <div class="timeline">
"""
    
    # Añadir experiencias visibles
    for exp in visible_experiences:
        bullets = "\n                ".join([f"<li>{escape_markdown_special_chars(bullet)}</li>" for bullet in exp['bullets']])
        timeline_section += f"""
      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="marker-line"></div>
          <div class="marker-circle"></div>
        </div>
        <div class="timeline-content">
          <div class="date-badge">{exp['dates']}</div>
          <h3>{exp['title']}</h3>
          <div class="company-info">
            <a href="{exp['url']}" target="_blank" class="company-link">{exp['company']}</a>
            <span class="location">{exp['location']}</span>
          </div>
          <div class="responsibilities">
            <ul>
                {bullets}
            </ul>
          </div>
        </div>
      </div>
"""
    
    # Añadir botón "Ver experiencia anterior" si hay experiencias ocultas
    if hidden_experiences:
        timeline_section += """
      <div class="timeline-item load-more-container">
        <button id="load-more-experience" class="load-more-button">
          <i class="fas fa-chevron-down"></i> Ver experiencia anterior
        </button>
      </div>
      
      <div class="hidden-timeline-items">
"""
        
        # Añadir experiencias ocultas
        for exp in hidden_experiences:
            bullets = "\n                ".join([f"<li>{escape_markdown_special_chars(bullet)}</li>" for bullet in exp['bullets']])
            timeline_section += f"""
        <div class="timeline-item">
          <div class="timeline-marker">
            <div class="marker-line"></div>
            <div class="marker-circle"></div>
          </div>
          <div class="timeline-content">
            <div class="date-badge">{exp['dates']}</div>
            <h3>{exp['title']}</h3>
            <div class="company-info">
              <a href="{exp['url']}" target="_blank" class="company-link">{exp['company']}</a>
              <span class="location">{exp['location']}</span>
            </div>
            <div class="responsibilities">
              <ul>
                {bullets}
              </ul>
            </div>
          </div>
        </div>
"""
        
        timeline_section += """
      </div>
"""
    
    timeline_section += """
    </div>
  </div>
</div>
"""
    
    return timeline_section

# Función para crear la sección de educación
def create_education_section():
    education_section = """
<div class="education-section">
  <div class="container">
    <h2>Education</h2>
    
    <div class="education-grid">
"""
    
    # Iconos para cada tipo de educación
    icons = {
        0: "fas fa-graduation-cap",  # Primer elemento (BSc)
        1: "fas fa-university",      # Segundo elemento (MBA)
        2: "fas fa-award"            # Tercer elemento (Diploma)
    }
    
    for i, edu in enumerate(education_data['education']):
        icon_class = icons.get(i, "fas fa-graduation-cap")  # Default a graduation-cap si no se encuentra
        education_section += f"""
      <div class="education-card">
        <div class="education-icon">
          <i class="{icon_class}"></i>
        </div>
        <div class="education-details">
          <h3>{edu['degree']}</h3>
          <div class="school-info">
            <a href="{edu['url']}" target="_blank" class="school-link">{edu['institution']}</a>
            <span class="education-period">{edu['dates'].replace('-', ' to ')}</span>
          </div>
          <p class="education-description">{escape_markdown_special_chars(edu['details'])}</p>
        </div>
      </div>
"""
    
    education_section += """
    </div>
  </div>
</div>
"""
    
    return education_section

# Función para crear la sección de habilidades y certificaciones
def create_skills_certifications_section():
    skills_cert_section = """
<div class="skills-certifications-section">
  <div class="container">
    <div class="skills-certifications-grid">
      <div class="skills-column">
        <h2>Technical Skills</h2>
"""
    
    # Mapeo de categorías a íconos FontAwesome
    skill_icons = {
        "Data Story Telling": "fas fa-chart-bar",
        "Programming and Cloud": "fas fa-code",
        "Machine Learning and AI": "fas fa-brain",
        "Soft Skills": "fas fa-users",
    }
    
    # Añadir categorías de habilidades
    for skill in skills_data['skills']:
        category = skill['category']
        icon = skill_icons.get(category, "fas fa-tools")  # Default a tools si no se encuentra
        
        skills_cert_section += f"""
        <div class="skill-category">
          <h3><i class="{icon}"></i> {category}</h3>
          <div class="skill-tags">
"""
        
        for tool in skill['tools']:
            skills_cert_section += f'            <span class="skill-tag">{tool}</span>\n'
        
        skills_cert_section += """
          </div>
        </div>
"""
    
    # Añadir sección de idiomas
    skills_cert_section += """
        <div class="skill-category">
          <h3><i class="fas fa-language"></i> Languages</h3>
          <div class="skill-tags">
"""
    
    for lang in languages_data['languages']:
        note = f" - {lang['note']}" if 'note' in lang else ""
        skills_cert_section += f'            <span class="skill-tag">{lang["name"]} [{lang["level"]}]{note}</span>\n'
    
    skills_cert_section += """
          </div>
        </div>
      </div>
      
      <div class="certifications-column">
        <h2>Certifications</h2>
"""
    
    # Añadir categorías de certificaciones
    cert_icons = {
        "AWS": "fab fa-aws",
        "Microsoft": "fab fa-microsoft",
        "Google": "fab fa-google"
    }
    
    for section in optional_sections_data['sections']:
        skills_cert_section += f"""
        <div class="certification-category">
          <h3>{section['section_name']}</h3>
          <ul class="certification-list">
"""
        
        for item in section['items']:
            # Determinar el icono en base al nombre de la institución
            icon = "fas fa-certificate"  # Default
            for key, value in cert_icons.items():
                if key.lower() in item['institution'].lower():
                    icon = value
                    break
            
            # Obtener fecha formateada
            date_parts = item['date'].split('.')
            month = date_parts[0] if len(date_parts) > 0 else ""
            year = date_parts[1] if len(date_parts) > 1 else ""
            
            skills_cert_section += f"""
            <li class="certification-item">
              <div class="certification-icon"><i class="{icon}"></i></div>
              <div class="certification-info">
                <h4>{escape_markdown_special_chars(item['name'])}</h4>
                <div class="certification-meta">
                  <span class="certification-provider">{escape_markdown_special_chars(item['institution'])}</span>
                  <span class="certification-date">{month} {year}</span>
                </div>
                <a href="{item['url']}" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>
"""
        
        skills_cert_section += """
          </ul>
        </div>
"""
    
    skills_cert_section += """
      </div>
    </div>
  </div>
</div>
"""
    
    return skills_cert_section

# Crear la parte final con CTA y script
footer = """
<div class="contact-cta">
  <div class="cta-content">
    <h2>Interested in working together?</h2>
    <a href="/contact" class="cta-button">Let's Connect <i class="fas fa-arrow-right"></i></a>
  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Manejar el botón "Ver experiencia anterior"
    const loadMoreButton = document.getElementById('load-more-experience');
    const hiddenItems = document.querySelector('.hidden-timeline-items');
    
    if (loadMoreButton && hiddenItems) {
      loadMoreButton.addEventListener('click', function() {
        hiddenItems.style.display = 'block';
        loadMoreButton.parentElement.style.display = 'none';
        
        // Animar la aparición de los elementos
        const items = hiddenItems.querySelectorAll('.timeline-item');
        items.forEach((item, index) => {
          setTimeout(() => {
            item.classList.add('fade-in');
          }, 100 * index);
        });
      });
    }
  });
</script>
"""

# Combinar todas las secciones
background_content = (
    header +
    create_work_experience_section() +
    create_education_section() +
    create_skills_certifications_section() +
    footer
)

# Escribir el archivo de salida
try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(background_content)
    print(f"Generated Background Markdown file at {output_file_path}")
except Exception as e:
    print(f"Error writing to file: {e}")
    raise