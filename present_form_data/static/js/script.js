function goBack() {                 // this is for the goBack button on the results page 
    window.history.back();
}

$(document).ready(function () {         // this is jquery for the checkboxes on the index page. When #submit is clicked, if none of the checkboxes
    $('#submit').click(function() {     // ... are checked, then give alert
    checked = $("input[type=checkbox]:checked").length;

    if(!checked) {
        alert("You must check at least one checkbox.");
        return false;
    }

    });
});