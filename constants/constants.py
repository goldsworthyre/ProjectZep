
SENSOR_CONSTANTS = {
    'defaults':{
        'default_canvas_width': 500,
        'default_canvas_height': 400,
    },
    'sensor_data_url':'/sensor/sensor_constants',
    'refresh_timer':500,
    'sensors':
    [
        {
            'name': 'Accelerometer',
            'id': 'accelerometer',
            'data_url': '/sensor/accel',
            'refresh_timer':1000,
            'line_width': 2,
            'canvas':{
                'width': 600,
                'height': 500,
                'zed': 500,
                'color': '#22C3DD',
                'dimension': '2d',
            }
        },
        {
            'name': 'Camera',
            'id': 'camera',
            'data_url': 'http://localhost:8090/test.webm',
            'line_width':10,
            'type': 'stream',
        },
    ],
}

CONTROL_CONSTANTS = {
                        'controls_url': '/control/config',
                        'keyboard':{
                            'FORWARD': 87,
                            'RIGHT': 68,
                            'LEFT': 65,
                            'BACK': 83,
                        },
                     }