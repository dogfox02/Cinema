let slideIndex = 0;
let leftButton = document.querySelector(".left-button");
let rightButton = document.querySelector(".right-button");
let slides = document.querySelectorAll(".carousel-item");
let timerID;

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showTimeSlides() {
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showTimeSlides, 4000); 
}

function showSlides(n) {
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

leftButton.onclick = function() {
  plusSlides(-1);
}

rightButton.onclick = function() {
  plusSlides(1);
}

showTimeSlides();

