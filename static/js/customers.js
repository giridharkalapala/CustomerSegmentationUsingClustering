document.addEventListener("DOMContentLoaded",()=>{

const modal=new bootstrap.Modal(document.getElementById("customerModal"));

document.querySelectorAll(".viewCustomer").forEach(btn=>{

btn.onclick=()=>{

document.getElementById("modalID").innerHTML=btn.dataset.id;
document.getElementById("modalGender").innerHTML=btn.dataset.gender;
document.getElementById("modalAge").innerHTML=btn.dataset.age;
document.getElementById("modalIncome").innerHTML="$"+btn.dataset.income;
document.getElementById("modalSpending").innerHTML=btn.dataset.spending;
document.getElementById("modalSegment").innerHTML=btn.dataset.segment;

modal.show();

};

});

});