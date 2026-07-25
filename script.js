// Theme toggle (light by default; choice persisted). Initial theme is applied
// by a tiny inline script in <head> to avoid a flash of the wrong theme.
const themeBtn = document.getElementById('themeToggle');
if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.getAttribute('data-theme') === 'dark';
    if (dark) { root.removeAttribute('data-theme'); }
    else { root.setAttribute('data-theme', 'dark'); }
    try { localStorage.setItem('theme', dark ? 'light' : 'dark'); } catch (e) {}
    themeBtn.setAttribute('aria-pressed', String(!dark));
  });
}

// Nav: blur background once scrolled
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile nav toggle (with aria state)
const toggle = document.getElementById('navToggle');
const links = document.getElementById('navLinks');
toggle.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
});
links.querySelectorAll('a').forEach(a =>
  a.addEventListener('click', () => {
    links.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  })
);

// Projects dropdown (click to toggle; also opens on hover/focus via CSS)
const projDd = document.querySelector('.nav-dd');
if (projDd) {
  const projBtn = projDd.querySelector('.nav-dd-btn');
  projBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = projDd.classList.toggle('open');
    projBtn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', (e) => {
    if (!projDd.contains(e.target)) {
      projDd.classList.remove('open');
      projBtn.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      projDd.classList.remove('open');
      projBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

// Scroll-reveal (skipped when the user prefers reduced motion)
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduce && 'IntersectionObserver' in window) {
  const targets = document.querySelectorAll('.card, .svc, .stack-col, .pub, .profile-text, .profile-photo, .loop-panel');
  targets.forEach(el => el.classList.add('reveal'));
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  targets.forEach(el => io.observe(el));
}

// Footer year
document.getElementById('year').textContent = new Date().getFullYear();
