'use strict';

// navbar variables
const nav = document.querySelector('.mobile-nav');
const navMenuBtn = document.querySelector('.nav-menu-btn');
const navCloseBtn = document.querySelector('.nav-close-btn');


// navToggle function
const navToggleFunc = function () { nav.classList.toggle('active'); }

navMenuBtn.addEventListener('click', navToggleFunc);
navCloseBtn.addEventListener('click', navToggleFunc);



// theme toggle variables
const themeBtn = document.querySelectorAll('.theme-btn');


for (let i = 0; i < themeBtn.length; i++) {

  themeBtn[i].addEventListener('click', function () {

    // toggle `light-theme` & `dark-theme` class from `body`
    // when clicked `theme-btn`
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    for (let i = 0; i < themeBtn.length; i++) {

      // When the `theme-btn` is clicked,
      // it toggles classes between `light` & `dark` for all `theme-btn`.
      themeBtn[i].classList.toggle('light');
      themeBtn[i].classList.toggle('dark');

    }

  })

}





// links



const paragraphs = document.querySelectorAll('p');

paragraphs.forEach((paragraph) => {
  const text = paragraph.textContent;
  const linkRegex = /(https?:\/\/[^\s]+)/g;
  const links = text.match(linkRegex);

  if (links) {
    const linkElements = links.map((link) => {
      const linkElement = document.createElement('a');
      linkElement.href = link;
      linkElement.textContent = link;
      return linkElement;
    });

    linkElements.forEach((linkElement) => {
      const regex = new RegExp(linkElement.textContent, 'g');
      paragraph.innerHTML = paragraph.innerHTML.replace(regex, linkElement.outerHTML);
    });
  }
});




