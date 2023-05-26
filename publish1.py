import paho.mqtt.client as mqtt
import json
import time
import random


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

i = 0
client.connect('localhost', 1883)
client.loop_start()
while(i<100):
    send_data =random.randrange(1,180)
    client.publish('common', send_data, 1) #"my name is gskim",1)
    i += 1
    time.sleep(2)
client.loop_stop()

client.disconnect()