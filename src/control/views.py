# Create your views here.
from src.control.requests.requests import ControlRequest, ControlDataRequest, ControlMovementRequest


def control(request):
    return ControlRequest(request).render()


def control_data(request):
    return ControlDataRequest(request).render()


def control_movement(request):
    return ControlMovementRequest(request).render()