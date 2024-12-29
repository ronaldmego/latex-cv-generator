import os
import json

def escape_markdown_special_chars(text):
    """Escape Markdown special characters, except for parentheses."""
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

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'Data')

profile_path = os.path.join(data_dir, 'profile.json')
personal_path = os.path.join(data_dir, 'personal.json')
work_experience_path = os.path.join(data_dir, 'work_experience.json')
education_path = os.path.join(data_dir, 'education.json')
skills_path = os.path.join(data_dir, 'skills.json')
languages_path = os.path.join(data_dir, 'languages.json')
optional_sections_path = os.path.join(data_dir, 'optional_sections.json')

output_file_path = os.path.join(base_dir, 'index.md')
template_file_path = os.path.join(base_dir, 'index_template.md')

profile_data = load_json(profile_path)
personal_data = load_json(personal_path)
work_experience_data = load_json(work_experience_path)
education_data = load_json(education_path)
skills_data = load_json(skills_path)
languages_data = load_json(languages_path)
optional_sections_data = load_json(optional_sections_path)

try:
    with open(template_file_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
except Exception as e:
    print(f"Error reading template file: {e}")
    raise

# Reemplazar las claves del template con los valores del JSON
template_content = template_content.replace('{{ profile }}', escape_markdown_special_chars(profile_data['profile']))

template_content = template_content.replace('{{ personal.name }}', personal_data['name'])
template_content = template_content.replace('{{ personal.lastname }}', personal_data['lastname'])
template_content = template_content.replace('{{ personal.header }}', personal_data['header'])

template_content = template_content.replace('{{ personal.mobile }}', personal_data['mobile'])
template_content = template_content.replace('{{ personal.email }}', personal_data['email'])
template_content = template_content.replace('{{ personal.location }}', personal_data['location'])
template_content = template_content.replace('{{ personal.linkedin_url }}', personal_data['linkedin_url'])
template_content = template_content.replace('{{ personal.github_url }}', personal_data['github_url'])
template_content = template_content.replace('{{ personal.twitter_url }}', personal_data['twitter_url'])

work_experience_md = ""
for experience in work_experience_data['experiences']:
    bullets = "\n        ".join([f"<li>{escape_markdown_special_chars(bullet)}</li>" for bullet in experience['bullets']])
    work_experience_md += f"""
<div class=\"experience-item\">
  <div class=\"experience-header\">
    <h3>{experience['title']}</h3>
    <div class=\"experience-meta\">
      <span class=\"company\"><a href=\"{experience['url']}\" target=\"_blank\">{experience['company']}</a></span>
      <span class=\"location\">{experience['location']}</span>
      <span class=\"period\">{experience['dates']}</span>
    </div>
  </div>
  <ul>
        {bullets}
  </ul>
</div>
"""

template_content = template_content.replace('{{ work_experience }}', work_experience_md)

education_md = ""
for edu in education_data['education']:
    education_md += f"""
<div class=\"education-item\">
  <div class=\"education-header\">
    <h3>{edu['degree']}</h3>
    <div class=\"education-meta\">
      <span class=\"school\"><a href=\"{edu['url']}\" target=\"_blank\">{edu['institution']}</a></span>
      <span class=\"location\">{edu['location']}</span>
      <span class=\"period\">{edu['dates']}</span>
    </div>
  </div>
  <p class=\"education-details\">{escape_markdown_special_chars(edu['details'])}</p>
</div>
"""

template_content = template_content.replace('{{ education }}', education_md)

skills_md = "<div class=\"skills-section\">\n"
for skill in skills_data['skills']:
    tools = ", ".join(skill['tools'])
    skills_md += f"<div class=\"skill-category\">\n<h4>{skill['category']}</h4>\n{tools}\n</div>\n"
skills_md += "</div>"

template_content = template_content.replace('{{ skills }}', skills_md)

languages_md = "<ul>\n"
for lang in languages_data['languages']:
    note = f" - {escape_markdown_special_chars(lang['note'])}" if 'note' in lang else ""
    languages_md += f"<li><strong>{lang['name']}</strong> [{lang['level']}] {note}</li>\n"
languages_md += "</ul>"

template_content = template_content.replace('{{ languages }}', languages_md)

optional_sections_md = ""
for section in optional_sections_data['sections']:
    section_name = section['section_name']
    optional_sections_md += f"<div class=\"certifications\">\n<h3>{section_name}</h3>\n<ul>\n"
    for item in section['items']:
        details = f" - {escape_markdown_special_chars(item['details'])}" if 'details' in item else ""
        optional_sections_md += f"<li>{escape_markdown_special_chars(item['name'])} ({item['date']}) - <a href=\"{item['url']}\" target=\"_blank\">{escape_markdown_special_chars(item['institution'])}</a>{details}</li>\n"
    optional_sections_md += "</ul>\n</div>\n"

template_content = template_content.replace('{{ optional_sections }}', optional_sections_md)

try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    print(f"Generated Markdown file at {output_file_path}")
except Exception as e:
    print(f"Error writing to file: {e}")
    raise