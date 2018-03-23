import random

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from sensor.constants.constants import SENSOR_CONSTANTS


def data(request):
    context = {'canvasWidth': SENSOR_CONSTANTS['accelerometer']['canvas']['width'],
               'canvasHeight': SENSOR_CONSTANTS['accelerometer']['canvas']['height'],}
    return render(request, 'data.html', context)


# Get the Accelerometer data from the sensor.
def accel(request):
    x = random.randint(0, 500)
    y = random.randint(0, 400)
    z = random.randint(0, 500)

    data = {'x': x, 'y': y, 'z': z}

    return JsonResponse(data)


def sensor_constants(request):
    return JsonResponse(SENSOR_CONSTANTS)