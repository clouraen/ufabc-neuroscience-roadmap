---
title: "Language Selection"
layout: default
redirect_from: /
---

<script>
  // Detect browser language
  const browserLang = navigator.language || navigator.userLanguage;
  const lang = browserLang.startsWith('pt') ? 'pt' : 'en';
  
  // Check if there's a saved preference
  const savedLang = localStorage.getItem('preferred-language');
  const preferredLang = savedLang || lang;
  
  // Redirect to preferred language
  window.location.href = '/' + preferredLang + '/';
</script>

<div style="text-align: center; padding: 50px;">
  <h1>🌍 Select Language / Selecionar Idioma</h1>
  <p style="margin: 30px 0;">
    <a href="/pt/" style="margin: 10px; padding: 15px 30px; background: #0066cc; color: white; text-decoration: none; border-radius: 5px;">Português</a>
    <a href="/en/" style="margin: 10px; padding: 15px 30px; background: #0066cc; color: white; text-decoration: none; border-radius: 5px;">English</a>
  </p>
  <p style="color: #666;">Redirecting automatically based on your browser language...</p>
</div>
