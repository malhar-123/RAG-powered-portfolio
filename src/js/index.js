// Import styles
import '../css/styles.scss';

// ===== CUSTOM CURSOR ANIMATION =====
const customCursor = document.getElementById('customCursor');

document.addEventListener('mousemove', (e) => {
  customCursor.style.left = e.clientX + 'px';
  customCursor.style.top = e.clientY + 'px';
});

// Hide custom cursor when mouse leaves window
document.addEventListener('mouseleave', () => {
  customCursor.style.opacity = '0';
});

document.addEventListener('mouseenter', () => {
  customCursor.style.opacity = '1';
});

// ===== SMOOTH SCROLLING FOR NAVIGATION =====
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const href = link.getAttribute('href');
    if (href.startsWith('#')) {
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Update active state
        navLinks.forEach((l) => l.classList.remove('active'));
        link.classList.add('active');
      }
    }
  });
});

// Highlight nav link based on scroll position
const observerOptions = {
  threshold: 0.3,
  rootMargin: '-100px 0px -66% 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      navLinks.forEach((link) => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${entry.target.id}`) {
          link.classList.add('active');
        }
      });
    }
  });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section[id]').forEach((section) => {
  observer.observe(section);
});

// Set current year in footer (if footer exists)
const yearElement = document.getElementById('year');
if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

// Scroll animations for elements
const scrollElements = document.querySelectorAll('.story-card, .exp-item, .project-card, .about-card, .achievement');

const elementInView = (el, dividend = 1) => {
  const elementTop = el.getBoundingClientRect().top;
  return elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend;
};

const elementOutofView = (el) => {
  const elementTop = el.getBoundingClientRect().top;
  return elementTop > (window.innerHeight || document.documentElement.clientHeight);
};

const displayScrollElements = () => {
  scrollElements.forEach((element) => {
    if (elementInView(element, 1.25)) {
      element.classList.add('scrolled');
    } else if (elementOutofView(element)) {
      element.classList.remove('scrolled');
    }
  });
};

window.addEventListener('scroll', () => {
  displayScrollElements();
});

// Trigger on load
displayScrollElements();

// ===== COUNTER ANIMATION FOR BEYOND CODE STATS =====
const animateCounter = (el) => {
  const target = parseInt(el.dataset.count);
  const suffix = el.dataset.suffix || '';
  const duration = 1000;
  const steps = 40;
  const interval = duration / steps;
  let current = 0;

  const timer = setInterval(() => {
    current += 1;
    el.textContent = Math.round((target / steps) * current) + suffix;
    if (current >= steps) {
      el.textContent = target + suffix;
      clearInterval(timer);
    }
  }, interval);
};

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const counter = entry.target.querySelector('.beyond-number[data-count]');
      if (counter && !counter.dataset.animated) {
        counter.dataset.animated = 'true';
        animateCounter(counter);
      }
    }
  });
}, { threshold: 0.6 });

document.querySelectorAll('.beyond-stat').forEach((stat) => {
  counterObserver.observe(stat);
});

// ===== TOUCH SUPPORT FOR FLIP CARDS ON MOBILE =====
const timelineContents = document.querySelectorAll('.timeline-content');

timelineContents.forEach((content) => {
  content.addEventListener('touchstart', (e) => {
    e.preventDefault();
    content.classList.toggle('flipped');
  });

  // Optional: click support too for better UX on mobile
  content.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      content.classList.toggle('flipped');
    }
  });

  // Reset flip when scrolling
  window.addEventListener('scroll', () => {
    content.classList.remove('flipped');
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// RAG CHATBOT — bubble toggle + message handling
// ═══════════════════════════════════════════════════════════════════════════════

(function () {
  // ── Config ─────────────────────────────────────────────────────────────────
  // Replace with your Render URL once deployed, e.g.:
  // const API_BASE = 'https://malhar-portfolio-rag.onrender.com';
  const API_BASE = 'https://malhar-portfolio-rag.onrender.com';

  // ── Element refs ───────────────────────────────────────────────────────────
  const bubble   = document.getElementById('chatBubble');
  const chatWin  = document.getElementById('chatWindow');
  const closeBtn = document.getElementById('chatClose');
  const input    = document.getElementById('chatInput');
  const sendBtn  = document.getElementById('chatSend');
  const messages = document.getElementById('chatMessages');

  if (!bubble || !chatWin) return; // guard: bail if markup isn't there

  // ── Toggle open / close ───────────────────────────────────────────────────
  let isOpen = false;

  function openChat() {
    isOpen = true;
    chatWin.classList.add('chat-window--visible');
    chatWin.setAttribute('aria-hidden', 'false');
    bubble.classList.add('chat-bubble--open');
    input.focus();
  }

  function closeChat() {
    isOpen = false;
    chatWin.classList.remove('chat-window--visible');
    chatWin.setAttribute('aria-hidden', 'true');
    bubble.classList.remove('chat-bubble--open');
  }

  bubble.addEventListener('click', () => (isOpen ? closeChat() : openChat()));
  closeBtn.addEventListener('click', closeChat);

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen) closeChat();
  });

  // ── Message helpers ────────────────────────────────────────────────────────
  function appendMsg(text, role) {
    const div = document.createElement('div');
    div.className = `chat-msg chat-msg--${role}`;
    const p = document.createElement('p');
    p.textContent = text;
    div.appendChild(p);
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return div;
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'chat-msg chat-msg--typing';
    div.id = 'typingIndicator';
    div.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function removeTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.remove();
  }

  // ── Send a message ─────────────────────────────────────────────────────────
  async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    input.value = '';
    sendBtn.disabled = true;
    appendMsg(text, 'user');
    showTyping();

    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });

      removeTyping();

      if (!res.ok) {
        appendMsg('Sorry, something went wrong. Please try again.', 'bot');
      } else {
        const data = await res.json();
        appendMsg(data.response, 'bot');
      }
    } catch {
      removeTyping();
      appendMsg(
        'Could not reach the server. The backend may be waking up — please try again in ~30 seconds.',
        'bot'
      );
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  }

  sendBtn.addEventListener('click', sendMessage);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
})();
