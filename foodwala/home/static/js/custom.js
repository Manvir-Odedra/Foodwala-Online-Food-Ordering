$(function () {
  // Main Menu JS
  $(window).scroll(function () {
    if ($(this).scrollTop() < 50) {
      $("nav").removeClass("site-top-nav");
      $("#back-to-top").fadeOut();
    } else {
      $("nav").addClass("site-top-nav");
      $("#back-to-top").fadeIn();
    }
  });

  // Shopping Cart Toggle JS
  $("#shopping-cart").on("click", function () {
    $("#cart-content").toggle("blind", "", 500);
  });

  // Back-To-Top Button JS
  $("#back-to-top").click(function (event) {
    event.preventDefault();
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  });

  // Delete Cart Item JS
  $(document).on("click", ".btn-delete", function (event) {
    event.preventDefault();
    $(this).closest("tr").remove();
    updateTotal();
  });

  // Update Total Price JS
  function updateTotal() {
    let total = 0;
    $("#cart-content tr").each(function () {
      const rowTotal = parseFloat($(this).find("td:nth-child(5)").text().replace("$", ""));
      if (!isNaN(rowTotal)) {
        total += rowTotal;
      }
    });
    $("#cart-content th:nth-child(5)").text("$" + total.toFixed(2));
    $(".tbl-full th:nth-child(6)").text("$" + total.toFixed(2));
  }

  // Cart Increment / Decrement (using jQuery)
  $(".quantity-selector").each(function () {
    const input = $(this).find(".qty-input");
    const btnPlus = $(this).find(".plus");
    const btnMinus = $(this).find(".minus");

    btnPlus.on("click", function () {
      input.val(parseInt(input.val()) + 1);
    });

    btnMinus.on("click", function () {
      if (parseInt(input.val()) > 1) {
        input.val(parseInt(input.val()) - 1);
      }
    });
  });
});

// Carousel Logic (vanilla JS)
const track = document.querySelector(".carousel-track");
const reviews = document.querySelectorAll(".review");
const reviewWidth = 340; // 320px + margins
const visibleCount = 3; // Show 3 at a time
let index = 0;

// Clone first few reviews and append them to the end
for (let i = 0; i < visibleCount; i++) {
  const clone = reviews[i].cloneNode(true);
  track.appendChild(clone);
}

// Start auto sliding
setInterval(() => {
  index++;

  // Animate the slide
  track.style.transition = 'transform 0.5s ease-in-out';
  track.style.transform = `translateX(-${index * reviewWidth}px)`;

  // When reaching the clones, reset back to real start instantly
  if (index === reviews.length) {
    setTimeout(() => {
      track.style.transition = 'none';
      track.style.transform = 'translateX(0px)';
      index = 0;
    }, 500);
  }
}, 1200);
