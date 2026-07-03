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