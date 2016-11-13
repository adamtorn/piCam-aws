# Spot Security: Module - Rasp Pi - AWS IoT
#!/usr/bin/python3
#initiate cmd: python3 iot-mqtt-subscriber.py          

#required libraries
import sys                                 
import ssl
import paho.mqtt.client as mqtt

# Called while client tries to establish connection with the server 
def on_connect(mqttc, obj, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

# Called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

# Called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

# Creating a client with client-id=mqtt-test
mqttc = mqtt.Client(client_id="mqtt-test")

mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

# Configure network encryption and authentication options. Enables SSL/TLS support.
# Add client-side certificates and enabling tlsv1.2 support as req'd by aws-iot service
mqttc.tls_set("/home/auth_data/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem.crt",
	            certfile="home/auth_data/mod-7ceea45e66-certificate.pem.crt",
	            keyfile="home/auth_data/mod-7ceea45e66-private.pem.key",
              tls_version=ssl.PROTOCOL_TLSv1_2, 
              ciphers=None)

# Connect to aws-account-specific-iot-endpoint
mqttc.connect("a27123o8bvt7qk.iot.us-west-2.amazonaws.com/things/iot-module/shadow", port=8883) #AWS IoT service hostname and portno

# Topic to publish to
mqttc.subscribe("$aws/things/iot-module/shadow/update", qos=1) #The names of these topics start with $aws/things/thingName/shadow."

# Auto handles reconnecting
mqttc.loop_forever()
