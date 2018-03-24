import random

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from sensor.constants.constants import SENSOR_CONSTANTS
from sensor.requests.requests import SensorRequest


def data(request):
    return SensorRequest(request).render()


# Get the Accelerometer data from the sensor.
def accel(request):
    x = random.randint(0, 500)
    y = random.randint(0, 400)
    z = random.randint(0, 500)

    data = {'x': x, 'y': y, 'z': z}

    return JsonResponse(data)


def sensor_constants(request):
    return JsonResponse(SENSOR_CONSTANTS)