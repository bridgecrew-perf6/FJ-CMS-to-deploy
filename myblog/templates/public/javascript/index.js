const hero_swiper = new Swiper(".hero_swiper", {
  loop: true,
  effect: "fade",
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".Hero .next_btn",
    prevEl: ".Hero .prev_btn",
  },
});

const blog_swiper = new Swiper(".blog_swiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".Blogs .next_btn",
    prevEl: ".Blogs .prev_btn",
  },
  breakpoints: {
    992: {
      slidesPerView: 3,
    },
    768: {
      slidesPerView: 2,
    },
  },
});

const destination_swiper = new Swiper(".destination_swiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".Destinations .next_btn",
    prevEl: ".Destinations .prev_btn",
  },
});

function toggleActiveClass(el) {
  const target = document.querySelector(el).classList;
  return target.toggle("active");
}

const header_links = document.querySelectorAll(".Header .middle a");

header_links.forEach((el) => {
  el.addEventListener("click", function () {
    header_links.forEach((el) => el.children[0].classList.remove("active"));
    this.children[0].classList.add("active");
  });
});

const product_nav_tab = document.querySelectorAll(
  ".Product .nav_tab .nav_item"
);

product_nav_tab.forEach((el) => {
  el.addEventListener("click", function () {
    product_nav_tab.forEach((el) => el.classList.remove("active"));
    this.classList.add("active");
  });
});

const quantity_btn = document.querySelectorAll(".quantity_btn i");
const quantity_input = document.querySelector(".quantity_btn > input");

quantity_btn.length > 0 &&
  quantity_btn[0].addEventListener("click", inputIncrement);
quantity_btn.length > 0 &&
  quantity_btn[1].addEventListener("click", inputDecrement);

function inputIncrement() {
  quantity_input.value = +quantity_input.value + 1;
}

function inputDecrement() {
  if (quantity_input.value > 1)
    quantity_input.value = +quantity_input.value - 1;
}

try {
  class dualRangeSlider {
    constructor(rangeElement) {
      this.range = rangeElement;
      this.min = Number(rangeElement.dataset.min);
      this.max = Number(rangeElement.dataset.max);
      this.handles = [...this.range.querySelectorAll(".handle")];
      this.priceLabelFrom = document.querySelector(
        ".dual-range-price-label .from"
      );
      this.priceLabelTo = document.querySelector(".dual-range-price-label .to");
      this.startPos = 0;
      this.activeHandle;

      this.handles.forEach((handle) => {
        handle.addEventListener("mousedown", this.startMove.bind(this));
        handle.addEventListener("touchstart", this.startMoveTouch.bind(this));
      });

      window.addEventListener("mouseup", this.stopMove.bind(this));
      window.addEventListener("touchend", this.stopMove.bind(this));
      window.addEventListener("touchcancel", this.stopMove.bind(this));
      window.addEventListener("touchleave", this.stopMove.bind(this));

      const rangeRect = this.range.getBoundingClientRect();
      const handleRect = this.handles[0].getBoundingClientRect();
      this.range.style.setProperty("--x-1", "0px");
      this.range.style.setProperty(
        "--x-2",
        rangeRect.width - handleRect.width / 2 + "px"
      );
      this.handles[0].dataset.value = this.range.dataset.min;
      this.handles[1].dataset.value = this.range.dataset.max;
      this.priceLabelFrom.innerHTML = this.formatNumber(this.range.dataset.min);
      this.priceLabelTo.innerHTML = this.formatNumber(this.range.dataset.max);
    }

    startMoveTouch(e) {
      const handleRect = e.target.getBoundingClientRect();
      this.startPos = e.touches[0].clientX - handleRect.x;
      this.activeHandle = e.target;
      this.moveTouchListener = this.moveTouch.bind(this);
      window.addEventListener("touchmove", this.moveTouchListener);
    }

    startMove(e) {
      this.startPos = e.offsetX;
      this.activeHandle = e.target;
      this.moveListener = this.move.bind(this);
      window.addEventListener("mousemove", this.moveListener);
    }

    moveTouch(e) {
      this.move({ clientX: e.touches[0].clientX });
    }

    move(e) {
      const isLeft = this.activeHandle.classList.contains("left");
      const property = isLeft ? "--x-1" : "--x-2";
      const parentRect = this.range.getBoundingClientRect();
      const handleRect = this.activeHandle.getBoundingClientRect();
      let newX = e.clientX - parentRect.x - this.startPos;
      if (isLeft) {
        const otherX = parseInt(this.range.style.getPropertyValue("--x-2"));
        newX = Math.min(newX, otherX - handleRect.width);
        newX = Math.max(newX, 0 - handleRect.width / 2);
        this.priceLabelFrom.innerHTML = this.formatNumber(
          this.calcHandleValue((newX + handleRect.width / 2) / parentRect.width)
        );
      } else {
        const otherX = parseInt(this.range.style.getPropertyValue("--x-1"));
        newX = Math.max(newX, otherX + handleRect.width);
        newX = Math.min(newX, parentRect.width - handleRect.width / 2);
        this.priceLabelTo.innerHTML = this.formatNumber(
          this.calcHandleValue((newX + handleRect.width / 2) / parentRect.width)
        );
      }
      this.activeHandle.dataset.value = this.calcHandleValue(
        (newX + handleRect.width / 2) / parentRect.width
      );
      this.range.style.setProperty(property, newX + "px");
    }

    calcHandleValue(percentage) {
      return Math.round(percentage * (this.max - this.min) + this.min);
    }

    formatNumber(number) {
      return new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      }).format(number);
    }

    stopMove() {
      window.removeEventListener("mousemove", this.moveListener);
      window.removeEventListener("touchmove", this.moveTouchListener);
    }
  }

  document.querySelector(".dual-range") &&
    new dualRangeSlider(document.querySelector(".dual-range"));
} catch (error) {
  console.log(error);
}
