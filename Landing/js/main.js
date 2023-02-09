const button = document.querySelector(".navbar__ham");
const menu = document.querySelector(".navbar__links");
const overlay = document.querySelector("#overlay");

button.addEventListener("click", () => {
  button.classList.toggle("open");
  menu.classList.toggle("navbar__open");
  overlay.classList.toggle("show");
});

overlay.addEventListener("click", () => {
  overlay.classList.toggle("show");
  button.classList.toggle("open");
  menu.classList.toggle("navbar__open");
});






const btns = document.querySelectorAll("[data-target]");
const close_modals = document.querySelectorAll(".close-modal");
const overlay2 = document.getElementById("overlay2");

btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelector(btn.dataset.target).classList.add("active");
    overlay2.classList.add("active");
  });
});

close_modals.forEach((btn) => {
  btn.addEventListener("click", () => {
    const modal = btn.closest(".modal");
    modal.classList.remove("active");
    overlay2.classList.remove("active");
  });
});

window.onclick = (event) => {
  if (event.target == overlay2) {
    const modals = document.querySelectorAll(".modal");
    modals.forEach((modal) => modal.classList.remove("active"));
    overlay2.classList.remove("active");
  }
};



//Get form element
var form=document.getElementById("login");
function submitForm(event){

   //Preventing page refresh
   event.preventDefault();
}

//Calling a function during form submission.
form.addEventListener('submit', submitForm);