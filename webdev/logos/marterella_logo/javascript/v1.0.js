function runAnimation() {
  // Set up the canvas
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  canvas.width = 400;
  canvas.height = 400;
  
  // Define the dots
  var dots = [
    { x: 50, y: 50 },
    { x: 350, y: 50 },
    { x: 350, y: 350 },
    { x: 50, y: 350 }
  ];
  
  // Define the animation parameters
  var duration = 1000; // Duration of the animation in milliseconds
  var start = null; // Start time of the animation
  
  // Define the animation function
  function animate(timestamp) {
    if (!start) start = timestamp;
    var progress = timestamp - start;
    if (progress > duration) progress = duration;
    
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw the dots
    ctx.fillStyle = "black";
    dots.forEach(function(dot) {
      var x = dot.x + ((canvas.width / 2 - dot.x) * progress / duration);
      var y = dot.y + ((canvas.height / 2 - dot.y) * progress / duration);
      ctx.beginPath();
      ctx.arc(x, y, 5, 0, 2 * Math.PI);
      ctx.fill();
    });
    
    // Request the next animation frame
    if (progress < duration) {
      requestAnimationFrame(animate);
    }
  }

  // Change the text at the top
  textBox.innerHTML = "Running Animation";
  
  // Start the animation
  requestAnimationFrame(animate);

  // Change the text at the top
  textBox.innerHTML = "Animation Complete";
}
