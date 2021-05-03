
var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
ctx.fillRect(50,50,100,200);
function doit() {
  ctx.clearRect(0,0,600,600);
  console.log("clicked clear");
}



function myFunction() {
  var x = document.getElementById("Toggle");
  if (x.innerHTML === "Hello") {
    x.innerHTML = "Swapped text!";
  } else {
    x.innerHTML = "Hello";
  }
}
