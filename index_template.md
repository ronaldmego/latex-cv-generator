---
layout: default
title: Ronald Mego - Data
---

<div class="header-container">
  <img src="{{ site.logo }}" alt="{{ personal.name }} {{ personal.lastname }}" class="profile-image">
  <h1>{{ personal.name }} {{ personal.lastname }}</h1>
  
  <div class="title-container">
    <h2>{{ personal.header }}</h2>
  </div>

  <div class="contact-info">
    <a href="tel:{{ personal.mobile }}" class="contact-item">
      <i class="fas fa-phone"></i> {{ personal.mobile }}
    </a>
    <a href="mailto:{{ personal.email }}" class="contact-item">
      <i class="fas fa-envelope"></i> {{ personal.email }}
    </a>
    <span class="contact-item">
      <i class="fas fa-map-marker-alt"></i> {{ personal.location }}
    </span>
    <a href="{{ personal.linkedin_url }}" class="contact-item" target="_blank">
      <i class="fab fa-linkedin"></i> LinkedIn
    </a>
    <a href="{{ personal.github_url }}" class="contact-item" target="_blank">
      <i class="fab fa-github"></i> GitHub
    </a>
    <a href="{{ personal.twitter_url }}" class="contact-item" target="_blank">
      <i class="fab fa-twitter"></i> Twitter
    </a>
  </div>
</div>

## Profile

{{ profile }}

## Professional Experience

{{ work_experience }}

## Education

{{ education }}

## Technical Skills and Certifications

{{ optional_sections }}

## Skills

{{ skills }}

## Languages

{{ languages }}