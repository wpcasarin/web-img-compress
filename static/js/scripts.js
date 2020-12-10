document.addEventListener("DOMContentLoaded", function () {
  var slider = document.getElementById("slider");
  var output = document.getElementById("sliderValue");
  output.innerHTML = slider.value;

  slider.oninput = function () {
    output.innerHTML = this.value;
  };
});

function openBrowser() {
  document.getElementById("browserInput").click();
}

function getName() {
  let fileName = document.querySelector("input[type=file]").files[0].name;
  document.getElementById("inputFileName").innerHTML = fileName;
}
