// Navbar Animation
window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".custom-navbar");

    if(window.scrollY>40){

        navbar.style.boxShadow="0 10px 30px rgba(0,0,0,.08)";

        navbar.style.padding="12px 0";

    }

    else{

        navbar.style.boxShadow="none";

        navbar.style.padding="18px 0";

    }

});