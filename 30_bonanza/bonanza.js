//Team Worm Ooga - Dean Carey Ethan Machleder Jeffrey Huang
//SoftDev
//K30: JSorcery
//2021-05-14

//access canvas and buttons via DOM
var c =  document.getElementById("playground")// GET CANVAS
var startButton = document.getElementById("buttonStart") // GET START BUTTON
var stopButton = document.getElementById("buttonStop") // GET STOP BUTTON

var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "blue"; // YOUR CODE HERE

var loc = [500,500];
var mv = [100,100];

var logo = new Image();
logo.src = "snake.jpg";
logo.onload = function(){ctx.drawImage(logo,500,500,100,100)};


var runIt = () => {
  console.log("run invoked...")
  startButton.disabled = true;
  loc = [loc[0]+mv[0],loc[1]]; //moving to left originally
  ctx.drawImage(logo,loc[0],loc[1],100,100);
  requestID = window.requestAnimationFrame(dvdIt);
};

c.addEventListener('keydown', function(event) {
  const key = event.key; // "ArrowRight", "ArrowLeft", "ArrowUp", or "ArrowDown"
    if (loc[1] == 0 | loc[1] == 420) {
      alert("You Died");
      console.log("clear invoked...")
      ctx.clearRect(0,0,1000,1000);
    }
});

var stopIt = () => {
    console.log("stopIt invoked...")
    console.log( requestID );
    startButton.disabled = false;
    dvdButton.disabled = false;
    window.cancelAnimationFrame(requestID);
};


startButton.addEventListener( "click", runIt);
stopButton.addEventListener( "click", stopIt);
