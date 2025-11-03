/**
 * CYBERPUNK 2077 INTERACTIVE EFFECTS
 * Neural Nexus JavaScript Enhancements
 */

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
  initCyberpunkEffects();
  initMatrixRain();
  initTypingEffect();
  initGlitchEffects();
  initScanlines();
});

/**
 * Initialize all cyberpunk effects
 */
function initCyberpunkEffects() {
  console.log('%c⚡ NEURAL.NEXUS ONLINE ////', 'color: #00f3ff; font-size: 20px; font-weight: bold;');
  console.log('%cSYSTEM STATUS: ACTIVE', 'color: #ff006e; font-size: 14px;');
  console.log('%cCYBERPUNK MODE: ENABLED', 'color: #ffbe0b; font-size: 14px;');
  
  // Add cyberpunk class to body
  document.body.classList.add('cyberpunk-active');
  
  // Add scanline effect to main content
  const content = document.querySelector('.md-content');
  if (content) {
    content.classList.add('scanline');
  }
  
  // Add glitch effect to site title
  const siteTitle = document.querySelector('.md-header__title');
  if (siteTitle) {
    const titleText = siteTitle.textContent;
    siteTitle.setAttribute('data-text', titleText);
    siteTitle.classList.add('neon-text');
  }
  
  // Add neon effect to navigation links
  const navLinks = document.querySelectorAll('.md-nav__link');
  navLinks.forEach(link => {
    link.addEventListener('mouseenter', function() {
      this.style.textShadow = '0 0 10px rgba(0, 243, 255, 0.8)';
    });
    link.addEventListener('mouseleave', function() {
      this.style.textShadow = '';
    });
  });
  
  // Add glow effect to buttons
  const buttons = document.querySelectorAll('.md-button');
  buttons.forEach(button => {
    button.classList.add('glitch-button');
  });
  
  // Add hologram effect to cards/admonitions
  const admonitions = document.querySelectorAll('.admonition');
  admonitions.forEach(admon => {
    admon.classList.add('hologram');
  });
}

/**
 * Matrix-style digital rain effect
 */
function initMatrixRain() {
  const canvas = document.createElement('canvas');
  canvas.id = 'matrix-canvas';
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100%';
  canvas.style.height = '100%';
  canvas.style.zIndex = '-1';
  canvas.style.opacity = '0.15';
  canvas.style.pointerEvents = 'none';
  document.body.appendChild(canvas);
  
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+-=[]{}|;:,.<>?/~`';
  const charArray = chars.split('');
  
  const fontSize = 14;
  const columns = canvas.width / fontSize;
  const drops = Array(Math.floor(columns)).fill(1);
  
  function drawMatrix() {
    ctx.fillStyle = 'rgba(10, 14, 39, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#00f3ff';
    ctx.font = fontSize + 'px monospace';
    
    for (let i = 0; i < drops.length; i++) {
      const text = charArray[Math.floor(Math.random() * charArray.length)];
      ctx.fillText(text, i * fontSize, drops[i] * fontSize);
      
      if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
  }
  
  setInterval(drawMatrix, 50);
  
  // Resize canvas on window resize
  window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
}

/**
 * Terminal-style typing effect for headers
 */
function initTypingEffect() {
  const headers = document.querySelectorAll('h1, h2');
  
  headers.forEach(header => {
    const text = header.textContent;
    header.textContent = '';
    header.style.borderRight = '2px solid #00f3ff';
    
    let charIndex = 0;
    const typingInterval = setInterval(() => {
      if (charIndex < text.length) {
        header.textContent += text.charAt(charIndex);
        charIndex++;
      } else {
        clearInterval(typingInterval);
        header.style.borderRight = 'none';
      }
    }, 50);
  });
}

/**
 * Random glitch effects on page elements
 */
function initGlitchEffects() {
  function randomGlitch() {
    const elements = document.querySelectorAll('h1, h2, h3, .md-nav__title');
    if (elements.length > 0) {
      const randomEl = elements[Math.floor(Math.random() * elements.length)];
      randomEl.style.animation = 'glitch-text 0.3s';
      
      setTimeout(() => {
        randomEl.style.animation = '';
      }, 300);
    }
  }
  
  // Random glitch every 5-10 seconds
  setInterval(() => {
    if (Math.random() > 0.7) {
      randomGlitch();
    }
  }, 5000);
}

/**
 * Add scanline overlay effect
 */
function initScanlines() {
  const scanlineOverlay = document.createElement('div');
  scanlineOverlay.className = 'scanline-overlay';
  scanlineOverlay.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.15),
      rgba(0, 0, 0, 0.15) 1px,
      transparent 1px,
      transparent 2px
    );
    pointer-events: none;
    z-index: 9999;
    opacity: 0.3;
  `;
  document.body.appendChild(scanlineOverlay);
}

/**
 * Add particle system for background
 */
function initParticleSystem() {
  const particleCanvas = document.createElement('canvas');
  particleCanvas.id = 'particle-canvas';
  particleCanvas.style.position = 'fixed';
  particleCanvas.style.top = '0';
  particleCanvas.style.left = '0';
  particleCanvas.style.width = '100%';
  particleCanvas.style.height = '100%';
  particleCanvas.style.zIndex = '-2';
  particleCanvas.style.opacity = '0.3';
  particleCanvas.style.pointerEvents = 'none';
  document.body.appendChild(particleCanvas);
  
  const ctx = particleCanvas.getContext('2d');
  particleCanvas.width = window.innerWidth;
  particleCanvas.height = window.innerHeight;
  
  const particles = [];
  const particleCount = 100;
  
  class Particle {
    constructor() {
      this.x = Math.random() * particleCanvas.width;
      this.y = Math.random() * particleCanvas.height;
      this.size = Math.random() * 3 + 1;
      this.speedX = Math.random() * 2 - 1;
      this.speedY = Math.random() * 2 - 1;
      this.color = Math.random() > 0.5 ? '#00f3ff' : '#ff006e';
    }
    
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      
      if (this.x > particleCanvas.width) this.x = 0;
      if (this.x < 0) this.x = particleCanvas.width;
      if (this.y > particleCanvas.height) this.y = 0;
      if (this.y < 0) this.y = particleCanvas.height;
    }
    
    draw() {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  
  function initParticles() {
    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }
  }
  
  function animateParticles() {
    ctx.clearRect(0, 0, particleCanvas.width, particleCanvas.height);
    
    particles.forEach(particle => {
      particle.update();
      particle.draw();
    });
    
    requestAnimationFrame(animateParticles);
  }
  
  initParticles();
  animateParticles();
  
  window.addEventListener('resize', function() {
    particleCanvas.width = window.innerWidth;
    particleCanvas.height = window.innerHeight;
  });
}

/**
 * Custom cursor effect
 */
function initCustomCursor() {
  const cursor = document.createElement('div');
  cursor.className = 'custom-cursor';
  cursor.style.cssText = `
    position: fixed;
    width: 20px;
    height: 20px;
    border: 2px solid #00f3ff;
    border-radius: 50%;
    pointer-events: none;
    z-index: 10000;
    transition: transform 0.1s;
    box-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
  `;
  document.body.appendChild(cursor);
  
  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX - 10 + 'px';
    cursor.style.top = e.clientY - 10 + 'px';
  });
  
  document.addEventListener('mousedown', () => {
    cursor.style.transform = 'scale(0.8)';
    cursor.style.borderColor = '#ff006e';
  });
  
  document.addEventListener('mouseup', () => {
    cursor.style.transform = 'scale(1)';
    cursor.style.borderColor = '#00f3ff';
  });
}

/**
 * Boot sequence animation
 */
function showBootSequence() {
  const bootScreen = document.createElement('div');
  bootScreen.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #0a0e27;
    color: #00f3ff;
    font-family: 'Roboto Mono', monospace;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 99999;
    padding: 2rem;
  `;
  
  const bootText = [
    '⚡ INITIALIZING NEURAL.NEXUS ///',
    'LOADING CYBERPUNK PROTOCOLS...',
    'CONNECTING TO MATRIX...',
    'SYSTEM CHECK: OK',
    'WELCOME TO THE FUTURE...'
  ];
  
  bootScreen.innerHTML = '<pre id="boot-output"></pre>';
  document.body.appendChild(bootScreen);
  
  const output = document.getElementById('boot-output');
  let lineIndex = 0;
  
  const bootInterval = setInterval(() => {
    if (lineIndex < bootText.length) {
      output.innerHTML += bootText[lineIndex] + '\n';
      lineIndex++;
    } else {
      clearInterval(bootInterval);
      setTimeout(() => {
        bootScreen.style.transition = 'opacity 0.5s';
        bootScreen.style.opacity = '0';
        setTimeout(() => {
          bootScreen.remove();
        }, 500);
      }, 1000);
    }
  }, 500);
}

// Uncomment to enable boot sequence
// window.addEventListener('load', showBootSequence);

/**
 * Add cyberpunk datetime display
 */
function initDateTimeDisplay() {
  const header = document.querySelector('.md-header');
  if (header) {
    const dateTime = document.createElement('div');
    dateTime.className = 'cyber-datetime';
    dateTime.style.cssText = `
      position: absolute;
      top: 10px;
      right: 20px;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.8em;
      color: #00f3ff;
      text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
    `;
    header.appendChild(dateTime);
    
    function updateDateTime() {
      const now = new Date();
      const formatted = now.toISOString().replace('T', ' ').substr(0, 19);
      dateTime.textContent = `⏰ ${formatted}`;
    }
    
    updateDateTime();
    setInterval(updateDateTime, 1000);
  }
}

// Initialize datetime display
initDateTimeDisplay();
