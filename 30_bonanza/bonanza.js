//Team Worm Ooga - Team Worm Ooga - Dean Carey, Ethan Machleder, Jeffrey Huang
//SoftDev
//K30: JSorcery
//2021-05-14

//access canvas and buttons via DOM
var c =  document.getElementById("playground")// GET CANVAS
var startButton = document.getElementById("buttonStart") // GET START BUTTON
var stopButton = document.getElementById("buttonStop") // GET STOP BUTTON
var restartButton = document.getElementById("buttonRestart") // GET RESTART BUTTON
var ctx = c.getContext("2d");// YOUR CODE HERE

stopButton.disabled = true;
restartButton.disabled = true;

var loc = [500,500]; //location of snake head
var mv = [50,50]; //velocity

var snake = new Image();
snake.src = "snake.jpg";
snake.onload = function(){ctx.drawImage(snake,500,500,50,50)};

var apple = new Image();
apple.src = "apple.jpg";
apple.onload = function(){ctx.drawImage(apple,100,100,50,50)};

var runIt = () => {
  console.log("run invoked...")
  startButton.disabled = true;
  stopButton.disabled = false;
  restartButton.disabled = false;
  ctx.clearRect(loc[0],loc[1],100,100); // clears previous snake head
  loc = [loc[0]+mv[0],loc[1]]; //moving to left when starting
  if (loc[0] < 0 | loc[0] > 1000) {
    alert("You Died");
    restart();
    return;
  }
  if (loc[1] < 0 | loc[1] > 1000) {
    alert("You Died");
    restart();
    return;
  }
  ctx.drawImage(snake,loc[0],loc[1],50,50);
  requestID = window.requestAnimationFrame(runIt);
};

c.addEventListener('keydown', function(event) {
  const key = event.key; // "ArrowRight", "ArrowLeft", "ArrowUp", or "ArrowDown"

});


document.onkeydown = checkKey;
function checkKey(e) {
    e = e || window.event;
    if (e.keyCode == '38') { // up arrow

    }
    else if (e.keyCode == '40') { // down arrow

    }
    else if (e.keyCode == '37') { // left arrow

    }
    else if (e.keyCode == '39') { // right arrow

    }

}


var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    startButton.disabled = false;
    window.cancelAnimationFrame(requestID);
};

var restart = () => {
    console.log("restart invoked...")
    ctx.clearRect(0,0,1000,1000);
    ctx.drawImage(snake,500,500,50,50);
    ctx.drawImage(apple,100,100,50,50);
    startButton.disabled = false;
    stopButton.disabled = true;
    restartButton.disabled = true;
}


startButton.addEventListener( "click", runIt);
stopButton.addEventListener( "click", stopIt);
