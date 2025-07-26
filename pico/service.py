from sensors import Humidity, photoresistor, ultrasonic

class SensorPublisher:
    def __init__(self, client, name, publish_fn = None):
        self._client = client
        self._name = name
        self._fn = publish_fn

    def set_publish_fn(self, fn):
        assert fn is not None, "Fn must be a function"
        self._fn = fn

    def publish(self, *args):
        payload = self._fn(*args)
        self._client.publish(self._topic, payload)
