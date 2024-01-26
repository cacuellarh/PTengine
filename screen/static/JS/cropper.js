const base_url = "http://18.188.170.117:8001/api/"
const image = document.getElementById("image_capture")
const cropper = new  Cropper(image, {
    aspectRatio: 0,  // Proporción de aspecto (puedes ajustar según tus necesidades)
    viewMode: 0,
    data : {
        "x": 486.86381543860324,
        "y": 903.6888531907867,
        "width": 133.15403438857885,
        "height": 42.799511053471775,
        "rotate": 0,
        "scaleX": 1,
        "scaleY": 1
    }    // Vista previa centrada
})

let data_form

const btn = document.getElementById("btn_cropp")
const save_cut = document.getElementById("save_cut")
const url = document.getElementById("url_input")
const btn_send = document.getElementById("send_form")

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
