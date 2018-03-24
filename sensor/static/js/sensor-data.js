/**
 * Created by ryan on 3/23/18.
 */


var timerValue = 1000;
var lineWidth = 2;
var canvas = null;
var ctx = null;

$(document).ready(function(){
    initializeCanvas();
    window.setInterval(getSensorData, timerValue)
});

function initializeCanvas(){
    canvas = document.getElementById("sensor-data");
    var accelRequest = $.get('/sensor/sensor_constants', function(data){
            var sensors = data.sensors;
            if(sensors){
                if(sensors.length > 0){
                    for(i=0; i<sensors.length;i++){
                        var sensor = sensors[i];
                        if(sensor.canvas){
                            var canvasConfig = sensor.canvas;
                            if(canvasConfig){
                                ctx = canvas.getContext(canvasConfig.dimension);
                                ctx.fillStyle = canvasConfig.color;
                            }
                        }
                    }
                }
            }
        }
    );
}

function getSensorData(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawOuterBox();
    drawCoordinatePlane();
    getAccelCoordinates();
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

// Get the Accelerometer coordinates via an ajax request.
function getAccelCoordinates(){
    var accelRequest = $.get('/sensor/accel', function(data){
            drawSensorPoint(data);
        }
    );
}

// Draw the data point for where the accelerometer is.
function drawSensorPoint(data){
    ctx.beginPath();
    var x = data.x;
    var y = data.y;
    var radius = 5;
    var startAngle = 0;
    var endAngle = Math.PI * 2;
    var clockwise = true;
    ctx.arc(x,y,radius, startAngle,endAngle, clockwise);
    ctx.fill();
    ctx.closePath();
}

