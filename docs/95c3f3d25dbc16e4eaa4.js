function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

/*
 * This is the main entry point for Webpack, the compiler & dependency loader.
 * All files that are necessary for your web page and need to be 'watched' for changes should be included here!
 */
// HTML Files
import '../index.html'; // Stylesheets

import '../css/styles.scss'; // Scripts

import './main.js';
/* ========= Utilities ========= */

var qs = function qs(sel) {
  var ctx = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : document;
  return ctx.querySelector(sel);
};

var qsa = function qsa(sel) {
  var ctx = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : document;
  return _toConsumableArray(ctx.querySelectorAll(sel));
};
/* ========= Navbar: shrink on scroll ========= */


var nav = qs('#navbar');
var links = qsa('#navLinks a');
var sections = links.map(function (a) {
  return qs(a.getAttribute('href'));
});

function resizeNav() {
  if (window.scrollY > 10) nav.classList.add('compact');else nav.classList.remove('compact');
}

window.addEventListener('scroll', resizeNav);
resizeNav();
/* ========= Smooth scrolling (no inline anchors behavior) ========= */

links.forEach(function (a) {
  a.addEventListener('click', function (e) {
    e.preventDefault();
    var id = a.getAttribute('href');
    qs(id).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  });
});
/* ========= Position indicator + active link ========= */

var indicator = qs('#readingIndicator');

function updateIndicator() {
  var _links$activeIdx;

  var docHeight = document.body.scrollHeight - window.innerHeight;
  var progress = Math.min(1, Math.max(0, window.scrollY / (docHeight || 1)));
  indicator.style.width = "".concat(progress * 100, "%"); // highlight the section whose top is just below nav bottom

  var navBottom = nav.getBoundingClientRect().bottom + window.scrollY;
  var activeIdx = sections.length - 1;

  for (var i = 0; i < sections.length; i++) {
    var top = sections[i].offsetTop;

    if (top - 4 > navBottom) {
      activeIdx = Math.max(0, i - 1);
      break;
    }
  }

  links.forEach(function (l) {
    return l.classList.remove('active');
  });
  (_links$activeIdx = links[activeIdx]) === null || _links$activeIdx === void 0 ? void 0 : _links$activeIdx.classList.add('active');
}

window.addEventListener('scroll', updateIndicator);
window.addEventListener('resize', updateIndicator);
window.addEventListener('load', updateIndicator);
/* ========= Modal logic (About + Work detail modals) ========= */

function openModal(el) {
  el.setAttribute('aria-hidden', 'false');
}

function closeModal(el) {
  el.setAttribute('aria-hidden', 'true');
}

qs('#openAboutModal').addEventListener('click', function () {
  return openModal(qs('#aboutModal'));
});
qsa('[data-open]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var target = qs(btn.getAttribute('data-open'));
    if (target) openModal(target);
  });
});
qsa('.modal').forEach(function (m) {
  m.addEventListener('click', function (e) {
    if (e.target.matches('[data-close], .modal__backdrop')) closeModal(m);
  });
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') qsa('.modal[aria-hidden="false"]').forEach(closeModal);
});
/* ========= Carousel (vanilla) ========= */

var track = qs('#caroTrack');
var prevBtn = qs('[data-caro-prev]');
var nextBtn = qs('[data-caro-next]');
var cur = 0;

function go(idx) {
  var slides = qsa('.caro-slide', track);
  cur = (idx + slides.length) % slides.length;
  track.style.transform = "translateX(-".concat(cur * 100, "%)");
  slides.forEach(function (s, i) {
    return s.classList.toggle('current', i === cur);
  });
}

prevBtn.addEventListener('click', function () {
  return go(cur - 1);
});
nextBtn.addEventListener('click', function () {
  return go(cur + 1);
});
var auto = setInterval(function () {
  return go(cur + 1);
}, 5000);
[prevBtn, nextBtn, track].forEach(function (el) {
  return el.addEventListener('pointerdown', function () {
    clearInterval(auto);
  });
});
/* ========= Footer year ========= */

qs('#year').textContent = new Date().getFullYear(); // =============================================================================
// RAG CHATBOT — bubble toggle + message handling
// =============================================================================

(function () {
  var API_BASE = 'https://rag-powered-portfolio.onrender.com';
  var bubble = document.getElementById('chatBubble');
  var chatWin = document.getElementById('chatWindow');
  var closeBtn = document.getElementById('chatClose');
  var input = document.getElementById('chatInput');
  var sendBtn = document.getElementById('chatSend');
  var messages = document.getElementById('chatMessages');
  if (!bubble || !chatWin) return;
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
  closeBtn.addEventListener('click', closeChat);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen) closeChat();
  });

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
  }

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
              appendMsg('Could not reach the server — it may be waking up. Please try again in ~30 seconds.', 'bot');

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