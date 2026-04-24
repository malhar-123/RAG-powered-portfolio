// Import styles
import '../css/styles.scss'; // ===== SMOOTH SCROLLING & NAV HIGHLIGHTING =====
// Update nav links on scroll

var observerOptions = {
  threshold: 0.3,
  rootMargin: '-100px 0px -66% 0px'
};
var observer = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      var navLinks = document.querySelectorAll('.nav-links a');
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
}); // Set current year in footer

var yearElement = document.getElementById('year');

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
} // Smooth scroll for nav links


document.querySelectorAll('.nav-links a').forEach(function (link) {
  link.addEventListener('click', function (e) {
    var href = link.getAttribute('href');

    if (href.startsWith('#')) {
      e.preventDefault();
      var target = document.querySelector(href);

      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
        link.classList.add('active');
      }
    }
  });
}); // Smooth scroll for CTA buttons

document.querySelectorAll('a[href^="#"]').forEach(function (link) {
  link.addEventListener('click', function (e) {
    var href = link.getAttribute('href');

    if (href !== '#' && href.length > 1) {
      e.preventDefault();
      var target = document.querySelector(href);

      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    }
  });
}); // Scroll animations for elements

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

displayScrollElements();