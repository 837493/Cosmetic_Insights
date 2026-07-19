// Cosmetic Insights — shared site behavior

document.addEventListener("DOMContentLoaded", () => {
  // Mobile nav toggle
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector("nav.links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      links.classList.toggle("open");
      const isOpen = links.classList.contains("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  // Highlight the active nav link based on current page
  const current = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.links a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === current) {
      a.classList.add("active");
    }
  });

  // Animate the hero mini bar chart on load, if present
  const bars = document.querySelectorAll(".mini-bars .bar");
  if (bars.length) {
    bars.forEach((bar, i) => {
      const target = bar.style.getPropertyValue("--target") || bar.style.height;
      bar.style.height = "0px";
      setTimeout(() => {
        bar.style.transition = "height 0.7s cubic-bezier(.2,.8,.2,1)";
        bar.style.height = target;
      }, 120 + i * 90);
    });
  }
});
