const navHTML = `
<nav class="nav" id="nav">
  <a href="index.html" class="nav-logo" data-h>
    <img src="images/logo-white-full.svg" alt="RVR Super Speciality Centre" class="nav-logo-img" style="height:48px;width:auto;">
  </a>
  <div class="nav-links">
    <a href="about.html" class="nav-link" data-h>About Us</a>
    <a href="our-care.html" class="nav-link" data-h>Our Care</a>
    <a href="specialists.html" class="nav-link" data-h>Our Specialists</a>
    <a href="spaces.html" class="nav-link" data-h>Spaces</a>
    <a href="welldesk.html" class="nav-link" data-h>Welldesk</a>
    <a href="reach-us.html" class="nav-link" data-h>Reach Us</a>
  </div>
  <button class="hamburger" aria-label="Menu" data-h><span class="bar"></span><span class="bar"></span><span class="bar"></span></button>
</nav>
<div class="mob-menu">
  <a href="index.html" class="nav-link" data-h>Home</a>
  <a href="about.html" class="nav-link" data-h>About Us</a>
  <a href="our-care.html" class="nav-link" data-h>Our Care</a>
  <a href="specialists.html" class="nav-link" data-h>Our Specialists</a>
  <a href="spaces.html" class="nav-link" data-h>Spaces</a>
  <a href="welldesk.html" class="nav-link" data-h>Welldesk</a>
  <a href="reach-us.html" class="nav-link" data-h>Reach Us</a>
</div>
`;

const navPlaceholder = document.getElementById('nav-placeholder');
if (navPlaceholder) {
  navPlaceholder.innerHTML = navHTML;
} else {
  document.body.insertAdjacentHTML('afterbegin', navHTML);
}

const currentPath = (location.pathname.split('/').pop() || 'index.html').split('?')[0];
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
  link.classList.remove('active');
  const href = link.getAttribute('href');
  if (href === currentPath || (currentPath === '' && href === 'index.html')) {
    link.classList.add('active');
  }
});

const logoImg = document.querySelector('.nav-logo-img');

if (logoImg) {
  let isChanged = false;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50 && !isChanged) {
      logoImg.src = 'images/RVR-Logo-Green-Full_logo.png';
      isChanged = true;
    } else if (window.scrollY <= 50 && isChanged) {
      logoImg.src = 'images/logo-white-full.svg';
      isChanged = false;
    }
  });
}

console.log(logoImg.src)