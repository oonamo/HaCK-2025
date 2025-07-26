import secrets
from time import sleep

from connections import connect_internet, connect_mqtt
from publisher import PUBLISHERS

WIFI_SSID = "UCLA_WEB"
WIFI_PASSWORD = None


def cb(topic, msg):
    pass


def main():
    try:
        connect_internet(WIFI_SSID, password=WIFI_PASSWORD)  # ssid (wifi name), pass
        client = connect_mqtt(
            secrets.MQTT_URL, secrets.USER, secrets.MQTT_PASS
        )  # url, user, pass

        client.set_callback(cb)

        PUBLISHERS.set_client(client)

        while True:
            if True:
                PUBLISHERS.publish_all()
            # client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print("keyboard interrupt")


if __name__ == "__main__":
    main()
