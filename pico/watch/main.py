import secrets
from time import sleep

from connections import connect_internet, connect_mqtt
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=1000000)
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

def lcd_handle(topic, payload):
    if topic == b"display":
        payload_str = payload.decode('utf-8')
        display.fill(0)
        display.text(payload_str, 0, 0, 1)
        display.show()

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
        client.check_msg()
        sleep(0.1)
except KeyboardInterrupt:
    print("keyboard interrupt")

# while True:
#     display.text("Hello World", 0, 0, 1)
#     display.show()
#     time.sleep(3)
#
