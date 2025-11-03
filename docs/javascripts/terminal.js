/**
 * TERMINAL INTERFACE
 * Interactive terminal-style command interface
 */

// Terminal commands registry
const terminalCommands = {
  help: {
    description: 'Display available commands',
    execute: () => {
      let output = 'AVAILABLE COMMANDS:\n\n';
      for (const [cmd, data] of Object.entries(terminalCommands)) {
        output += `  ${cmd.toUpperCase().padEnd(15)} - ${data.description}\n`;
      }
      return output;
    }
  },
  
  status: {
    description: 'System status information',
    execute: () => {
      return `
⚡ NEURAL.NEXUS STATUS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYSTEM:        ONLINE
MISSION:       ENEM 2026 → UFABC
PROTOCOLS:     CYBERPUNK MODE
NEUROSCIENCE:  ACTIVE
PROGRESS:      CALCULATING...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`;
    }
  },
  
  mission: {
    description: 'Display mission objectives',
    execute: () => {
      return `
🎯 MISSION OBJECTIVES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[█████████░] 90% - ENEM 2026 Preparation
[███████░░░] 70% - Python & Neuroscience
[█████░░░░░] 50% - Open Source Contribution
[███░░░░░░░] 30% - Research Publications

TARGET: UFABC Computational Neuroscience
ROUTE:  PIBIC → FAPESP → BEPE → MASTER'S
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`;
    }
  },
  
  neuro: {
    description: 'Neuroscience learning progress',
    execute: () => {
      return `
🧠 NEUROSCIENCE PROTOCOLS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Coursera: Computational Neuroscience
✓ Neuromatch Academy: In Progress
✓ abagen: Contributing
✓ MNE-Python: Learning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT: Neural Signal Processing
`;
    }
  },
  
  github: {
    description: 'GitHub profile link',
    execute: () => {
      window.open('https://github.com/clouraen', '_blank');
      return 'Opening GitHub profile...';
    }
  },
  
  matrix: {
    description: 'Enter the Matrix',
    execute: () => {
      return `
Wake up, Neo...
The Matrix has you...
Follow the white rabbit.

Knock, knock, Neo.
`;
    }
  },
  
  cyberpunk: {
    description: 'Cyberpunk 2077 quote',
    execute: () => {
      const quotes = [
        '"In 2077, what makes someone a criminal? Getting caught."',
        '"If you wanna make it in Night City, you gotta have chrome."',
        '"Never fade away..." - Johnny Silverhand',
        '"Wake the f*** up, Samurai. We have a city to burn."',
        '"The future is now, choom."'
      ];
      return quotes[Math.floor(Math.random() * quotes.length)];
    }
  },
  
  clear: {
    description: 'Clear terminal screen',
    execute: () => {
      return '[CLEAR]';
    }
  },
  
  whoami: {
    description: 'Display user information',
    execute: () => {
      return `
USER: Cleiton Moura Loura
ROLE: Aspiring Neuroscientist
LOCATION: Brazil → UFABC (2026)
SKILLS: Python, Neuroscience, Open Source
DREAM: Computational Neuroscience Research
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Open knowledge is the future of neuroscience."
`;
    }
  }
};

/**
 * Initialize terminal interface
 */
function initTerminal() {
  // Create terminal toggle button
  const terminalBtn = document.createElement('button');
  terminalBtn.className = 'terminal-toggle';
  terminalBtn.innerHTML = '⌨️ TERMINAL';
  terminalBtn.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    padding: 12px 24px;
    background: #0a0e27;
    color: #00f3ff;
    border: 2px solid #00f3ff;
    border-radius: 4px;
    font-family: 'Roboto Mono', monospace;
    font-weight: 700;
    text-transform: uppercase;
    cursor: pointer;
    z-index: 9998;
    box-shadow: 0 0 20px rgba(0, 243, 255, 0.4);
    transition: all 0.3s ease;
  `;
  
  terminalBtn.addEventListener('mouseenter', () => {
    terminalBtn.style.background = '#00f3ff';
    terminalBtn.style.color = '#0a0e27';
    terminalBtn.style.boxShadow = '0 0 30px rgba(0, 243, 255, 0.7)';
  });
  
  terminalBtn.addEventListener('mouseleave', () => {
    terminalBtn.style.background = '#0a0e27';
    terminalBtn.style.color = '#00f3ff';
    terminalBtn.style.boxShadow = '0 0 20px rgba(0, 243, 255, 0.4)';
  });
  
  document.body.appendChild(terminalBtn);
  
  // Create terminal window
  const terminal = document.createElement('div');
  terminal.className = 'cyber-terminal';
  terminal.style.cssText = `
    position: fixed;
    bottom: -600px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 900px;
    height: 500px;
    background: rgba(10, 14, 39, 0.98);
    border: 2px solid #00f3ff;
    border-radius: 8px 8px 0 0;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    box-shadow: 0 -10px 50px rgba(0, 243, 255, 0.3);
    transition: bottom 0.4s ease;
    font-family: 'Roboto Mono', monospace;
  `;
  
  // Terminal header
  const terminalHeader = document.createElement('div');
  terminalHeader.style.cssText = `
    background: linear-gradient(135deg, #0f1419, #1a1f2e);
    padding: 12px 20px;
    border-bottom: 1px solid #00f3ff;
    display: flex;
    justify-content: space-between;
    align-items: center;
  `;
  terminalHeader.innerHTML = `
    <span style="color: #00f3ff; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
      ⚡ NEURAL.NEXUS TERMINAL ///
    </span>
    <button id="terminal-close" style="
      background: transparent;
      border: 1px solid #ff006e;
      color: #ff006e;
      padding: 4px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-family: 'Roboto Mono', monospace;
      font-weight: 700;
    ">✕ CLOSE</button>
  `;
  
  // Terminal output area
  const terminalOutput = document.createElement('div');
  terminalOutput.id = 'terminal-output';
  terminalOutput.style.cssText = `
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    color: #00f3ff;
    font-size: 14px;
    line-height: 1.6;
  `;
  
  // Welcome message
  terminalOutput.innerHTML = `
<div style="color: #ffbe0b; font-weight: 700;">
⚡ WELCOME TO NEURAL.NEXUS TERMINAL ///
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</div>
<div style="color: #8892b0; margin: 10px 0;">
Type 'help' to see available commands.
Type 'status' for system information.
</div>
<div style="color: #00f3ff;">
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</div>
  `;
  
  // Terminal input area
  const terminalInputArea = document.createElement('div');
  terminalInputArea.style.cssText = `
    display: flex;
    padding: 15px 20px;
    border-top: 1px solid #00f3ff;
    background: #0f1419;
  `;
  
  const prompt = document.createElement('span');
  prompt.textContent = 'root@nexus:~$ ';
  prompt.style.cssText = `
    color: #ff006e;
    font-weight: 700;
    margin-right: 10px;
  `;
  
  const terminalInput = document.createElement('input');
  terminalInput.id = 'terminal-input';
  terminalInput.type = 'text';
  terminalInput.style.cssText = `
    flex: 1;
    background: transparent;
    border: none;
    color: #00f3ff;
    font-family: 'Roboto Mono', monospace;
    font-size: 14px;
    outline: none;
  `;
  terminalInput.setAttribute('autocomplete', 'off');
  terminalInput.setAttribute('spellcheck', 'false');
  
  terminalInputArea.appendChild(prompt);
  terminalInputArea.appendChild(terminalInput);
  
  // Assemble terminal
  terminal.appendChild(terminalHeader);
  terminal.appendChild(terminalOutput);
  terminal.appendChild(terminalInputArea);
  document.body.appendChild(terminal);
  
  // Terminal state
  let terminalOpen = false;
  let commandHistory = [];
  let historyIndex = -1;
  
  // Toggle terminal
  function toggleTerminal() {
    terminalOpen = !terminalOpen;
    terminal.style.bottom = terminalOpen ? '0' : '-600px';
    if (terminalOpen) {
      terminalInput.focus();
    }
  }
  
  terminalBtn.addEventListener('click', toggleTerminal);
  document.getElementById('terminal-close').addEventListener('click', toggleTerminal);
  
  // Handle command input
  terminalInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const command = terminalInput.value.trim().toLowerCase();
      if (command) {
        executeCommand(command);
        commandHistory.push(command);
        historyIndex = commandHistory.length;
        terminalInput.value = '';
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex > 0) {
        historyIndex--;
        terminalInput.value = commandHistory[historyIndex];
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        historyIndex++;
        terminalInput.value = commandHistory[historyIndex];
      } else {
        historyIndex = commandHistory.length;
        terminalInput.value = '';
      }
    }
  });
  
  // Execute command
  function executeCommand(command) {
    const outputDiv = document.getElementById('terminal-output');
    
    // Display command
    const cmdLine = document.createElement('div');
    cmdLine.style.cssText = 'margin-top: 15px; color: #ff006e; font-weight: 700;';
    cmdLine.textContent = `root@nexus:~$ ${command}`;
    outputDiv.appendChild(cmdLine);
    
    // Execute command
    const cmd = terminalCommands[command];
    let result = '';
    
    if (cmd) {
      result = cmd.execute();
    } else {
      result = `Command not found: ${command}\nType 'help' for available commands.`;
    }
    
    // Display result
    if (result === '[CLEAR]') {
      outputDiv.innerHTML = `
<div style="color: #ffbe0b; font-weight: 700;">
⚡ NEURAL.NEXUS TERMINAL ///
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</div>
      `;
    } else {
      const resultDiv = document.createElement('pre');
      resultDiv.style.cssText = `
        margin: 10px 0;
        color: #8892b0;
        white-space: pre-wrap;
        font-family: 'Roboto Mono', monospace;
      `;
      resultDiv.textContent = result;
      outputDiv.appendChild(resultDiv);
    }
    
    // Scroll to bottom
    outputDiv.scrollTop = outputDiv.scrollHeight;
  }
  
  // Keyboard shortcut to open terminal (Ctrl+`)
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === '`') {
      e.preventDefault();
      toggleTerminal();
    }
  });
}

// Initialize terminal on page load
document.addEventListener('DOMContentLoaded', initTerminal);
