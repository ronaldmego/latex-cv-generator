Project Documentation Summary
=========================
Root Directory: D:\APPs\latex-cv-generator
Files Analyzed: 19
Total Size: 72.91 KB
Timestamp: 2025-04-23 09:24:14

Skipped Files Sample:
-------------------
- minified/compressed library code: Data\profile.json
- unknown type (2 files):
  • cv.aux
  • cv.log
- too few lines (2): cv.out

Directory Structure
==================

latex-cv-generator
├── .gitignore
├── Data/
│   ├── education.json
│   ├── languages.json
│   ├── optional_sections.json
│   ├── personal.json
│   ├── profile.json
│   ├── skills.json
│   └── work_experience.json
├── Dockerfile
├── background.md
├── compile_latex.py
├── cv.aux
├── cv.log
├── cv.out
├── cv.tex
├── cv_template-no-phone.tex
├── cv_template-with-phone.tex
├── cv_template.tex
├── entrypoint.sh
├── generate_cv.py
├── generate_index.py
├── readme.md
└── requirements.txt

File Contents
=============


================================================================================
File: .gitignore
================================================================================

# Secrets
.env

# LaTeX temporary files
*.aux
*.log
*.out
*.synctex.gz
*.fls
*.fdb_latexmk
*.pdf

# Python temporary files
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Docker files
*.tar
*.tar.gz

# IDE specific files
.vscode/
.idea/
*.swp
*.swo
.DS_Store

#Ignore Folder or subfolders
ref/



================================================================================
File: Data\education.json
================================================================================

{
    "education": [
        {
            "dates": "2005-2011",
            "url": "https://www.credential.net/922f2fe3-2fe4-4233-bbb6-1579ff468aa9?username=ronaldfriizmegosolano20070",
            "institution": "Universidad Nacional de Ingenieria",
            "degree": "BSc. Applied Statistics",
            "location": "Lima, Peru",
            "details": "Thesis Project: “Segmentation of subscribers by traffic consumption in prepaid lines of Telefonica using k-means multivariate cluster analysis”. Top student, outstanding grade."
        },
        {
            "dates": "2016-2018",
            "url": "https://www.credential.net/f953e37b-11e7-4570-89aa-6f21d606132d?username=ronaldfriizmegosolano20070",
            "institution": "PAD Business School",
            "degree": "Master in Business Administration (MBA)",
            "location": "Lima, Peru",
            "details": "Thesis Project: “Application of non-operational troubleshooting of Telefonica and its sales channels”. Outstanding grade."
        },
        {
            "dates": "2024-2024",
            "url": "https://www.credential.net/f6bd85db-4850-4f50-9609-7990eb0aaadc",
            "institution": "Massachusetts Institute of Technology",
            "degree": "Diploma Data Leadership & Leveraging Data Systems",
            "location": "Cambridge, MA, USA",
            "details": "Participated in an immersive program with leaders in data management at the MIT Executive Program."
        }
    ]
}



================================================================================
File: Data\languages.json
================================================================================

{
    "section_name": "Languages",
    "languages": [
        {
            "name": "English",
            "level": "Fluent"
        },
        {
            "name": "Spanish",
            "level": "Fluent",
            "note": "Native"
        }
    ]
}



================================================================================
File: Data\optional_sections.json
================================================================================

{
    "sections": [
        {
            "section_name": "Specialized Programs and Diplomas",
            "items": [
                {
                    "name": "Data Monetization, Management, and Trends",
                    "date": "May. 2024",
                    "url": "https://courses.edx.org/certificates/447c3529a7dc42aa8bf27297a97b0c88",
                    "institution": "IEUniversity & edX"
                },
                {
                    "name": "Data Strategy: Data as Competitive Advantage",
                    "date": "Jan. 2022",
                    "url": "https://certificates.emeritus.org/39607ed0-10b6-4387-be32-5b34af6a5040",
                    "institution": "Berkeley Executive Education"
                },
                {
                    "name": "Entrepreneurship and Innovation Program",
                    "date": "May. 2018",
                    "url": "https://www.credential.net/54b357e1-243e-47ea-a40f-bcfdcfa04b18?username=ronaldfriizmegosolano20070",
                    "institution": "Darden School of Business - Charlottesville, VA, USA"
                },
                {
                    "name": "Diploma in Applied Finance",
                    "date": "Jul. 2012",
                    "url": "https://www.credential.net/322f33cb-ee81-453d-994a-3f81db550be9?username=ronaldfriizmegosolano20070",
                    "institution": "Universidad del Pacifico"
                }
            ]
        },
        {
            "section_name": "Technical Skills and Certifications",
            "items": [
                {
                    "name": "AWS Cloud Certified Cloud Practitioner",
                    "date": "Apr. 2024",
                    "url": "https://www.credly.com/badges/b1438ac5-468e-4964-b6ac-2894b7e2204b/linked_in_profile",
                    "institution": "Amazon Web Services"
                },
                {
                    "name": "Cloud Data en Azure",
                    "date": "Dec. 2023",
                    "url": "https://www.credential.net/f49190f2-99e2-4af9-83a9-26bef312b87f?username=ronaldfriizmegosolano20070",
                    "institution": "Bootcamp Institute & Microsoft"
                },
                {
                    "name": "GCP, Big Data and ML",
                    "date": "May. 2020",
                    "url": "https://www.coursera.org/account/accomplishments/certificate/RPWJ8S2L8CYW",
                    "institution": "Coursera & Google"
                },
                {
                    "name": "Data Science in Python",
                    "date": "Aug. 2020",
                    "url": "https://www.coursera.org/account/accomplishments/verify/MYX5XU65HP95",
                    "institution": "Coursera & University of Michigan"
                }
            ]
        }
    ]
}



================================================================================
File: Data\personal.json
================================================================================

{
    "name": "Ronald",
    "lastname": "Mego",
    "header": "Head of Data Analytics & Innovation | Agentic AI / Gen AI | Telecom | Fintech",
    "linkedin_url": "https://www.linkedin.com/in/ronaldmego/",
    "github_url": "https://github.com/ronaldmego",
    "x_url": "https://ronaldmego.github.io/",
    "twitter_url": "https://x.com/MGOData",
    "mobile": "+507 64654515",
    "email": "ronald.mego@outlook.com",
    "location": "Panama City, PA"
}



================================================================================
File: Data\skills.json
================================================================================

{
    "section_name": "Skills",
    "skills": [
        {
            "category": "Data Strategy",
            "tools": ["Data Governance", "Data Quality", "Data Monetization", "Data Privacy", "Data Security", "Data Ethics"]
        },
        {
            "category": "Soft Skills",
            "tools": ["Leadership", "Team Management", "Project Management", "Agile Methodologies", "Stakeholder Management"]
        },
        {
            "category": "Financial Skills",
            "tools": ["Financial Modeling", "Revenue Forecasting", "Cost Analysis", "Pricing Strategy", "Profitability Analysis"]
        },
        {
            "category": "Machine Learning",
            "tools": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning", "Natural Language Processing"]
        },
        {
            "category": "Cloud & DevOps",
            "tools": ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform"]
        },
        {
            "category": "Data Story Telling",
            "tools": ["Advanced Excel", "Advanced Power Point", "PowerBI", "Tableau", "Looker Studio", "QuickSight","Shiny", "Streamlit"]
        },
        {
            "category": "Data tools",
            "tools": ["Python", "R", "SQL", "Spark", "Hadoop", "Snowflake", "Redshift", "BigQuery", "Synapse", "CI/CD", "ML Ops", "Airflow"]
        }
    ]
}



================================================================================
File: Data\work_experience.json
================================================================================

{
    "experiences": [
        {
            "dates": "01/2025 ‐ present",
            "company": "Millicom | Tigo",
            "url": "https://www.millicom.com/",
            "title": "Data Analytics and Innovation Manager",
            "location": "Panama City, PA",
            "bullets": [
                "Lead and develop a Data Analytics Roadmap to enhance Tigo Users Digital experience (~50 million), leveraging AI and Machine Learning models.",
                "Design and implement a Data Governance and Monetization Strategy to drive new revenue streams and optimize costs, aligning with the Global CDO."
            ]            
        },
        {
            "dates": "08/2023 ‐ 12/2024",
            "company": "Millicom | Tigo",
            "url": "https://www.millicom.com/",
            "title": "Head of Data - MFS",
            "location": "Panama City, PA",
            "bullets": [
                "Leading Tigo Money's data strategy across Data Governance, analytics and dashboarding to enable monetizable use cases while ensuring compliance standards.",
                "Implement Data Analytics tools andframewrok for Mobile Financial Services with Lending Risk management, Fraud detection and Customer Insights."
            ]            
        },
        {
            "dates": "12/2021 ‐ 07/2023",
            "company": "Millicom | Tigo",
            "url": "https://www.millicom.com/",
            "title": "Head of Marketing Analytics - MFS",
            "location": "Panama City, PA",
            "bullets": [
                "Design and lead the Customer Segmentation and Campaign Management strategy powered by Customer Intelligence for Tigo Money, aligned with the Global CMO",
                "Develop and implement a Digital Marketing Analytics framework to measure the effectiveness of marketing campaigns, optimizing the funnel conversion and increasing ROI."
            ]            
        },        
        {
            "dates": "11/2019 ‐ 11/2021",
            "company": "Grupo El Comercio",
            "url": "https://grupoelcomercio.com.pe/",
            "title": "Data Manager",
            "location": "Lima, PE",
            "bullets": [
                "Lead Data Governance and Develop user segmentation models and content recommendation models, supporting business objectives related to subscription growth and engagement.",
                "Implement a zero and 1st (first) party data consolidation project into a golden record, enabling audience data monetization and the generation of new revenue streams."
            ]
        },
        {
            "dates": "11/2016 ‐ 10/2019",
            "company": "Telefonica | Movistar",
            "url": "https://telefonica.com.pe/",
            "title": "Customer Insights Manager",
            "location": "Lima, PE",
            "bullets": [
                "Data Governance for 17 million customers across home, prepaid, and postpaid products, establishing a single source of truth (SSOT) to support the Customer 360 business strategy, enhancing customer satisfaction and campaign effectiveness.",
                "Develop dashboards for sales, collections, and customer support, and implement the first text mining model to analyze customer satisfaction in chatbot interactions."
            ]
        },
        {
            "dates": "08/2009 ‐ 10/2016",
            "company": "Telefónica | Movistar",
            "url": "https://telefonica.com.pe/",
            "title": "Customer Data Specialist",
            "location": "Lima, PE",
            "bullets": [
                "Delivered robust, customer-centric, and commercially monetizable data solutions, earning outstanding recognition for achievements.",
                "Developed analytical models for marketing, sales, customer experience, and collections, optimizing strategies for B2C mobile prepaid, postpaid, and home services."
            ]
        },
        {
            "dates": "03/2016 ‐ 08/2016",
            "company": "Universidad Nacional de Ingenieria",
            "url": "https://portal.uni.edu.pe/",
            "title": "Professor of Applied Computational Statistics",
            "location": "Lima, PE",
            "bullets": [
                "Design and execute curriculum incorporating real-world business case studies and data analysis projects, effectively bridging the gap between theoretical knowledge and practical application.",
                "Mentor students on academic and career paths in data science and statistics, with several students successfully securing internships and roles in top-tier companies."
            ]
        }        
    ]
}



================================================================================
File: Dockerfile
================================================================================

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




================================================================================
File: background.md
================================================================================

---
layout: default
title: Ronald Mego - Professional Background
---

<div class="professional-banner smaller">
  <div class="banner-content">
    <h1>Ronald Mego</h1>
    <p class="tagline">Professional Background</p>
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
      <p class="summary-text">Data leader with 15+ years of experience helping companies as a professional and consultant in telecom, fintech, and e-commerce industries.</p>
      <p class="summary-text">I focus on building data-driven solutions that drive revenue growth, optimize costs, and enhance customer experience. My approach combines business strategy with technical expertise in analytics, AI, and data architecture, leading multicultural teams to deliver impactful results. I specialize in turning complex data challenges into clear insights that enable better organizational decision-making. Currently leading data & AI initiatives at Millicom | Tigo, where I develop data monetization strategies and implement innovative analytics solutions across Latin America.</p>
    </div>
  </div>
</div>

<div class="timeline-section">
  <div class="container">
    <h2>Professional Experience</h2>
    
    <div class="timeline">

      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="marker-line"></div>
          <div class="marker-circle"></div>
        </div>
        <div class="timeline-content">
          <div class="date-badge">01/2025 ‐ present</div>
          <h3>Data Analytics and Innovation Manager</h3>
          <div class="company-info">
            <a href="https://www.millicom.com/" target="_blank" class="company-link">Millicom | Tigo</a>
            <span class="location">Panama City, PA</span>
          </div>
          <div class="responsibilities">
            <ul>
                <li>Lead and develop a Data Analytics Roadmap to enhance Tigo Users Digital experience (~50 million), leveraging AI and Machine Learning models.</li>
                <li>Design and implement a Data Monetization Strategy to drive new revenue streams and optimize costs, aligning with the Global CDO.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="marker-line"></div>
          <div class="marker-circle"></div>
        </div>
        <div class="timeline-content">
          <div class="date-badge">08/2023 ‐ 12/2024</div>
          <h3>Head of Data - MFS</h3>
          <div class="company-info">
            <a href="https://www.millicom.com/" target="_blank" class="company-link">Millicom | Tigo</a>
            <span class="location">Panama City, PA</span>
          </div>
          <div class="responsibilities">
            <ul>
                <li>Leading Tigo Money's data strategy across data governance, analytics and dashboarding to enable monetizable use cases while ensuring compliance standards.</li>
                <li>Implement Data Analytics tools andframewrok for Mobile Financial Services with Lending Risk management, Fraud detection and Customer Insights.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="marker-line"></div>
          <div class="marker-circle"></div>
        </div>
        <div class="timeline-content">
          <div class="date-badge">12/2021 ‐ 07/2023</div>
          <h3>Head of Marketing Analytics - MFS</h3>
          <div class="company-info">
            <a href="https://www.millicom.com/" target="_blank" class="company-link">Millicom | Tigo</a>
            <span class="location">Panama City, PA</span>
          </div>
          <div class="responsibilities">
            <ul>
                <li>Design and lead the Customer Segmentation and Campaign Management strategy powered by Customer Intelligence for Tigo Money, aligned with the Global CMO</li>
                <li>Develop and implement a Digital Marketing Analytics framework to measure the effectiveness of marketing campaigns, optimizing the funnel conversion and increasing ROI.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="marker-line"></div>
          <div class="marker-circle"></div>
        </div>
        <div class="timeline-content">
          <div class="date-badge">11/2019 ‐ 11/2021</div>
          <h3>Data Manager</h3>
          <div class="company-info">
            <a href="https://grupoelcomercio.com.pe/" target="_blank" class="company-link">Grupo El Comercio</a>
            <span class="location">Lima, PE</span>
          </div>
          <div class="responsibilities">
            <ul>
                <li>Develop user segmentation models and content recommendation models, supporting business objectives related to subscription growth and engagement.</li>
                <li>Implement a zero and 1st (first) party data consolidation project into a golden record, enabling audience data monetization and the generation of new revenue streams.</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="timeline-item load-more-container">
        <button id="load-more-experience" class="load-more-button">
          <i class="fas fa-chevron-down"></i> Ver experiencia anterior
        </button>
      </div>
      
      <div class="hidden-timeline-items">

        <div class="timeline-item">
          <div class="timeline-marker">
            <div class="marker-line"></div>
            <div class="marker-circle"></div>
          </div>
          <div class="timeline-content">
            <div class="date-badge">11/2016 ‐ 10/2019</div>
            <h3>Customer Insights Manager</h3>
            <div class="company-info">
              <a href="https://telefonica.com.pe/" target="_blank" class="company-link">Telefonica | Movistar</a>
              <span class="location">Lima, PE</span>
            </div>
            <div class="responsibilities">
              <ul>
                <li>Manage and model data for 17 million customers across home, prepaid, and postpaid products, establishing a single source of truth (SSOT) to support the Customer 360 business strategy, enhancing customer satisfaction and campaign effectiveness.</li>
                <li>Develop dashboards for sales, collections, and customer support, and implement the first text mining model to analyze customer satisfaction in chatbot interactions.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="timeline-item">
          <div class="timeline-marker">
            <div class="marker-line"></div>
            <div class="marker-circle"></div>
          </div>
          <div class="timeline-content">
            <div class="date-badge">08/2009 ‐ 10/2016</div>
            <h3>Customer Data Specialist</h3>
            <div class="company-info">
              <a href="https://telefonica.com.pe/" target="_blank" class="company-link">Telefónica | Movistar</a>
              <span class="location">Lima, PE</span>
            </div>
            <div class="responsibilities">
              <ul>
                <li>Delivered robust, customer-centric, and commercially monetizable data solutions, earning outstanding recognition for achievements.</li>
                <li>Developed analytical models for marketing, sales, customer experience, and collections, optimizing strategies for B2C mobile prepaid, postpaid, and home services.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="timeline-item">
          <div class="timeline-marker">
            <div class="marker-line"></div>
            <div class="marker-circle"></div>
          </div>
          <div class="timeline-content">
            <div class="date-badge">03/2016 ‐ 08/2016</div>
            <h3>Professor of Applied Computational Statistics</h3>
            <div class="company-info">
              <a href="https://portal.uni.edu.pe/" target="_blank" class="company-link">Universidad Nacional de Ingenieria</a>
              <span class="location">Lima, PE</span>
            </div>
            <div class="responsibilities">
              <ul>
                <li>Design and execute curriculum incorporating real-world business case studies and data analysis projects, effectively bridging the gap between theoretical knowledge and practical application.</li>
                <li>Mentor students on academic and career paths in data science and statistics, with several students successfully securing internships and roles in top-tier companies.</li>
              </ul>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
</div>

<div class="education-section">
  <div class="container">
    <h2>Education</h2>
    
    <div class="education-grid">

      <div class="education-card">
        <div class="education-icon">
          <i class="fas fa-graduation-cap"></i>
        </div>
        <div class="education-details">
          <h3>BSc. Applied Statistics</h3>
          <div class="school-info">
            <a href="https://www.credential.net/922f2fe3-2fe4-4233-bbb6-1579ff468aa9?username=ronaldfriizmegosolano20070" target="_blank" class="school-link">Universidad Nacional de Ingenieria</a>
            <span class="education-period">2005 to 2011</span>
          </div>
          <p class="education-description">Thesis Project: “Segmentation of subscribers by traffic consumption in prepaid lines of Telefonica using k-means multivariate cluster analysis”. Top student, outstanding grade.</p>
        </div>
      </div>

      <div class="education-card">
        <div class="education-icon">
          <i class="fas fa-university"></i>
        </div>
        <div class="education-details">
          <h3>Master in Business Administration (MBA)</h3>
          <div class="school-info">
            <a href="https://www.credential.net/f953e37b-11e7-4570-89aa-6f21d606132d?username=ronaldfriizmegosolano20070" target="_blank" class="school-link">PAD Business School</a>
            <span class="education-period">2016 to 2018</span>
          </div>
          <p class="education-description">Thesis Project: “Application of non-operational troubleshooting of Telefonica and its sales channels”. Outstanding grade.</p>
        </div>
      </div>

      <div class="education-card">
        <div class="education-icon">
          <i class="fas fa-award"></i>
        </div>
        <div class="education-details">
          <h3>Diploma Data Leadership & Leveraging Data Systems</h3>
          <div class="school-info">
            <a href="https://www.credential.net/f6bd85db-4850-4f50-9609-7990eb0aaadc" target="_blank" class="school-link">Massachusetts Institute of Technology</a>
            <span class="education-period">2024 to 2024</span>
          </div>
          <p class="education-description">Participated in an immersive program with leaders in data management at the MIT Executive Program.</p>
        </div>
      </div>

    </div>
  </div>
</div>

<div class="skills-certifications-section">
  <div class="container">
    <div class="skills-certifications-grid">
      <div class="skills-column">
        <h2>Technical Skills</h2>

        <div class="skill-category">
          <h3><i class="fas fa-chart-bar"></i> Data Story Telling</h3>
          <div class="skill-tags">
            <span class="skill-tag">Advanced Excel</span>
            <span class="skill-tag">Advanced Power Point</span>
            <span class="skill-tag">PowerBI</span>
            <span class="skill-tag">Tableau</span>
            <span class="skill-tag">Looker Studio</span>
            <span class="skill-tag">QuickSight</span>
            <span class="skill-tag">Shiny</span>
            <span class="skill-tag">Streamlit</span>

          </div>
        </div>

        <div class="skill-category">
          <h3><i class="fas fa-tools"></i> Data tools</h3>
          <div class="skill-tags">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">R</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">Spark</span>
            <span class="skill-tag">Hadoop</span>
            <span class="skill-tag">Snowflake</span>
            <span class="skill-tag">Redshift</span>
            <span class="skill-tag">BigQuery</span>
            <span class="skill-tag">Synapse</span>
            <span class="skill-tag">CI/CD</span>
            <span class="skill-tag">ML Ops</span>
            <span class="skill-tag">Airflow</span>

          </div>
        </div>

        <div class="skill-category">
          <h3><i class="fas fa-tools"></i> Financial Skills</h3>
          <div class="skill-tags">
            <span class="skill-tag">Financial Modeling</span>
            <span class="skill-tag">Revenue Forecasting</span>
            <span class="skill-tag">Cost Analysis</span>
            <span class="skill-tag">Pricing Strategy</span>
            <span class="skill-tag">Profitability Analysis</span>

          </div>
        </div>

        <div class="skill-category">
          <h3><i class="fas fa-tools"></i> Data Strategy</h3>
          <div class="skill-tags">
            <span class="skill-tag">Data Governance</span>
            <span class="skill-tag">Data Quality</span>
            <span class="skill-tag">Data Monetization</span>
            <span class="skill-tag">Data Privacy</span>
            <span class="skill-tag">Data Security</span>
            <span class="skill-tag">Data Ethics</span>

          </div>
        </div>

        <div class="skill-category">
          <h3><i class="fas fa-users"></i> Soft Skills</h3>
          <div class="skill-tags">
            <span class="skill-tag">Leadership</span>
            <span class="skill-tag">Communication</span>
            <span class="skill-tag">Team Collaboration</span>
            <span class="skill-tag">Problem Solving</span>
            <span class="skill-tag">Impactull Presentation Skills</span>

          </div>
        </div>

        <div class="skill-category">
          <h3><i class="fas fa-language"></i> Languages</h3>
          <div class="skill-tags">
            <span class="skill-tag">English [Fluent]</span>
            <span class="skill-tag">Spanish [Fluent] - Native</span>

          </div>
        </div>
      </div>
      
      <div class="certifications-column">
        <h2>Certifications</h2>

        <div class="certification-category">
          <h3>Specialized Programs and Diplomas</h3>
          <ul class="certification-list">

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>Data Monetization, Management, and Trends</h4>
                <div class="certification-meta">
                  <span class="certification-provider">IEUniversity & edX</span>
                  <span class="certification-date">May  2024</span>
                </div>
                <a href="https://courses.edx.org/certificates/447c3529a7dc42aa8bf27297a97b0c88" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>Data Strategy: Data as Competitive Advantage</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Berkeley Executive Education</span>
                  <span class="certification-date">Jan  2022</span>
                </div>
                <a href="https://certificates.emeritus.org/39607ed0-10b6-4387-be32-5b34af6a5040" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>Entrepreneurship and Innovation Program</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Darden School of Business - Charlottesville, VA, USA</span>
                  <span class="certification-date">May  2018</span>
                </div>
                <a href="https://www.credential.net/54b357e1-243e-47ea-a40f-bcfdcfa04b18?username=ronaldfriizmegosolano20070" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>Diploma in Applied Finance</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Universidad del Pacifico</span>
                  <span class="certification-date">Jul  2012</span>
                </div>
                <a href="https://www.credential.net/322f33cb-ee81-453d-994a-3f81db550be9?username=ronaldfriizmegosolano20070" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

          </ul>
        </div>

        <div class="certification-category">
          <h3>Technical Skills and Certifications</h3>
          <ul class="certification-list">

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>AWS Cloud Certified Cloud Practitioner</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Amazon Web Services</span>
                  <span class="certification-date">Apr  2024</span>
                </div>
                <a href="https://www.credly.com/badges/b1438ac5-468e-4964-b6ac-2894b7e2204b/linked_in_profile" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fab fa-microsoft"></i></div>
              <div class="certification-info">
                <h4>Cloud Data en Azure</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Bootcamp Institute & Microsoft</span>
                  <span class="certification-date">Dec  2023</span>
                </div>
                <a href="https://www.credential.net/f49190f2-99e2-4af9-83a9-26bef312b87f?username=ronaldfriizmegosolano20070" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fab fa-google"></i></div>
              <div class="certification-info">
                <h4>GCP, Big Data and ML</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Coursera & Google</span>
                  <span class="certification-date">May  2020</span>
                </div>
                <a href="https://www.coursera.org/account/accomplishments/certificate/RPWJ8S2L8CYW" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

            <li class="certification-item">
              <div class="certification-icon"><i class="fas fa-certificate"></i></div>
              <div class="certification-info">
                <h4>Data Science in Python</h4>
                <div class="certification-meta">
                  <span class="certification-provider">Coursera & University of Michigan</span>
                  <span class="certification-date">Aug  2020</span>
                </div>
                <a href="https://www.coursera.org/account/accomplishments/verify/MYX5XU65HP95" target="_blank" class="certification-link">
                  <i class="fas fa-external-link-alt"></i> View Credential
                </a>
              </div>
            </li>

          </ul>
        </div>

      </div>
    </div>
  </div>
</div>

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




================================================================================
File: compile_latex.py
================================================================================

# compile_latex.py
import os
import subprocess

def compile_latex():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to your LaTeX file relative to the script location
    latex_file_path = os.path.join(script_dir, 'cv.tex')
    
    # Check if the LaTeX file exists
    if not os.path.exists(latex_file_path):
        print(f"Error: LaTeX file not found at {latex_file_path}")
        return
    
    # Change the working directory to the script location
    os.chdir(script_dir)
    
    # Compile the LaTeX file to PDF
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", latex_file_path], 
            check=True,
            capture_output=True,
            text=True
        )
        print("PDF generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the PDF: {e}")
        print("\nError output:")
        print(e.output)
    except FileNotFoundError:
        print("Error: pdflatex command not found. Please ensure LaTeX is installed and in your system PATH.")

if __name__ == "__main__":
    compile_latex()



================================================================================
File: cv.tex
================================================================================

\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{black}
\nopagenumbers{}
\usepackage[utf8]{inputenc}
\usepackage{ragged2e}
\usepackage[scale=0.915]{geometry}
\usepackage{import}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{amssymb}
\usepackage{enumitem}

% Sobrescribir estilos para nombre
\renewcommand*{\namefont}{\color{black}\bfseries\Huge}
\renewcommand*{\namestyle}[2]{\namefont #1~#2}

% Sobrescribir estilos para secciones
\renewcommand{\sectionfont}{\color{black}\Large\bfseries}
\renewcommand{\subsectionfont}{\color{black}\large\bfseries}

\name{\textbf{\textcolor{black}{Ronald}}}{\textbf{\textcolor{black}{Mego}}}

\newcommand*{\customcventry}[7][.13em]{
\begin{tabular}{@{}l}
{\bfseries #4} \
{\itshape #3}
\end{tabular}
\hfill
\begin{tabular}{l@{}}
{\bfseries #5} \
{\itshape #2}
\end{tabular}
\ifx&#7&%
\else{\ %
\begin{minipage}{\maincolumnwidth}%
\small#7%
\end{minipage}}\fi%
\par\addvspace{#1}}

\begin{document}

\makecvtitle
\vspace*{-12mm}

\begin{center}\textbf{Head of Data Analytics \& Innovation | Agentic AI / Gen AI | Telecom | Fintech}\end{center}

\vspace{-1.7em}

\begin{center}
\begin{tabular}{ c c c c c c }
\faMobile {+507 64654515} & \enspace  \emailsymbol {ronald.mego@outlook.com} & \enspace \faHome {Panama City, PA} & 
\enspace \faGlobe \href{{https://ronaldmego.github.io/}}{\textcolor{blue}{Web}} &
\enspace \faGithub \href{{https://github.com/ronaldmego}}{\textcolor{blue}{github}} &
\enspace \faLinkedin \href{{https://www.linkedin.com/in/ronaldmego/}}{\textcolor{blue}{LinkedIn}}
\end{tabular}
\end{center}

\vspace{-1.5em}

\section{Profile}
{Data leader with 15+ years of experience helping companies as a professional and consultant in telecom, fintech, and e-commerce industries. I focus on building data-driven solutions that drive revenue growth, optimize costs, and enhance customer experience. My approach combines business strategy with technical expertise in analytics, AI, and data architecture, leading multicultural teams to deliver impactful results. I specialize in turning complex data challenges into clear insights that enable better organizational decision-making. Currently leading data \& AI initiatives at Millicom | Tigo, where I develop data governance projects and implement innovative AI solutions across Latin America.}

\vspace{-0.5em}

\section{Professional Experience}

\customcventry{01/2025 ‐ present}{\color{blue}\href{https://www.millicom.com/}{Millicom | Tigo}}{Data Analytics and Innovation Manager}{Panama City, PA}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Lead and develop a Data Analytics Roadmap to enhance Tigo Users Digital experience (\textasciitilde{}50 million), leveraging AI and Machine Learning models.
\item Design and implement a Data Governance and Monetization Strategy to drive new revenue streams and optimize costs, aligning with the Global CDO.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{08/2023 ‐ 12/2024}{\color{blue}\href{https://www.millicom.com/}{Millicom | Tigo}}{Head of Data - MFS}{Panama City, PA}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Leading Tigo Money's data strategy across Data Governance, analytics and dashboarding to enable monetizable use cases while ensuring compliance standards.
\item Implement Data Analytics tools andframewrok for Mobile Financial Services with Lending Risk management, Fraud detection and Customer Insights.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{12/2021 ‐ 07/2023}{\color{blue}\href{https://www.millicom.com/}{Millicom | Tigo}}{Head of Marketing Analytics - MFS}{Panama City, PA}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Design and lead the Customer Segmentation and Campaign Management strategy powered by Customer Intelligence for Tigo Money, aligned with the Global CMO
\item Develop and implement a Digital Marketing Analytics framework to measure the effectiveness of marketing campaigns, optimizing the funnel conversion and increasing ROI.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{11/2019 ‐ 11/2021}{\color{blue}\href{https://grupoelcomercio.com.pe/}{Grupo El Comercio}}{Data Manager}{Lima, PE}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Lead Data Governance and Develop user segmentation models and content recommendation models, supporting business objectives related to subscription growth and engagement.
\item Implement a zero and 1st (first) party data consolidation project into a golden record, enabling audience data monetization and the generation of new revenue streams.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{11/2016 ‐ 10/2019}{\color{blue}\href{https://telefonica.com.pe/}{Telefonica | Movistar}}{Customer Insights Manager}{Lima, PE}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Data Governance for 17 million customers across home, prepaid, and postpaid products, establishing a single source of truth (SSOT) to support the Customer 360 business strategy, enhancing customer satisfaction and campaign effectiveness.
\item Develop dashboards for sales, collections, and customer support, and implement the first text mining model to analyze customer satisfaction in chatbot interactions.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{08/2009 ‐ 10/2016}{\color{blue}\href{https://telefonica.com.pe/}{Telefónica | Movistar}}{Customer Data Specialist}{Lima, PE}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Delivered robust, customer-centric, and commercially monetizable data solutions, earning outstanding recognition for achievements.
\item Developed analytical models for marketing, sales, customer experience, and collections, optimizing strategies for B2C mobile prepaid, postpaid, and home services.
\end{itemize}
\vspace{-0.1em}
}}

\customcventry{03/2016 ‐ 08/2016}{\color{blue}\href{https://portal.uni.edu.pe/}{Universidad Nacional de Ingenieria}}{Professor of Applied Computational Statistics}{Lima, PE}{}{{
\begin{itemize}[leftmargin=0.6cm, label={\textbullet}, itemsep=-0.2em]
\item Design and execute curriculum incorporating real-world business case studies and data analysis projects, effectively bridging the gap between theoretical knowledge and practical application.
\item Mentor students on academic and career paths in data science and statistics, with several students successfully securing internships and roles in top-tier companies.
\end{itemize}
\vspace{-0.1em}
}}


\vspace{-0.8em}

\section{Education}

\customcventry{2005-2011}{\color{blue}\href{https://www.credential.net/922f2fe3-2fe4-4233-bbb6-1579ff468aa9?username=ronaldfriizmegosolano20070}{Universidad Nacional de Ingenieria}}{BSc. Applied Statistics}{Lima, Peru}{}{Thesis Project: “Segmentation of subscribers by traffic consumption in prepaid lines of Telefonica using k-means multivariate cluster analysis”. Top student, outstanding grade.}

\customcventry{2016-2018}{\color{blue}\href{https://www.credential.net/f953e37b-11e7-4570-89aa-6f21d606132d?username=ronaldfriizmegosolano20070}{PAD Business School}}{Master in Business Administration (MBA)}{Lima, Peru}{}{Thesis Project: “Application of non-operational troubleshooting of Telefonica and its sales channels”. Outstanding grade.}

\customcventry{2024-2024}{\color{blue}\href{https://www.credential.net/f6bd85db-4850-4f50-9609-7990eb0aaadc}{Massachusetts Institute of Technology}}{Diploma Data Leadership & Leveraging Data Systems}{Cambridge, MA, USA}{}{Participated in an immersive program with leaders in data management at the MIT Executive Program.}


\vspace{-0.8em}


\section{Specialized Programs and Diplomas}
{\begin{itemize}[label=\textbullet, itemsep=-0.2em]
\item Data Monetization, Management, and Trends (May. 2024) - \underline{\color{blue}\href{https://courses.edx.org/certificates/447c3529a7dc42aa8bf27297a97b0c88}{IEUniversity \& edX}}
\item Data Strategy: Data as Competitive Advantage (Jan. 2022) - \underline{\color{blue}\href{https://certificates.emeritus.org/39607ed0-10b6-4387-be32-5b34af6a5040}{Berkeley Executive Education}}
\item Entrepreneurship and Innovation Program (May. 2018) - \underline{\color{blue}\href{https://www.credential.net/54b357e1-243e-47ea-a40f-bcfdcfa04b18?username=ronaldfriizmegosolano20070}{Darden School of Business - Charlottesville, VA, USA}}
\item Diploma in Applied Finance (Jul. 2012) - \underline{\color{blue}\href{https://www.credential.net/322f33cb-ee81-453d-994a-3f81db550be9?username=ronaldfriizmegosolano20070}{Universidad del Pacifico}}
\end{itemize}}

\section{Technical Skills and Certifications}
{\begin{itemize}[label=\textbullet, itemsep=-0.2em]
\item AWS Cloud Certified Cloud Practitioner (Apr. 2024) - \underline{\color{blue}\href{https://www.credly.com/badges/b1438ac5-468e-4964-b6ac-2894b7e2204b/linked_in_profile}{Amazon Web Services}}
\item Cloud Data en Azure (Dec. 2023) - \underline{\color{blue}\href{https://www.credential.net/f49190f2-99e2-4af9-83a9-26bef312b87f?username=ronaldfriizmegosolano20070}{Bootcamp Institute \& Microsoft}}
\item GCP, Big Data and ML (May. 2020) - \underline{\color{blue}\href{https://www.coursera.org/account/accomplishments/certificate/RPWJ8S2L8CYW}{Coursera \& Google}}
\item Data Science in Python (Aug. 2020) - \underline{\color{blue}\href{https://www.coursera.org/account/accomplishments/verify/MYX5XU65HP95}{Coursera \& University of Michigan}}
\end{itemize}}


\vspace{-1.5em}

\section{Skills}
\begin{itemize}[label=\textbullet, itemsep=-0.2em]
\item \textbf{Data Strategy}: Data Governance, Data Quality, Data Monetization, Data Privacy, Data Security, Data Ethics
\item \textbf{Soft Skills}: Leadership, Team Management, Project Management, Agile Methodologies, Stakeholder Management
\item \textbf{Financial Skills}: Financial Modeling, Revenue Forecasting, Cost Analysis, Pricing Strategy, Profitability Analysis
\item \textbf{Machine Learning}: Supervised Learning, Unsupervised Learning, Reinforcement Learning, Deep Learning, Natural Language Processing
\item \textbf{Cloud \& DevOps}: AWS, Azure, GCP, Docker, Kubernetes, Terraform
\item \textbf{Data Story Telling}: Advanced Excel, Advanced Power Point, PowerBI, Tableau, Looker Studio, QuickSight, Shiny, Streamlit
\item \textbf{Data tools}: Python, R, SQL, Spark, Hadoop, Snowflake, Redshift, BigQuery, Synapse, CI/CD, ML Ops, Airflow
\end{itemize}


\vspace{-1.5em}

\section{Languages}
\begin{multicols}{2}
\begin{itemize}[label=\textbullet, itemsep=-0.2em]
\item \textbf{English} [Fluent]
\item \textbf{Spanish} [Fluent] - Native
\end{itemize}
\end{multicols}


\end{document}



================================================================================
File: cv_template-no-phone.tex
================================================================================

\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{black}
\nopagenumbers{}
\usepackage[utf8]{inputenc}
\usepackage{ragged2e}
\usepackage[scale=0.915]{geometry}
\usepackage{import}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{amssymb}
\usepackage{enumitem}

% Sobrescribir estilos para nombre
\renewcommand*{\namefont}{\color{black}\bfseries\Huge}
\renewcommand*{\namestyle}[2]{\namefont #1~#2}

% Sobrescribir estilos para secciones
\renewcommand{\sectionfont}{\color{black}\Large\bfseries}
\renewcommand{\subsectionfont}{\color{black}\large\bfseries}

\name{\textbf{\textcolor{black}{{{ name }}}}}{\textbf{\textcolor{black}{{{ lastname }}}}}

\newcommand*{\customcventry}[7][.13em]{
\begin{tabular}{@{}l}
{\bfseries #4} \
{\itshape #3}
\end{tabular}
\hfill
\begin{tabular}{l@{}}
{\bfseries #5} \
{\itshape #2}
\end{tabular}
\ifx&#7&%
\else{\ %
\begin{minipage}{\maincolumnwidth}%
\small#7%
\end{minipage}}\fi%
\par\addvspace{#1}}

\begin{document}

\makecvtitle
\vspace*{-12mm}

\begin{center}\textbf{{{ header }}}\end{center}

\vspace{-1.7em}

\begin{center}
\begin{tabular}{ c c c c c c }
\enspace  \emailsymbol {{{ email }}} & \enspace \faHome {{{ location }}} & 
\enspace \faGlobe \href{{{{ x_url }}}}{\textcolor{blue}{Web}} &
\enspace \faGithub \href{{{{ github_url }}}}{\textcolor{blue}{github}} &
\enspace \faLinkedin \href{{{{ linkedin_url }}}}{\textcolor{blue}{LinkedIn}}
\end{tabular}
\end{center}

\vspace{-1.5em}

\section{Profile}
{{ profile }}

\vspace{-0.5em}

\section{Professional Experience}
{{ work_experience }}

\vspace{-0.8em}

\section{Education}
{{ education }}

\vspace{-0.8em}

{{ optional_sections }}

\vspace{-1.5em}

{{ skills_section }}

\vspace{-1.5em}

{{ languages_section }}

\end{document}



================================================================================
File: cv_template-with-phone.tex
================================================================================

\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{black}
\nopagenumbers{}
\usepackage[utf8]{inputenc}
\usepackage{ragged2e}
\usepackage[scale=0.915]{geometry}
\usepackage{import}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{amssymb}
\usepackage{enumitem}

% Sobrescribir estilos para nombre
\renewcommand*{\namefont}{\color{black}\bfseries\Huge}
\renewcommand*{\namestyle}[2]{\namefont #1~#2}

% Sobrescribir estilos para secciones
\renewcommand{\sectionfont}{\color{black}\Large\bfseries}
\renewcommand{\subsectionfont}{\color{black}\large\bfseries}

\name{\textbf{\textcolor{black}{{{ name }}}}}{\textbf{\textcolor{black}{{{ lastname }}}}}

\newcommand*{\customcventry}[7][.13em]{
\begin{tabular}{@{}l}
{\bfseries #4} \
{\itshape #3}
\end{tabular}
\hfill
\begin{tabular}{l@{}}
{\bfseries #5} \
{\itshape #2}
\end{tabular}
\ifx&#7&%
\else{\ %
\begin{minipage}{\maincolumnwidth}%
\small#7%
\end{minipage}}\fi%
\par\addvspace{#1}}

\begin{document}

\makecvtitle
\vspace*{-12mm}

\begin{center}\textbf{{{ header }}}\end{center}

\vspace{-1.7em}

\begin{center}
\begin{tabular}{ c c c c c c }
\faMobile {{{ mobile }}} & \enspace  \emailsymbol {{{ email }}} & \enspace \faHome {{{ location }}} & 
\enspace \faGlobe \href{{{{ x_url }}}}{\textcolor{blue}{Web}} &
\enspace \faGithub \href{{{{ github_url }}}}{\textcolor{blue}{github}} &
\enspace \faLinkedin \href{{{{ linkedin_url }}}}{\textcolor{blue}{LinkedIn}}
\end{tabular}
\end{center}

\vspace{-1.5em}

\section{Profile}
{{ profile }}

\vspace{-0.5em}

\section{Professional Experience}
{{ work_experience }}

\vspace{-0.8em}

\section{Education}
{{ education }}

\vspace{-0.8em}

{{ optional_sections }}

\vspace{-1.5em}

{{ skills_section }}

\vspace{-1.5em}

{{ languages_section }}

\end{document}



================================================================================
File: cv_template.tex
================================================================================

\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{black}
\nopagenumbers{}
\usepackage[utf8]{inputenc}
\usepackage{ragged2e}
\usepackage[scale=0.915]{geometry}
\usepackage{import}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{amssymb}
\usepackage{enumitem}

% Sobrescribir estilos para nombre
\renewcommand*{\namefont}{\color{black}\bfseries\Huge}
\renewcommand*{\namestyle}[2]{\namefont #1~#2}

% Sobrescribir estilos para secciones
\renewcommand{\sectionfont}{\color{black}\Large\bfseries}
\renewcommand{\subsectionfont}{\color{black}\large\bfseries}

\name{\textbf{\textcolor{black}{{{ name }}}}}{\textbf{\textcolor{black}{{{ lastname }}}}}

\newcommand*{\customcventry}[7][.13em]{
\begin{tabular}{@{}l}
{\bfseries #4} \
{\itshape #3}
\end{tabular}
\hfill
\begin{tabular}{l@{}}
{\bfseries #5} \
{\itshape #2}
\end{tabular}
\ifx&#7&%
\else{\ %
\begin{minipage}{\maincolumnwidth}%
\small#7%
\end{minipage}}\fi%
\par\addvspace{#1}}

\begin{document}

\makecvtitle
\vspace*{-12mm}

\begin{center}\textbf{{{ header }}}\end{center}

\vspace{-1.7em}

\begin{center}
\begin{tabular}{ c c c c c c }
\faMobile {{{ mobile }}} & \enspace  \emailsymbol {{{ email }}} & \enspace \faHome {{{ location }}} & 
\enspace \faGlobe \href{{{{ x_url }}}}{\textcolor{blue}{Web}} &
\enspace \faGithub \href{{{{ github_url }}}}{\textcolor{blue}{github}} &
\enspace \faLinkedin \href{{{{ linkedin_url }}}}{\textcolor{blue}{LinkedIn}}
\end{tabular}
\end{center}

\vspace{-1.5em}

\section{Profile}
{{ profile }}

\vspace{-0.5em}

\section{Professional Experience}
{{ work_experience }}

\vspace{-0.8em}

\section{Education}
{{ education }}

\vspace{-0.8em}

{{ optional_sections }}

\vspace{-1.5em}

{{ skills_section }}

\vspace{-1.5em}

{{ languages_section }}

\end{document}



================================================================================
File: entrypoint.sh
================================================================================

#!/bin/bash
python3 generate_cv.py
python3 compile_latex.py
python3 generate_index.py



================================================================================
File: generate_cv.py
================================================================================

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



================================================================================
File: generate_index.py
================================================================================

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
    <h1>Ronald Mego</h1>
    <p class="tagline">Professional Background</p>
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



================================================================================
File: readme.md
================================================================================

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



================================================================================
File: requirements.txt
================================================================================

# Versiones específicas de las dependencias necesarias para generar el CV
json5==0.9.14
# Estas son las dependencias básicas que tu script necesita
# Agregamos más si el script falla por falta de alguna

