const navToggle = document.getElementById("nav-toggle");
const navClose = document.getElementById("nav-close");
const navMenu = document.getElementById("nav-menu");

if (navToggle) {
    navToggle.addEventListener("click", () => {
        navMenu.classList.add("active")
        console.log("clicked")

    });
}
if (navClose) {
    navClose.addEventListener("click", () => {
        console.log("clicked")
        navMenu.classList.remove("active")

    })

}

// const addToCartButton = document.getElementsByName(".add-cart-button");
// addToCartButton.addEventListener('click', function () {
//     console.log("clicked")
//     addToCartButton.classList.add('shake');
//
//     setTimeout(function () {
//         addToCartButton.classList.remove('shake');
//     }, 500);
// });