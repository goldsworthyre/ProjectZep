from constants.constants import SENSOR_CONSTANTS
from django.http import JsonResponse

from src.sensor import SensorRequest, SensorDataRequest


def data(request):
    return SensorRequest(request).render()


# Get the Accelerometer data from the sensor.
def accel(request):
    return SensorDataRequest(request).render()


def sensor_constants(request):
    return JsonResponse(SENSOR_CONSTANTS)