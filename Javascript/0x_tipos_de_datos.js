var estatura = 1.71 // scope global o local, sometida a hoisting
let peso = 60 //scope de bloque, no esta sometida hoisting
const nombre = "Matthias" //constante, no sometida a hoisting

//¿como imprimir?
//alert()
//console.log()

//tipos de datos
//NUMBERS
let edad = 29;
let sueldo = 1200000;
const pi = 3.14;
//Notación científica y BigInt
const n_grande = 1e6 // 1 millón 1000000
const n_pequeño = 1e-6// 0.000001

const bigint = 21341868754768421285285416893n;

//STRINGS
let string1 = "HOLA MARGE";
let string2 = "Hola Carlita";
let frase = `Este es un saludo: $[string1]`;

//INFINIDAD
console.log(edad / 0);

//BOOLEANOS
console.log("############ BOOLEANOS ############");
let V = true;
let F = false;

if (V) {
    //si es true
    console.log("es verda");
};

//NULL
console.log("############ NULL ############");

//INDEFINIDO
let institucion;
console.log(institucion);

//OBJETOS
let user = new Object(); //sintaxis de creodor de objetos
let user1 = {}; //sintaxis de "objeto literal"

//obj literal
let usuario = {
    name: "Mateo",
    age: 30,
    city: "Osorno",
    "correo electronico": "momazosmateo@gmail.com",
};

//agregar al objeto literal

usuario.estado = true;
console.table(usuario);

console.log(usuario["correo electronico"])

delete usuario.estado;

//transformar y ver tipo de dato
console.log("############ TRANSFORMAR ############")
console.log(typeof edad)
edad = String(edad)
console.log(typeof edad)

alert("HOLA")
