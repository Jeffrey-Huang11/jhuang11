
var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
ctx.fillRect(50,50,100,200);

//clears the canvas
function doit() {
  ctx.clearRect(0,0,600,600);
  console.log("clicked clear");
}

//toggles rectangle or dot draw mode if mouse within canvas
function no() {
  var x = document.getElementById("Toggle");
  if (x.innerHTML === "Hello") {
    x.innerHTML = "Rectangle Mode";
  } else {
    x.innerHTML = "Dot Mode";
  }
}
