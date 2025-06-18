document.addEventListener('DOMContentLoaded', function() {
    const tableContentWrapper = document.getElementById('table-content-wrapper');
    const filterForm = document.getElementById('filter-form');
    const searchBox = document.getElementById('customSearchBox');
    let searchTimeout;

    // The core function to fetch and update the table
    const updateTable = () => {
        // Show a loading indicator
        tableContentWrapper.innerHTML = '<div class="d-flex justify-content-center align-items-center p-5"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>';
        
        const formData = new FormData(filterForm);
        const params = new URLSearchParams(formData);
        
        // Add search term to parameters
        if (searchBox.value) {
            params.append('search', searchBox.value);
        }

        const url = `/records/?${params.toString()}`;
        
        fetch(url, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.text())
        .then(html => {
            tableContentWrapper.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching table data:', error);
            tableContentWrapper.innerHTML = '<div class="alert alert-danger">Failed to load data. Please try again.</div>';
        });
    };

    // --- Event Listeners ---

    // Handle form submission (clicking the "Apply" button)
    filterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        updateTable();
    });
    
    // Handle real-time search with debouncing to avoid excessive requests
    searchBox.addEventListener('keyup', () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            updateTable();
        }, 500); // Wait 500ms after user stops typing
    });

    // Handle pagination clicks using event delegation
    tableContentWrapper.addEventListener('click', (e) => {
        if (e.target.matches('.page-link') && e.target.dataset.page) {
            e.preventDefault();
            const page = e.target.dataset.page;
            
            // Get current filters and append the new page number
            const formData = new FormData(filterForm);
            const params = new URLSearchParams(formData);
            if (searchBox.value) {
                params.append('search', searchBox.value);
            }
            params.set('page', page); // Set the clicked page number

            const url = `/records/?${params.toString()}`;
            
            // Fetch the specific page
            fetch(url, { headers: {'X-Requested-With': 'XMLHttpRequest'} })
                .then(response => response.text())
                .then(html => tableContentWrapper.innerHTML = html);
        }

        // Handle delete button click
        if (e.target.closest('.btn-outline-danger[data-id]')) {
             const deleteButton = e.target.closest('.btn-outline-danger[data-id]');
             const activityId = deleteButton.dataset.id;
             if (confirm(`Are you sure you want to delete activity #${activityId}?`)) {
                 // In a real app, you would send a DELETE request here
                 alert(`DELETE request for activity ${activityId} would be sent here.`);
                 // Example: fetch(`/api/activity/${activityId}`, { method: 'DELETE' }).then(() => updateTable());
             }
        }
    });
});