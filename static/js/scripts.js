const hide_buttons = document.querySelectorAll('.hide_button');
console.log(hide_buttons)
hide_buttons.forEach(button =>{
  button.addEventListener('click', event => {
    hideBreakfast(event.target.id)
  })
})

function hideBreakfast(id) {
  var x, btn;
  if (id === "breakfast_btn") {
    x = document.getElementById("breakfast");
    btn = document.getElementById("breakfast_btn");
  }
  else if (id === "2nd_breakfast_btn"){
    x = document.getElementById("second_breakfast");
    btn = document.getElementById("2nd_breakfast_btn");
  }
  else if (id === "lunch_btn"){
    x = document.getElementById("lunch");
    btn = document.getElementById("lunch_btn");
  }
  else if (id === "snack_btn"){
    x = document.getElementById("snack");
    btn = document.getElementById("snack_btn");
  }
  else if (id === "supper_btn"){
    x = document.getElementById("supper");
    btn = document.getElementById("supper_btn");
  }

  if (x.style.display === "none") {
    btn.innerHTML = "+";
    x.style.display = "table"
  } else {
    btn.innerHTML = "-";
    x.style.display = "none";
  }
}