import django
from django.http import JsonResponse
from django.shortcuts import render
from django.template import context
from requests import request

from common.requests.request import Request
from constants.constants import CONTROL_CONSTANTS


class ControlRequest(Request):
    def __init__(self, request):
        super().__init__(request)
        self.camera_url = None
        self.camera_data_url = None
        self.initialize_camera_data()
        self.initialize_control_defaults()

    def initialize_control_defaults(self):
        if 'controls_url' in CONTROL_CONSTANTS:
            self.control_data_url = CONTROL_CONSTANTS['controls_url']

    def initialize_camera_data(self):
        for sensor in self.sensors:
            if 'type' in sensor:
                sensor_type = sensor['type']
                if sensor_type == 'stream':
                    if 'data_url' in sensor:
                        self.camera_url = sensor['data_url']

    def render(self):
        self.context.update({'camera_url' : self.camera_url, 'control_data_url': self.control_data_url, 'csrf_token': csrf_token})
        return render(self.request, 'control.html', self.context)

class ControlDataRequest(Request):
    def __init__(self, request):
        super().__init__(request)

    def render(self):
        data = CONTROL_CONSTANTS
        return JsonResponse(data)


class ControlMovementRequest(Request):
    def __init__(self, request):
        super().__init__(request)

    def render(self):
        action = self.request.POST['action']
        return JsonResponse({'action': action})