function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

// Import styles
import '../css/styles.scss'; // ===== CUSTOM CURSOR ANIMATION =====

var customCursor = document.getElementById('customCursor');
document.addEventListener('mousemove', function (e) {
  customCursor.style.left = e.clientX + 'px';
  customCursor.style.top = e.clientY + 'px';
}); // Hide custom cursor when mouse leaves window

document.addEventListener('mouseleave', function () {
  customCursor.style.opacity = '0';
});
document.addEventListener('mouseenter', function () {
  customCursor.style.opacity = '1';
}); // ===== SMOOTH SCROLLING FOR NAVIGATION =====

var navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(function (link) {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    var href = link.getAttribute('href');

    if (href.startsWith('#')) {
      var target = document.querySelector(href);

      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        }); // Update active state

        navLinks.forEach(function (l) {
          return l.classList.remove('active');
        });
        link.classList.add('active');
      }
    }
  });
}); // Highlight nav link based on scroll position

var observerOptions = {
  threshold: 0.3,
  rootMargin: '-100px 0px -66% 0px'
};
var observer = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      navLinks.forEach(function (link) {
        link.classList.remove('active');

        if (link.getAttribute('href') === "#".concat(entry.target.id)) {
          link.classList.add('active');
        }
      });
    }
  });
}, observerOptions); // Observe all sections

document.querySelectorAll('section[id]').forEach(function (section) {
  observer.observe(section);
}); // Set current year in footer (if footer exists)

var yearElement = document.getElementById('year');

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
} // Scroll animations for elements


var scrollElements = document.querySelectorAll('.story-card, .exp-item, .project-card, .about-card, .achievement');

var elementInView = function elementInView(el) {
  var dividend = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;
  var elementTop = el.getBoundingClientRect().top;
  return elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend;
};

var elementOutofView = function elementOutofView(el) {
  var elementTop = el.getBoundingClientRect().top;
  return elementTop > (window.innerHeight || document.documentElement.clientHeight);
};

var displayScrollElements = function displayScrollElements() {
  scrollElements.forEach(function (element) {
    if (elementInView(element, 1.25)) {
      element.classList.add('scrolled');
    } else if (elementOutofView(element)) {
      element.classList.remove('scrolled');
    }
  });
};

window.addEventListener('scroll', function () {
  displayScrollElements();
}); // Trigger on load

displayScrollElements(); // ===== COUNTER ANIMATION FOR BEYOND CODE STATS =====

var animateCounter = function animateCounter(el) {
  var target = parseInt(el.dataset.count);
  var suffix = el.dataset.suffix || '';
  var duration = 1000;
  var steps = 40;
  var interval = duration / steps;
  var current = 0;
  var timer = setInterval(function () {
    current += 1;
    el.textContent = Math.round(target / steps * current) + suffix;

    if (current >= steps) {
      el.textContent = target + suffix;
      clearInterval(timer);
    }
  }, interval);
};

var counterObserver = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      var counter = entry.target.querySelector('.beyond-number[data-count]');

      if (counter && !counter.dataset.animated) {
        counter.dataset.animated = 'true';
        animateCounter(counter);
      }
    }
  });
}, {
  threshold: 0.6
});
document.querySelectorAll('.beyond-stat').forEach(function (stat) {
  counterObserver.observe(stat);
}); // ===== TOUCH SUPPORT FOR FLIP CARDS ON MOBILE =====

var timelineContents = document.querySelectorAll('.timeline-content');
timelineContents.forEach(function (content) {
  content.addEventListener('touchstart', function (e) {
    e.preventDefault();
    content.classList.toggle('flipped');
  }); // Optional: click support too for better UX on mobile

  content.addEventListener('click', function () {
    if (window.innerWidth <= 768) {
      content.classList.toggle('flipped');
    }
  }); // Reset flip when scrolling

  window.addEventListener('scroll', function () {
    content.classList.remove('flipped');
  });
}); // ═══════════════════════════════════════════════════════════════════════════════
// RAG CHATBOT — bubble toggle + message handling
// ═══════════════════════════════════════════════════════════════════════════════

(function () {
  // ── Config ─────────────────────────────────────────────────────────────────
  // Replace with your Render URL once deployed, e.g.:
  // const API_BASE = 'https://malhar-portfolio-rag.onrender.com';
  var API_BASE = 'https://malhar-portfolio-rag.onrender.com'; // ── Element refs ───────────────────────────────────────────────────────────

  var bubble = document.getElementById('chatBubble');
  var chatWin = document.getElementById('chatWindow');
  var closeBtn = document.getElementById('chatClose');
  var input = document.getElementById('chatInput');
  var sendBtn = document.getElementById('chatSend');
  var messages = document.getElementById('chatMessages');
  if (!bubble || !chatWin) return; // guard: bail if markup isn't there
  // ── Toggle open / close ───────────────────────────────────────────────────

  var isOpen = false;

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

  bubble.addEventListener('click', function () {
    return isOpen ? closeChat() : openChat();
  });
  closeBtn.addEventListener('click', closeChat); // Close on Escape key

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen) closeChat();
  }); // ── Message helpers ────────────────────────────────────────────────────────

  function appendMsg(text, role) {
    var div = document.createElement('div');
    div.className = "chat-msg chat-msg--".concat(role);
    var p = document.createElement('p');
    p.textContent = text;
    div.appendChild(p);
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return div;
  }

  function showTyping() {
    var div = document.createElement('div');
    div.className = 'chat-msg chat-msg--typing';
    div.id = 'typingIndicator';
    div.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function removeTyping() {
    var el = document.getElementById('typingIndicator');
    if (el) el.remove();
  } // ── Send a message ─────────────────────────────────────────────────────────


  function sendMessage() {
    return _sendMessage.apply(this, arguments);
  }

  function _sendMessage() {
    _sendMessage = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
      var text, res, data;
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              text = input.value.trim();

              if (text) {
                _context.next = 3;
                break;
              }

              return _context.abrupt("return");

            case 3:
              input.value = '';
              sendBtn.disabled = true;
              appendMsg(text, 'user');
              showTyping();
              _context.prev = 7;
              _context.next = 10;
              return fetch("".concat(API_BASE, "/chat"), {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                  message: text
                })
              });

            case 10:
              res = _context.sent;
              removeTyping();

              if (res.ok) {
                _context.next = 16;
                break;
              }

              appendMsg('Sorry, something went wrong. Please try again.', 'bot');
              _context.next = 20;
              break;

            case 16:
              _context.next = 18;
              return res.json();

            case 18:
              data = _context.sent;
              appendMsg(data.response, 'bot');

            case 20:
              _context.next = 26;
              break;

            case 22:
              _context.prev = 22;
              _context.t0 = _context["catch"](7);
              removeTyping();
              appendMsg('Could not reach the server. The backend may be waking up — please try again in ~30 seconds.', 'bot');

            case 26:
              _context.prev = 26;
              sendBtn.disabled = false;
              input.focus();
              return _context.finish(26);

            case 30:
            case "end":
              return _context.stop();
          }
        }
      }, _callee, null, [[7, 22, 26, 30]]);
    }));
    return _sendMessage.apply(this, arguments);
  }

  sendBtn.addEventListener('click', sendMessage);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
})();