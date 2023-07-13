function calcular(){
	

let dia1 = Number(document.getElementById("dia").value);
let mes1 = Number(document.getElementById("mes").value);
let año1 = Number(document.getElementById("año").value);

let dia2 = Number(document.getElementById("dia2").value);
let mes2 = Number(document.getElementById("mes2").value);
let año2 = Number(document.getElementById("año2").value);

if ((mes1 == 4 || mes1 == 6 || mes1 == 9 || mes1 == 11) && dia1 > 30 ) {
    alert("Fecha invalida")
};

if ((mes2 == 4 || mes2 == 6 || mes2 == 9 || mes2 == 11) && dia2 > 30 ) {
    alert("Fecha invalida")
};

if (mes1 == 2 && dia1 > 29){
    alert("Fecha invalida")
};

if (mes2 == 2 && dia2 > 29){
    alert("Fecha invalida")
};

if (mes1 == 2 && dia1 == 29 && año1%4 != 0 ){
    alert("Fecha invalida")
};


let diff_año = (año2 - año1);
let diff_dia = (dia2 - dia1);
let diff_mes = (mes2 - mes1);


let total_años = diff_año;
let total_meses = diff_año * 12 + diff_mes;
let total_dias = diff_año * 365 + diff_mes * 30 + diff_dia + Math.floor(total_años/4);

if (diff_dia < 0 && total_meses > 0){
    total_meses -= 1;
};

if (diff_dia < 0 && diff_mes <= 0 && total_años > 0){
    total_años -= 1;
};


document.getElementById("años").innerHTML = `años de diferencia: ${total_años}`;
document.getElementById("meses").innerHTML = `meses de diferencia: ${total_meses}`;
document.getElementById("dias").innerHTML = `dias de diferencia: ${total_dias}`;

};
