document.addEventListener("DOMContentLoaded", function () {
  var chips = document.querySelectorAll(".chip");
  var cards = document.querySelectorAll(".card");

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      chips.forEach(function (c) { c.classList.remove("active"); });
      chip.classList.add("active");

      var filter = chip.getAttribute("data-filter");

      cards.forEach(function (card) {
        var category = card.getAttribute("data-category");
        var show = filter === "all" || filter === category;
        card.style.display = show ? "" : "none";
      });
    });
  });
});
