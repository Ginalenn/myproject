
  document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("side_nav");
    const collapseBtn = document.getElementById("collapse-btn");
    const mobileCloseBtn = document.getElementById("mobile-close-btn");
    const navLinks = sidebar.querySelectorAll(".nav-link");

    // Animate sidebar toggle
    collapseBtn.addEventListener("click", function () {
      sidebar.classList.toggle("collapsed");
      collapseBtn.querySelector("i").classList.toggle("fa-angle-left");
      collapseBtn.querySelector("i").classList.toggle("fa-angle-right");
    });

    // Handle active button styling
    navLinks.forEach(link => {
      link.addEventListener("click", function () {
        navLinks.forEach(l => l.classList.remove("active"));
        this.classList.add("active");
      });
    });

    // Mobile close
    if (mobileCloseBtn) {
      mobileCloseBtn.addEventListener("click", function () {
        sidebar.classList.remove("show");
      });
    }
  });

