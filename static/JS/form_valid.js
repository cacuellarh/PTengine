
window.onload = () => {

    const btn_capture = document.getElementById("capture");
    const url_input = document.getElementById("url_input");
    btn_capture.disabled = true;


    url_input.addEventListener("keyup", () => {
        var value = url_input.value;

        if (value !== "") {
            btn_capture.disabled = false;

        } else {
            btn_capture.disabled = true;
            btn_capture.classList.remove("disabled")
        }
    });
};