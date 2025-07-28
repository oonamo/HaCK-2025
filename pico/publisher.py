from sensors import Humidity, photoresistor, ultrasonic

from service import SensorPublisher


def request_humidty() -> (float, None):
    val = Humidity.get_humidity()
    if val is None:
        val = -1
    return val


def request_tempature() -> (float, None):
    val = Humidity.get_temperature()
    if val is None:
        val = -1
    return val


def request_lumens() -> float:
    return photoresistor.read_pr_lumens()


def request_distance_cm() -> float:
    val = ultrasonic.get_distance_cm()
    if val is None:
        val = -1
    return val


class Publishers:
    def __init__(self, client, topics, defer_client: False):
        self._publishers: list[SensorPublisher] = {}
        self._client_init = False
        self._topics = topics
        self._client = client

        if defer_client:
            return

        self._init_client()

    def set_client(self, client):
        self._client = client

    def _init_client(self):
        for topic in self._topics:
            self._publishers[topic] = SensorPublisher(
                self._client, topic, self._topics[topic]
            )

        self._client_init = True

    def publish(self, topic, *args):
        if not self._client_init:
            self._init_client()

        if self._publishers[topic]:
            print("trying publish")
            self._publishers[topic].publish(*args)
            print("did publish")

    def publish_all(self):
        for topic in self._topics:
            self.publish(topic)

    def get_topics(self) -> list[str]:
        return [topic for topic in self._topics]


PUBLISHERS = Publishers(
    client=None,
    defer_client=True,
    topics={
        "temp": request_tempature,
        "humidity": request_humidty,
        "light": request_lumens,
        "ultrasonic": request_distance_cm,
    },
)
