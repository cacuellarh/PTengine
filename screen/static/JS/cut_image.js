//const base_url = "http://127.0.0.1:8000/"
const base_url = "https://trackmyprice.co/"


document.addEventListener("DOMContentLoaded", function() {
    // Selecciona la imagen y el contenedor
    const image = document.getElementById("image_capture");
    const container = document.querySelector(".cut_seccion");

    // Espera a que se cargue completamente la imagen
    image.onload = function() {

        const cropper = new Cropper(image, {
            aspectRatio: 1,  // Proporción de aspecto (puedes ajustar según tus necesidades)
            viewMode: 0,
            zoomOnWheel: true,
            guides: false
        });

        cropper.setCropBoxData({
            width: 20,
            height: 20
        });
    };
});
//1 - Boton para cortar precio
const btn = document.getElementById("btn_cropp")
// 1.1 Modal confirmacion de precio
const modal_price_confirm = document.getElementById("notification_wrapper_id")
// 1.2 h4 mostrar precio escaneado
const price_scan = document.getElementById("price_scan")
// 1.3 h4 mostrar precio escaneado
const btn_cancel_modalprice = document.getElementById("cancel_modalprice")
// 1.4 h4 mostrar precio escaneado
const btn_confirm_modalprice = document.getElementById("confirm_modalprice")

const save_cut = document.getElementById("save_cut")
const btn_send = document.getElementById("send_form")
const btn_capture = document.getElementById("capture")
const image = document.getElementById("image_capture")
const email = document.getElementById("email")
const frequency = document.getElementById("frequency")
let description = document.getElementById("description")
//Modal, Envio de token a email
const modal_confirm = document.getElementById("modal_email_confirm")
let data_form
let price_check = false

//Lista de validaciones
let validations_form = {

    email_required : false,
    email_check : false,
    price_check : false,
    price_as_number : false
}
const cropper = new  Cropper(image, {
    aspectRatio: 0,  // Proporción de aspecto (puedes ajustar según tus necesidades)
    viewMode: 3,
    zoomOnWheel: false

})

const moveYT = document.getElementById("moveY-T")
const moveYB = document.getElementById("moveY-B")
const moveXL = document.getElementById("moveX-L")
const moveXR = document.getElementById("moveX-R")
const zoom_up = document.getElementById("zoom+")
const zoom_down = document.getElementById("zoom-")
const url_input = document.getElementById("url_")
const email_valid = document.getElementById("email_valid")

//loader
const load = document.getElementById("loader");

//funciones estado de loader

function modal_loader_status(status){

    if(status){

        load.classList.remove("hidden_loader")
    }else{

        load.classList.add("hidden_loader")
    }
}


//Modal confirmacion de precio
function modal_state(status, price= undefined){

    if(status){

        modal_price_confirm.classList.remove("disabled")
        price_scan.textContent = "$"+price;
    }else{

        modal_price_confirm.classList.add("disabled")
        price_scan.textContent = undefined
    }
}
// boton cancelar -> cierra ventana
btn_cancel_modalprice.addEventListener("click", ()=>{

    modal_state(false)
})

//boton confirmar -> guarda precio en formulario para enviar


//validar campo email
email_valid.style.display="none"
email.addEventListener("focusout", ()=>{
    input_email_valid()
    
})
let moveYTPressed = false;
let moveYBPressed = false;
let speed = 26
// Manejador para el evento mousedown del botón moveYT
moveYT.addEventListener("mousedown", () => {
    moveYTPressed = true;

    // Llama a la función para mover hacia arriba repetidamente
    moveUpRepeatedly();
});
///////////////////////////////////////////////////////////////////
// Manejador para el evento mouseup del botón moveYT
moveYT.addEventListener("mouseup", () => {
    moveYTPressed = false;
    speed = 26
});

// Manejador para el evento mousedown del botón moveYB
moveYB.addEventListener("mousedown", () => {
    moveYBPressed = true;

    // Llama a la función para mover hacia abajo repetidamente
    moveDownRepeatedly();
});

// Manejador para el evento mouseup del botón moveYB
moveYB.addEventListener("mouseup", () => {
    moveYBPressed = false;
    speed = 26
});

// Función para mover hacia arriba repetidamente mientras el botón moveYT está presionado
function moveUpRepeatedly() {
    if (moveYTPressed) {      
        cropper.move(0, speed); // Mueve hacia arriba
        speed++
        console.log("subiendo a velocidad" + speed)
        setTimeout(moveUpRepeatedly, 100); // Llama a la función nuevamente después de 100ms
    }
}

// Función para mover hacia abajo repetidamente mientras el botón moveYB está presionado
function moveDownRepeatedly() {
    if (moveYBPressed) {
        cropper.move(0, -speed); // Mueve hacia abajo
        speed++
        console.log("bajando a velocidad " + speed)
        setTimeout(moveDownRepeatedly, 100); // Llama a la función nuevamente después de 100ms
    }
}
///////////////////////////////////////////////////////////////////
moveXL.addEventListener("click", ()=>{
    cropper.move(12,0)
})

moveXR.addEventListener("click", ()=>{
    cropper.move(-12,0)
})

zoom_up.addEventListener("click", ()=>{
    cropper.zoom(0.1)
})

zoom_down.addEventListener("click", ()=>{
    cropper.zoom(-0.1)
})


btn.addEventListener("click", ()=>{

    
    generate_metadata()

})

btn_send.addEventListener("click", ()=>{

    modal_loader_status(true)

    if(email.value != ""){
        validations_form.email_required = true
    }else{
        validations_form.email_required = false
    }

    console.log(validations_form)
    if(validations_form.email_check && validations_form.email_required && validations_form.price_as_number && validations_form.price_check){
        send_api()
    }else{

        alert("Por favor valide los campos")
        modal_loader_status(false)
        
    } 
 
})


btn_capture.addEventListener("click", ()=>{

    cropper.destroy()
    image.src = "../static/img/default.jpg"
    
})

function generate_metadata(){

    //cargando loader -> abrir modal de confirmacion
    modal_loader_status(true)

    var img_cut = cropper.getCroppedCanvas()
    console.log("url:; " + url_input.value)

    img_cut.toBlob((blob)=>{
        const form = new FormData()
        form.append("image", blob, "image_cut.png")
        const csrftoken = getCookie('csrftoken');

        fetch(base_url + "save_image",{method:"POST", body: form, headers: {'X-CSRFToken': csrftoken}})
            .then(res => {
                
                return res.json()
            })
            .then(data =>{

                res_view = {

                    price : data.Data,
                    coordinates : cropper.getData(),
                    url : url_input.value
                }

                modal_loader_status(false)
                modal_state(true, res_view.price.price)

                //Se checkea precio en lista de requerimientos y se valida que sea numero
                btn_confirm_modalprice.addEventListener("click", ()=>{

                    validations_form.price_check = true
                    console.log(res_view.price.price)
                    if(!isNaN(res_view.price.price)){
                
                        data_form = res_view
                        validations_form.price_as_number = true

                    }else{
                
                        alert("El area seleccionada no contiene un numero valido.")
                        validations_form.price_as_number = false
                    }
                    modal_state(false)
                    
                })
                

            })
            .catch(error =>{
                console.error(error)
            })

    })
}

function input_email_valid(){

    let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if(regex.test(email.value)){
        console.log("correo valido");
        email_valid.style.display="none";
        validations_form.email_check = true;
        return true;
    }else{
        console.log("correo invalido");
        email_valid.style.display="block";
        validations_form.email_check = false;
        return false;
    }
    
}

function send_api(){

    form_metadata = new FormData()
    
    form_metadata.append("price", data_form.price.price)
    form_metadata.append("x", data_form.coordinates.x)
    form_metadata.append("y", data_form.coordinates.y)
    form_metadata.append("width", data_form.coordinates.width)
    form_metadata.append("height", data_form.coordinates.height)
    form_metadata.append("ImageTrackDescription", description.value)
    form_metadata.append("url", data_form.url)
    form_metadata.append("email", email.value)

    const csrftoken = getCookie('csrftoken');
    fetch(base_url +"save_image_db",{method:"POST", body: form_metadata, headers:{'X-CSRFToken': csrftoken }})
            .then(res => {
                return res.json()
            })
            .then(data =>{

                
                if(data.Status){

                    load.classList.add("hidden_loader")
                    modal_confirm.classList.remove("disabled")
                }else{
                    modal_confirm.classList.add("disabled")
                    load.classList.add("hidden_loader")
                }
                
            })
            .catch(error =>{
                console.error(error)
            })
    
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Buscar el token CSRF en las cookies
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}