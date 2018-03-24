import random

from django.http import JsonResponse
from django.shortcuts import render
from django.template import context
from requests import request

from common.requests.request import Request
from sensor.constants.constants import SENSOR_CONSTANTS


class SensorRequest(Request):
    def __init__(self, request):
        self.defaults = {}
        self.sensors = []
        self.initialize_defaults()
        self.initialize_sensor_data()
        self.initialize_urls()
        super().__init__(request)

    def initialize_defaults(self):
        defaults = self.get_constant_value(SENSOR_CONSTANTS, 'defaults')
        self.defaults = defaults

    def initialize_sensor_data(self):
        sensors = self.get_constant_value(SENSOR_CONSTANTS, 'sensors')
        for sensor in sensors:
            self.sensors.append(sensor)

    def initialize_urls(self):
        self.sensor_data_url = self.get_constant_value(SENSOR_CONSTANTS, 'sensor_data_url')

    def render(self):
        self.context.update({'sensors': self.sensors, 'defaults': self.defaults, 'sensor_data_url': self.sensor_data_url})
        return render(self.request, 'data.html', self.context)


class SensorDataRequest(SensorRequest):
    def __init__(self, request):
        self.sensor_number = 0
        if 'sensor_number' in request.GET:
            self.sensor_number = int(request.GET['sensor_number'])
        super().__init__(request)

    def render(self):
        data = {}
        if self.sensor_number is not None:
            if self.sensors:
                sensor = self.sensors[self.sensor_number]
                if 'canvas' in sensor:
                    canvas = sensor['canvas']
                    if 'width' in canvas:
                        x = random.randint(0, canvas['width'])
                    if 'height' in canvas:
                        y = random.randint(0, canvas['height'])
                    if 'zed' in canvas:
                        z = random.randint(0, canvas['zed'])

            data = {'x': x, 'y': y, 'z': z}

        return JsonResponse(data)