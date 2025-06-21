document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('side_nav');
    const content = document.querySelector('.content'); // Assuming your main content has this class
    const toggleBtn = document.getElementById('sidebar_toggle');
    let tooltipInstances = [];

    if (!sidebar || !content || !toggleBtn) {
        console.error("Sidebar components not found. Interactivity will be limited.");
        return;
    }
    
    // Function to enable tooltips on collapsed sidebar
    const enableTooltips = () => {
        const tooltipTriggerList = [].slice.call(sidebar.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipInstances = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl, {
                trigger: 'hover' // Show tooltip on hover
            });
        });
    };

    // Function to disable and destroy existing tooltips
    const disableTooltips = () => {
        tooltipInstances.forEach(tooltip => tooltip.dispose());
        tooltipInstances = [];
    };
    
    const setSidebarState = (isCollapsed) => {
        if (isCollapsed) {
            sidebar.classList.add('collapsed');
            content.classList.add('expanded');
            localStorage.setItem('sidebarCollapsed', 'true');
            enableTooltips(); // Activate tooltips
        } else {
            sidebar.classList.remove('collapsed');
            content.classList.remove('expanded');
            localStorage.setItem('sidebarCollapsed', 'false');
            disableTooltips(); // Deactivate tooltips
        }
    };

    // Check for saved state on page load
    const isInitiallyCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    setSidebarState(isInitiallyCollapsed);

    // Add click event listener to the toggle button
    toggleBtn.addEventListener('click', function() {
        const currentState = sidebar.classList.contains('collapsed');
        setSidebarState(!currentState);
    });
});


// myapp/static/myapp/js/side.js (Upgraded for Full Responsiveness)

document.addEventListener('DOMContentLoaded', function() {
    // --- Get all necessary elements ---
    const sidebar = document.getElementById('side_nav');
    const content = document.getElementById('main_content'); // Use ID for reliability
    const toggleBtn = document.getElementById('sidebar_toggle');
    const overlay = document.getElementById('sidebar_overlay');
    
    // Check if essential elements exist
    if (!sidebar || !content || !toggleBtn || !overlay) {
        console.error("A required element for sidebar interactivity is missing.");
        return;
    }

    let desktopTooltipInstances = [];
    const mobileBreakpoint = 991.98;

    // --- Desktop-specific functions ---
    const enableDesktopTooltips = () => {
        const tooltipTriggerList = [].slice.call(sidebar.querySelectorAll('[data-bs-toggle="tooltip"]'));
        desktopTooltipInstances = tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, { trigger: 'hover' }));
    };

    const disableDesktopTooltips = () => {
        desktopTooltipInstances.forEach(tooltip => tooltip.dispose());
        desktopTooltipInstances = [];
    };
    
    const setDesktopSidebarState = (isCollapsed) => {
        if (isCollapsed) {
            sidebar.classList.add('collapsed');
            content.classList.add('expanded');
            localStorage.setItem('sidebarCollapsed', 'true');
            enableDesktopTooltips();
        } else {
            sidebar.classList.remove('collapsed');
            content.classList.remove('expanded');
            localStorage.setItem('sidebarCollapsed', 'false');
            disableDesktopTooltips();
        }
    };
    
    // --- Mobile-specific function ---
    const toggleMobileSidebar = () => {
        const isOpen = sidebar.classList.toggle('is-open');
        overlay.classList.toggle('is-visible', isOpen);
    };

    // --- Main Event Listener for the Toggle Button ---
    toggleBtn.addEventListener('click', function() {
        if (window.innerWidth > mobileBreakpoint) {
            // It's a desktop - perform collapse/expand
            const currentState = sidebar.classList.contains('collapsed');
            setDesktopSidebarState(!currentState);
        } else {
            // It's a mobile device - perform slide in/out
            toggleMobileSidebar();
        }
    });

    // --- Event listener for the overlay to close the sidebar ---
    overlay.addEventListener('click', toggleMobileSidebar);

    // --- Initial setup on page load ---
    const initializeSidebar = () => {
        // Only apply the desktop collapsed state if we are on a desktop
        if (window.innerWidth > mobileBreakpoint) {
            const isInitiallyCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
            setDesktopSidebarState(isInitiallyCollapsed);
        } else {
            // On mobile, ensure desktop tooltips are off and desktop classes are clean
            disableDesktopTooltips();
            sidebar.classList.remove('collapsed');
            content.classList.remove('expanded');
        }
    };

    // Run the initial setup
    initializeSidebar();

    // Add a resize listener to handle transitions between mobile and desktop views
    window.addEventListener('resize', () => {
        // If resizing from mobile to desktop, clean up mobile classes
        if (window.innerWidth > mobileBreakpoint) {
            sidebar.classList.remove('is-open');
            overlay.classList.remove('is-visible');
        }
        // Re-initialize to apply the correct state for the new screen size
        initializeSidebar();
    });
});