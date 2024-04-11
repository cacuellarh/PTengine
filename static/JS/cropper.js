setTimeout(function() {
    const load = document.getElementById("loader");
    const btn_capture = document.getElementById("capture")

    btn_capture.addEventListener("click", () => {
        load.classList.remove("hidden_loader");
    });

}, 500); // Ajusta el tiempo según sea necesario

