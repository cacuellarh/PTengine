setTimeout(function() {

    document.querySelector('.close').addEventListener('click', function() {
        var helpUsForm = document.getElementById('help_us_form');
        helpUsForm.classList.add('disabled');
    });
}, 500);