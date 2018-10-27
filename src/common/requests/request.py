from src.constants.constants import SENSOR_CONSTANTS


class Request(object):
    def __init__(self, request):
        self.defaults = {}
        self.sensors = []
        self.request = request
        self.context = {}
        self.initialize_defaults()
        self.initialize_sensor_data()
        self.initialize_urls()

    def get_constant_value(self, object, key):
        value = None
        if object and key:
            value = object[key]
        return value

    def initialize_defaults(self):
        defaults = self.get_constant_value(SENSOR_CONSTANTS, 'defaults')
        self.defaults = defaults

    def initialize_sensor_data(self):
        sensors = self.get_constant_value(SENSOR_CONSTANTS, 'sensors')
        for sensor in sensors:
            self.sensors.append(sensor)

    def initialize_urls(self):
        self.sensor_data_url = self.get_constant_value(SENSOR_CONSTANTS, 'sensor_data_url')