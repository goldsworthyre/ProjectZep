/**
 * Created by Ryan Goldsworthy on 3/23/18.
 */

function initializeCanvas(sensorDataUrl){
    var sensor_objects = [];
    $.get(sensorDataUrl, function(data) {
            var sensors = data.sensors;
            var timerValue = 1000;
            if (data.refresh_timer) {
                timerValue = data.refresh_timer;
            }
            if (sensors) {
                if (sensors.length > 0) {
                    for (i = 0; i < sensors.length; i++) {
                        sensor = sensors[i];
                        sensor_object = new Sensor(sensor, i);
                        sensor_objects.push(sensor_object);
                    }
                }
            }
            window.setInterval(function(){
                for(var i=0;i<sensor_objects.length;i++){
                    sensor_object = sensor_objects[i];
                    sensor_object.getSensorData();
                }
            }, timerValue);
        }
    );
}

// Allows the drawing of sensor data from the
// server config.
function Sensor(sensor_config, sensor_number){
    this.canvas = null;
    this.ctx = null;
    this.id = null;
    this.data_url = null;
    this.sensor_number = sensor_number;

    this.sensor = sensor_config;

    if(this.sensor.id){
        this.id = this.sensor.id;
        this.canvas = document.getElementById(this.id);
    }

    if(this.sensor.canvas){
        var canvasConfig = this.sensor.canvas;
        if(canvasConfig){
            this.ctx = this.canvas.getContext(canvasConfig.dimension);
            this.ctx.fillStyle = canvasConfig.color;
            this.ctx.lineWidth = canvasConfig.line_width;
        }
    }

    if(this.sensor.data_url){
        this.data_url = this.sensor.data_url;
    }

    this.getSensorData = function(){
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.drawCoordinatePlane();
        this.getSensorDataValues();
    }

    this.drawCoordinatePlane = function(){
        this.drawLine(this.canvas.width / 2 - this.ctx.lineWidth, 0, this.canvas.width / 2, this.canvas.height, 2);
        this.drawLine(0, this.canvas.height / 2 - this.ctx.lineWidth, this.canvas.width, this.canvas.height / 2 );
        this.drawOuterBox();
    }

    this.drawOuterBox = function(){
        this.ctx.strokeRect(0,0,this.canvas.width,this.canvas.height);
    }

    this.drawLine = function(x1, y1, x2, y2){
        this.ctx.beginPath();
        this.ctx.moveTo(x1, y1);
        this.ctx.lineTo(x2, y2);
        this.ctx.stroke();
    }

    // Get the Accelerometer coordinates via an ajax request.
    this.getSensorDataValues = function(){
        var _obj = this;
        var accelRequest = $.get(_obj.data_url, {sensor_number: _obj.sensor_number}, function(data){
                _obj.drawSensorPoint(data);
            }
        );
    }

    // Draw the data point for where the accelerometer is.
    this.drawSensorPoint = function(data){
        this.ctx.beginPath();
        var x = data.x;
        var y = data.y;
        var radius = 5;
        var startAngle = 0;
        var endAngle = Math.PI * 2;
        var clockwise = true;
        this.ctx.arc(x,y,radius, startAngle,endAngle, clockwise);
        this.ctx.fill();
        this.ctx.closePath();
    }
}
