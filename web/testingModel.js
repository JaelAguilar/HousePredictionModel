var modelo = null;
//Cargamos el modelo entrenado
(async () => {
    console.log("Cargando el modelo...");
    modelo = await tf.loadLayersModel("model.json");
    console.log("Modelo cargado!");
})();

const btn = document.getElementById("btn");
//let en vez de var
//parsefloat es en los que ingresar
//0 y 1 parseInt
btn.onclick = () => {
    let m2 = document.getElementById('m2').value;
    let esta = document.getElementById('esta').value;
    let m2construidos = document.getElementById('m2construidos').value;
    let recam = document.getElementById('recam').value;
    let terreno = document.getElementById('terreno').value;
    let pisoduela = document.getElementById('pisoduela').value;
    let armarios = document.getElementById('armarios').value;
    let jardint = document.getElementById('jardint').value;
    let cercado = document.getElementById('cercado').value;
    let estacionat = document.getElementById('estacionat').value;
    let amueblado = document.getElementById('amueblado').value;
    let jardin = document.getElementById('jardin').value;
    let internetb = document.getElementById('internetb').value;
    let estacionamientov = document.getElementById('estacionamientov').value;
    let calefaccion = document.getElementById('calefaccion').value;
    let balcon = document.getElementById('balcon').value;
    let tv = document.getElementById('tv').value;
    let patio = document.getElementById('patio').value;
    let garage = document.getElementById('garage').value;
    let jacuzzi = document.getElementById('jacuzzi').value;
    let estudio = document.getElementById('estudio').value;
    let pisolo = document.getElementById('pisolo').value;
    let alarma = document.getElementById('alarma').value;
    let tennis = document.getElementById('tennis').value;
    let cocina = document.getElementById('cocina').value;
    let cuartoservicio = document.getElementById('cuartoservicio').value;
    let gym = document.getElementById('gym').value;
    let estacionamientoa = document.getElementById('estacionamientoa').value;
    let juegos = document.getElementById('juegos').value;
    let clima = document.getElementById('clima').value;
    let terraza = document.getElementById('terraza').value;
    let entretenimientolibre = document.getElementById('entretenimientolibre').value;
    let estacionamientovisita = document.getElementById('estacionamientovisita').value;
    let comunicador = document.getElementById('comunicador').value;
    let chimenea = document.getElementById('chimenea').value;
    let alberca = document.getElementById('alberca').value;


    //tensor va en el modelo
    //tensor = entrada
    //let en vez de var
    //parsefloat es en los que ingresar
    //0 y 1 parseInt

    if (modelo != null) {
        let tensor = tf.tensor2d(
            [[
                parseFloat(baño), parseInt(pisoduela), parseInt(armarios), parseInt(jardint), parseInt(cercado), parseFloat(esta), parseInt(estacionat),
                parseFloat(m2construidos), parseInt(amueblado), parseFloat(recam), parseInt(jardin), parseInt(internetb), parseInt(estacionamientov), parseInt(calefaccion),
                parseInt(balcon), parseInt(tv), parseInt(patio), parseInt(garage), parseInt(jacuzzi), parseInt(estudio), parseInt(pisolo),
                parseInt(alarma), parseInt(tennis), parseInt(cocina), parseInt(cuartoservicio), parseInt(gym), parseInt(estacionamientoa), parseInt(juegos),
                parseInt(clima), parseInt(terraza), parseInt(entretenimientolibre), parseInt(estacionamientovisita), parseInt(comunicador), parseInt(chimenea), parseFloat(terreno),
                parseInt(alberca)

            ]])
        let prediccion = modelo.predict(tensor).dataSync();
        prediccion = Math.round(prediccion, 2)
        document.getElementById("resultado").innerHTML = "Precio: " + prediccion + "€/mes";
    } else {
        document.getElementById("resultado").innerHTML = "Intenta de nuevo en un rato...";
    }
}
