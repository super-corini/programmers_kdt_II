document.querySelector("body").addEventListener("click", function (e) {
  console.log(e);
  if (e.target.className == "info") {
    console.log(e.target);
    e.target.nextElementSibling.classList.toggle("hide");
  }
});
