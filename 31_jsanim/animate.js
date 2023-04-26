var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "green";

var requestID;

var clear = (e) => {
  ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
  window.cancelAnimationFrame(requestID);

  clear();
  ctx.beginPath();
  ctx.arc(250, 250, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();

  if (growing) {
    radius++;
  }
  if (!growing) {
    radius--;
  }
  if (radius == 250) {
    growing = false;
  }
  if (radius == 0) {
    growing = true;
  }

  requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
  console.log("stopIt invoked...");
  console.log(requestID);

  window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
