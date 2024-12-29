# generate_cv.py
import os
import json

# Function to escape LaTeX special characters
def escape_latex_special_chars(text):
    special_chars = {
        '%': '\\%',
        '&': '\\&',
        '$': '\\$',
        '#': '\\#',
        '_': '\\_',
        '{': '\\{',
        '}': '\\}',
        '?': '\\?',
        '~': '\\textasciitilde{}',
        '^': '\\textasciicircum{}'
    }
    for char, escape in special_chars.items():
        text = text.replace(char, escape)
    return text

# Define paths relative to the script location
script_dir = os.path.dirname(os.path.abspath(__file__))
latex_template_path = os.path.join(script_dir, 'Data')
output_directory = script_dir
template_file_path = os.path.join(script_dir, 'cv_template.tex')

# Define JSON file paths
profile_file_path = os.path.join(latex_template_path, 'profile.json')
personal_file_path = os.path.join(latex_template_path, 'personal.json')
work_experience_file_path = os.path.join(latex_template_path, 'work_experience.json')
education_file_path = os.path.join(latex_template_path, 'education.json')
optional_sections_file_path = os.path.join(latex_template_path, 'optional_sections.json')
languages_file_path = os.path.join(latex_template_path, 'languages.json')
skills_file_path = os.path.join(latex_template_path, 'skills.json')

# Load profile data from JSON file
try:
    with open(profile_file_path, 'r', encoding='utf-8') as f:
        profile_data = json.load(f)
except Exception as e:
    print(f"Error loading data from profile JSON file: {e}")
    raise

# Load personal data from JSON file
try:
    with open(personal_file_path, 'r', encoding='utf-8') as f:
        personal_data = json.load(f)
except Exception as e:
    print(f"Error loading data from personal JSON file: {e}")
    raise

# Create lowercase versions of name and lastname
personal_data['namelower'] = personal_data['name'].lower()
personal_data['lastnamelower'] = personal_data['lastname'].lower()

# Load work experience data from JSON file
try:
    with open(work_experience_file_path, 'r', encoding='utf-8') as f:
        work_experience_data = json.load(f)
except Exception as e:
    print(f"Error loading data from work experience JSON file: {e}")
    raise

# Load education data from JSON file
try:
    with open(education_file_path, 'r', encoding='utf-8') as f:
        education_data = json.load(f)
except Exception as e:
    print(f"Error loading data from education JSON file: {e}")
    raise

# Load optional_sections data from JSON file
try:
    with open(optional_sections_file_path, 'r', encoding='utf-8') as f:
        optional_sections_data = json.load(f)
except Exception as e:
    print(f"Error loading data from optional_sections JSON file: {e}")
    raise

# Load languages data from JSON file
try:
    with open(languages_file_path, 'r', encoding='utf-8') as f:
        languages_data = json.load(f)
except Exception as e:
    print(f"Error loading data from languages JSON file: {e}")
    raise

# Load skills data from JSON file
try:
    with open(skills_file_path, 'r', encoding='utf-8') as f:
        skills_data = json.load(f)
except Exception as e:
    print(f"Error loading data from skills JSON file: {e}")
    raise

# Read the LaTeX template
try:
    with open(template_file_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
except Exception as e:
    print(f"Error reading LaTeX template file: {e}")
    raise

# Escape LaTeX special characters in the profile and personal sections
profile_section = escape_latex_special_chars(profile_data['profile'])
personal_section = {k: escape_latex_special_chars(v) for k, v in personal_data.items()}

# Convert work experience data to LaTeX format with escaped special characters
work_experience_section = ""
for experience in work_experience_data['experiences']:
    bullets = "\n".join([f"\\item {escape_latex_special_chars(bullet)}" for bullet in experience['bullets']])
    work_experience_section += f"""
\\customcventry{{{experience['dates']}}}{{\\color{{blue}}\\href{{{experience['url']}}}{{{experience['company']}}}}}{{{experience['title']}}}{{{experience['location']}}}{{}}{{{{
\\begin{{itemize}}[leftmargin=0.6cm, label={{\\textbullet}}, itemsep=-0.2em]
{bullets}
\\end{{itemize}}
\\vspace{{-0.1em}}
}}}}
"""

# Convert education data to LaTeX format with escaped special characters
education_section = ""
for education in education_data['education']:
    education_section += f"""
\\customcventry{{{education['dates']}}}{{\\color{{blue}}\\href{{{education['url']}}}{{{education['institution']}}}}}{{{education['degree']}}}{{{education['location']}}}{{}}{{{escape_latex_special_chars(education['details'])}}}
"""

# Convert optional_sections data to LaTeX format with escaped special characters
optional_sections = ""
for section in optional_sections_data['sections']:
    section_name = section['section_name']
    optional_sections += f"\n\\section{{{section_name}}}\n"
    optional_sections += "{\\begin{itemize}[label=\\textbullet, itemsep=-0.2em]\n"
    for item in section['items']:
        # Check if 'details' exists and append it if present
        details = f" - {escape_latex_special_chars(item['details'])}" if 'details' in item else ""
        item_entry = f"\\item {escape_latex_special_chars(item['name'])} ({item['date']}) - \\underline{{\\color{{blue}}\\href{{{item['url']}}}{{{escape_latex_special_chars(item['institution'])}}}}}{details}\n"
        optional_sections += item_entry
    optional_sections += "\\end{itemize}}\n"

# Convert skills data to LaTeX format with escaped special characters
skills_section = f"\\section{{{skills_data['section_name']}}}\n"
skills_section += "\\begin{itemize}[label=\\textbullet, itemsep=-0.2em]\n"
for skill in skills_data['skills']:
    tools = ", ".join(skill['tools'])
    skills_section += f"\\item \\textbf{{{escape_latex_special_chars(skill['category'])}}}: {escape_latex_special_chars(tools)}\n"
skills_section += "\\end{itemize}\n"

# Convert languages data to LaTeX format with escaped special characters
languages_section = f"\\section{{{languages_data['section_name']}}}\n"
languages_section += "\\begin{multicols}{2}\n\\begin{itemize}[label=\\textbullet, itemsep=-0.2em]\n"
for language in languages_data['languages']:
    note = f" - {escape_latex_special_chars(language['note'])}" if 'note' in language else ""
    languages_section += f"\\item \\textbf{{{escape_latex_special_chars(language['name'])}}} [{escape_latex_special_chars(language['level'])}]{note}\n"
languages_section += "\\end{itemize}\n\\end{multicols}\n"

# Inject the profile, personal, work experience, education, optional sections, languages section, and skills section into the template
rendered_content = template_content
for key, value in personal_section.items():
    rendered_content = rendered_content.replace(f'{{{{ {key} }}}}', value)
rendered_content = rendered_content.replace('{{ profile }}', '{' + profile_section + '}')
rendered_content = rendered_content.replace('{{ work_experience }}', work_experience_section)
rendered_content = rendered_content.replace('{{ education }}', education_section)
rendered_content = rendered_content.replace('{{ optional_sections }}', optional_sections)
rendered_content = rendered_content.replace('{{ skills_section }}', skills_section)
rendered_content = rendered_content.replace('{{ languages_section }}', languages_section)

# Write the rendered LaTeX to a file
output_file_path = os.path.join(output_directory, 'cv.tex')
try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(rendered_content)
    print(f"Rendered LaTeX written to {output_file_path}")
except Exception as e:
    print(f"Error writing to file: {e}")
    raise