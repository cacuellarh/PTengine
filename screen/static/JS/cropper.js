setTimeout(function() {
    const load = document.getElementById("loader");
    const btn_capture = document.getElementById("capture")

    btn_capture.addEventListener("click", () => {
        load.classList.remove("hidden_loader");
    });

    document.querySelector('.close').addEventListener('click', function() {
        var helpUsForm = document.getElementById('help_us_form');
        helpUsForm.classList.add('disabled');
    });
}, 500); // Ajusta el tiempo según sea necesario