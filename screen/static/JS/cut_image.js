const base_url = "http://127.0.0.1:8000/api/"

//const base_url = "http://195.35.14.162:8002/api/"
const btn = document.getElementById("btn_cropp")
const save_cut = document.getElementById("save_cut")
const btn_send = document.getElementById("send_form")
const btn_capture = document.getElementById("capture")
const image = document.getElementById("image_capture")
const email = document.getElementById("email")
const frequency = document.getElementById("frequency")
const modal_confirm = document.getElementById("modal_email_confirm")
let data_form
let price_check = false
let validations_form = {

    email_required : false,
    email_check : false,
    price_check : false,
    price_as_number : false
}

const cropper = new  Cropper(image, {
    aspectRatio: 0,  // Proporción de aspecto (puedes ajustar según tus necesidades)
    viewMode: 1,

})

cropper.setCropBoxData({
    width: 20,
    height: 20
});
const moveYT = document.getElementById("moveY-T")
const moveYB = document.getElementById("moveY-B")
const moveXL = document.getElementById("moveX-L")
const moveXR = document.getElementById("moveX-R")
const zoom_up = document.getElementById("zoom+")
const zoom_down = document.getElementById("zoom-")
const url_input = document.getElementById("url_")
const email_valid = document.getElementById("email_valid")
const load = document.getElementById("loader");

//validar campo email
email_valid.style.display="none"
email.addEventListener("focusout", ()=>{
    input_email_valid()
})
moveYT.addEventListener("click", ()=>{
    cropper.move(0,13)
})
moveYB.addEventListener("click", ()=>{
    cropper.move(0,-13)
})

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

    load.classList.remove("hidden_loader")

    if(email.value != ""){
        validations_form.email_required = true
    }else{
        validations_form.email_required = false
    }

    if(validations_form.email_check && validations_form.email_required && validations_form.price_as_number && validations_form.price_check){
        send_api()
    }else{

        alert("Por favor valide los campos")
        
    } 
 

    

})


btn_capture.addEventListener("click", ()=>{

    cropper.destroy()
    image.src = "../static/img/default.jpg"
    
})

function generate_metadata(){


    var img_cut = cropper.getCroppedCanvas()
    console.log("url:; " + url_input.value)

    img_cut.toBlob((blob)=>{
        const form = new FormData()
        form.append("image", blob, "image_cut.png")

        fetch(base_url + "save_image",{method:"POST", body: form})
            .then(res => {
                
                return res.json()
            })
            .then(data =>{

                res_view = {

                    price : data.Data,
                    coordinates : cropper.getData(),
                    url : url_input.value
                }

                if(confirm("El precio correcto seleccionado es : $" + res_view.price.price + "?")){

                    validations_form.price_check = true
                    console.log(res_view.price.price)
                    if(!isNaN(res_view.price.price)){

                        data_form = res_view
                        validations_form.price_as_number = true
                    }else{

                        alert("El area seleccionada no contiene un numero valido.")
                        validations_form.price_as_number = false
                    }
                    
                }else{
                    price_check = false
                    validations_form.price_check = false
                }
        
            })
            .catch(error =>{
                console.error(error)
            })

    })
}

function input_email_valid(){

    let email = document.getElementById("email");
    let email_ = email.value;
    console.log(email_);
    let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if(regex.test(email_)){
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
    form_metadata.append("rotate", data_form.coordinates.rotate)
    form_metadata.append("scaleX", data_form.coordinates.scaleX)
    form_metadata.append("scaleY", data_form.coordinates.scaleY)
    form_metadata.append("url", data_form.url)
    form_metadata.append("email", email.value)
    form_metadata.append("frequency_fk", frequency.value)

    fetch(base_url +"save_image_db",{method:"POST", body: form_metadata})
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