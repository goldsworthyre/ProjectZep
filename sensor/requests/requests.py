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
        super().__init__(request)

    def initialize_defaults(self):
        defaults = self.get_constant_value(SENSOR_CONSTANTS, 'defaults')
        self.defaults = defaults

    def initialize_sensor_data(self):
        sensors = self.get_constant_value(SENSOR_CONSTANTS, 'sensors')
        for sensor in sensors:
            self.sensors.append(sensor)

    def render(self):
        self.context.update({'sensors': self.sensors, 'defaults': self.defaults})
        return render(self.request, 'data.html', self.context)