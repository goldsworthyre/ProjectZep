
SENSOR_CONSTANTS = {
    'defaults':{
        'default_canvas_width': 500,
        'default_canvas_height': 400,
    },
    'sensors':
        [
            {
                'name': 'Accelerometer',
                'id': 'accelerometer',
                'data_url': '/sensor/accel',
                'canvas':{
                    'width': 1000,
                    'height': 900,
                    'zed': 500,
                    'color': '#22C3DD',
                    'dimension': '2d',
                }
            },
            {
                'name': 'Camera',
                'id': 'camera',
                'data_url': '/sensor/accel',
                'canvas': {
                    'width': 500,
                    'height': 400,
                    'zed': 500,
                    'color': '#FF0000',
                    'dimension': '2d',
                }
            },
        ],
}