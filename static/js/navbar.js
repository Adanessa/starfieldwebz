window.onscroll = function() { 
    var navbar = document.getElementById("navbar");
    var sticky = navbar.offsetTop;

    if (window.scrollY >= sticky) {
        navbar.classList.add("sticky");
    } else {
        navbar.classList.remove("sticky");
    }
};