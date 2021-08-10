
import pygame
import dataformatter
import socket

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print('Initialized Joystick : %s' % j.get_name())

# IP OF RECEIVER
UDP_IP = "192.168.74.51"
UDP_PORT = 5555

while True:
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
            triangle = 0

            dataTranslator = dataformatter.JoystickDataPacketTranslator()
            dataString = dataTranslator.createDataString(l3x, l3y, r3x, r3y, l2, r2, l1, r1, triangle)
            print(dataString)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(dataString.encode('utf-8'), (UDP_IP, UDP_PORT))