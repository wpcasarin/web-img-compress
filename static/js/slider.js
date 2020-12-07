document.addEventListener("DOMContentLoaded", function () {
  var slider = document.getElementById("slider");
  var output = document.getElementById("sliderValue");
  output.innerHTML = slider.value;

  slider.oninput = function () {
    output.innerHTML = this.value;
  };
});
