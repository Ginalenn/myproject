// myapp/static/myapp/js/manage_records.js

$(document).ready(function() {

    // --- Custom Date Range Filtering Function ---
    $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex) {
            var min = $('#dateFromFilter').val();
            var max = $('#dateToFilter').val();
            // Use data from the 'Date From' column (index 3). Adjust if your column order changes.
            var date = data[3] || 0; 
            
            return (min === "" && max === "") || (min === "" && date <= max) || (min <= date && max === "") || (min <= date && date <= max);
        }
    );

    // --- Initialize the DataTable ---
    var table = $('#activities-table').DataTable({
        // Make the table responsive
        responsive: true,

        // Re-arrange the table controls for a cleaner look
        dom:  "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>" + // Length menu and global search
              "<'row'<'col-sm-12'tr>>" + // The table itself
              "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>" + // Info and pagination
              "<'row'<'col-sm-12 mt-3'B>>", // Buttons at the bottom

        // Configure the Buttons extension (Column Visibility, Export, etc.)
        buttons: [
            {
                extend: 'colvis',
                className: 'btn btn-outline-secondary btn-sm',
                text: '<i class="fa-solid fa-eye me-2"></i>Show/Hide Columns'
            },
            // You can add export buttons here if needed:
            // { extend: 'excel', className: 'btn btn-outline-success btn-sm', text: 'Export to Excel' }
        ],

        // Default sort by ID descending (newest first)
        "order": [[ 0, "desc" ]],

        // Define properties for specific columns
        "columnDefs": [
            { "orderable": false, "searchable": false, "targets": -1 }, // Disable sort/search on Actions column
            { "className": "text-center", "targets": 6 } // Center the 'Proof?' column content
        ]
    });

    // --- Link Filter Panel Controls to the DataTable ---
    function applyFilter(columnIndex, value, isExact = false) {
        table.column(columnIndex).search(isExact ? `^${value}$` : value, isExact, !isExact).draw();
    }
    
    $('#idFilter').on('keyup change', function() { applyFilter(0, this.value); });
    $('#titleFilter').on('keyup change', function() { applyFilter(1, this.value); });
    $('#strategyFilter').on('change', function() { applyFilter(2, this.value, true); });
    $('#fundingAgencyFilter').on('change', function() { applyFilter(5, this.value, true); });
    $('#proofFilter').on('change', function() { applyFilter(6, this.value, true); });
    $('#userFilter').on('change', function() { applyFilter(7, this.value, true); });
    $('#dateFromFilter, #dateToFilter').on('change', () => table.draw());

    // --- Clear All Filters Button ---
    $('#clearAllFiltersBtn').on('click', function() {
        $('#filters-panel input, #filters-panel select').val('');
        table.search('').columns().search('').draw();
    });

    // --- Handle Clicks on Action Buttons in the Dropdown ---
    $('#activities-table tbody').on('click', 'a.action-view', function() {
        var activityId = $(this).data('activity-id');
        alert('View Details for Activity ID: ' + activityId);
        // Here you would trigger a modal or navigate to a detail page
    });

    $('#activities-table tbody').on('click', 'a.action-edit', function() {
        var activityId = $(this).data('activity-id');
        alert('Edit Activity ID: ' + activityId);
        // Here you would navigate to the edit form for this activity
    });

    $('#activities-table tbody').on('click', 'a.action-delete', function() {
        var activityId = $(this).data('activity-id');
        if (confirm('Are you sure you want to delete Activity ID: ' + activityId + '?')) {
            alert('Deleting Activity ID: ' + activityId);
            // Here you would make an AJAX call to your Django delete view
        }
    });
});