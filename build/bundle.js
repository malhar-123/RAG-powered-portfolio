/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "../node_modules/css-loader/dist/cjs.js!../node_modules/postcss-loader/dist/cjs.js!../node_modules/sass-loader/dist/cjs.js!./css/styles.scss":
/*!***************************************************************************************************************************************************!*\
  !*** ../node_modules/css-loader/dist/cjs.js!../node_modules/postcss-loader/dist/cjs.js!../node_modules/sass-loader/dist/cjs.js!./css/styles.scss ***!
  \***************************************************************************************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/sourceMaps.js */ "../node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/api.js */ "../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, `@charset "UTF-8";
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif;
  background: #000000;
  color: #FFFFFF;
  line-height: 1.6;
  font-weight: 400;
  cursor: none;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.custom-cursor {
  position: fixed;
  width: 20px;
  height: 20px;
  border: 2px solid #FFFF00;
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 10px rgba(255, 255, 0, 0.3);
  transition: all 0.05s ease-out;
}

.sidebar-nav {
  display: none;
}

.sidebar-close {
  display: none;
}

.sidebar-menu {
  display: none;
}

.nav-item {
  display: none;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #333333;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 2rem;
  z-index: 1000;
}

.header-nav {
  display: flex;
  gap: 3rem;
  align-items: center;
}

.nav-link {
  color: #E0E0E0;
  font-weight: 500;
  font-size: 0.95rem;
  letter-spacing: 0.5px;
  text-transform: capitalize;
  transition: all 0.3s ease;
  position: relative;
}
.nav-link:hover {
  color: #FFFF00;
}
.nav-link::after {
  content: "";
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: #FFFF00;
  transition: width 0.3s ease;
}
.nav-link:hover::after {
  width: 100%;
}

.menu-burger {
  display: none;
}

.header-logo {
  display: none;
}

.header-actions {
  display: none;
}

.theme-toggle {
  display: none;
}

.remix-btn {
  display: none;
}

.hero {
  padding-top: 120px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000000;
  position: relative;
}

.hero-content {
  text-align: center;
  max-width: 1000px;
  width: 100%;
  padding: 0 2rem;
}

.hero-title {
  font-family: "Playfair Display", serif;
  font-size: clamp(4rem, 20vw, 10rem);
  font-weight: 900;
  color: #FFFFFF;
  line-height: 1.1;
  letter-spacing: -2px;
  margin: 0 0 1.5rem 0;
  text-transform: capitalize;
}

.hero-tagline {
  color: #E0E0E0;
  font-size: clamp(1rem, 3vw, 1.3rem);
  font-weight: 400;
  letter-spacing: 0.5px;
  margin: 0;
  line-height: 1.6;
}

section {
  padding: 6rem 2rem;
  border-bottom: 1px solid #333333;
}
section:last-of-type {
  border-bottom: none;
}

.section-title {
  font-family: "Playfair Display", serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 900;
  color: #FFFF00;
  text-transform: uppercase;
  margin-bottom: 3rem;
  letter-spacing: -0.5px;
}

.section-intro {
  color: #E0E0E0;
  font-size: 1.05rem;
  max-width: 700px;
  margin-bottom: 3rem;
}

.skills-evolution-timeline {
  position: relative;
  padding: 3rem 0;
  max-width: 900px;
  margin: 0 auto;
}

.timeline-line {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, #FFFF00, #DDDD00, transparent);
  transform: translateX(-50%);
}
@media (max-width: 768px) {
  .timeline-line {
    left: 30px;
  }
}

.timeline-item {
  margin-bottom: 1.5rem;
  display: flex;
  position: relative;
  opacity: 0.8;
  transition: all 0.4s ease;
}
.timeline-item:hover {
  opacity: 1;
  transform: scale(1.02);
}
.timeline-item:nth-child(odd) {
  flex-direction: row;
}
.timeline-item:nth-child(even) {
  flex-direction: row-reverse;
}
@media (max-width: 768px) {
  .timeline-item {
    flex-direction: row !important;
    margin-left: 0;
  }
}

.timeline-dot {
  position: absolute;
  left: 50%;
  top: 30px;
  width: 16px;
  height: 16px;
  background: #FFFF00;
  border: 3px solid #000000;
  border-radius: 50%;
  transform: translateX(-50%);
  box-shadow: 0 0 20px rgba(255, 255, 0, 0.5);
  z-index: 10;
  flex-shrink: 0;
}
@media (max-width: 768px) {
  .timeline-dot {
    left: 30px;
    top: 30px;
  }
}

.timeline-content {
  width: 45%;
  padding: 1.5rem;
  background: #262626;
  border: 1px solid #333333;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
  perspective: 1000px;
  min-height: 400px;
}
.timeline-content:hover {
  border-color: #FFFF00;
  box-shadow: 0 0 30px rgba(255, 255, 0, 0.1);
  background: rgba(38, 38, 38, 0.8);
}
@media (max-width: 768px) {
  .timeline-content {
    width: calc(100% - 80px);
    margin-left: 70px;
    padding: 2rem;
    min-height: 350px;
  }
}

.flip-card {
  width: 100%;
  height: 100%;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  transform-style: preserve-3d;
}

.timeline-content:hover .flip-card-inner,
.timeline-content.flipped .flip-card-inner {
  transform: rotateY(180deg);
}

@media (max-width: 768px) {
  .timeline-content:hover .flip-card-inner {
    transform: rotateY(0deg);
  }
}
.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  box-sizing: border-box;
  overflow: hidden;
}

.flip-card-front {
  transform: rotateY(0deg);
  padding: 0.6rem;
}

.flip-card-back {
  transform: rotateY(180deg);
  background: transparent;
  padding: 0.8rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.description-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  width: 100%;
}
.description-list li {
  color: #E0E0E0;
  font-size: 0.85rem;
  line-height: 1.35;
  padding: 0.35rem 0 0.35rem 1.8rem;
  position: relative;
  font-weight: 500;
  transition: all 0.2s ease;
}
.description-list li::before {
  content: "▸";
  position: absolute;
  left: 0.3rem;
  color: #FFFF00;
  font-weight: 900;
  font-size: 0.9rem;
}
.description-list li:hover {
  color: #FFFF00;
  padding-left: 2rem;
}

.timeline-item:nth-child(odd) .timeline-content {
  margin-right: auto;
  margin-left: 0;
}
@media (max-width: 768px) {
  .timeline-item:nth-child(odd) .timeline-content {
    margin-left: 70px;
    margin-right: 0;
  }
}

.timeline-item:nth-child(even) .timeline-content {
  margin-left: auto;
  margin-right: 0;
}
@media (max-width: 768px) {
  .timeline-item:nth-child(even) .timeline-content {
    margin-left: 70px;
    margin-right: 0;
  }
}

.timeline-year {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 700;
  color: #FFFF00;
  background: rgba(255, 255, 0, 0.1);
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  margin-bottom: 0.2rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.timeline-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0.1rem 0 0.1rem 0;
  font-family: "Playfair Display", serif;
}

.timeline-subtitle {
  font-size: 0.95rem;
  color: #FFFF00;
  font-weight: 600;
  margin-bottom: 0.3rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.timeline-description {
  font-size: 0.95rem;
  color: #E0E0E0;
  line-height: 1.7;
  margin-top: 1rem;
}

.skills-box {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin: 0.3rem 0;
  align-items: center;
}

.skill-chip {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  background: rgba(255, 255, 0, 0.08);
  border: 1px solid rgba(255, 255, 0, 0.3);
  border-radius: 20px;
  font-size: 0.75rem;
  color: #FFFF00;
  font-weight: 500;
  transition: all 0.3s ease;
  white-space: nowrap;
}
.skill-chip:hover {
  background: rgba(255, 255, 0, 0.15);
  border-color: #FFFF00;
  box-shadow: 0 0 10px rgba(255, 255, 0, 0.2);
}

.about-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 4rem;
}

@keyframes cardFadeUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes factSlideIn {
  from {
    opacity: 0;
    transform: translateX(-16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
.about-card {
  background: #1a1a1a;
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid #333333;
  border-top: 3px solid #FFFF00;
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
}
.about-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(ellipse at top left, rgba(255, 255, 0, 0.04) 0%, transparent 60%);
  pointer-events: none;
}
.about-card.scrolled {
  animation: cardFadeUp 0.6s ease forwards;
}
.about-card.scrolled .fact-item {
  animation: factSlideIn 0.4s ease forwards;
}
.about-card.scrolled .fact-item:nth-child(1) {
  animation-delay: 0.18s;
}
.about-card.scrolled .fact-item:nth-child(2) {
  animation-delay: 0.26s;
}
.about-card.scrolled .fact-item:nth-child(3) {
  animation-delay: 0.34s;
}
.about-card.scrolled .fact-item:nth-child(4) {
  animation-delay: 0.42s;
}
.about-card.scrolled .beyond-stat {
  animation: factSlideIn 0.4s ease forwards;
}
.about-card.scrolled .beyond-stat:nth-child(1) {
  animation-delay: 0.18s;
}
.about-card.scrolled .beyond-stat:nth-child(2) {
  animation-delay: 0.26s;
}
.about-card.scrolled .beyond-stat:nth-child(3) {
  animation-delay: 0.34s;
}
.about-card.scrolled .beyond-stat:nth-child(4) {
  animation-delay: 0.42s;
}
.about-card:hover {
  border-color: #FFFF00;
  box-shadow: 0 8px 32px rgba(255, 255, 0, 0.08);
  transform: translateY(-4px);
}

.about-card-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.75rem;
}
.about-card-header .about-card-fa-icon {
  font-size: 1.1rem;
  color: #FFFF00;
  width: 1.2rem;
  text-align: center;
}
.about-card-header h3 {
  color: #FFFF00;
  font-size: 1.3rem;
  font-weight: 700;
  margin: 0;
}

.about-intro {
  color: #999999;
  font-size: 0.88rem;
  font-style: italic;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  border-left: 2px solid #FFFF00;
  padding-left: 0.75rem;
}

.facts-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.fact-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  color: #E0E0E0;
  font-size: 0.95rem;
  line-height: 1.6;
  opacity: 0;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  transition: background 0.2s ease;
}
.fact-item:hover {
  background: #262626;
}
.fact-item .fact-fa-icon {
  font-size: 0.85rem;
  color: #FFFF00;
  flex-shrink: 0;
  margin-top: 4px;
  width: 1rem;
  text-align: center;
}
.fact-item strong {
  color: #FFFF00;
}

.stack-domains {
  margin-top: 1.25rem;
  padding-top: 1.1rem;
  border-top: 1px solid #333333;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.stack-domain {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.stack-domain-label {
  font-size: 0.7rem;
  font-weight: 700;
  color: #999999;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  width: 2.8rem;
  flex-shrink: 0;
}

.stack-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.stack-chip {
  font-size: 0.75rem;
  font-weight: 600;
  color: #FFFF00;
  background: rgba(255, 255, 0, 0.07);
  border: 1px solid rgba(255, 255, 0, 0.25);
  border-radius: 4px;
  padding: 0.2rem 0.6rem;
  letter-spacing: 0.02em;
  transition: background 0.2s ease, border-color 0.2s ease;
}
.stack-chip:hover {
  background: rgba(255, 255, 0, 0.14);
  border-color: #FFFF00;
}

.beyond-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.85rem;
}

.beyond-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: #262626;
  border: 1px solid #333333;
  border-radius: 10px;
  padding: 1.1rem 0.75rem;
  opacity: 0;
  transition: all 0.25s ease;
  cursor: default;
}
.beyond-stat:hover {
  border-color: #FFFF00;
  background: #2a2a00;
  transform: scale(1.03);
}
.beyond-stat .beyond-fa-icon {
  font-size: 1.4rem;
  color: #999999;
  margin-bottom: 0.4rem;
  transition: color 0.2s ease;
}
.beyond-stat:hover .beyond-fa-icon {
  color: #FFFF00;
}
.beyond-stat .beyond-number {
  color: #FFFF00;
  font-size: 1.5rem;
  font-weight: 800;
  line-height: 1.2;
}
.beyond-stat .beyond-number--text {
  font-size: 1.2rem;
}
.beyond-stat .beyond-label {
  color: #999999;
  font-size: 0.78rem;
  margin-top: 0.2rem;
  line-height: 1.4;
}
.beyond-stat--highlight {
  border-color: rgba(255, 255, 0, 0.2);
  background: linear-gradient(135deg, #262626 0%, #1e1e00 100%);
}
.beyond-stat--highlight .beyond-fa-icon {
  color: #FFFF00;
}
.beyond-stat--highlight .beyond-label {
  color: #E0E0E0;
  font-style: italic;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.project-card {
  background: #1a1a1a;
  padding: 2rem;
  border-radius: 8px;
  border: 1px solid #333333;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}
.project-card:hover {
  background: #262626;
  border-color: #FFFF00;
  transform: translateY(-4px);
}
.project-card.featured {
  grid-column: span 2;
}
@media (max-width: 768px) {
  .project-card.featured {
    grid-column: span 1;
  }
}
.project-card .project-tag {
  display: inline-block;
  background: #FFFF00;
  color: #000000;
  padding: 0.3rem 0.8rem;
  border-radius: 12px;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 1rem;
  align-self: flex-start;
}
.project-card h3 {
  color: #FFFFFF;
  font-size: 1.1rem;
  margin-bottom: 0.75rem;
  font-weight: 700;
  line-height: 1.35;
}
.project-card p {
  color: #E0E0E0;
  font-size: 0.92rem;
  line-height: 1.65;
  flex-grow: 1;
}

.project-link {
  display: inline-block;
  margin-top: 1.25rem;
  color: #FFFF00;
  font-size: 0.82rem;
  font-weight: 600;
  text-decoration: none;
  letter-spacing: 0.02em;
  border-bottom: 1px solid rgba(255, 255, 0, 0.35);
  padding-bottom: 2px;
  transition: border-color 0.2s ease, opacity 0.2s ease;
  align-self: flex-start;
}
.project-link:hover {
  border-color: #FFFF00;
  opacity: 0.8;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.project-tech span {
  background: rgba(255, 255, 0, 0.1);
  color: #FFFF00;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.8rem;
  border: 1px solid rgba(255, 255, 0, 0.3);
}

.bullet-list {
  list-style: none;
  padding: 0;
  margin: 0.85rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}
.bullet-list li {
  color: #E0E0E0;
  font-size: 0.92rem;
  line-height: 1.6;
  padding-left: 1.1rem;
  position: relative;
}
.bullet-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.58em;
  width: 5px;
  height: 5px;
  background: #FFFF00;
  border-radius: 50%;
  flex-shrink: 0;
}
.bullet-list li strong {
  color: #FFFF00;
}

.exp-timeline {
  margin-top: 3rem;
}

.exp-item {
  background: #1a1a1a;
  padding: 2rem;
  margin-bottom: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #FFFF00;
  transition: all 0.3s ease;
}
.exp-item:hover {
  background: #262626;
  transform: translateX(4px);
}
.exp-item h3 {
  color: #FFFFFF;
  font-size: 1.05rem;
  margin-bottom: 0.25rem;
  font-weight: 700;
}
.exp-item .exp-role {
  color: #999999;
  font-size: 0.85rem;
  font-weight: 500;
}
.exp-item p {
  color: #E0E0E0;
  font-size: 0.95rem;
  margin: 0.8rem 0;
  line-height: 1.6;
}

.exp-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 0.3rem;
  flex-wrap: wrap;
}

.exp-date {
  color: #999999;
  font-size: 0.8rem;
  white-space: nowrap;
  padding-top: 0.2rem;
  flex-shrink: 0;
}

.exp-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 1rem;
}
.exp-tags span {
  background: rgba(255, 255, 0, 0.1);
  color: #FFFF00;
  padding: 0.3rem 0.7rem;
  border-radius: 4px;
  font-size: 0.75rem;
  border: 1px solid rgba(255, 255, 0, 0.3);
}

.edu-items {
  display: grid;
  gap: 2rem;
  margin-top: 3rem;
}

.edu-item {
  background: #1a1a1a;
  padding: 2rem;
  border-radius: 8px;
  border: 1px solid #333333;
}
.edu-item h3 {
  color: #FFFF00;
  font-size: 1.1rem;
  margin-bottom: 0.3rem;
  font-weight: 700;
}
.edu-item .edu-school {
  color: #999999;
  font-size: 0.9rem;
  display: block;
  margin-bottom: 0.8rem;
}
.edu-item p {
  color: #E0E0E0;
  font-size: 0.95rem;
  line-height: 1.6;
}

.edu-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.3rem;
}

.edu-date {
  color: #999999;
  font-size: 0.8rem;
  white-space: nowrap;
  padding-top: 0.2rem;
  flex-shrink: 0;
}

.leadership {
  padding: 6rem 2rem;
}

.leadership-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-top: 3rem;
}

.leadership-card {
  background: #1a1a1a;
  padding: 1.75rem;
  border-radius: 8px;
  border: 1px solid #333333;
  border-top: 3px solid rgba(255, 255, 0, 0.35);
  transition: all 0.3s ease;
}
.leadership-card:hover {
  border-top-color: #FFFF00;
  background: #262626;
  transform: translateY(-3px);
}
.leadership-card h3 {
  color: #FFFF00;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.2rem;
}
.leadership-card p {
  color: #E0E0E0;
  font-size: 0.9rem;
  line-height: 1.65;
  margin-top: 0.75rem;
}

.leadership-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  flex-wrap: wrap;
}

.leadership-org {
  color: #999999;
  font-size: 0.82rem;
  font-weight: 500;
  display: block;
}

.leadership-date {
  color: #999999;
  font-size: 0.78rem;
  white-space: nowrap;
  flex-shrink: 0;
  padding-top: 0.15rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 3rem;
  margin-top: 3rem;
}

.skill-category h3 {
  color: #FFFF00;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  font-weight: 700;
}

.skill-items {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.skill {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.skill-name {
  color: #E0E0E0;
  font-size: 0.95rem;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.skill-pct {
  color: #FFFF00;
  font-weight: 700;
  font-size: 0.85rem;
}

.skill-bar {
  height: 6px;
  background: #1a1a1a;
  border-radius: 3px;
  overflow: hidden;
  border: 1px solid #333333;
}

.skill-fill {
  height: 100%;
  background: linear-gradient(90deg, #FFFF00, #DDDD00);
  border-radius: 3px;
  animation: fillBar 1.5s ease-out forwards;
}

@keyframes fillBar {
  from {
    width: 0;
  }
}
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.metric {
  background: #1a1a1a;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  border: 1px solid #333333;
  transition: all 0.3s ease;
}
.metric:hover {
  background: #262626;
  border-color: #FFFF00;
  transform: scale(1.05);
}
.metric .metric-value {
  color: #FFFF00;
  font-size: 2.5rem;
  font-weight: 900;
  margin-bottom: 0.5rem;
}
.metric .metric-label {
  color: #E0E0E0;
  font-size: 0.9rem;
  font-weight: 600;
  line-height: 1.4;
}
.metric .metric-context {
  color: #999999;
  font-size: 0.78rem;
  margin-top: 0.35rem;
  line-height: 1.4;
}

.exploring {
  padding: 6rem 2rem;
}

.exploring-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 3rem;
}

.exploring-card {
  background: #1a1a1a;
  border: 1px solid #333333;
  border-radius: 10px;
  padding: 1.75rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.exploring-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #FFFF00, transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}
.exploring-card:hover {
  background: #262626;
  border-color: #FFFF00;
  transform: translateY(-4px);
}
.exploring-card:hover::before {
  opacity: 1;
}
.exploring-card h3 {
  color: #FFFFFF;
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0.6rem 0 0.75rem;
}
.exploring-card p {
  color: #E0E0E0;
  font-size: 0.9rem;
  line-height: 1.65;
}

.exploring-card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.exploring-domain {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: #FFFF00;
  background: rgba(255, 255, 0, 0.08);
  border: 1px solid rgba(255, 255, 0, 0.2);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.exploring-status {
  font-size: 0.72rem;
  color: #4ade80;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}
.exploring-status i {
  font-size: 0.55rem;
  animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.3;
  }
}
.contact {
  text-align: center;
}
.contact .contact-intro {
  color: #E0E0E0;
  font-size: 1.1rem;
  max-width: 600px;
  margin: 1rem auto 3rem;
  font-weight: 400;
}

.contact-email-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: #FFFF00;
  color: #000000;
  font-size: 1rem;
  font-weight: 700;
  padding: 0.9rem 2rem;
  border-radius: 8px;
  text-decoration: none;
  margin: 1.5rem auto 2.5rem;
  transition: all 0.25s ease;
  letter-spacing: 0.01em;
}
.contact-email-btn i {
  font-size: 1rem;
}
.contact-email-btn:hover {
  background: #DDDD00;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 255, 0, 0.2);
}

.contact-info {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  flex-wrap: wrap;
}

.contact-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #999999;
  font-weight: 500;
  font-size: 0.9rem;
  padding: 0.55rem 1.1rem;
  border: 1px solid #333333;
  border-radius: 6px;
  transition: all 0.25s ease;
}
.contact-link i {
  font-size: 0.9rem;
}
.contact-link:hover {
  color: #FFFF00;
  border-color: #FFFF00;
  background: rgba(255, 255, 0, 0.05);
}

.footer {
  display: none;
}

@media (max-width: 768px) {
  .header {
    padding: 0 1rem;
    height: 70px;
  }

  .header-nav {
    gap: 1.5rem;
  }

  .nav-link {
    font-size: 0.85rem;
  }

  .hero {
    padding-top: 100px;
    min-height: auto;
  }

  .hero-title {
    font-size: clamp(2.5rem, 10vw, 5rem);
  }

  .hero-tagline {
    font-size: 1rem;
  }

  .about-grid {
    grid-template-columns: 1fr;
  }

  .beyond-grid {
    grid-template-columns: 1fr 1fr;
  }

  section {
    padding: 4rem 1.5rem;
  }
}
@media (max-width: 480px) {
  .header {
    height: 60px;
    padding: 0 0.5rem;
  }

  .header-nav {
    gap: 1rem;
    flex-wrap: wrap;
  }

  .nav-link {
    font-size: 0.75rem;
  }

  .hero-title {
    font-size: clamp(2rem, 8vw, 4rem);
  }

  .hero-tagline {
    font-size: 0.9rem;
  }

  .hero-title-wrapper {
    min-height: 300px;
  }
}
.chat-bubble {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 9000;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 18px;
  border: 2px solid #FFFF00;
  border-radius: 50px;
  background: #000000;
  color: #FFFF00;
  font-family: "Inter", sans-serif;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(255, 255, 0, 0.25);
  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.15s;
}
.chat-bubble:hover {
  background: #FFFF00;
  color: #000000;
  box-shadow: 0 6px 28px rgba(255, 255, 0, 0.4);
  transform: translateY(-2px);
}
.chat-bubble__icon {
  font-size: 1rem;
}
.chat-bubble__label {
  line-height: 1;
}
.chat-bubble::after {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 50px;
  border: 2px solid rgba(255, 255, 0, 0.35);
  animation: chat-pulse 2.4s ease-out infinite;
  pointer-events: none;
}
.chat-bubble.chat-bubble--open::after {
  display: none;
}

@keyframes chat-pulse {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  70% {
    opacity: 0;
    transform: scale(1.18);
  }
  100% {
    opacity: 0;
    transform: scale(1.18);
  }
}
.chat-window {
  position: fixed;
  bottom: 90px;
  right: 28px;
  z-index: 8999;
  width: 360px;
  max-height: 520px;
  display: flex;
  flex-direction: column;
  border: 1px solid #FFFF00;
  border-radius: 16px;
  background: #1a1a1a;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 0, 0.12);
  overflow: hidden;
  opacity: 0;
  transform: translateY(16px) scale(0.96);
  pointer-events: none;
  transition: opacity 0.22s ease, transform 0.22s ease;
}
.chat-window.chat-window--visible {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: all;
}
.chat-window__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 16px;
  background: #262626;
  border-bottom: 1px solid #333333;
}
.chat-window__header-info {
  display: flex;
  align-items: center;
  gap: 10px;
}
.chat-window__avatar {
  font-size: 1.4rem;
  line-height: 1;
}
.chat-window__name {
  font-family: "Inter", sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0;
}
.chat-window__status {
  font-family: "Inter", sans-serif;
  font-size: 0.7rem;
  color: #999999;
  margin: 0;
}
.chat-window__close {
  background: none;
  border: none;
  color: #999999;
  font-size: 1rem;
  cursor: pointer;
  padding: 4px;
  border-radius: 6px;
  transition: color 0.15s, background 0.15s;
}
.chat-window__close:hover {
  color: #FFFF00;
  background: rgba(255, 255, 0, 0.08);
}
.chat-window__messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scrollbar-width: thin;
  scrollbar-color: #333333 transparent;
}
.chat-window__messages::-webkit-scrollbar {
  width: 4px;
}
.chat-window__messages::-webkit-scrollbar-thumb {
  background: #333333;
  border-radius: 4px;
}
.chat-window__input-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 14px;
  border-top: 1px solid #333333;
  background: #262626;
}
.chat-window__input {
  flex: 1;
  background: #000000;
  border: 1px solid #333333;
  border-radius: 8px;
  padding: 9px 12px;
  color: #FFFFFF;
  font-family: "Inter", sans-serif;
  font-size: 0.82rem;
  outline: none;
  transition: border-color 0.15s;
}
.chat-window__input::-moz-placeholder {
  color: #999999;
}
.chat-window__input::placeholder {
  color: #999999;
}
.chat-window__input:focus {
  border-color: #FFFF00;
}
.chat-window__send {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  border: none;
  background: #FFFF00;
  color: #000000;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
  display: flex;
  align-items: center;
  justify-content: center;
}
.chat-window__send:hover {
  background: #DDDD00;
  transform: scale(1.06);
}
.chat-window__send:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  transform: none;
}

.chat-msg {
  max-width: 86%;
  font-family: "Inter", sans-serif;
  font-size: 0.82rem;
  line-height: 1.55;
  border-radius: 12px;
  padding: 10px 13px;
}
.chat-msg p {
  margin: 0;
}
.chat-msg--bot {
  align-self: flex-start;
  background: #262626;
  color: #E0E0E0;
  border-bottom-left-radius: 4px;
}
.chat-msg--user {
  align-self: flex-end;
  background: #FFFF00;
  color: #000000;
  font-weight: 600;
  border-bottom-right-radius: 4px;
}
.chat-msg--typing {
  align-self: flex-start;
  background: #262626;
  padding: 12px 16px;
}
.chat-msg--typing span {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #999999;
  margin: 0 2px;
  animation: typing-dot 1.2s infinite;
}
.chat-msg--typing span:nth-child(2) {
  animation-delay: 0.2s;
}
.chat-msg--typing span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing-dot {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.4;
  }
  30% {
    transform: translateY(-5px);
    opacity: 1;
  }
}
@media (max-width: 480px) {
  .chat-window {
    right: 12px;
    bottom: 84px;
    width: calc(100vw - 24px);
    max-height: 60vh;
  }

  .chat-bubble {
    right: 12px;
    bottom: 20px;
  }
}`, "",{"version":3,"sources":["webpack://./css/styles.scss"],"names":[],"mappings":"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","sourcesContent":["// ===== HIGH CONTRAST BLACK + NEON YELLOW THEME =====\n\n// ===== VARIABLES =====\n$bg-primary: #000000;\n$bg-secondary: #1a1a1a;\n$bg-tertiary: #262626;\n$accent: #FFFF00;\n$accent-dark: #DDDD00;\n$text-primary: #FFFFFF;\n$text-secondary: #E0E0E0;\n$text-tertiary: #999999;\n$border-color: #333333;\n\n// ===== RESET & BASE =====\n* {\n  margin: 0;\n  padding: 0;\n  box-sizing: border-box;\n}\n\nhtml {\n  scroll-behavior: smooth;\n}\n\nbody {\n  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;\n  background: $bg-primary;\n  color: $text-primary;\n  line-height: 1.6;\n  font-weight: 400;\n  cursor: none;\n}\n\na {\n  color: inherit;\n  text-decoration: none;\n  transition: color 0.2s ease;\n}\n\nimg {\n  max-width: 100%;\n  height: auto;\n  display: block;\n}\n\n.container {\n  max-width: 1200px;\n  margin: 0 auto;\n  padding: 0 2rem;\n}\n\n// ===== CUSTOM CURSOR =====\n.custom-cursor {\n  position: fixed;\n  width: 20px;\n  height: 20px;\n  border: 2px solid $accent;\n  border-radius: 50%;\n  pointer-events: none;\n  z-index: 9999;\n  transform: translate(-50%, -50%);\n  box-shadow: 0 0 10px rgba(255, 255, 0, 0.3);\n  transition: all 0.05s ease-out;\n}\n\n// ===== SIDEBAR NAVIGATION (HIDDEN) =====\n.sidebar-nav {\n  display: none;\n}\n\n.sidebar-close {\n  display: none;\n}\n\n.sidebar-menu {\n  display: none;\n}\n\n.nav-item {\n  display: none;\n}\n\n// ===== HEADER =====\n.header {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 80px;\n  background: rgba(0, 0, 0, 0.95);\n  backdrop-filter: blur(10px);\n  border-bottom: 1px solid $border-color;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  padding: 0 2rem;\n  z-index: 1000;\n}\n\n.header-nav {\n  display: flex;\n  gap: 3rem;\n  align-items: center;\n}\n\n.nav-link {\n  color: $text-secondary;\n  font-weight: 500;\n  font-size: 0.95rem;\n  letter-spacing: 0.5px;\n  text-transform: capitalize;\n  transition: all 0.3s ease;\n  position: relative;\n\n  &:hover {\n    color: $accent;\n  }\n\n  &::after {\n    content: '';\n    position: absolute;\n    bottom: -5px;\n    left: 0;\n    width: 0;\n    height: 2px;\n    background: $accent;\n    transition: width 0.3s ease;\n  }\n\n  &:hover::after {\n    width: 100%;\n  }\n}\n\n.menu-burger {\n  display: none;\n}\n\n.header-logo {\n  display: none;\n}\n\n.header-actions {\n  display: none;\n}\n\n.theme-toggle {\n  display: none;\n}\n\n.remix-btn {\n  display: none;\n}\n\n// ===== HERO SECTION =====\n.hero {\n  padding-top: 120px;\n  min-height: 100vh;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  background: $bg-primary;\n  position: relative;\n}\n\n.hero-content {\n  text-align: center;\n  max-width: 1000px;\n  width: 100%;\n  padding: 0 2rem;\n}\n\n.hero-title {\n  font-family: 'Playfair Display', serif;\n  font-size: clamp(4rem, 20vw, 10rem);\n  font-weight: 900;\n  color: $text-primary;\n  line-height: 1.1;\n  letter-spacing: -2px;\n  margin: 0 0 1.5rem 0;\n  text-transform: capitalize;\n}\n\n.hero-tagline {\n  color: $text-secondary;\n  font-size: clamp(1rem, 3vw, 1.3rem);\n  font-weight: 400;\n  letter-spacing: 0.5px;\n  margin: 0;\n  line-height: 1.6;\n}\n\n// ===== SECTIONS =====\nsection {\n  padding: 6rem 2rem;\n  border-bottom: 1px solid $border-color;\n\n  &:last-of-type {\n    border-bottom: none;\n  }\n}\n\n.section-title {\n  font-family: 'Playfair Display', serif;\n  font-size: clamp(2rem, 5vw, 3rem);\n  font-weight: 900;\n  color: $accent;\n  text-transform: uppercase;\n  margin-bottom: 3rem;\n  letter-spacing: -0.5px;\n}\n\n.section-intro {\n  color: $text-secondary;\n  font-size: 1.05rem;\n  max-width: 700px;\n  margin-bottom: 3rem;\n}\n\n// ===== SKILLS EVOLUTION TIMELINE =====\n.skills-evolution-timeline {\n  position: relative;\n  padding: 3rem 0;\n  max-width: 900px;\n  margin: 0 auto;\n}\n\n.timeline-line {\n  position: absolute;\n  left: 50%;\n  top: 0;\n  bottom: 0;\n  width: 2px;\n  background: linear-gradient(to bottom, $accent, $accent-dark, transparent);\n  transform: translateX(-50%);\n\n  @media (max-width: 768px) {\n    left: 30px;\n  }\n}\n\n.timeline-item {\n  margin-bottom: 1.5rem;\n  display: flex;\n  position: relative;\n  opacity: 0.8;\n  transition: all 0.4s ease;\n\n  &:hover {\n    opacity: 1;\n    transform: scale(1.02);\n  }\n\n  &:nth-child(odd) {\n    flex-direction: row;\n  }\n\n  &:nth-child(even) {\n    flex-direction: row-reverse;\n  }\n\n  @media (max-width: 768px) {\n    flex-direction: row !important;\n    margin-left: 0;\n  }\n}\n\n.timeline-dot {\n  position: absolute;\n  left: 50%;\n  top: 30px;\n  width: 16px;\n  height: 16px;\n  background: $accent;\n  border: 3px solid $bg-primary;\n  border-radius: 50%;\n  transform: translateX(-50%);\n  box-shadow: 0 0 20px rgba(255, 255, 0, 0.5);\n  z-index: 10;\n  flex-shrink: 0;\n\n  @media (max-width: 768px) {\n    left: 30px;\n    top: 30px;\n  }\n}\n\n.timeline-content {\n  width: 45%;\n  padding: 1.5rem;\n  background: $bg-tertiary;\n  border: 1px solid $border-color;\n  border-radius: 12px;\n  transition: all 0.3s ease;\n  position: relative;\n  perspective: 1000px;\n  min-height: 400px;\n\n  &:hover {\n    border-color: $accent;\n    box-shadow: 0 0 30px rgba(255, 255, 0, 0.1);\n    background: rgba(38, 38, 38, 0.8);\n  }\n\n  @media (max-width: 768px) {\n    width: calc(100% - 80px);\n    margin-left: 70px;\n    padding: 2rem;\n    min-height: 350px;\n  }\n}\n\n.flip-card {\n  width: 100%;\n  height: 100%;\n}\n\n.flip-card-inner {\n  position: relative;\n  width: 100%;\n  height: 100%;\n  transition: transform 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);\n  transform-style: preserve-3d;\n}\n\n.timeline-content:hover .flip-card-inner,\n.timeline-content.flipped .flip-card-inner {\n  transform: rotateY(180deg);\n}\n\n@media (max-width: 768px) {\n  .timeline-content:hover .flip-card-inner {\n    transform: rotateY(0deg);\n  }\n}\n\n.flip-card-front,\n.flip-card-back {\n  position: absolute;\n  width: 100%;\n  height: 100%;\n  backface-visibility: hidden;\n  display: flex;\n  flex-direction: column;\n  justify-content: flex-start;\n  box-sizing: border-box;\n  overflow: hidden;\n}\n\n.flip-card-front {\n  transform: rotateY(0deg);\n  padding: 0.6rem;\n}\n\n.flip-card-back {\n  transform: rotateY(180deg);\n  background: transparent;\n  padding: 0.8rem;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.description-list {\n  list-style: none;\n  margin: 0;\n  padding: 0;\n  display: flex;\n  flex-direction: column;\n  gap: 0.4rem;\n  width: 100%;\n\n  li {\n    color: $text-secondary;\n    font-size: 0.85rem;\n    line-height: 1.35;\n    padding: 0.35rem 0 0.35rem 1.8rem;\n    position: relative;\n    font-weight: 500;\n    transition: all 0.2s ease;\n\n    &::before {\n      content: \"▸\";\n      position: absolute;\n      left: 0.3rem;\n      color: $accent;\n      font-weight: 900;\n      font-size: 0.9rem;\n    }\n\n    &:hover {\n      color: $accent;\n      padding-left: 2rem;\n    }\n  }\n}\n\n.timeline-item:nth-child(odd) .timeline-content {\n  margin-right: auto;\n  margin-left: 0;\n\n  @media (max-width: 768px) {\n    margin-left: 70px;\n    margin-right: 0;\n  }\n}\n\n.timeline-item:nth-child(even) .timeline-content {\n  margin-left: auto;\n  margin-right: 0;\n\n  @media (max-width: 768px) {\n    margin-left: 70px;\n    margin-right: 0;\n  }\n}\n\n.timeline-year {\n  display: inline-block;\n  font-size: 0.85rem;\n  font-weight: 700;\n  color: $accent;\n  background: rgba(255, 255, 0, 0.1);\n  padding: 0.4rem 0.8rem;\n  border-radius: 20px;\n  margin-bottom: 0.2rem;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n}\n\n.timeline-title {\n  font-size: 1.4rem;\n  font-weight: 700;\n  color: $text-primary;\n  margin: 0.1rem 0 0.1rem 0;\n  font-family: 'Playfair Display', serif;\n}\n\n.timeline-subtitle {\n  font-size: 0.95rem;\n  color: $accent;\n  font-weight: 600;\n  margin-bottom: 0.3rem;\n  text-transform: uppercase;\n  letter-spacing: 0.5px;\n}\n\n.timeline-description {\n  font-size: 0.95rem;\n  color: $text-secondary;\n  line-height: 1.7;\n  margin-top: 1rem;\n}\n\n.skills-box {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 0.3rem;\n  margin: 0.3rem 0;\n  align-items: center;\n}\n\n.skill-chip {\n  display: inline-block;\n  padding: 0.4rem 0.8rem;\n  background: rgba(255, 255, 0, 0.08);\n  border: 1px solid rgba(255, 255, 0, 0.3);\n  border-radius: 20px;\n  font-size: 0.75rem;\n  color: $accent;\n  font-weight: 500;\n  transition: all 0.3s ease;\n  white-space: nowrap;\n\n  &:hover {\n    background: rgba(255, 255, 0, 0.15);\n    border-color: $accent;\n    box-shadow: 0 0 10px rgba(255, 255, 0, 0.2);\n  }\n}\n\n// ===== ABOUT SECTION =====\n.about-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));\n  gap: 2rem;\n  margin-top: 4rem;\n}\n\n@keyframes cardFadeUp {\n  from {\n    opacity: 0;\n    transform: translateY(30px);\n  }\n  to {\n    opacity: 1;\n    transform: translateY(0);\n  }\n}\n\n@keyframes factSlideIn {\n  from {\n    opacity: 0;\n    transform: translateX(-16px);\n  }\n  to {\n    opacity: 1;\n    transform: translateX(0);\n  }\n}\n\n.about-card {\n  background: $bg-secondary;\n  padding: 2rem;\n  border-radius: 12px;\n  border: 1px solid $border-color;\n  border-top: 3px solid $accent;\n  position: relative;\n  overflow: hidden;\n  opacity: 0;\n  transform: translateY(30px);\n  transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;\n\n  &::before {\n    content: '';\n    position: absolute;\n    top: 0; left: 0; right: 0; bottom: 0;\n    background: radial-gradient(ellipse at top left, rgba(255,255,0,0.04) 0%, transparent 60%);\n    pointer-events: none;\n  }\n\n  &.scrolled {\n    animation: cardFadeUp 0.6s ease forwards;\n\n    .fact-item {\n      animation: factSlideIn 0.4s ease forwards;\n      @for $i from 1 through 4 {\n        &:nth-child(#{$i}) {\n          animation-delay: #{0.1 + $i * 0.08}s;\n        }\n      }\n    }\n\n    .beyond-stat {\n      animation: factSlideIn 0.4s ease forwards;\n      @for $i from 1 through 4 {\n        &:nth-child(#{$i}) {\n          animation-delay: #{0.1 + $i * 0.08}s;\n        }\n      }\n    }\n  }\n\n  &:hover {\n    border-color: $accent;\n    box-shadow: 0 8px 32px rgba(255, 255, 0, 0.08);\n    transform: translateY(-4px);\n  }\n}\n\n.about-card-header {\n  display: flex;\n  align-items: center;\n  gap: 0.6rem;\n  margin-bottom: 0.75rem;\n\n  .about-card-fa-icon {\n    font-size: 1.1rem;\n    color: $accent;\n    width: 1.2rem;\n    text-align: center;\n  }\n\n  h3 {\n    color: $accent;\n    font-size: 1.3rem;\n    font-weight: 700;\n    margin: 0;\n  }\n}\n\n.about-intro {\n  color: $text-tertiary;\n  font-size: 0.88rem;\n  font-style: italic;\n  margin-bottom: 1.5rem;\n  line-height: 1.6;\n  border-left: 2px solid $accent;\n  padding-left: 0.75rem;\n}\n\n.facts-list {\n  list-style: none;\n  display: flex;\n  flex-direction: column;\n  gap: 0.65rem;\n}\n\n.fact-item {\n  display: flex;\n  align-items: flex-start;\n  gap: 0.75rem;\n  color: $text-secondary;\n  font-size: 0.95rem;\n  line-height: 1.6;\n  opacity: 0;\n  padding: 0.5rem 0.75rem;\n  border-radius: 6px;\n  transition: background 0.2s ease;\n\n  &:hover {\n    background: $bg-tertiary;\n  }\n\n  .fact-fa-icon {\n    font-size: 0.85rem;\n    color: $accent;\n    flex-shrink: 0;\n    margin-top: 4px;\n    width: 1rem;\n    text-align: center;\n  }\n\n  strong {\n    color: $accent;\n  }\n}\n\n// Stack domains — grouped tech\n.stack-domains {\n  margin-top: 1.25rem;\n  padding-top: 1.1rem;\n  border-top: 1px solid $border-color;\n  display: flex;\n  flex-direction: column;\n  gap: 0.5rem;\n}\n\n.stack-domain {\n  display: flex;\n  align-items: center;\n  gap: 0.6rem;\n}\n\n.stack-domain-label {\n  font-size: 0.7rem;\n  font-weight: 700;\n  color: $text-tertiary;\n  text-transform: uppercase;\n  letter-spacing: 0.08em;\n  width: 2.8rem;\n  flex-shrink: 0;\n}\n\n// Stack row — core tech chips\n.stack-row {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 0.4rem;\n}\n\n.stack-chip {\n  font-size: 0.75rem;\n  font-weight: 600;\n  color: $accent;\n  background: rgba(255, 255, 0, 0.07);\n  border: 1px solid rgba(255, 255, 0, 0.25);\n  border-radius: 4px;\n  padding: 0.2rem 0.6rem;\n  letter-spacing: 0.02em;\n  transition: background 0.2s ease, border-color 0.2s ease;\n\n  &:hover {\n    background: rgba(255, 255, 0, 0.14);\n    border-color: $accent;\n  }\n}\n\n// Beyond Code grid\n.beyond-grid {\n  display: grid;\n  grid-template-columns: 1fr 1fr;\n  gap: 0.85rem;\n}\n\n.beyond-stat {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  text-align: center;\n  background: $bg-tertiary;\n  border: 1px solid $border-color;\n  border-radius: 10px;\n  padding: 1.1rem 0.75rem;\n  opacity: 0;\n  transition: all 0.25s ease;\n  cursor: default;\n\n  &:hover {\n    border-color: $accent;\n    background: #2a2a00;\n    transform: scale(1.03);\n  }\n\n  .beyond-fa-icon {\n    font-size: 1.4rem;\n    color: $text-tertiary;\n    margin-bottom: 0.4rem;\n    transition: color 0.2s ease;\n  }\n\n  &:hover .beyond-fa-icon {\n    color: $accent;\n  }\n\n  .beyond-number {\n    color: $accent;\n    font-size: 1.5rem;\n    font-weight: 800;\n    line-height: 1.2;\n\n    &--text {\n      font-size: 1.2rem;\n    }\n  }\n\n  .beyond-label {\n    color: $text-tertiary;\n    font-size: 0.78rem;\n    margin-top: 0.2rem;\n    line-height: 1.4;\n  }\n\n  &--highlight {\n    border-color: rgba(255, 255, 0, 0.2);\n    background: linear-gradient(135deg, $bg-tertiary 0%, #1e1e00 100%);\n\n    .beyond-fa-icon {\n      color: $accent;\n    }\n\n    .beyond-label {\n      color: $text-secondary;\n      font-style: italic;\n    }\n  }\n}\n\n// ===== PROJECTS SECTION =====\n.projects-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));\n  gap: 2rem;\n  margin-top: 3rem;\n}\n\n.project-card {\n  background: $bg-secondary;\n  padding: 2rem;\n  border-radius: 8px;\n  border: 1px solid $border-color;\n  display: flex;\n  flex-direction: column;\n  transition: all 0.3s ease;\n\n  &:hover {\n    background: $bg-tertiary;\n    border-color: $accent;\n    transform: translateY(-4px);\n  }\n\n  &.featured {\n    grid-column: span 2;\n\n    @media (max-width: 768px) {\n      grid-column: span 1;\n    }\n  }\n\n  .project-tag {\n    display: inline-block;\n    background: $accent;\n    color: $bg-primary;\n    padding: 0.3rem 0.8rem;\n    border-radius: 12px;\n    font-size: 0.72rem;\n    font-weight: 700;\n    text-transform: uppercase;\n    letter-spacing: 0.04em;\n    margin-bottom: 1rem;\n    align-self: flex-start;\n  }\n\n  h3 {\n    color: $text-primary;\n    font-size: 1.1rem;\n    margin-bottom: 0.75rem;\n    font-weight: 700;\n    line-height: 1.35;\n  }\n\n  p {\n    color: $text-secondary;\n    font-size: 0.92rem;\n    line-height: 1.65;\n    flex-grow: 1;\n  }\n}\n\n.project-link {\n  display: inline-block;\n  margin-top: 1.25rem;\n  color: $accent;\n  font-size: 0.82rem;\n  font-weight: 600;\n  text-decoration: none;\n  letter-spacing: 0.02em;\n  border-bottom: 1px solid rgba(255, 255, 0, 0.35);\n  padding-bottom: 2px;\n  transition: border-color 0.2s ease, opacity 0.2s ease;\n  align-self: flex-start;\n\n  &:hover {\n    border-color: $accent;\n    opacity: 0.8;\n  }\n}\n\n.project-tech {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 0.6rem;\n\n  span {\n    background: rgba(255, 255, 0, 0.1);\n    color: $accent;\n    padding: 0.4rem 0.8rem;\n    border-radius: 6px;\n    font-size: 0.8rem;\n    border: 1px solid rgba(255, 255, 0, 0.3);\n  }\n}\n\n// Shared bullet list used in exp / leadership / projects\n.bullet-list {\n  list-style: none;\n  padding: 0;\n  margin: 0.85rem 0 0;\n  display: flex;\n  flex-direction: column;\n  gap: 0.45rem;\n\n  li {\n    color: $text-secondary;\n    font-size: 0.92rem;\n    line-height: 1.6;\n    padding-left: 1.1rem;\n    position: relative;\n\n    &::before {\n      content: '';\n      position: absolute;\n      left: 0;\n      top: 0.58em;\n      width: 5px;\n      height: 5px;\n      background: $accent;\n      border-radius: 50%;\n      flex-shrink: 0;\n    }\n\n    strong {\n      color: $accent;\n    }\n  }\n}\n\n// ===== EXPERIENCE SECTION =====\n.exp-timeline {\n  margin-top: 3rem;\n}\n\n.exp-item {\n  background: $bg-secondary;\n  padding: 2rem;\n  margin-bottom: 1.5rem;\n  border-radius: 8px;\n  border-left: 4px solid $accent;\n  transition: all 0.3s ease;\n\n  &:hover {\n    background: $bg-tertiary;\n    transform: translateX(4px);\n  }\n\n  h3 {\n    color: $text-primary;\n    font-size: 1.05rem;\n    margin-bottom: 0.25rem;\n    font-weight: 700;\n  }\n\n  .exp-role {\n    color: $text-tertiary;\n    font-size: 0.85rem;\n    font-weight: 500;\n  }\n\n  p {\n    color: $text-secondary;\n    font-size: 0.95rem;\n    margin: 0.8rem 0;\n    line-height: 1.6;\n  }\n}\n\n.exp-header {\n  display: flex;\n  justify-content: space-between;\n  align-items: flex-start;\n  gap: 1rem;\n  margin-bottom: 0.3rem;\n  flex-wrap: wrap;\n}\n\n.exp-date {\n  color: $text-tertiary;\n  font-size: 0.8rem;\n  white-space: nowrap;\n  padding-top: 0.2rem;\n  flex-shrink: 0;\n}\n\n.exp-tags {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 0.6rem;\n  margin-top: 1rem;\n\n  span {\n    background: rgba(255, 255, 0, 0.1);\n    color: $accent;\n    padding: 0.3rem 0.7rem;\n    border-radius: 4px;\n    font-size: 0.75rem;\n    border: 1px solid rgba(255, 255, 0, 0.3);\n  }\n}\n\n// ===== EDUCATION SECTION =====\n.edu-items {\n  display: grid;\n  gap: 2rem;\n  margin-top: 3rem;\n}\n\n.edu-item {\n  background: $bg-secondary;\n  padding: 2rem;\n  border-radius: 8px;\n  border: 1px solid $border-color;\n\n  h3 {\n    color: $accent;\n    font-size: 1.1rem;\n    margin-bottom: 0.3rem;\n    font-weight: 700;\n  }\n\n  .edu-school {\n    color: $text-tertiary;\n    font-size: 0.9rem;\n    display: block;\n    margin-bottom: 0.8rem;\n  }\n\n  p {\n    color: $text-secondary;\n    font-size: 0.95rem;\n    line-height: 1.6;\n  }\n}\n\n.edu-header {\n  display: flex;\n  justify-content: space-between;\n  align-items: flex-start;\n  gap: 1rem;\n  flex-wrap: wrap;\n  margin-bottom: 0.3rem;\n}\n\n.edu-date {\n  color: $text-tertiary;\n  font-size: 0.8rem;\n  white-space: nowrap;\n  padding-top: 0.2rem;\n  flex-shrink: 0;\n}\n\n// ===== LEADERSHIP SECTION =====\n.leadership {\n  padding: 6rem 2rem;\n}\n\n.leadership-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));\n  gap: 1.5rem;\n  margin-top: 3rem;\n}\n\n.leadership-card {\n  background: $bg-secondary;\n  padding: 1.75rem;\n  border-radius: 8px;\n  border: 1px solid $border-color;\n  border-top: 3px solid rgba(255, 255, 0, 0.35);\n  transition: all 0.3s ease;\n\n  &:hover {\n    border-top-color: $accent;\n    background: $bg-tertiary;\n    transform: translateY(-3px);\n  }\n\n  h3 {\n    color: $accent;\n    font-size: 1rem;\n    font-weight: 700;\n    margin-bottom: 0.2rem;\n  }\n\n  p {\n    color: $text-secondary;\n    font-size: 0.9rem;\n    line-height: 1.65;\n    margin-top: 0.75rem;\n  }\n}\n\n.leadership-card-header {\n  display: flex;\n  justify-content: space-between;\n  align-items: flex-start;\n  gap: 1rem;\n  flex-wrap: wrap;\n}\n\n.leadership-org {\n  color: $text-tertiary;\n  font-size: 0.82rem;\n  font-weight: 500;\n  display: block;\n}\n\n.leadership-date {\n  color: $text-tertiary;\n  font-size: 0.78rem;\n  white-space: nowrap;\n  flex-shrink: 0;\n  padding-top: 0.15rem;\n}\n\n// ===== SKILLS SECTION =====\n.skills-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));\n  gap: 3rem;\n  margin-top: 3rem;\n}\n\n.skill-category {\n  h3 {\n    color: $accent;\n    font-size: 1.2rem;\n    margin-bottom: 1.5rem;\n    font-weight: 700;\n  }\n}\n\n.skill-items {\n  display: flex;\n  flex-direction: column;\n  gap: 1.5rem;\n}\n\n.skill {\n  display: flex;\n  flex-direction: column;\n  gap: 0.5rem;\n}\n\n.skill-name {\n  color: $text-secondary;\n  font-size: 0.95rem;\n  font-weight: 500;\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n\n.skill-pct {\n  color: $accent;\n  font-weight: 700;\n  font-size: 0.85rem;\n}\n\n.skill-bar {\n  height: 6px;\n  background: $bg-secondary;\n  border-radius: 3px;\n  overflow: hidden;\n  border: 1px solid $border-color;\n}\n\n.skill-fill {\n  height: 100%;\n  background: linear-gradient(90deg, $accent, $accent-dark);\n  border-radius: 3px;\n  animation: fillBar 1.5s ease-out forwards;\n}\n\n@keyframes fillBar {\n  from {\n    width: 0;\n  }\n}\n\n// ===== ACHIEVEMENTS SECTION =====\n.metrics-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n  gap: 2rem;\n  margin: 3rem 0;\n}\n\n.metric {\n  background: $bg-secondary;\n  padding: 2rem;\n  border-radius: 8px;\n  text-align: center;\n  border: 1px solid $border-color;\n  transition: all 0.3s ease;\n\n  &:hover {\n    background: $bg-tertiary;\n    border-color: $accent;\n    transform: scale(1.05);\n  }\n\n  .metric-value {\n    color: $accent;\n    font-size: 2.5rem;\n    font-weight: 900;\n    margin-bottom: 0.5rem;\n  }\n\n  .metric-label {\n    color: $text-secondary;\n    font-size: 0.9rem;\n    font-weight: 600;\n    line-height: 1.4;\n  }\n\n  .metric-context {\n    color: $text-tertiary;\n    font-size: 0.78rem;\n    margin-top: 0.35rem;\n    line-height: 1.4;\n  }\n}\n\n// ===== CURRENTLY EXPLORING SECTION =====\n.exploring {\n  padding: 6rem 2rem;\n}\n\n.exploring-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: 1.5rem;\n  margin-top: 3rem;\n}\n\n.exploring-card {\n  background: $bg-secondary;\n  border: 1px solid $border-color;\n  border-radius: 10px;\n  padding: 1.75rem;\n  transition: all 0.3s ease;\n  position: relative;\n  overflow: hidden;\n\n  &::before {\n    content: '';\n    position: absolute;\n    top: 0; left: 0; right: 0;\n    height: 2px;\n    background: linear-gradient(90deg, $accent, transparent);\n    opacity: 0;\n    transition: opacity 0.3s ease;\n  }\n\n  &:hover {\n    background: $bg-tertiary;\n    border-color: $accent;\n    transform: translateY(-4px);\n\n    &::before {\n      opacity: 1;\n    }\n  }\n\n  h3 {\n    color: $text-primary;\n    font-size: 1.15rem;\n    font-weight: 700;\n    margin: 0.6rem 0 0.75rem;\n  }\n\n  p {\n    color: $text-secondary;\n    font-size: 0.9rem;\n    line-height: 1.65;\n  }\n}\n\n.exploring-card-top {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n\n.exploring-domain {\n  font-size: 0.72rem;\n  font-weight: 700;\n  text-transform: uppercase;\n  letter-spacing: 0.07em;\n  color: $accent;\n  background: rgba(255, 255, 0, 0.08);\n  border: 1px solid rgba(255, 255, 0, 0.2);\n  padding: 0.2rem 0.6rem;\n  border-radius: 4px;\n}\n\n.exploring-status {\n  font-size: 0.72rem;\n  color: #4ade80;\n  display: flex;\n  align-items: center;\n  gap: 0.35rem;\n\n  i {\n    font-size: 0.55rem;\n    animation: pulse-dot 2s ease-in-out infinite;\n  }\n}\n\n@keyframes pulse-dot {\n  0%, 100% { opacity: 1; }\n  50% { opacity: 0.3; }\n}\n\n// ===== CONTACT SECTION =====\n.contact {\n  text-align: center;\n\n  .contact-intro {\n    color: $text-secondary;\n    font-size: 1.1rem;\n    max-width: 600px;\n    margin: 1rem auto 3rem;\n    font-weight: 400;\n  }\n}\n\n.contact-email-btn {\n  display: inline-flex;\n  align-items: center;\n  gap: 0.6rem;\n  background: $accent;\n  color: $bg-primary;\n  font-size: 1rem;\n  font-weight: 700;\n  padding: 0.9rem 2rem;\n  border-radius: 8px;\n  text-decoration: none;\n  margin: 1.5rem auto 2.5rem;\n  transition: all 0.25s ease;\n  letter-spacing: 0.01em;\n\n  i {\n    font-size: 1rem;\n  }\n\n  &:hover {\n    background: $accent-dark;\n    transform: translateY(-2px);\n    box-shadow: 0 6px 20px rgba(255, 255, 0, 0.2);\n  }\n}\n\n.contact-info {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  gap: 1.25rem;\n  flex-wrap: wrap;\n}\n\n.contact-link {\n  display: inline-flex;\n  align-items: center;\n  gap: 0.4rem;\n  color: $text-tertiary;\n  font-weight: 500;\n  font-size: 0.9rem;\n  padding: 0.55rem 1.1rem;\n  border: 1px solid $border-color;\n  border-radius: 6px;\n  transition: all 0.25s ease;\n\n  i {\n    font-size: 0.9rem;\n  }\n\n  &:hover {\n    color: $accent;\n    border-color: $accent;\n    background: rgba(255, 255, 0, 0.05);\n  }\n}\n\n// ===== FOOTER =====\n.footer {\n  display: none;\n}\n\n// ===== RESPONSIVE =====\n@media (max-width: 768px) {\n  .header {\n    padding: 0 1rem;\n    height: 70px;\n  }\n\n  .header-nav {\n    gap: 1.5rem;\n  }\n\n  .nav-link {\n    font-size: 0.85rem;\n  }\n\n  .hero {\n    padding-top: 100px;\n    min-height: auto;\n  }\n\n  .hero-title {\n    font-size: clamp(2.5rem, 10vw, 5rem);\n  }\n\n  .hero-tagline {\n    font-size: 1rem;\n  }\n\n  .about-grid {\n    grid-template-columns: 1fr;\n  }\n\n  .beyond-grid {\n    grid-template-columns: 1fr 1fr;\n  }\n\n  section {\n    padding: 4rem 1.5rem;\n  }\n}\n\n@media (max-width: 480px) {\n  .header {\n    height: 60px;\n    padding: 0 0.5rem;\n  }\n\n  .header-nav {\n    gap: 1rem;\n    flex-wrap: wrap;\n  }\n\n  .nav-link {\n    font-size: 0.75rem;\n  }\n\n  .hero-title {\n    font-size: clamp(2rem, 8vw, 4rem);\n  }\n\n  .hero-tagline {\n    font-size: 0.9rem;\n  }\n\n  .hero-title-wrapper {\n    min-height: 300px;\n  }\n}\n\n\n// ═══════════════════════════════════════════════════════════════════════════════\n// RAG CHATBOT — chat bubble + window\n// Uses existing palette variables — zero impact on the rest of the stylesheet.\n// ═══════════════════════════════════════════════════════════════════════════════\n\n// ── Chat bubble (trigger) ────────────────────────────────────────────────────\n.chat-bubble {\n  position: fixed;\n  bottom: 28px;\n  right: 28px;\n  z-index: 9000;\n\n  display: flex;\n  align-items: center;\n  gap: 8px;\n\n  padding: 12px 18px;\n  border: 2px solid $accent;\n  border-radius: 50px;\n  background: $bg-primary;\n  color: $accent;\n  font-family: 'Inter', sans-serif;\n  font-size: 0.85rem;\n  font-weight: 600;\n  letter-spacing: 0.03em;\n  cursor: pointer;\n  box-shadow: 0 4px 20px rgba(255, 255, 0, 0.25);\n  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.15s;\n\n  &:hover {\n    background: $accent;\n    color: $bg-primary;\n    box-shadow: 0 6px 28px rgba(255, 255, 0, 0.4);\n    transform: translateY(-2px);\n  }\n\n  &__icon { font-size: 1rem; }\n  &__label { line-height: 1; }\n\n  // Pulse ring when window is closed\n  &::after {\n    content: '';\n    position: absolute;\n    inset: -4px;\n    border-radius: 50px;\n    border: 2px solid rgba(255, 255, 0, 0.35);\n    animation: chat-pulse 2.4s ease-out infinite;\n    pointer-events: none;\n  }\n\n  &.chat-bubble--open::after { display: none; }\n}\n\n@keyframes chat-pulse {\n  0%   { opacity: 1; transform: scale(1); }\n  70%  { opacity: 0; transform: scale(1.18); }\n  100% { opacity: 0; transform: scale(1.18); }\n}\n\n// ── Chat window ──────────────────────────────────────────────────────────────\n.chat-window {\n  position: fixed;\n  bottom: 90px;\n  right: 28px;\n  z-index: 8999;\n  width: 360px;\n  max-height: 520px;\n\n  display: flex;\n  flex-direction: column;\n  border: 1px solid $accent;\n  border-radius: 16px;\n  background: $bg-secondary;\n  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 0, 0.12);\n  overflow: hidden;\n\n  // Hidden by default — toggled via JS\n  opacity: 0;\n  transform: translateY(16px) scale(0.96);\n  pointer-events: none;\n  transition: opacity 0.22s ease, transform 0.22s ease;\n\n  &.chat-window--visible {\n    opacity: 1;\n    transform: translateY(0) scale(1);\n    pointer-events: all;\n  }\n\n  // Header\n  &__header {\n    display: flex;\n    align-items: center;\n    justify-content: space-between;\n    padding: 14px 16px;\n    background: $bg-tertiary;\n    border-bottom: 1px solid $border-color;\n  }\n\n  &__header-info {\n    display: flex;\n    align-items: center;\n    gap: 10px;\n  }\n\n  &__avatar {\n    font-size: 1.4rem;\n    line-height: 1;\n  }\n\n  &__name {\n    font-family: 'Inter', sans-serif;\n    font-size: 0.85rem;\n    font-weight: 700;\n    color: $text-primary;\n    margin: 0;\n  }\n\n  &__status {\n    font-family: 'Inter', sans-serif;\n    font-size: 0.7rem;\n    color: $text-tertiary;\n    margin: 0;\n  }\n\n  &__close {\n    background: none;\n    border: none;\n    color: $text-tertiary;\n    font-size: 1rem;\n    cursor: pointer;\n    padding: 4px;\n    border-radius: 6px;\n    transition: color 0.15s, background 0.15s;\n\n    &:hover {\n      color: $accent;\n      background: rgba(255, 255, 0, 0.08);\n    }\n  }\n\n  // Message list\n  &__messages {\n    flex: 1;\n    overflow-y: auto;\n    padding: 16px;\n    display: flex;\n    flex-direction: column;\n    gap: 12px;\n    scrollbar-width: thin;\n    scrollbar-color: $border-color transparent;\n\n    &::-webkit-scrollbar { width: 4px; }\n    &::-webkit-scrollbar-thumb { background: $border-color; border-radius: 4px; }\n  }\n\n  // Input row\n  &__input-row {\n    display: flex;\n    align-items: center;\n    gap: 8px;\n    padding: 12px 14px;\n    border-top: 1px solid $border-color;\n    background: $bg-tertiary;\n  }\n\n  &__input {\n    flex: 1;\n    background: $bg-primary;\n    border: 1px solid $border-color;\n    border-radius: 8px;\n    padding: 9px 12px;\n    color: $text-primary;\n    font-family: 'Inter', sans-serif;\n    font-size: 0.82rem;\n    outline: none;\n    transition: border-color 0.15s;\n\n    &::placeholder { color: $text-tertiary; }\n\n    &:focus { border-color: $accent; }\n  }\n\n  &__send {\n    flex-shrink: 0;\n    width: 36px;\n    height: 36px;\n    border-radius: 8px;\n    border: none;\n    background: $accent;\n    color: $bg-primary;\n    font-size: 0.85rem;\n    cursor: pointer;\n    transition: background 0.15s, transform 0.1s;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n\n    &:hover { background: $accent-dark; transform: scale(1.06); }\n    &:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }\n  }\n}\n\n// ── Individual messages ───────────────────────────────────────────────────────\n.chat-msg {\n  max-width: 86%;\n  font-family: 'Inter', sans-serif;\n  font-size: 0.82rem;\n  line-height: 1.55;\n  border-radius: 12px;\n  padding: 10px 13px;\n\n  p { margin: 0; }\n\n  // Bot messages — left-aligned, dark bg\n  &--bot {\n    align-self: flex-start;\n    background: $bg-tertiary;\n    color: $text-secondary;\n    border-bottom-left-radius: 4px;\n  }\n\n  // User messages — right-aligned, yellow bg\n  &--user {\n    align-self: flex-end;\n    background: $accent;\n    color: $bg-primary;\n    font-weight: 600;\n    border-bottom-right-radius: 4px;\n  }\n\n  // Typing indicator (three dots)\n  &--typing {\n    align-self: flex-start;\n    background: $bg-tertiary;\n    padding: 12px 16px;\n\n    span {\n      display: inline-block;\n      width: 6px;\n      height: 6px;\n      border-radius: 50%;\n      background: $text-tertiary;\n      margin: 0 2px;\n      animation: typing-dot 1.2s infinite;\n\n      &:nth-child(2) { animation-delay: 0.2s; }\n      &:nth-child(3) { animation-delay: 0.4s; }\n    }\n  }\n}\n\n@keyframes typing-dot {\n  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }\n  30%            { transform: translateY(-5px); opacity: 1; }\n}\n\n// ── Mobile adjustments ────────────────────────────────────────────────────────\n@media (max-width: 480px) {\n  .chat-window {\n    right: 12px;\n    bottom: 84px;\n    width: calc(100vw - 24px);\n    max-height: 60vh;\n  }\n\n  .chat-bubble {\n    right: 12px;\n    bottom: 20px;\n  }\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "../node_modules/css-loader/dist/runtime/api.js":
/*!******************************************************!*\
  !*** ../node_modules/css-loader/dist/runtime/api.js ***!
  \******************************************************/
/***/ ((module) => {


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/

module.exports = function (cssWithMappingToString) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = "";
      var needLayer = typeof item[5] !== "undefined";

      if (item[4]) {
        content += "@supports (".concat(item[4], ") {");
      }

      if (item[2]) {
        content += "@media ".concat(item[2], " {");
      }

      if (needLayer) {
        content += "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {");
      }

      content += cssWithMappingToString(item);

      if (needLayer) {
        content += "}";
      }

      if (item[2]) {
        content += "}";
      }

      if (item[4]) {
        content += "}";
      }

      return content;
    }).join("");
  }; // import a list of modules into the list


  list.i = function i(modules, media, dedupe, supports, layer) {
    if (typeof modules === "string") {
      modules = [[null, modules, undefined]];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var k = 0; k < this.length; k++) {
        var id = this[k][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _k = 0; _k < modules.length; _k++) {
      var item = [].concat(modules[_k]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        continue;
      }

      if (typeof layer !== "undefined") {
        if (typeof item[5] === "undefined") {
          item[5] = layer;
        } else {
          item[1] = "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {").concat(item[1], "}");
          item[5] = layer;
        }
      }

      if (media) {
        if (!item[2]) {
          item[2] = media;
        } else {
          item[1] = "@media ".concat(item[2], " {").concat(item[1], "}");
          item[2] = media;
        }
      }

      if (supports) {
        if (!item[4]) {
          item[4] = "".concat(supports);
        } else {
          item[1] = "@supports (".concat(item[4], ") {").concat(item[1], "}");
          item[4] = supports;
        }
      }

      list.push(item);
    }
  };

  return list;
};

/***/ }),

/***/ "../node_modules/css-loader/dist/runtime/sourceMaps.js":
/*!*************************************************************!*\
  !*** ../node_modules/css-loader/dist/runtime/sourceMaps.js ***!
  \*************************************************************/
/***/ ((module) => {



module.exports = function (item) {
  var content = item[1];
  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (typeof btoa === "function") {
    var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(cssMapping))));
    var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
    var sourceMapping = "/*# ".concat(data, " */");
    return [content].concat([sourceMapping]).join("\n");
  }

  return [content].join("\n");
};

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!*****************************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \*****************************************************************************/
/***/ ((module) => {



var stylesInDOM = [];
function getIndexByIdentifier(identifier) {
  var result = -1;
  for (var i = 0; i < stylesInDOM.length; i++) {
    if (stylesInDOM[i].identifier === identifier) {
      result = i;
      break;
    }
  }
  return result;
}
function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];
  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var indexByIdentifier = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3],
      supports: item[4],
      layer: item[5]
    };
    if (indexByIdentifier !== -1) {
      stylesInDOM[indexByIdentifier].references++;
      stylesInDOM[indexByIdentifier].updater(obj);
    } else {
      var updater = addElementStyle(obj, options);
      options.byIndex = i;
      stylesInDOM.splice(i, 0, {
        identifier: identifier,
        updater: updater,
        references: 1
      });
    }
    identifiers.push(identifier);
  }
  return identifiers;
}
function addElementStyle(obj, options) {
  var api = options.domAPI(options);
  api.update(obj);
  var updater = function updater(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap && newObj.supports === obj.supports && newObj.layer === obj.layer) {
        return;
      }
      api.update(obj = newObj);
    } else {
      api.remove();
    }
  };
  return updater;
}
module.exports = function (list, options) {
  options = options || {};
  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];
    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDOM[index].references--;
    }
    var newLastIdentifiers = modulesToDom(newList, options);
    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];
      var _index = getIndexByIdentifier(_identifier);
      if (stylesInDOM[_index].references === 0) {
        stylesInDOM[_index].updater();
        stylesInDOM.splice(_index, 1);
      }
    }
    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/insertBySelector.js":
/*!*********************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/insertBySelector.js ***!
  \*********************************************************************/
/***/ ((module) => {



var memo = {};

/* istanbul ignore next  */
function getTarget(target) {
  if (typeof memo[target] === "undefined") {
    var styleTarget = document.querySelector(target);

    // Special case to return head of iframe instead of iframe itself
    if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
      try {
        // This will throw an exception if access to iframe is blocked
        // due to cross-origin restrictions
        styleTarget = styleTarget.contentDocument.head;
      } catch (e) {
        // istanbul ignore next
        styleTarget = null;
      }
    }
    memo[target] = styleTarget;
  }
  return memo[target];
}

/* istanbul ignore next  */
function insertBySelector(insert, style) {
  var target = getTarget(insert);
  if (!target) {
    throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
  }
  target.appendChild(style);
}
module.exports = insertBySelector;

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/insertStyleElement.js":
/*!***********************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/insertStyleElement.js ***!
  \***********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function insertStyleElement(options) {
  var element = document.createElement("style");
  options.setAttributes(element, options.attributes);
  options.insert(element, options.options);
  return element;
}
module.exports = insertStyleElement;

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js":
/*!***********************************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js ***!
  \***********************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {



/* istanbul ignore next  */
function setAttributesWithoutAttributes(styleElement) {
  var nonce =  true ? __webpack_require__.nc : 0;
  if (nonce) {
    styleElement.setAttribute("nonce", nonce);
  }
}
module.exports = setAttributesWithoutAttributes;

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/styleDomAPI.js":
/*!****************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/styleDomAPI.js ***!
  \****************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function apply(styleElement, options, obj) {
  var css = "";
  if (obj.supports) {
    css += "@supports (".concat(obj.supports, ") {");
  }
  if (obj.media) {
    css += "@media ".concat(obj.media, " {");
  }
  var needLayer = typeof obj.layer !== "undefined";
  if (needLayer) {
    css += "@layer".concat(obj.layer.length > 0 ? " ".concat(obj.layer) : "", " {");
  }
  css += obj.css;
  if (needLayer) {
    css += "}";
  }
  if (obj.media) {
    css += "}";
  }
  if (obj.supports) {
    css += "}";
  }
  var sourceMap = obj.sourceMap;
  if (sourceMap && typeof btoa !== "undefined") {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  }

  // For old IE
  /* istanbul ignore if  */
  options.styleTagTransform(css, styleElement, options.options);
}
function removeStyleElement(styleElement) {
  // istanbul ignore if
  if (styleElement.parentNode === null) {
    return false;
  }
  styleElement.parentNode.removeChild(styleElement);
}

/* istanbul ignore next  */
function domAPI(options) {
  if (typeof document === "undefined") {
    return {
      update: function update() {},
      remove: function remove() {}
    };
  }
  var styleElement = options.insertStyleElement(options);
  return {
    update: function update(obj) {
      apply(styleElement, options, obj);
    },
    remove: function remove() {
      removeStyleElement(styleElement);
    }
  };
}
module.exports = domAPI;

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/styleTagTransform.js":
/*!**********************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/styleTagTransform.js ***!
  \**********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function styleTagTransform(css, styleElement) {
  if (styleElement.styleSheet) {
    styleElement.styleSheet.cssText = css;
  } else {
    while (styleElement.firstChild) {
      styleElement.removeChild(styleElement.firstChild);
    }
    styleElement.appendChild(document.createTextNode(css));
  }
}
module.exports = styleTagTransform;

/***/ }),

/***/ "./css/styles.scss":
/*!*************************!*\
  !*** ./css/styles.scss ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/styleDomAPI.js */ "../node_modules/style-loader/dist/runtime/styleDomAPI.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/insertBySelector.js */ "../node_modules/style-loader/dist/runtime/insertBySelector.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js */ "../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/insertStyleElement.js */ "../node_modules/style-loader/dist/runtime/insertStyleElement.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! !../../node_modules/style-loader/dist/runtime/styleTagTransform.js */ "../node_modules/style-loader/dist/runtime/styleTagTransform.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_node_modules_postcss_loader_dist_cjs_js_node_modules_sass_loader_dist_cjs_js_styles_scss__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! !!../../node_modules/css-loader/dist/cjs.js!../../node_modules/postcss-loader/dist/cjs.js!../../node_modules/sass-loader/dist/cjs.js!./styles.scss */ "../node_modules/css-loader/dist/cjs.js!../node_modules/postcss-loader/dist/cjs.js!../node_modules/sass-loader/dist/cjs.js!./css/styles.scss");

      
      
      
      
      
      
      
      
      

var options = {};

options.styleTagTransform = (_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default());
options.setAttributes = (_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default());

      options.insert = _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default().bind(null, "head");
    
options.domAPI = (_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default());
options.insertStyleElement = (_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default());

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_node_modules_postcss_loader_dist_cjs_js_node_modules_sass_loader_dist_cjs_js_styles_scss__WEBPACK_IMPORTED_MODULE_6__["default"], options);




       /* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_node_modules_postcss_loader_dist_cjs_js_node_modules_sass_loader_dist_cjs_js_styles_scss__WEBPACK_IMPORTED_MODULE_6__["default"] && _node_modules_css_loader_dist_cjs_js_node_modules_postcss_loader_dist_cjs_js_node_modules_sass_loader_dist_cjs_js_styles_scss__WEBPACK_IMPORTED_MODULE_6__["default"].locals ? _node_modules_css_loader_dist_cjs_js_node_modules_postcss_loader_dist_cjs_js_node_modules_sass_loader_dist_cjs_js_styles_scss__WEBPACK_IMPORTED_MODULE_6__["default"].locals : undefined);


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			id: moduleId,
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/nonce */
/******/ 	(() => {
/******/ 		__webpack_require__.nc = undefined;
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry needs to be wrapped in an IIFE because it needs to be isolated against other modules in the chunk.
(() => {
/*!*********************!*\
  !*** ./js/index.js ***!
  \*********************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _css_styles_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../css/styles.scss */ "./css/styles.scss");
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }

function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }

// Import styles
 // ===== CUSTOM CURSOR ANIMATION =====

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
})();

/******/ })()
;
//# sourceMappingURL=bundle.js.map