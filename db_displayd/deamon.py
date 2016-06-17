#!/usr/bin/env python3
# from config.py import LEAFS
import socket
import time
from serial import Serial, time
import paho.mqtt.client as mqtt
import subprocess

client = None
sock = None


def setup():
    print("Starting db_displayd")
    global client
    client = mqtt.Client(client_id="piui_c-base")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("msggwt1.service.deutschebahn.com", 1905, 60)
    print("Connected to MQTT")
    global sock
    sock = None  # todo



def main():
    time.sleep(1000)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$PIUI/#")
    client.subscribe("$PIUI/display/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # decode this


def list():
    pass


def switch(drum, leaf):
    pass


def reset(drum):
    pass


if __name__ == "__main__":
    setup()
    client.loop_forever()
