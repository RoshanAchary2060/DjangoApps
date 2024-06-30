function showDate() {
  var today = new Date();
  var para = document.querySelector("p");
  para.innerHTML = today.toString();
}
