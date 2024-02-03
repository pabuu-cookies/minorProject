function showProfileOptions() {
    var profileOptions = document.querySelector('.userProfileContainer .profileOptions');

    // Toggle the visibility of profileOptions
    if (profileOptions.style.display === 'block') {
        profileOptions.style.display = 'none';
    } else {
        profileOptions.style.display = 'block';
    }
}
function openFilterModal() {
    document.getElementById("filterModal").style.display = "flex";
}

// Close the modal
function closeFilterModal() {
    document.getElementById("filterModal").style.display = "none";
}

//APPLY FILTER-->GO
function applyFilters() {
    var filterMetadata = get_filter_metadata();  

    // Make an AJAX request to send the data to the backend using Fetch API
    fetch('/path/to/handle_filter_submission/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(filterMetadata),
    })
    .then(response => {
        if (!response.ok) {
            // Handle errors
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {//success reponse
        var successMessage = 'Adding result of ' + data.exam_type + ' batch: ' + data.batch_number + ', sem: ' + data.semester + ', faculty: ' + data.faculty;
        toastr.success(successMessage);
        console.log(successMessage);
        window.location.href = `/add_result.html?semester=${data.semester}&batch=${data.batch_number}&faculty=${data.faculty}&exam_type=${data.exam_type}`;

    })
    .catch(error => {
        console.error('Fetch error:', error);
        toastr.error('An error occurred. Please try again.');
        closeFilterModal() ;
    })
    .finally(() => {
        // Close the modal after sending the request
        closeFilterModal() ;
    });
}

// Function to open the course modal
function openCourseModal() {
     document.getElementById("courseModal").style.display = "flex";
}

// Function to close the course modal
function closeCourseModal() {
   document.getElementById("courseModal").style.display = "none";
}

//TO GET THE FILTER VALUES
function get_filter_metadata(){
    var faculty=document.getElementById('faculty').value;
    var semester=document.getElementById('semester').value;
    var examType=document.getElementById('type').value;
    var batchNumber=document.getElementById('batchNumber').value;

    return {
        faculty:faculty,
        semester:semester,
        exam_type:examType,
        batch_number:batchNumber
    };
}
        





