

class Request(object):
    def __init__(self, request):
        self.request = request
        self.context = {}

    def get_constant_value(self, object, key):
        value = None
        if object and key:
            value = object[key]
        return value