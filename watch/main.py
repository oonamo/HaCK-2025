import secrets
from time import sleep, time

from connections import connect_internet, connect_mqtt
from face import WatchFace
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=1000000)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

watch_face = WatchFace(64, 128, display)

WAIT_TIME = 30
time_of_last_msg = None
start_time = time()

SPLIT_LENGTH = 16


def lcd_handle(topic, payload):
    global time_of_last_msg
    if topic == b"display":
        time_of_last_msg = time()
        payload_str = payload.decode("utf-8")
        display.fill(0)
        lines = [payload_str[i: i + SPLIT_LENGTH] for i in range(0, len(payload_str), SPLIT_LENGTH)]
        print(lines)
        for i in range(0, len(lines)):
            print(i, lines[i])
            display.text(lines[i], i, i*10, 1)
        display.show()

watch_face.draw()

def main():
    try:
        connect_internet(
            secrets.WIFI_SSID, password=secrets.WIFI_PASSWORD
        )  # ssid (wifi name), pass
        client = connect_mqtt(
            secrets.MQTT_URL, secrets.MQTT_USER, secrets.MQTT_PASS
        )  # url, user, pass
        client.set_callback(lcd_handle)

        client.subscribe("display")

        while True:
            # if not time_of_last_msg or time_of_last_msg + WAIT_TIME < time():
            #     watch_face.draw()
            client.check_msg()
            sleep(0.1)
    except KeyboardInterrupt:
        print("keyboard interrupt")

if __name__ == "__main__":
    main()
