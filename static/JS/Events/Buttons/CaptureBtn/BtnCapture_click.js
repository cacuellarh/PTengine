import { OpenLoader } from "../../Loader/LoaderOpen.js";
const btn_capture = document.getElementById("capture");
const UrlInput = document.getElementById("url_input");
BtnCapture_Click(OpenLoader);

function BtnCapture_Click(handdle) {
  btn_capture.addEventListener("click", () => {
    if (UrlInput.value != "") {
      handdle();
    } else {
      alert("Por favor Ingrese una URL.");
    }
  });
}
