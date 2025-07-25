from connections import connect_mqtt, connect_internet
from time import sleep
import secrets

WIFI_SSID = "UCLA_WEB"
WIFI_PASSWORD = None

def main():
    try:
        connect_internet(WIFI_SSID,password=WIFI_PASSWORD) #ssid (wifi name), pass
        client = connect_mqtt(secrets.MQTT_URL, secrets.USER, secrets.MQTT_PASS) # url, user, pass

        while True:
            client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()
