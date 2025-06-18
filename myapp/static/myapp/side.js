document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("side_nav");
    const collapseBtn = document.getElementById("collapse-btn"); // Desktop collapse button
    const mobileMenuBtn = document.getElementById("mobile-menu-btn"); // Mobile open button
    const mainContent = document.querySelector('.main-content-wrapper');

    // Make sure the elements exist before adding listeners
    if (!sidebar) {
        console.error("Sidebar element with ID 'side_nav' not found.");
        return;
    }

    // --- Desktop Sidebar Collapse/Expand ---
    if (collapseBtn && mainContent) {
        collapseBtn.addEventListener("click", function () {
            // Toggle classes on both the sidebar and the main content wrapper
            sidebar.classList.toggle("collapsed");
            mainContent.classList.toggle("collapsed");

            // Animate the collapse button icon
            const icon = collapseBtn.querySelector("i");
            if (icon) {
                icon.classList.toggle("fa-angles-left");
                icon.classList.toggle("fa-angles-right");
            }
        });
    }

    // --- Mobile Sidebar Show/Hide ---
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", function () {
            sidebar.classList.add("sidebar-show");
        });
    }

    // --- Close Mobile Sidebar when clicking outside of it ---
    // This adds an overlay to the page for a better user experience
    document.addEventListener('click', function(event) {
        if (sidebar.classList.contains('sidebar-show') && !sidebar.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
            sidebar.classList.remove('sidebar-show');
        }
    });

});