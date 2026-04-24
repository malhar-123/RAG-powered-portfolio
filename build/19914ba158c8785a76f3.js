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

displayScrollElements(); // ===== TOUCH SUPPORT FOR FLIP CARDS ON MOBILE =====

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
});