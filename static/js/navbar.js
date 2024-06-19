window.onscroll = function() { 
    myFunction();
};
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.scrollY >= sticky) {
        navbar.classList.add("sticky");
        document.body.style.paddingTop = navbar.offsetHeight + 'px';
    } else {
        navbar.classList.remove("sticky");
        document.body.style.paddingTop = '0'
    }

    if (window.scrollYOffset === 0) {
        navbar.classList.remove("sticky");
    }
};
