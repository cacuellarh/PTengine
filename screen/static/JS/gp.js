let base_url = ""
const id_input = document.getElementById("id_image")
let id = id_input.value
document.addEventListener("DOMContentLoaded", function(){

    load_conf()
    load_gp()
    //load_data()    
})

function load_gp(){
    ctx = document.getElementById("chart")
    var char_c = new Chart(ctx, {
    
        
    type: "bar",
    data: {
        labels:["Enero", "Febrero", "Marzo", "Abril"],
        datasets: [{
            label: ["nov","diciembre", "enero", "sdasd", "enero"],
            data:[12,23,12,34,56,36,39],
            backgroundColor:["rgb(145, 10, 103)"]

        }]
    }
})
}

function load_data(){

    fetch(base_url + "details/")
    .then(res =>{
        return res.json()
    })
    .then(data =>{
        console.log(data)
    })
}

function load_conf(){

    fetch('/static/JS/conf.json')
    .then(res =>{

        return res.json()
    })
    .then(data =>{

        base_url = data.url_base
    })
}