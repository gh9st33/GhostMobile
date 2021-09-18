import paho.mqtt.client as mqtt_client
import pygame
import dataformatter
import random
#import socket
import json
import time

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print('Initialized Joystick : %s' % j.get_name())

# IP OF RECEIVER
#UDP_IP = "192.168.74.51"
#UDP_PORT = 5555

BROKER = '13.90.118.171'
PORT = 1883
TOPIC = "input/joystick"
BTNTOPIC = "inpute/button"
# generate client ID with pub prefix randomly
CLIENT_ID = "python-jstick-pub-{id}".format(id=random.randint(0, 1000))
USERNAME = 'gh9st'
PASSWORD = '021511'
FLAG_CONNECTED = 0
def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    if rc == 0:
        FLAG_CONNECTED = 1
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code {rc}".format(rc=rc), )

def connect_mqtt():
    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def publish(client):
    msg_count = 0
    last_msg = ""
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                l3x = j.get_axis(0) * 128  # -128-128 range
                l3y = j.get_axis(1) * 128  # -128-128 range
                r3x = j.get_axis(3) * 128  # -128-128 range
                r3y = j.get_axis(4) * 128  # -128-128 range
                l2 = j.get_axis(4)  # -1-1 range
                r2 = j.get_axis(5)  # -1-1
                l1 = j.get_axis(6)  # -1-1 range
                r1 = j.get_axis(7)  # -1-1 range
                if l3x < -5 or l3x > 5 or l3y < -5 or l3y > 5 or r3x < -5 or r3x > 5 or r3y < -5 or r3y > 5:
                    dataTranslator = dataformatter.JoystickDataPacketTranslator()
                    dataString = dataTranslator.createDataString(int(l3x), int(l3y), int(r3x), int(r3y), int(l2), int(r2), (l1), (r1))
                    print(dataString)
                    client.publish(TOPIC, dataString)
            if event.type == pygame.JOYBUTTONDOWN:
                b1 = j.get_button(0)
                if b1 == 1:
                    client.publish("input/button", "down")
                    print("sent buttondown status")
            if event.type == pygame.JOYBUTTONUP:
                b1 = j.get_button(0)
                if b1 == 0:
                    client.publish("input/button", "up")
                    print("sent buttonup status")



        

def run():
    client = connect_mqtt()
    client.loop_start()
    time.sleep(1)
    if FLAG_CONNECTED:
        publish(client)

    else:
        client.loop_stop()

def joystickSend():
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                l3x = j.get_axis(0) * 128  # -128-128 range
                l3y = j.get_axis(1) * 128  # -128-128 range
                r3x = j.get_axis(2) * 128  # -128-128 range
                r3y = j.get_axis(3) * 128  # -128-128 range
                l2 = j.get_axis(4)  # -1-1 range
                r2 = j.get_axis(5)  # -1-1
                l1 = j.get_axis(6)  # -1-1 range
                r1 = j.get_axis(7)  # -1-1 range
                dataTranslator = dataformatter.JoystickDataPacketTranslator()
                dataString = dataTranslator.createDataString(int(l3x), int(l3y), int(r3x), int(r3y), int(l2), int(r2), (l1), (r1))
                print(dataString)
                        

            # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock.sendto(dataString.encode('utf-8'), (UDP_IP, UDP_PORT))

while True:
    run()