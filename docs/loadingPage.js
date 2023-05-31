/* When the user clicks on the button,
            toggle between hiding and showing the dropdown content */
function closeSelector() {
    document.getElementById("direccionDropdown").classList.toggle("show");
}

function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("direccion");
    filter = input.value.toUpperCase();
    div = document.getElementById("direccionDropdown");
    a = div.getElementsByTagName("div");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

let address
function selectedAddress(direc) {
    address = direc
    console.log(address)
    closeSelector()
}


const inputDireccion = document.getElementById('direccionDropdown')

direcciones.forEach(direccion => {
    inputDireccion.insertAdjacentHTML("beforeend",`<div onclick="selectedAddress('${direccion}')">${direccion}</div>`)
});