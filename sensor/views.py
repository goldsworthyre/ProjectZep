import random

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from sensor.constants.constants import SENSOR_CONSTANTS
from sensor.requests.requests import SensorRequest, SensorDataRequest


def data(request):
    return SensorRequest(request).render()


# Get the Accelerometer data from the sensor.
def accel(request):
    return SensorDataRequest(request).render()


def sensor_constants(request):
    return JsonResponse(SENSOR_CONSTANTS)