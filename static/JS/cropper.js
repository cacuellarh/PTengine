const base_url = "http://18.188.170.117:8001/api/"
const image = document.getElementById("image_capture")
const cropper = new  Cropper(image, {
    aspectRatio: 1,  // Proporción de aspecto (puedes ajustar según tus necesidades)
    viewMode: 1
})

let data_form

const btn = document.getElementById("btn_cropp")
const save_cut = document.getElementById("save_cut")
const url = document.getElementById("url_input")
const btn_send = document.getElementById("send_form")
const btn_capture = document.getElementById("capture")
const moveYT = document.getElementById("moveY-T")
const moveYB = document.getElementById("moveY-B")
const moveXL = document.getElementById("moveX-L")
const moveXR = document.getElementById("moveX-R")
const zoom_up = document.getElementById("zoom+")
const zoom_down = document.getElementById("zoom-")


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

    send_api()

})

function generate_metadata(){

    var img_cut = cropper.getCroppedCanvas()

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
                    url : url.value
                }

                console.log(res_view)
                
                data_form = res_view

            })
            .catch(error =>{
                console.error(error)
            })

    })
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

    fetch(base_url +"save_image_db",{method:"POST", body: form_metadata})
            .then(res => {
                return res.json()
            })
            .then(data =>{

                console.log(data)
                
            })
            .catch(error =>{
                console.error(error)
            })

    
}
