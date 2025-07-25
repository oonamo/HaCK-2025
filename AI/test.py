import paho.mqtt as paho
import paho.mqtt.client as p_client
import secrets

client = p_client.Client(client_id="", userdata=None, protocol=paho.client.MQTTv5)
client.tls_set(tls_version=paho.client.ssl.PROTOCOL_TLS)
client.username_pw_set(secrets.USERNAME, secrets.PASSWORD)

client.connect(secrets.URL, 8883)

def on_connect(client, userdata, flags, rc, props):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # client.publish("pico/camera", "Hello, from publisher!")
    else:
        print(f"Failed to connect, return code {rc}\n")

client.on_connect = on_connect
client.loop_forever()
