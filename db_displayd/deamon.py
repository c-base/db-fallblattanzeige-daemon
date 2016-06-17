#!/usr/bin/env python3
from config import LEAFS
from socket import Socket
from serial import Serial
import paho.mqtt.client as mqtt

client
sock

def setup():
    global client
    client = mqtt.Client(client_id="piui1")
    client.on_connect = on_connect
    client.on_message = on_message
    global sock
    sock = # todo


def main():
    '''Main Deamon loop'''
	

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$PIUI/#")
    client.subscribe("$PIUI/display/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)) # decode this
    output = subprocess.check_output(msg.payload) 
    # client.publish("$PIUI/out", payload=output, qos=0, retain=False)
	
def list():

def switch(drum, leaf):

def reset(drum):

