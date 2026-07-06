document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("customerSearch");

    const rows = document.querySelectorAll("tbody tr");

    input.addEventListener("keyup", () => {

        const value = input.value.toLowerCase();

        rows.forEach(row => {

            row.style.display =
                row.innerText.toLowerCase().includes(value)
                ? ""
                : "none";

        });

    });

});
// =======================
// window.addEventListener("load", function () {
//     document.getElementById("loader").style.display = "none";
// });
// =======================

const topBtn = document.getElementById("topBtn");

window.addEventListener("scroll", function () {

    if(window.scrollY > 200){
        topBtn.style.display = "block";
    }else{
        topBtn.style.display = "none";
    }

});

topBtn.addEventListener("click", function () {

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

});