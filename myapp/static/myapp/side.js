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