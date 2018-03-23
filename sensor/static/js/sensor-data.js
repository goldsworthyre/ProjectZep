/**
 * Created by ryan on 3/23/18.
 */


var timerValue = 1000;
var lineWidth = 2;
var canvas = null;
var ctx = null;

$(document).ready(function(){
    canvas = document.getElementById("sensor-data");
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "#22C3DD";
    window.setInterval(getSensorData, timerValue)
});

function getSensorData(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawOuterBox();
    drawCoordinatePlane();
    drawSensorPoint(ctx);
}

function drawCoordinatePlane(){
    ctx.lineWidth = lineWidth;
    drawLine(canvas.width / 2 - lineWidth, 0, canvas.width / 2, canvas.height, 2);
    drawLine(0, canvas.height / 2 - lineWidth, canvas.width, canvas.height / 2 );
}

function drawOuterBox(){
    ctx.strokeRect(0,0,canvas.width,canvas.height);
}

function drawLine(x1, y1, x2, y2){
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}

function drawSensorPoint(){
    ctx.beginPath();
    var x = Math.floor(Math.random() * 200);
    var y = Math.floor(Math.random() * 250);
    var radius = 5;
    var startAngle = 0;
    var endAngle = Math.PI * 2;
    var clockwise = true;
    ctx.arc(x,y,radius, startAngle,endAngle, clockwise);
    ctx.fill();
    ctx.closePath();
}

