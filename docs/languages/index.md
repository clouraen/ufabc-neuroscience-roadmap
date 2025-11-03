---
title: "Select Language"
layout: default
---

# 🌍 Select Language / Selecionar Idioma

Choose your preferred language to view the content.

<script src="/languages.json"></script>
<script>
  fetch('/languages.json')
    .then(response => response.json())
    .then(data => {
      const container = document.querySelector('.languages-grid');
      const languages = data.languages;
      const sorted = Object.entries(languages).sort((a, b) => a[1].name.localeCompare(b[1].name));
      
      sorted.forEach(([code, info]) => {
        const div = document.createElement('div');
        div.className = 'language-card';
        div.style.cssText = 'padding: 15px; margin: 10px; border: 1px solid #ddd; border-radius: 5px; text-align: center; cursor: pointer; transition: all 0.3s;';
        div.innerHTML = `
          <div style="font-size: 2em; margin-bottom: 10px;">${info.flag}</div>
          <div style="font-weight: bold; margin-bottom: 5px;">${info.native}</div>
          <div style="font-size: 0.9em; color: #666;">${info.name}</div>
        `;
        div.onclick = () => {
          localStorage.setItem('preferred-language', code);
          window.location.href = '/' + code + '/';
        };
        div.onmouseover = function() { this.style.backgroundColor = '#f5f5f5'; };
        div.onmouseout = function() { this.style.backgroundColor = 'white'; };
        container.appendChild(div);
      });
    })
    .catch(err => {
      document.querySelector('.languages-grid').innerHTML = '<p>Error loading languages. Please try again later.</p>';
    });
</script>

<style>
  .languages-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 10px;
    margin: 20px 0;
  }
  
  .language-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
</style>

<div class="languages-grid"></div>

<p style="text-align: center; color: #666; margin-top: 30px;">
  Total languages supported: <strong id="lang-count">Loading...</strong>
</p>

<script>
  fetch('/languages.json')
    .then(response => response.json())
    .then(data => {
      document.getElementById('lang-count').textContent = Object.keys(data.languages).length;
    });
</script>

