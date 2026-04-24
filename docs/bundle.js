/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "../node_modules/css-loader/dist/cjs.js!../node_modules/postcss-loader/dist/cjs.js!../node_modules/sass-loader/dist/cjs.js!./css/styles.scss":
/*!***************************************************************************************************************************************************!*\
  !*** ../node_modules/css-loader/dist/cjs.js!../node_modules/postcss-loader/dist/cjs.js!../node_modules/sass-loader/dist/cjs.js!./css/styles.scss ***!
  \***************************************************************************************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/sourceMaps.js */ "../node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/api.js */ "../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/getUrl.js */ "../node_modules/css-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__);
// Imports



var ___CSS_LOADER_URL_IMPORT_0___ = new URL(/* asset import */ __webpack_require__(/*! ../assets/hero.jpg */ "./assets/hero.jpg"), __webpack_require__.b);
var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
var ___CSS_LOADER_URL_REPLACEMENT_0___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()(___CSS_LOADER_URL_IMPORT_0___);
// Module
___CSS_LOADER_EXPORT___.push([module.id, `* {
  box-sizing: border-box;
}

html, body {
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}

body {
  font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  color: #f8fafc;
  background: #0b1020;
}

img, video {
  max-width: 100%;
  display: block;
}

.container {
  width: min(1100px, 92vw);
  margin-inline: auto;
}

.stripe {
  padding: 6rem 0;
}

h1, h2, h3 {
  margin: 0 0 1rem;
}

p {
  color: #64748b;
  line-height: 1.7;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  backdrop-filter: saturate(110%) blur(6px);
}

.nav {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 1rem;
  padding: 1.2rem 1.2rem;
  transition: padding 0.25s ease;
  background: rgba(5, 9, 20, 0.75);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}
.nav .logo {
  font-weight: 800;
  color: #f8fafc;
  text-decoration: none;
  font-size: clamp(\$min, calc(1.2rem + 1vw), \$max);
}
.nav .nav-links {
  justify-self: end;
  display: flex;
  gap: 1.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav .nav-links a {
  color: #f8fafc;
  text-decoration: none;
  opacity: 0.8;
  transition: opacity 0.2s, transform 0.2s;
}
.nav .nav-links a.active {
  opacity: 1;
  border-bottom: 2px solid #2f6df6;
}
.nav .nav-links a:hover {
  opacity: 1;
  transform: translateY(-1px);
}
.nav.compact {
  padding: 0.5rem 1.2rem;
}

.reading-indicator {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, #2f6df6, #78a0f9);
  transition: width 0.1s linear;
}

.hero {
  min-height: 92vh;
  display: grid;
  place-items: center;
  text-align: center;
  background: radial-gradient(1200px 600px at 70% 20%, rgba(47, 109, 246, 0.15), transparent);
}
.hero.has-fixed-bg {
  background-image: url(${___CSS_LOADER_URL_REPLACEMENT_0___});
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
}
.hero .hero__content {
  background: rgba(0, 0, 0, 0.362);
  padding: 2rem;
  border: 1px solid rgba(255, 255, 255, 0);
  border-radius: 16px;
  animation: fadeInUp 0.7s ease both;
}
.hero .hero__title {
  font-size: clamp(\$min, calc(2rem + 1vw), \$max);
  font-weight: 800;
}
.hero .hero__subtitle {
  font-size: clamp(\$min, calc(1rem + 1vw), \$max);
  margin-bottom: 1.2rem;
  color: #d9d2d2;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.btn {
  display: inline-block;
  padding: 0.8rem 1.1rem;
  border-radius: 999px;
  background: #2f6df6;
  color: white;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(47, 109, 246, 0.3);
}

.btn-outline {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: center;
}

.portrait {
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.badges {
  display: grid;
  gap: 0.5rem;
  padding: 0;
  list-style: none;
}
.badges li {
  background: rgba(255, 255, 255, 0.05);
  padding: 0.6rem 0.8rem;
  border-radius: 10px;
}
.badges i {
  margin-right: 0.5rem;
  color: #2f6df6;
}

.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.2rem;
}

.card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  padding: 1.2rem;
  transition: transform 0.2s ease, border-color 0.2s;
}
.card:hover {
  transform: translateY(-3px);
  border-color: rgba(255, 255, 255, 0.16);
}

.link-as-btn {
  background: none;
  color: #2f6df6;
  border: 0;
  padding: 0.4rem 0;
  cursor: pointer;
}

.modal {
  position: fixed;
  inset: 0;
  display: none;
}

.modal[aria-hidden=false] {
  display: block;
}

.modal__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
}

.modal__dialog {
  position: absolute;
  inset: 0;
  margin: auto;
  width: min(680px, 92vw);
  background: #0d1328;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 1.2rem;
  top: 10%;
  animation: fadeInUp 0.25s ease both;
}

.modal__close {
  position: absolute;
  right: 0.8rem;
  top: 0.6rem;
  font-size: 1.6rem;
  background: none;
  color: #f8fafc;
  border: 0;
  cursor: pointer;
}

.carousel {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.caro-track {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 100%;
  transition: transform 0.35s ease;
}

.caro-slide {
  position: relative;
}

.caro-slide img {
  width: 100%;
  height: auto;
  display: block;
}

.caro-slide figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0.6rem 0.9rem;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
}

.caro-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.55);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #f8fafc;
  padding: 0.6rem 0.8rem;
  border-radius: 50%;
  cursor: pointer;
}

.caro-btn.prev {
  left: 0.6rem;
}

.caro-btn.next {
  right: 0.6rem;
}

.video video {
  width: 100%;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.center {
  text-align: center;
  display: grid;
  place-items: center;
  gap: 0.6rem;
}

.social {
  display: flex;
  gap: 1rem;
  font-size: 1.3rem;
}
.social a {
  color: #f8fafc;
  opacity: 0.8;
}
.social a:hover {
  opacity: 1;
}

.footer {
  padding: 2rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  color: #64748b;
}

@media (max-width: 1024px) {
  .cards {
    grid-template-columns: 1fr 1fr;
  }

  .columns {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 720px) {
  .cards {
    grid-template-columns: 1fr;
  }
}
.subhead {
  margin: 18px 0 10px;
  font-size: 1rem;
  opacity: 0.9;
  letter-spacing: 0.2px;
}

.section-divider {
  height: 1px;
  margin: 26px 0;
  background: rgba(255, 255, 255, 0.08);
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
  border: 2px solid #2f6df6;
  border-radius: 50px;
  background: #0b1020;
  color: #2f6df6;
  font-family: "Inter", sans-serif;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(255, 255, 0, 0.25);
  transition: background 0.2s, color 0.2s, transform 0.15s;
}
.chat-bubble:hover {
  background: #2f6df6;
  color: #0b1020;
  transform: translateY(-2px);
}
.chat-bubble__icon {
  font-size: 1rem;
}
.chat-bubble::after {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 50px;
  border: 2px solid rgba(255, 255, 0, 0.3);
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
  border: 1px solid #2f6df6;
  border-radius: 16px;
  background: #111827;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.7);
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
  background: #1e293b;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.chat-window__header-info {
  display: flex;
  align-items: center;
  gap: 10px;
}
.chat-window__avatar {
  font-size: 1.4rem;
}
.chat-window__name {
  font-family: "Inter", sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  color: #f8fafc;
  margin: 0;
}
.chat-window__status {
  font-family: "Inter", sans-serif;
  font-size: 0.7rem;
  color: #94a3b8;
  margin: 0;
}
.chat-window__close {
  background: none;
  border: none;
  color: #94a3b8;
  font-size: 1rem;
  cursor: pointer;
  padding: 4px;
  border-radius: 6px;
  transition: color 0.15s;
}
.chat-window__close:hover {
  color: #2f6df6;
}
.chat-window__messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.08) transparent;
}
.chat-window__input-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  background: #1e293b;
}
.chat-window__input {
  flex: 1;
  background: #0b1020;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 9px 12px;
  color: #f8fafc;
  font-family: "Inter", sans-serif;
  font-size: 0.82rem;
  outline: none;
}
.chat-window__input::-moz-placeholder {
  color: #94a3b8;
}
.chat-window__input::placeholder {
  color: #94a3b8;
}
.chat-window__input:focus {
  border-color: #2f6df6;
}
.chat-window__send {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  border: none;
  background: #2f6df6;
  color: #0b1020;
  font-size: 0.85rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, transform 0.1s;
}
.chat-window__send:hover {
  background: #1a4fc4;
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
  background: #1e293b;
  color: #cbd5e1;
  border-bottom-left-radius: 4px;
}
.chat-msg--user {
  align-self: flex-end;
  background: #2f6df6;
  color: #0b1020;
  font-weight: 600;
  border-bottom-right-radius: 4px;
}
.chat-msg--typing {
  align-self: flex-start;
  background: #1e293b;
  padding: 12px 16px;
}
.chat-msg--typing span {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #94a3b8;
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
}`, "",{"version":3,"sources":["webpack://./css/styles.scss"],"names":[],"mappings":"AA2BA;EAAI,sBAAA;AAzBJ;;AA0BA;EAAa,SAAA;EAAW,UAAA;EAAY,uBAAA;AApBpC;;AAqBA;EACE,4EAAA;EACA,cAjBM;EAkBN,mBAnBG;AACL;;AAqBA;EAAa,eAAA;EAAiB,cAAA;AAhB9B;;AAkBA;EAnBE,wBAAA;EACA,mBAAA;AAKF;;AAeA;EAAU,eAAA;AAXV;;AAYA;EAAa,gBAAA;AARb;;AASA;EAAI,cA7BI;EA6BW,gBAAA;AAJnB;;AAOA;EACE,gBAAA;EAAkB,MAAA;EAAQ,aAAA;EAC1B,yCAAA;AAFF;;AAKA;EACE,kBAAA;EACA,aAAA;EAAe,+BAAA;EAAiC,mBAAA;EAChD,SAAA;EAAW,sBAAA;EACX,8BAAA;EACA,gCAAA;EAAkC,kDAAA;AAEpC;AAAE;EAAQ,gBAAA;EAAkB,cA1CpB;EA0CmC,qBAAA;EAjCzC,gDAAA;AAuCF;AAJE;EACE,iBAAA;EAAmB,aAAA;EAAe,WAAA;EAAa,gBAAA;EAAkB,SAAA;EAAW,UAAA;AAWhF;AAVI;EAAI,cA9CA;EA8Ce,qBAAA;EAAuB,YAAA;EAAc,wCAAA;AAgB5D;AAfI;EAAW,UAAA;EAAY,gCAAA;AAmB3B;AAlBI;EAAU,UAAA;EAAY,2BAAA;AAsB1B;AAnBE;EAAY,sBAAA;AAsBd;;AAlBA;EACE,kBAAA;EAAoB,OAAA;EAAS,SAAA;EAC7B,WAAA;EAAa,SAAA;EACb,oDAAA;EACA,6BAAA;AAwBF;;AApBA;EACE,gBAAA;EACA,aAAA;EAAe,mBAAA;EACf,kBAAA;EACA,2FAAA;AAwBF;AAtBE;EACE,yDAAA;EACA,sBAAA;EACA,4BAAA;EACA,2BAAA;AAwBJ;AArBE;EACE,gCAAA;EACA,aAAA;EAAe,wCAAA;EAA0C,mBAAA;EACzD,kCAAA;AAyBJ;AAtBE;EAzEA,8CAAA;EAyEgD,gBAAA;AA0BlD;AAzBE;EA1EA,8CAAA;EA0EqD,qBAAA;EAAuB,cAAA;AA8B9E;;AA3BA;EACE;IAAO,UAAA;IAAY,2BAAA;EAgCnB;EA/BA;IAAO,UAAA;IAAY,wBAAA;EAmCnB;AACF;AAhCA;EACE,qBAAA;EACA,sBAAA;EAAuB,oBAAA;EACvB,mBA5GM;EA4Gc,YAAA;EAAc,qBAAA;EAAuB,YAAA;EAAc,eAAA;EACvE,qDAAA;AAuCF;AAtCE;EAAU,2BAAA;EAA6B,8CAAA;AA0CzC;;AAxCA;EACE,uBAAA;EAAyB,2CAAA;AA4C3B;;AAxCA;EAAW,aAAA;EAAe,8BAAA;EAAgC,SAAA;EAAW,mBAAA;AA+CrE;;AA9CA;EAAY,mBAAA;EAAqB,0CAAA;AAmDjC;;AAlDA;EAAU,aAAA;EAAe,WAAA;EAAY,UAAA;EAAY,gBAAA;AAyDjD;AAxDE;EAAK,qCAAA;EAAmC,sBAAA;EAAsB,mBAAA;AA6DhE;AA5DE;EAAI,oBAAA;EAAqB,cAzHnB;AAyLR;;AA5DA;EAAS,aAAA;EAAe,qCAAA;EAAuC,WAAA;AAkE/D;;AAjEA;EACE,qCAAA;EAAmC,2CAAA;EAAyC,mBAAA;EAC5E,eAAA;EAAiB,kDAAA;AAuEnB;AAtEE;EAAU,2BAAA;EAA6B,uCAAA;AA0EzC;;AAxEA;EAAe,gBAAA;EAAkB,cAnIzB;EAmIwC,SAAA;EAAW,iBAAA;EAAkB,eAAA;AAgF7E;;AA9EA;EAAS,eAAA;EAAiB,QAAA;EAAU,aAAA;AAoFpC;;AAnFA;EAA8B,cAAA;AAuF9B;;AAtFA;EAAmB,kBAAA;EAAoB,QAAA;EAAU,8BAAA;AA4FjD;;AA3FA;EACE,kBAAA;EAAoB,QAAA;EAAU,YAAA;EAAc,uBAAA;EAC5C,mBAAA;EAAqB,2CAAA;EAAyC,mBAAA;EAAqB,eAAA;EACnF,QAAA;EAAU,mCAAA;AAqGZ;;AAnGA;EAAgB,kBAAA;EAAoB,aAAA;EAAc,WAAA;EAAY,iBAAA;EAAmB,gBAAA;EAAkB,cAhI3F;EAgI0G,SAAA;EAAW,eAAA;AA8G7H;;AA3GA;EAAY,kBAAA;EAAoB,gBAAA;EAAkB,mBAAA;EAAqB,0CAAA;AAkHvE;;AAjHA;EAAc,aAAA;EAAe,sBAAA;EAAwB,uBAAA;EAAyB,gCAAA;AAwH9E;;AAvHA;EAAc,kBAAA;AA2Hd;;AA1HA;EAAkB,WAAA;EAAa,YAAA;EAAc,cAAA;AAgI7C;;AA/HA;EACE,kBAAA;EAAoB,OAAA;EAAS,QAAA;EAAU,SAAA;EAAW,sBAAA;EAAsB,4DAAA;AAuI1E;;AArIA;EACE,kBAAA;EAAoB,QAAA;EAAU,2BAAA;EAC9B,+BAAA;EAA6B,2CAAA;EAAyC,cA5IhE;EA4I+E,sBAAA;EAAsB,kBAAA;EAC3G,eAAA;AA8IF;;AA5IA;EAAiB,YAAA;AAgJjB;;AA/IA;EAAiB,aAAA;AAmJjB;;AAhJA;EAAe,WAAA;EAAa,mBAAA;EAAqB,0CAAA;AAsJjD;;AAnJA;EAAU,kBAAA;EAAoB,aAAA;EAAe,mBAAA;EAAqB,WAAA;AA0JlE;;AAzJA;EAAU,aAAA;EAAe,SAAA;EAAW,iBAAA;AA+JpC;AA9JE;EAAI,cAxJE;EAwJa,YAAA;AAkKrB;AAjKE;EAAU,UAAA;AAoKZ;;AAhKA;EAAU,eAAA;EAAiB,+CAAA;EAA6C,cA/JhE;AAqUR;;AAnKA;EACE;IAAS,8BAAA;EAuKT;;EAtKA;IAAW,0BAAA;EA0KX;AACF;AAzKA;EACE;IAAS,0BAAA;EA4KT;AACF;AA3KA;EACE,mBAAA;EACA,eAAA;EACA,YAAA;EACA,qBAAA;AA6KF;;AA1KA;EACE,WAAA;EACA,cAAA;EACA,qCAAA;AA6KF;;AArKA;EACE,eAAA;EACA,YAAA;EACA,WAAA;EACA,aAAA;EACA,aAAA;EACA,mBAAA;EACA,QAAA;EACA,kBAAA;EACA,yBAAA;EACA,mBAAA;EACA,mBA9MW;EA+MX,cAjNO;EAkNP,gCAAA;EACA,kBAAA;EACA,gBAAA;EACA,eAAA;EACA,8CAAA;EACA,wDAAA;AAwKF;AAtKE;EAAU,mBAzNH;EAyNwB,cAvNpB;EAuNwC,2BAAA;AA2KrD;AA1KE;EAAU,eAAA;AA6KZ;AA3KE;EACE,WAAA;EACA,kBAAA;EACA,WAAA;EACA,mBAAA;EACA,wCAAA;EACA,4CAAA;EACA,oBAAA;AA6KJ;AA3KE;EAA6B,aAAA;AA8K/B;;AA3KA;EACE;IAAO,UAAA;IAAY,mBAAA;EAgLnB;EA/KA;IAAO,UAAA;IAAY,sBAAA;EAmLnB;EAlLA;IAAO,UAAA;IAAY,sBAAA;EAsLnB;AACF;AApLA;EACE,eAAA;EACA,YAAA;EACA,WAAA;EACA,aAAA;EACA,YAAA;EACA,iBAAA;EACA,aAAA;EACA,sBAAA;EACA,yBAAA;EACA,mBAAA;EACA,mBAtPa;EAuPb,yCAAA;EACA,gBAAA;EACA,UAAA;EACA,uCAAA;EACA,oBAAA;EACA,oDAAA;AAsLF;AApLE;EAAyB,UAAA;EAAY,iCAAA;EAAmC,mBAAA;AAyL1E;AAvLE;EACE,aAAA;EACA,mBAAA;EACA,8BAAA;EACA,kBAAA;EACA,mBApQU;EAqQV,kDAAA;AAyLJ;AAvLE;EAAiB,aAAA;EAAe,mBAAA;EAAqB,SAAA;AA4LvD;AA3LE;EAAY,iBAAA;AA8Ld;AA7LE;EAAU,gCAAA;EAAkC,kBAAA;EAAoB,gBAAA;EAAkB,cAxQrE;EAwQ2F,SAAA;AAoM1G;AAnME;EAAY,gCAAA;EAAkC,iBAAA;EAAmB,cAvQnD;EAuQ0E,SAAA;AAyM1F;AAxME;EACE,gBAAA;EAAkB,YAAA;EAAc,cAzQpB;EAyQ2C,eAAA;EAAiB,eAAA;EACxE,YAAA;EAAc,kBAAA;EAAoB,uBAAA;AAgNtC;AA/MI;EAAU,cAlRL;AAoeT;AA/ME;EACE,OAAA;EAAS,gBAAA;EAAkB,aAAA;EAC3B,aAAA;EAAe,sBAAA;EAAwB,SAAA;EACvC,qBAAA;EAAuB,sDAAA;AAsN3B;AAnNE;EACE,aAAA;EAAe,mBAAA;EAAqB,QAAA;EACpC,kBAAA;EAAoB,+CAAA;EAAqC,mBAzR/C;AAkfd;AAvNE;EACE,OAAA;EAAS,mBA9RA;EA8RyB,2CAAA;EAClC,kBAAA;EAAoB,iBAAA;EAAmB,cA5R5B;EA6RX,gCAAA;EAAkC,kBAAA;EAAoB,aAAA;AA+N1D;AA9NI;EAAiB,cA5RL;AA6fhB;AAjOI;EAAiB,cA5RL;AA6fhB;AAhOI;EAAU,qBApSL;AAugBT;AAjOE;EACE,WAAA;EAAa,YAAA;EAAc,kBAAA;EAAoB,YAAA;EAC/C,mBAxSK;EAwSgB,cAtSZ;EAsSgC,kBAAA;EAAoB,eAAA;EAC7D,aAAA;EAAe,mBAAA;EAAqB,uBAAA;EACpC,4CAAA;AA2OJ;AA1OI;EAAU,mBA1SA;EA0S0B,sBAAA;AA8OxC;AA7OI;EAAa,YAAA;EAAc,mBAAA;EAAqB,eAAA;AAkPpD;;AA9OA;EACE,cAAA;EACA,gCAAA;EACA,kBAAA;EACA,iBAAA;EACA,mBAAA;EACA,kBAAA;AAiPF;AAhPE;EAAI,SAAA;AAmPN;AAjPE;EAAS,sBAAA;EAAwB,mBArTrB;EAqT+C,cAnT5C;EAmToE,8BAAA;AAuPrF;AAtPE;EAAU,oBAAA;EAAsB,mBA1TzB;EA0T8C,cAxT1C;EAwT8D,gBAAA;EAAkB,+BAAA;AA6P7F;AA5PE;EACE,sBAAA;EAAwB,mBAxTd;EAwTwC,kBAAA;AAgQtD;AA/PI;EACE,qBAAA;EAAuB,UAAA;EAAY,WAAA;EAAa,kBAAA;EAChD,mBAxTU;EAwTkB,aAAA;EAAe,mCAAA;AAsQjD;AArQM;EAAiB,qBAAA;AAwQvB;AAvQM;EAAiB,qBAAA;AA0QvB;;AArQA;EACE;IAAgB,wBAAA;IAA0B,YAAA;EA0Q1C;EAzQA;IAAiB,2BAAA;IAA6B,UAAA;EA6Q9C;AACF;AA3QA;EACE;IAAe,WAAA;IAAa,YAAA;IAAc,yBAAA;IAA2B,gBAAA;EAiRrE;;EAhRA;IAAe,WAAA;IAAa,YAAA;EAqR5B;AACF","sourcesContent":["// ===== Variables & Mixins (SCSS requirement) =====\r\n$brand: #2f6df6;\r\n$accent: #2f6df6;\r\n$accent-dark: #1a4fc4;\r\n$bg-primary: #0b1020;\r\n$bg-secondary: #111827;\r\n$bg-tertiary: #1e293b;\r\n$text-primary: #f8fafc;\r\n$text-secondary: #cbd5e1;\r\n$text-tertiary: #94a3b8;\r\n$border-color: rgba(255,255,255,0.08);\r\n$ink: #0f172a;\r\n$muted: #64748b;\r\n$bg: #0b1020;\r\n$light: #f8fafc;\r\n$maxw: 1100px;\r\n\r\n@mixin container {\r\n  width: min(#{$maxw}, 92vw);\r\n  margin-inline: auto;\r\n}\r\n\r\n@mixin fluid-type($min, $max) {\r\n  font-size: clamp($min, calc(#{$min} + 1vw), $max);\r\n}\r\n\r\n// ===== Base =====\r\n* { box-sizing: border-box; }\r\nhtml, body { margin: 0; padding: 0; scroll-behavior: smooth; }\r\nbody {\r\n  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;\r\n  color: $light;\r\n  background: $bg;\r\n}\r\n\r\nimg, video { max-width: 100%; display: block; }\r\n\r\n.container { @include container; }\r\n\r\n.stripe { padding: 6rem 0; }\r\nh1, h2, h3 { margin: 0 0 1rem; }\r\np { color: $muted; line-height: 1.7; }\r\n\r\n// ===== Header / Navbar (Sticky + Resize) =====\r\n.site-header {\r\n  position: sticky; top: 0; z-index: 1000;\r\n  backdrop-filter: saturate(110%) blur(6px);\r\n}\r\n\r\n.nav {\r\n  position: relative;\r\n  display: grid; grid-template-columns: auto 1fr; align-items: center;\r\n  gap: 1rem; padding: 1.2rem 1.2rem;\r\n  transition: padding 0.25s ease;\r\n  background: rgba(5, 9, 20, 0.75); border-bottom: 1px solid rgba(255,255,255,0.06);\r\n\r\n  .logo { font-weight: 800; color: $light; text-decoration: none; @include fluid-type(1.2rem, 1.6rem); }\r\n\r\n  .nav-links {\r\n    justify-self: end; display: flex; gap: 1.2rem; list-style: none; margin: 0; padding: 0;\r\n    a { color: $light; text-decoration: none; opacity: 0.8; transition: opacity .2s, transform .2s; }\r\n    a.active { opacity: 1; border-bottom: 2px solid $brand; }\r\n    a:hover { opacity: 1; transform: translateY(-1px); }\r\n  }\r\n\r\n  &.compact { padding: 0.5rem 1.2rem; }\r\n}\r\n\r\n// Reading progress bar (position indicator)\r\n.reading-indicator {\r\n  position: absolute; left: 0; bottom: 0;\r\n  height: 3px; width: 0%;\r\n  background: linear-gradient(90deg, $brand, lighten($brand, 15%));\r\n  transition: width .1s linear;\r\n}\r\n\r\n// ===== Hero (fixed background + vertical centering + animation) =====\r\n.hero {\r\n  min-height: 92vh;\r\n  display: grid; place-items: center;\r\n  text-align: center;\r\n  background: radial-gradient(1200px 600px at 70% 20%, rgba(47,109,246,.15), transparent);\r\n\r\n  &.has-fixed-bg {\r\n    background-image: url('../assets/hero.jpg');\r\n    background-size: cover;\r\n    background-attachment: fixed; // requirement\r\n    background-position: center;\r\n  }\r\n\r\n  .hero__content {\r\n    background: rgba(0, 0, 0, 0.362);\r\n    padding: 2rem; border: 1px solid rgba(255, 255, 255, 0); border-radius: 16px;\r\n    animation: fadeInUp .7s ease both;\r\n  }\r\n\r\n  .hero__title { @include fluid-type(2rem, 3rem); font-weight: 800; }\r\n  .hero__subtitle { @include fluid-type(1rem, 1.2rem); margin-bottom: 1.2rem; color: #d9d2d2; }\r\n}\r\n\r\n@keyframes fadeInUp {\r\n  from { opacity: 0; transform: translateY(10px); }\r\n  to   { opacity: 1; transform: translateY(0); }\r\n}\r\n\r\n// Buttons\r\n.btn {\r\n  display: inline-block;\r\n  padding: .8rem 1.1rem; border-radius: 999px;\r\n  background: $brand; color: white; text-decoration: none; border: none; cursor: pointer;\r\n  transition: transform .2s ease, box-shadow .2s ease;\r\n  &:hover { transform: translateY(-1px); box-shadow: 0 8px 24px rgba(47,109,246,.3); }\r\n}\r\n.btn-outline {\r\n  background: transparent; border: 1px solid rgba(255,255,255,.25);\r\n}\r\n\r\n// ===== About (multi-column) =====\r\n.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; }\r\n.portrait { border-radius: 16px; border: 1px solid rgba(255,255,255,.1); }\r\n.badges { display: grid; gap: .5rem; padding: 0; list-style: none;\r\n  li { background: rgba(255,255,255,.05); padding: .6rem .8rem; border-radius: 10px; }\r\n  i { margin-right: .5rem; color: $brand; }\r\n}\r\n\r\n// ===== Work (cards + modals) =====\r\n.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; }\r\n.card {\r\n  background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); border-radius: 14px;\r\n  padding: 1.2rem; transition: transform .2s ease, border-color .2s;\r\n  &:hover { transform: translateY(-3px); border-color: rgba(255,255,255,.16); }\r\n}\r\n.link-as-btn { background: none; color: $brand; border: 0; padding: .4rem 0; cursor: pointer; }\r\n\r\n.modal { position: fixed; inset: 0; display: none; }\r\n.modal[aria-hidden=\"false\"] { display: block; }\r\n.modal__backdrop { position: absolute; inset: 0; background: rgba(0,0,0,.6); }\r\n.modal__dialog {\r\n  position: absolute; inset: 0; margin: auto; width: min(680px, 92vw);\r\n  background: #0d1328; border: 1px solid rgba(255,255,255,.12); border-radius: 16px; padding: 1.2rem;\r\n  top: 10%; animation: fadeInUp .25s ease both;\r\n}\r\n.modal__close { position: absolute; right: .8rem; top: .6rem; font-size: 1.6rem; background: none; color: $light; border: 0; cursor: pointer; }\r\n\r\n// ===== Carousel =====\r\n.carousel { position: relative; overflow: hidden; border-radius: 16px; border: 1px solid rgba(255,255,255,.1); }\r\n.caro-track { display: grid; grid-auto-flow: column; grid-auto-columns: 100%; transition: transform .35s ease; }\r\n.caro-slide { position: relative; }\r\n.caro-slide img { width: 100%; height: auto; display: block; }\r\n.caro-slide figcaption {\r\n  position: absolute; left: 0; right: 0; bottom: 0; padding: .6rem .9rem; background: linear-gradient(transparent, rgba(0,0,0,.7));\r\n}\r\n.caro-btn {\r\n  position: absolute; top: 50%; transform: translateY(-50%);\r\n  background: rgba(0,0,0,.55); border: 1px solid rgba(255,255,255,.15); color: $light; padding: .6rem .8rem; border-radius: 50%;\r\n  cursor: pointer;\r\n}\r\n.caro-btn.prev { left: .6rem; }\r\n.caro-btn.next { right: .6rem; }\r\n\r\n// ===== Video =====\r\n.video video { width: 100%; border-radius: 16px; border: 1px solid rgba(255,255,255,.1); }\r\n\r\n// ===== Contact (centered content) =====\r\n.center { text-align: center; display: grid; place-items: center; gap: .6rem; }\r\n.social { display: flex; gap: 1rem; font-size: 1.3rem;\r\n  a { color: $light; opacity: .8; }\r\n  a:hover { opacity: 1; }\r\n}\r\n\r\n// ===== Footer =====\r\n.footer { padding: 2rem 0; border-top: 1px solid rgba(255,255,255,.06); color: $muted; }\r\n\r\n// ===== Responsive breakpoints =====\r\n@media (max-width: 1024px) {\r\n  .cards { grid-template-columns: 1fr 1fr; }\r\n  .columns { grid-template-columns: 1fr; }\r\n}\r\n@media (max-width: 720px) {\r\n  .cards { grid-template-columns: 1fr; }\r\n}\r\n.subhead {\r\n  margin: 18px 0 10px;\r\n  font-size: 1rem;\r\n  opacity: 0.9;\r\n  letter-spacing: 0.2px;\r\n}\r\n\r\n.section-divider {\r\n  height: 1px;\r\n  margin: 26px 0;\r\n  background: rgba(255, 255, 255, 0.08);\r\n}\r\n\r\n\r\n// =============================================================================\r\n// RAG CHATBOT — chat bubble + window\r\n// =============================================================================\r\n\r\n.chat-bubble {\r\n  position: fixed;\r\n  bottom: 28px;\r\n  right: 28px;\r\n  z-index: 9000;\r\n  display: flex;\r\n  align-items: center;\r\n  gap: 8px;\r\n  padding: 12px 18px;\r\n  border: 2px solid $accent;\r\n  border-radius: 50px;\r\n  background: $bg-primary;\r\n  color: $accent;\r\n  font-family: 'Inter', sans-serif;\r\n  font-size: 0.85rem;\r\n  font-weight: 600;\r\n  cursor: pointer;\r\n  box-shadow: 0 4px 20px rgba(255,255,0,0.25);\r\n  transition: background 0.2s, color 0.2s, transform 0.15s;\r\n\r\n  &:hover { background: $accent; color: $bg-primary; transform: translateY(-2px); }\r\n  &__icon { font-size: 1rem; }\r\n\r\n  &::after {\r\n    content: '';\r\n    position: absolute;\r\n    inset: -4px;\r\n    border-radius: 50px;\r\n    border: 2px solid rgba(255,255,0,0.3);\r\n    animation: chat-pulse 2.4s ease-out infinite;\r\n    pointer-events: none;\r\n  }\r\n  &.chat-bubble--open::after { display: none; }\r\n}\r\n\r\n@keyframes chat-pulse {\r\n  0%   { opacity: 1; transform: scale(1); }\r\n  70%  { opacity: 0; transform: scale(1.18); }\r\n  100% { opacity: 0; transform: scale(1.18); }\r\n}\r\n\r\n.chat-window {\r\n  position: fixed;\r\n  bottom: 90px;\r\n  right: 28px;\r\n  z-index: 8999;\r\n  width: 360px;\r\n  max-height: 520px;\r\n  display: flex;\r\n  flex-direction: column;\r\n  border: 1px solid $accent;\r\n  border-radius: 16px;\r\n  background: $bg-secondary;\r\n  box-shadow: 0 8px 40px rgba(0,0,0,0.7);\r\n  overflow: hidden;\r\n  opacity: 0;\r\n  transform: translateY(16px) scale(0.96);\r\n  pointer-events: none;\r\n  transition: opacity 0.22s ease, transform 0.22s ease;\r\n\r\n  &.chat-window--visible { opacity: 1; transform: translateY(0) scale(1); pointer-events: all; }\r\n\r\n  &__header {\r\n    display: flex;\r\n    align-items: center;\r\n    justify-content: space-between;\r\n    padding: 14px 16px;\r\n    background: $bg-tertiary;\r\n    border-bottom: 1px solid $border-color;\r\n  }\r\n  &__header-info { display: flex; align-items: center; gap: 10px; }\r\n  &__avatar { font-size: 1.4rem; }\r\n  &__name { font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 700; color: $text-primary; margin: 0; }\r\n  &__status { font-family: 'Inter', sans-serif; font-size: 0.7rem; color: $text-tertiary; margin: 0; }\r\n  &__close {\r\n    background: none; border: none; color: $text-tertiary; font-size: 1rem; cursor: pointer;\r\n    padding: 4px; border-radius: 6px; transition: color 0.15s;\r\n    &:hover { color: $accent; }\r\n  }\r\n\r\n  &__messages {\r\n    flex: 1; overflow-y: auto; padding: 16px;\r\n    display: flex; flex-direction: column; gap: 12px;\r\n    scrollbar-width: thin; scrollbar-color: $border-color transparent;\r\n  }\r\n\r\n  &__input-row {\r\n    display: flex; align-items: center; gap: 8px;\r\n    padding: 12px 14px; border-top: 1px solid $border-color; background: $bg-tertiary;\r\n  }\r\n  &__input {\r\n    flex: 1; background: $bg-primary; border: 1px solid $border-color;\r\n    border-radius: 8px; padding: 9px 12px; color: $text-primary;\r\n    font-family: 'Inter', sans-serif; font-size: 0.82rem; outline: none;\r\n    &::placeholder { color: $text-tertiary; }\r\n    &:focus { border-color: $accent; }\r\n  }\r\n  &__send {\r\n    width: 36px; height: 36px; border-radius: 8px; border: none;\r\n    background: $accent; color: $bg-primary; font-size: 0.85rem; cursor: pointer;\r\n    display: flex; align-items: center; justify-content: center;\r\n    transition: background 0.15s, transform 0.1s;\r\n    &:hover { background: $accent-dark; transform: scale(1.06); }\r\n    &:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }\r\n  }\r\n}\r\n\r\n.chat-msg {\r\n  max-width: 86%;\r\n  font-family: 'Inter', sans-serif;\r\n  font-size: 0.82rem;\r\n  line-height: 1.55;\r\n  border-radius: 12px;\r\n  padding: 10px 13px;\r\n  p { margin: 0; }\r\n\r\n  &--bot { align-self: flex-start; background: $bg-tertiary; color: $text-secondary; border-bottom-left-radius: 4px; }\r\n  &--user { align-self: flex-end; background: $accent; color: $bg-primary; font-weight: 600; border-bottom-right-radius: 4px; }\r\n  &--typing {\r\n    align-self: flex-start; background: $bg-tertiary; padding: 12px 16px;\r\n    span {\r\n      display: inline-block; width: 6px; height: 6px; border-radius: 50%;\r\n      background: $text-tertiary; margin: 0 2px; animation: typing-dot 1.2s infinite;\r\n      &:nth-child(2) { animation-delay: 0.2s; }\r\n      &:nth-child(3) { animation-delay: 0.4s; }\r\n    }\r\n  }\r\n}\r\n\r\n@keyframes typing-dot {\r\n  0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }\r\n  30%            { transform: translateY(-5px); opacity: 1; }\r\n}\r\n\r\n@media (max-width: 480px) {\r\n  .chat-window { right: 12px; bottom: 84px; width: calc(100vw - 24px); max-height: 60vh; }\r\n  .chat-bubble { right: 12px; bottom: 20px; }\r\n}\r\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "../node_modules/css-loader/dist/runtime/api.js":
/*!******************************************************!*\
  !*** ../node_modules/css-loader/dist/runtime/api.js ***!
  \******************************************************/
/***/ ((module) => {

"use strict";

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

/***/ "../node_modules/css-loader/dist/runtime/getUrl.js":
/*!*********************************************************!*\
  !*** ../node_modules/css-loader/dist/runtime/getUrl.js ***!
  \*********************************************************/
/***/ ((module) => {

"use strict";


module.exports = function (url, options) {
  if (!options) {
    options = {};
  }

  if (!url) {
    return url;
  }

  url = String(url.__esModule ? url.default : url); // If url is already wrapped in quotes, remove them

  if (/^['"].*['"]$/.test(url)) {
    url = url.slice(1, -1);
  }

  if (options.hash) {
    url += options.hash;
  } // Should url be wrapped?
  // See https://drafts.csswg.org/css-values-3/#urls


  if (/["'() \t\n]|(%20)/.test(url) || options.needQuotes) {
    return "\"".concat(url.replace(/"/g, '\\"').replace(/\n/g, "\\n"), "\"");
  }

  return url;
};

/***/ }),

/***/ "../node_modules/css-loader/dist/runtime/sourceMaps.js":
/*!*************************************************************!*\
  !*** ../node_modules/css-loader/dist/runtime/sourceMaps.js ***!
  \*************************************************************/
/***/ ((module) => {

"use strict";


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

/***/ "../node_modules/html-loader/dist/runtime/getUrl.js":
/*!**********************************************************!*\
  !*** ../node_modules/html-loader/dist/runtime/getUrl.js ***!
  \**********************************************************/
/***/ ((module) => {

"use strict";


module.exports = function (url, options) {
  if (!options) {
    // eslint-disable-next-line no-param-reassign
    options = {};
  }

  if (!url) {
    return url;
  } // eslint-disable-next-line no-underscore-dangle, no-param-reassign


  url = String(url.__esModule ? url.default : url);

  if (options.hash) {
    // eslint-disable-next-line no-param-reassign
    url += options.hash;
  }

  if (options.maybeNeedQuotes && /[\t\n\f\r "'=<>`]/.test(url)) {
    return "\"".concat(url, "\"");
  }

  return url;
};

/***/ }),

/***/ "../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!*****************************************************************************!*\
  !*** ../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \*****************************************************************************/
/***/ ((module) => {

"use strict";


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

"use strict";


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

"use strict";


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

"use strict";


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

"use strict";


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

"use strict";


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

/***/ "./assets/hero.jpg":
/*!*************************!*\
  !*** ./assets/hero.jpg ***!
  \*************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
module.exports = __webpack_require__.p + "e52c3c19926ab84cbe7d.jpg";

/***/ }),

/***/ "./assets/portrait.jpg":
/*!*****************************!*\
  !*** ./assets/portrait.jpg ***!
  \*****************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
module.exports = __webpack_require__.p + "ad73cc6843d9c4c9dac3.jpg";

/***/ }),

/***/ "./css/styles.scss":
/*!*************************!*\
  !*** ./css/styles.scss ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
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


/***/ }),

/***/ "./index.html":
/*!********************!*\
  !*** ./index.html ***!
  \********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_html_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/html-loader/dist/runtime/getUrl.js */ "../node_modules/html-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_html_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_html_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_0__);
// Imports

var ___HTML_LOADER_IMPORT_0___ = new URL(/* asset import */ __webpack_require__(/*! ./assets/portrait.jpg */ "./assets/portrait.jpg"), __webpack_require__.b);
var ___HTML_LOADER_IMPORT_1___ = new URL(/* asset import */ __webpack_require__(/*! ./js/index.js */ "./js/index.js?5952"), __webpack_require__.b);
// Module
var ___HTML_LOADER_REPLACEMENT_0___ = _node_modules_html_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_0___default()(___HTML_LOADER_IMPORT_0___);
var ___HTML_LOADER_REPLACEMENT_1___ = _node_modules_html_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_0___default()(___HTML_LOADER_IMPORT_1___);
var code = "<!doctype html>\r\n<html lang=\"en\">\r\n<head>\r\n  <meta charset=\"utf-8\" />\r\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\r\n  <title>Malhar Gudekar · Portfolio</title>\r\n\r\n  <!-- Webfont (ok to use) -->\r\n  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\r\n  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap\" rel=\"stylesheet\">\r\n\r\n  <!-- Font Awesome (allowed as “scalable vector icons through CSS”) -->\r\n  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css\" referrerpolicy=\"no-referrer\"/>\r\n\r\n  <!--link rel=\"stylesheet\" href=\"./css/styles.css\" /-->\r\n</head>\r\n<body>\r\n\r\n  <!-- Sticky / Resizing Navbar with Position Indicator -->\r\n  <header id=\"top\" class=\"site-header\">\r\n    <nav class=\"nav\" id=\"navbar\">\r\n      <a class=\"logo\" href=\"#top\">Malhar Ravindra Gudekar</a>\r\n      <!-- NAV: simplify -->\r\n      <ul class=\"nav-links\" id=\"navLinks\">\r\n        <li><a href=\"#hero\" data-section=\"hero\">Home</a></li>\r\n        <li><a href=\"#about\" data-section=\"about\">About</a></li>\r\n        <li><a href=\"#experience\" data-section=\"experience\">Experience</a></li>\r\n        <li><a href=\"#projects\" data-section=\"projects\">Projects</a></li>\r\n        <li><a href=\"#contact\" data-section=\"contact\">Contact</a></li>\r\n        \r\n      </ul>\r\n\r\n      <!-- position indicator bar -->\r\n      <div class=\"reading-indicator\" id=\"readingIndicator\"></div>\r\n    </nav>\r\n  </header>\r\n\r\n  <!-- HERO: change CTAs -->\r\n  <section id=\"hero\" class=\"stripe hero has-fixed-bg\" aria-label=\"Intro\">\r\n    <div class=\"hero__content\">\r\n      <h1 class=\"hero__title\">Hi, I’m Malhar.</h1>\r\n      <p class=\"hero__subtitle\">\r\n        I design and ship end-to-end data and AI systems spanning analytics, forecasting, NLP, and production ML—\r\n        across healthcare, finance, and secure digital platforms.\r\n      </p>\r\n      <div class=\"hero__cta\">\r\n        <a class=\"btn\" href=\"#projects\">View Projects</a>\r\n        <a class=\"btn btn-outline\" href=\"./assets/Malhar Gudekar Resume (1).pdf\" target=\"_blank\" rel=\"noopener\">\r\n          Resume\r\n        </a>\r\n        <!-- optional third -->\r\n        <button class=\"btn btn-ghost\" id=\"openAboutModal\">Quick Bio</button>\r\n      </div>\r\n    </div>\r\n  </section>\r\n\r\n\r\n  <!-- Modal (About quick bio) -->\r\n  <div class=\"modal\" id=\"aboutModal\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"aboutTitle\">\r\n    <div class=\"modal__backdrop\" data-close></div>\r\n    <div class=\"modal__dialog\" role=\"document\">\r\n      <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n      <h2 id=\"aboutTitle\">About Me</h2>\r\n      <p>Master of Science in Information Management @ UIUC | Applied Data Scientist & ML Engineer</p>\r\n      <p>Bachelor of Engineering in Computer Science @ Mumbai University</p>\r\n      <p>I build end-to-end data and machine learning systems, from analytics and forecasting to production ML and RAG pipelines. My work spans healthcare, finance, and security, including real-time misinformation detection, AI-powered retrieval systems, and predictive credit risk modeling.</p>\r\n      <p>Experience across:</p>\r\n      <p>• Healthcare AI & misinformation detection</p>\r\n      <p>• Data engineering & analytics platforms</p>\r\n      <p>• Secure, AI-powered product development</p>\r\n      <p>Experienced with Python, SQL, ML/NLP, FastAPI, Kafka, Docker, and AWS. Currently seeking full-time roles in Data Science, Machine Learning, or Analytics Engineering.</p>\r\n    </div>\r\n  </div>\r\n\r\n  <!-- Stripe: About (multi-column layout) -->\r\n  <!-- ABOUT: remove “student-first” framing -->\r\n  <section id=\"about\" class=\"stripe about\">\r\n    <div class=\"container columns\">\r\n      <div class=\"col\">\r\n        <img class=\"portrait\" src=\"" + ___HTML_LOADER_REPLACEMENT_0___ + "\" alt=\"Portrait of Malhar\">\r\n      </div>\r\n      <div class=\"col\">\r\n        <h2>About</h2>\r\n        <p>\r\n          I build and deploy data, ML, and AI systems with real-world impact across healthcare, finance, and secure platforms.\r\n        </p>\r\n        <ul class=\"badges\">\r\n          <li><i class=\"fa-solid fa-wand-magic-sparkles\"></i> Real-time ML pipelines (Kafka, Neo4j, AWS EKS)</li>\r\n          <li><i class=\"fa-solid fa-database\"></i> Production RAG systems (FastAPI, PostgreSQL, pgVector)</li>\r\n          <li><i class=\"fa-solid fa-shield\"></i> Secure, data-driven products across research and industry</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n  </section>\r\n\r\n\r\n  <!-- Stripe: Work (cards) -->\r\n  <!-- EXPERIENCE: rename from work + split UIUC into two cards -->\r\n  <section id=\"experience\" class=\"stripe work\">\r\n    <div class=\"container\">\r\n      <h2>Experience</h2>\r\n\r\n      <!-- Core Technical Experience -->\r\n      <h3 class=\"subhead\">Core Technical Experience</h3>\r\n      <div class=\"cards\">\r\n\r\n        <article class=\"card\">\r\n          <h3>UIUC — Research Assistant (Finance & Health)</h3>\r\n          <p>mHealth platform integrating wearable data + conversational AI for personalized coaching.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-uiuc-mhealth\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>UIUC — Research Assistant (CHI: Infodemic AI)</h3>\r\n          <p>Real-time NLP + streaming pipelines for large-scale health misinformation detection.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-uiuc-chi\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>Business Intelligence Group — Technical Consultant</h3>\r\n          <p>Production RAG pipeline for automated payer rule extraction + policy retrieval.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-big\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>Stu/Dio at Illinois — Project Manager</h3>\r\n          <p>Cross-functional delivery for a consumer app; shipped fast iterations with user feedback loops.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-studio\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>Swift Mobil — Data Analyst</h3>\r\n          <p>Python data pipelines + graph analysis + Power BI dashboards for operational decision support.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-swift\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>Pscope Technologies — Data Analyst</h3>\r\n          <p>Automated reporting + built Power BI dashboards for cross-functional KPI tracking.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-pscope\">Details</button>\r\n        </article>\r\n      </div>\r\n\r\n      <!-- Divider -->\r\n      <div class=\"section-divider\" aria-hidden=\"true\"></div>\r\n\r\n      <!-- Leadership & Campus Roles -->\r\n      <h3 class=\"subhead\">Leadership & Campus Roles</h3>\r\n      <div class=\"cards\">\r\n\r\n        <article class=\"card\">\r\n          <h3>UIUC Career Center — Student Career Navigator</h3>\r\n          <p>Built career resources + mentored peers; improved engagement and job-search confidence.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-career-nav\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>University of Illinois System — Data Quality & Accessibility Assistant</h3>\r\n          <p>Improved document structure, metadata, and accessibility QA for compliance-ready records.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-accessibility\">Details</button>\r\n        </article>\r\n\r\n        <article class=\"card\">\r\n          <h3>National Service Scheme — Team Lead</h3>\r\n          <p>Led community initiatives and field programs focused on social welfare, outreach, and impact execution.</p>\r\n          <button class=\"link-as-btn\" data-open=\"#details-nss\">Details</button>\r\n        </article>\r\n\r\n      </div>\r\n    </div>\r\n\r\n    <!-- =========================\r\n     EXPERIENCE MODALS (REWRITTEN)\r\n     ========================= -->\r\n\r\n    <!-- Stu/Dio -->\r\n    <div class=\"modal\" id=\"details-studio\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"studioTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"studioTitle\">Stu/Dio at Illinois — Project Manager</h3>\r\n        <p><strong>Aug 2025 – Present</strong> · Champaign, IL</p>\r\n\r\n        <p>\r\n          Led cross-functional delivery for <strong>DeepCover</strong>, coordinating engineering, design, and QA to ship iterative builds\r\n          and stakeholder-ready demos.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Drove <strong>25% user growth</strong> and improved app ratings to <strong>4.0 stars</strong> on both the App Store and Play Store through rapid iteration and feedback loops</li>\r\n          <li>Implemented <strong>Scrum/Kanban</strong> workflows with JIRA-based sprint planning, backlog prioritization, and release tracking</li>\r\n          <li>Streamlined QA cycles and milestone delivery to ensure <strong>on-time demos</strong> and production-ready builds</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- Business Intelligence Group -->\r\n    <div class=\"modal\" id=\"details-big\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"bigTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"bigTitle\">Business Intelligence Group — Technical Consultant</h3>\r\n        <p><strong>Aug 2025 – Dec 2025</strong> · Champaign, IL</p>\r\n\r\n        <p>\r\n          Built a production-oriented <strong>RAG pipeline</strong> to automate extraction and retrieval of payer/insurance billing rules\r\n          from healthcare PDFs and portals.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Developed <strong>Selenium-based crawlers</strong> to ingest unstructured policy documents and convert them into a structured, queryable knowledge base</li>\r\n          <li>Implemented <strong>FastAPI</strong> services with <strong>PostgreSQL + pgVector</strong> for semantic search and version-controlled policy retrieval</li>\r\n          <li>Reduced manual rule lookup time by <strong>60%</strong>, improving billing efficiency and policy compliance for healthcare teams</li>\r\n          <li>Delivered a scalable system aligned with real-world healthcare workflows and operational constraints</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- UIUC: Finance & Health (mHealth) -->\r\n    <div class=\"modal\" id=\"details-uiuc-mhealth\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"mhealthTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"mhealthTitle\">University of Illinois Urbana-Champaign — Research Assistant (Finance & Health)</h3>\r\n        <p><strong>May 2025 – Present</strong> · Champaign, IL</p>\r\n\r\n        <p>\r\n          Built and deployed a cross-platform <strong>mHealth application</strong> integrating wearable data and conversational AI to support\r\n          personalized coaching for older adults.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Developed a <strong>Flutter + Dart</strong> app enabling real-time activity tracking and personalized feedback for <strong>100+ users</strong></li>\r\n          <li>Designed a <strong>PostgreSQL</strong> schema for longitudinal activity, conversation history, and user profiles, improving query performance and context retrieval by <strong>40%</strong></li>\r\n          <li>Engineered an AI chatbot with <strong>RAG-based retrieval</strong> and <strong>history summarization</strong>, reducing multi-turn context loss by <strong>55%</strong></li>\r\n          <li>Shipped a reliable, user-centered system aligned with healthcare usability and data quality requirements</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- UIUC: CHI Infodemic AI -->\r\n    <div class=\"modal\" id=\"details-uiuc-chi\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"chiTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"chiTitle\">University of Illinois Urbana-Champaign — Research Assistant (CHI: Infodemic AI)</h3>\r\n        <p><strong>Jan 2025 – May 2025</strong> · Champaign, IL</p>\r\n\r\n        <p>\r\n          Designed and scaled real-time pipelines for detecting viral health misinformation across social platforms using streaming and graph-based modeling.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Integrated <strong>Apache Kafka</strong> and <strong>Neo4j Streams</strong> for high-throughput ingestion and relationship-aware analysis across TikTok and YouTube data</li>\r\n          <li>Built modular <strong>Python NLP</strong> pipelines and deployed on <strong>AWS EKS</strong> via Docker, reducing inference latency by <strong>40%+</strong></li>\r\n          <li>Developed scalable inference APIs and CI/CD workflows to ensure reproducible, reliable deployments</li>\r\n          <li>Supported <strong>WHO-aligned</strong> misinformation tracking with an emphasis on scalability and operational robustness</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- Swift Mobil -->\r\n    <div class=\"modal\" id=\"details-swift\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"swiftTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"swiftTitle\">Swift Mobil Software Solutions Provider — Data Analyst</h3>\r\n        <p><strong>Jul 2023 – Oct 2023</strong> · Mumbai, IN</p>\r\n\r\n        <p>\r\n          Worked on ingestion, transformation, and analytics workflows to improve operational visibility and decision-making.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Processed large <strong>REST API datasets</strong> using <strong>Python (Pandas, NumPy)</strong> and prepared clean data stored in <strong>AWS S3</strong>, improving reporting accuracy by <strong>20%</strong></li>\r\n          <li>Used <strong>Neo4j</strong> and <strong>SQL</strong> analysis to detect patterns and anomalies, enabling <strong>30% faster</strong> root-cause analysis</li>\r\n          <li>Built and maintained <strong>Power BI dashboards</strong> for logistics and financial KPIs, reducing manual reporting time by <strong>40%</strong></li>\r\n          <li>Translated operational data into actionable insights through analytics and visualization</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- Pscope -->\r\n    <div class=\"modal\" id=\"details-pscope\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"pscopeTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"pscopeTitle\">Pscope Technologies Pvt. Ltd. — Data Analyst</h3>\r\n        <p><strong>Jan 2023 – Jun 2023</strong> · Mumbai, IN</p>\r\n\r\n        <p>\r\n          Built analytics automation and dashboards to support performance tracking across Sales, Finance, and Operations.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Automated Excel reporting workflows with <strong>VBA</strong>, reducing report preparation time by <strong>30%</strong></li>\r\n          <li>Designed and maintained <strong>20+ Power BI dashboards</strong> using <strong>SQL + DAX</strong> for cross-functional performance reporting</li>\r\n          <li>Consolidated and validated <strong>CRM/ERP</strong> datasets to improve accuracy and data consistency</li>\r\n          <li>Collaborated in Agile sprints using <strong>Jira</strong> to deliver iterative, stakeholder-driven analytics improvements</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n    \r\n  <div class=\"modal\" id=\"details-career-nav\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"careerNavTitle\">\r\n    <div class=\"modal__backdrop\" data-close></div>\r\n    <div class=\"modal__dialog\" role=\"document\">\r\n      <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n      <h3 id=\"careerNavTitle\">Student Career Navigator — UIUC Career Center</h3>\r\n      <p><strong>Aug 2025 – Present</strong> · Champaign, IL · On-site</p>\r\n\r\n      <p>\r\n        Supported the UIUC Career Center by designing data-informed career resources, mentoring students,\r\n        and delivering workshops to improve job-readiness and engagement outcomes.\r\n      </p>\r\n\r\n      <ul>\r\n        <li>Designed and refined career resources, increasing student engagement by <strong>27%</strong> and improving accessibility for international students</li>\r\n        <li>Mentored <strong>10+ students</strong> on career strategy, resume positioning, and networking, improving job-search confidence by <strong>35%</strong></li>\r\n        <li>Led workshops on industry networking and recruitment preparation, translating best practices into actionable guidance</li>\r\n        <li>Analyzed <strong>17,000+ student records</strong> for the Illinois Success Report to identify academic and engagement trends, enabling data-driven improvements in student services</li>\r\n      </ul>\r\n    </div>\r\n  </div>\r\n\r\n    <div class=\"modal\" id=\"details-accessibility\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"accessibilityTitle\">\r\n      <div class=\"modal__backdrop\" data-close></div>\r\n      <div class=\"modal__dialog\" role=\"document\">\r\n        <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n        <h3 id=\"accessibilityTitle\">Data Quality & Accessibility Assistant — University of Illinois System</h3>\r\n        <p><strong>Jun 2025 – Present</strong> · Champaign, IL · Remote</p>\r\n\r\n        <p>\r\n          Focused on improving data quality, accessibility compliance, and documentation standards\r\n          across institutional records and reporting systems.\r\n        </p>\r\n\r\n        <ul>\r\n          <li>Standardized <strong>50+ documents</strong> by improving structure, metadata, and tagging using <strong>Adobe Acrobat Pro DC</strong></li>\r\n          <li>Validated screen-reader compatibility through manual QA checks, contributing to improved accessibility compliance</li>\r\n          <li>Identified and documented layout and tagging inconsistencies to improve cross-document consistency</li>\r\n          <li>Collaborated using a centralized QA tracker to capture key accessibility KPIs and improve overall data quality processes</li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n    \r\n\r\n\r\n    <div class=\"modal\" id=\"details-nss\" aria-hidden=\"true\" role=\"dialog\" aria-labelledby=\"nssTitle\">\r\n    <div class=\"modal__backdrop\" data-close></div>\r\n    <div class=\"modal__dialog\" role=\"document\">\r\n      <button class=\"modal__close\" aria-label=\"Close\" data-close>&times;</button>\r\n\r\n      <h3 id=\"nssTitle\">National Service Scheme — Team Lead</h3>\r\n      <p><strong>Jun 2020 – Jun 2022</strong> · India</p>\r\n\r\n      <p>\r\n        Led community-focused programs aimed at improving social welfare through structured planning,\r\n        on-ground execution, and volunteer coordination.\r\n      </p>\r\n\r\n      <ul>\r\n        <li>Organized and managed initiatives including <strong>food donation drives</strong>, <strong>child welfare programs</strong>, and <strong>environmental clean-up campaigns</strong></li>\r\n        <li>Led <strong>week-long rural outreach camps</strong>, conducting surveys to identify local challenges and translating findings into actionable interventions</li>\r\n        <li>Coordinated volunteers and logistics to ensure timely execution and community participation</li>\r\n        <li>Raised awareness around public health, education, and sustainability to support long-term community well-being</li>\r\n      </ul>\r\n    </div>\r\n  </div>\r\n\r\n  </section>\r\n\r\n\r\n\r\n\r\n  <!-- PROJECTS: new section (your best 4–5) -->\r\n<section id=\"projects\" class=\"stripe work\">\r\n  <div class=\"container\">\r\n    <h2>Projects</h2>\r\n\r\n    <div class=\"cards\">\r\n\r\n      <!-- Predictive Credit -->\r\n      <article class=\"card\">\r\n        <h3>Predictive Credit Limit Adjustment & Risk Segmentation</h3>\r\n        <p>\r\n          Forecasted Q4 customer spend and recommended credit line changes using LightGBM,\r\n          enabling personalized risk-aware credit decisions.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://www.kaggle.com/code/malharravigudekar/notebookebd4dc2b02\" target=\"_blank\" rel=\"noopener\">\r\n          Case Study\r\n        </a>\r\n      </article>\r\n\r\n      <!-- BASILISK -->\r\n      <article class=\"card\">\r\n        <h3>BASILISK — Security Hub</h3>\r\n        <p>\r\n          Hybrid cryptography platform for secure communication, integrity, and non-repudiation.\r\n          Published in a UGC Care Group 1 journal.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://github.com/malhar-123/Basilisk\" target=\"_blank\" rel=\"noopener\">\r\n          Read More\r\n        </a>\r\n      </article>\r\n\r\n      <!-- F1 -->\r\n      <article class=\"card\">\r\n        <h3>F1 Race Outcome Prediction (FastF1)</h3>\r\n        <p>\r\n          Engineered lap- and race-level features from FastF1 data and used GBM +\r\n          Monte Carlo simulations to predict grid finish positions.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://github.com/malhar-123/f1-race-prediction\" target=\"_blank\" rel=\"noopener\">\r\n          View Project\r\n        </a>\r\n      </article>\r\n\r\n      <!-- FMCG Forecasting -->\r\n      <article class=\"card\">\r\n        <h3>FMCG Sales Demand Forecasting</h3>\r\n        <p>\r\n          Built ARIMA-based demand forecasting models in R with 80% accuracy,\r\n          reducing stockouts and overstock through data-driven planning.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://github.com/malhar-123/fmcg-demand-forecasting\" target=\"_blank\" rel=\"noopener\">\r\n          View Analysis\r\n        </a>\r\n      </article>\r\n\r\n      <!-- Database Systems -->\r\n      <article class=\"card\">\r\n        <h3>Database Design for Nonresident Alien Payments</h3>\r\n        <p>\r\n          Designed SQL + Neo4j systems for tax-compliant payments,\r\n          modeling complex visa, treaty, and compliance relationships.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://malhar-123.github.io/tax-payment-data-model/\" target=\"_blank\" rel=\"noopener\">\r\n          View Design\r\n        </a>\r\n      </article>\r\n\r\n      <!-- Optional: AR / Product -->\r\n      <article class=\"card\">\r\n        <h3>AI-Powered AR Virtual Try-On (Product Case Study)</h3>\r\n        <p>\r\n          Led competitive analysis and customer segmentation to design an AR\r\n          roadmap for Glossier, projecting higher conversion and lower returns.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"./assets/IS534_Final_Presentation_Team_5.pdf\" target=\"_blank\" rel=\"noopener\">\r\n          Case Study\r\n        </a>\r\n      </article>\r\n      <!-- Environmental Analytics -->\r\n      <article class=\"card\">\r\n        <h3>Environmental Data Analytics & Visualization</h3>\r\n        <p>\r\n          Analyzed 7-year environmental trends using Power BI heat maps and tree maps,\r\n          identifying regional toxin concentration patterns.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://app.powerbi.com/reportEmbed?reportId=ee3bf52d-c2c5-4ef0-a2fc-21215337e93e&autoAuth=true&ctid=44467e6f-462c-4ea2-823f-7800de5434e3\" target=\"_blank\" rel=\"noopener\">View Project</a>\r\n      </article>\r\n\r\n      <!-- Facial Analysis -->\r\n      <article class=\"card\">\r\n        <h3>Advanced Facial Analysis System</h3>\r\n        <p>\r\n          Built a real-time computer vision pipeline using Python, OpenCV, and CNNs,\r\n          achieving 98% emotion classification accuracy.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://github.com/malhar-123/python_face_detection\" target=\"_blank\" rel=\"noopener\">View Project</a>\r\n      </article>\r\n\r\n      <!-- Expense Tracker -->\r\n      <article class=\"card\">\r\n        <h3>Mobile Expense Tracker App</h3>\r\n        <p>\r\n          Developed a Flutter-based mobile app with Provider state management and\r\n          interactive charts to visualize personal spending patterns.\r\n        </p>\r\n        <a class=\"link-as-btn\" href=\"https://github.com/malhar-123/Mobile-Expense-Tracking-and-PA\" target=\"_blank\" rel=\"noopener\">View App</a>\r\n      </article>  \r\n    </div>\r\n  </div>\r\n</section>\r\n\r\n\r\n\r\n  <section id=\"personal\" class=\"stripe extras\">\r\n  <div class=\"container\">\r\n    <h2>Beyond Work</h2>\r\n\r\n    <ul class=\"extras-list\">\r\n      <li>\r\n        <strong>Endurance & Discipline:</strong>\r\n        Long-distance running and triathlon training — consistency, goal-setting,\r\n        and showing up even when progress is incremental.\r\n      </li>\r\n\r\n      <li>\r\n        <strong>Systems Curiosity:</strong>\r\n        Formula 1 — performance optimization, data-driven strategy,\r\n        and engineering trade-offs under real-world constraints.\r\n      </li>\r\n\r\n      <li>\r\n        <strong>Craft & Focus:</strong>\r\n        Cooking as a way to unwind while still thinking in systems —\r\n        inputs, timing, iteration, and feedback.\r\n      </li>\r\n\r\n      <li>\r\n        <strong>Exploration:</strong>\r\n        Hiking and long drives — time to reset, reflect, and explore new environments.\r\n      </li>\r\n    </ul>\r\n  </div>\r\n</section>\r\n\r\n\r\n  <!-- Stripe: Contact (centered) -->\r\n  <section id=\"contact\" class=\"stripe contact\">\r\n    <div class=\"container center\">\r\n      <h2>Let’s connect</h2>\r\n      <p>Reach out for collaborations or opportunities.</p>\r\n      <div class=\"social\">\r\n        <a aria-label=\"GitHub\" href=\"https://github.com/malhar-123\" target=\"_blank\"><i class=\"fa-brands fa-github\"></i></a>\r\n        <a aria-label=\"LinkedIn\" href=\"https://www.linkedin.com/in/malhar-gudekar/\" target=\"_blank\"><i class=\"fa-brands fa-linkedin\"></i></a>\r\n        <a aria-label=\"Email\" href=\"mailto:gudekar2@illinois.edu\"><i class=\"fa-solid fa-envelope\"></i></a>\r\n      </div>\r\n    </div>\r\n  </section>\r\n\r\n  <footer class=\"stripe footer\">\r\n    <div class=\"container\">\r\n      <small>&copy; <span id=\"year\"></span> Malhar Gudekar</small>\r\n    </div>\r\n  </footer>\r\n\r\n  <" + "script src=\"" + ___HTML_LOADER_REPLACEMENT_1___ + "\" defer><" + "/script>\r\n\r\n  <!-- ── RAG CHATBOT ── -->\r\n  <button class=\"chat-bubble\" id=\"chatBubble\" aria-label=\"Open AI chat\">\r\n    <i class=\"fa-solid fa-comment-dots chat-bubble__icon\"></i>\r\n    <span class=\"chat-bubble__label\">Ask AI</span>\r\n  </button>\r\n\r\n  <div class=\"chat-window\" id=\"chatWindow\" aria-hidden=\"true\">\r\n    <div class=\"chat-window__header\">\r\n      <div class=\"chat-window__header-info\">\r\n        <span class=\"chat-window__avatar\">🤖</span>\r\n        <div>\r\n          <p class=\"chat-window__name\">Ask about Malhar</p>\r\n          <p class=\"chat-window__status\">Powered by Groq · llama3-70b</p>\r\n        </div>\r\n      </div>\r\n      <button class=\"chat-window__close\" id=\"chatClose\" aria-label=\"Close chat\">\r\n        <i class=\"fa-solid fa-xmark\"></i>\r\n      </button>\r\n    </div>\r\n    <div class=\"chat-window__messages\" id=\"chatMessages\">\r\n      <div class=\"chat-msg chat-msg--bot\">\r\n        <p>Hi! I'm Malhar's AI assistant. Ask me anything about his experience, projects, or skills.</p>\r\n      </div>\r\n    </div>\r\n    <div class=\"chat-window__input-row\">\r\n      <input class=\"chat-window__input\" id=\"chatInput\" type=\"text\" placeholder=\"Ask a question…\" maxlength=\"500\" autocomplete=\"off\" />\r\n      <button class=\"chat-window__send\" id=\"chatSend\" aria-label=\"Send\">\r\n        <i class=\"fa-solid fa-paper-plane\"></i>\r\n      </button>\r\n    </div>\r\n  </div>\r\n  <!-- ── END RAG CHATBOT ── -->\r\n\r\n</body>\r\n</html>\r\n\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000";
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (code);

/***/ }),

/***/ "./js/index.js?5952":
/*!*********************!*\
  !*** ./js/index.js ***!
  \*********************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";
module.exports = __webpack_require__.p + "95c3f3d25dbc16e4eaa4.js";

/***/ }),

/***/ "./js/main.js":
/*!********************!*\
  !*** ./js/main.js ***!
  \********************/
/***/ (() => {

// main.js — additional scripts entry point

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
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = __webpack_modules__;
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
/******/ 	/* webpack/runtime/global */
/******/ 	(() => {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
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
/******/ 	/* webpack/runtime/publicPath */
/******/ 	(() => {
/******/ 		var scriptUrl;
/******/ 		if (__webpack_require__.g.importScripts) scriptUrl = __webpack_require__.g.location + "";
/******/ 		var document = __webpack_require__.g.document;
/******/ 		if (!scriptUrl && document) {
/******/ 			if (document.currentScript && document.currentScript.tagName.toUpperCase() === 'SCRIPT')
/******/ 				scriptUrl = document.currentScript.src;
/******/ 			if (!scriptUrl) {
/******/ 				var scripts = document.getElementsByTagName("script");
/******/ 				if(scripts.length) {
/******/ 					var i = scripts.length - 1;
/******/ 					while (i > -1 && (!scriptUrl || !/^http(s?):/.test(scriptUrl))) scriptUrl = scripts[i--].src;
/******/ 				}
/******/ 			}
/******/ 		}
/******/ 		// When supporting browsers where an automatic publicPath is not supported you must specify an output.publicPath manually via configuration
/******/ 		// or pass an empty string ("") and set the __webpack_public_path__ variable from your code to use your own logic.
/******/ 		if (!scriptUrl) throw new Error("Automatic publicPath is not supported in this browser");
/******/ 		scriptUrl = scriptUrl.replace(/^blob:/, "").replace(/#.*$/, "").replace(/\?.*$/, "").replace(/\/[^\/]+$/, "/");
/******/ 		__webpack_require__.p = scriptUrl;
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/jsonp chunk loading */
/******/ 	(() => {
/******/ 		__webpack_require__.b = document.baseURI || self.location.href;
/******/ 		
/******/ 		// object to store loaded and loading chunks
/******/ 		// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 		// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
/******/ 		var installedChunks = {
/******/ 			"main": 0
/******/ 		};
/******/ 		
/******/ 		// no chunk on demand loading
/******/ 		
/******/ 		// no prefetching
/******/ 		
/******/ 		// no preloaded
/******/ 		
/******/ 		// no HMR
/******/ 		
/******/ 		// no HMR manifest
/******/ 		
/******/ 		// no on chunks loaded
/******/ 		
/******/ 		// no jsonp function
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/nonce */
/******/ 	(() => {
/******/ 		__webpack_require__.nc = undefined;
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry needs to be wrapped in an IIFE because it needs to be in strict mode.
(() => {
"use strict";
/*!*********************!*\
  !*** ./js/index.js ***!
  \*********************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _index_html__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../index.html */ "./index.html");
/* harmony import */ var _css_styles_scss__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../css/styles.scss */ "./css/styles.scss");
/* harmony import */ var _main_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./main.js */ "./js/main.js");
/* harmony import */ var _main_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_main_js__WEBPACK_IMPORTED_MODULE_2__);
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
 // Stylesheets

 // Scripts


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
})();

/******/ })()
;
//# sourceMappingURL=bundle.js.map