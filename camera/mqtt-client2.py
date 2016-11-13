# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import AWSIoTPythonSDK
import os
import json
import logging
import ssl
import time
import subprocess

logging.basicConfig()

def customCallback(client, userdata, message):
    stuff = json.loads(message.payload)
    
dir_path = os.path.dirname(os.path.realpath(__file__))

offlinePublishQueueSize = 20
baseReconnectQuietTimeSecond = 1;
maxReconnectQuietTimeSecond = 32;
stableConnectionTimeSecond = 20;
queueSize = 20

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("linux_camera")

myMQTTClient.configureEndpoint("a27123o8bvt7qk.iot.us-west-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials(dir_path + "/auth_data/VeriSign-Class_203-Public-Primary-Certification-Authority-G5.pem.crt",
                                  dir_path + "/auth_data/cam-1621824b15-private.pem.key",
                                  dir_path + "/auth_data/cam-1621824b15-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myMQTTClient.configureAutoReconnectBackoffTime(baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond)

# Progressive Reconect Backoff
# When non-client-side disconnect occurs, SDK will auto-reconnect
# Defaults:

# Drop the newest request in the queue
AWSIoTPythonSDK.MQTTLib.DROP_NEWEST = 1

# Offline Publish Requests Queueing with Draining
# If client temp offline and disconnected due to network failure, 
# publish requests will be added to internal queue until num reaches size limit of queue
AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.configureOfflinePublishQueueing(myMQTTClient, queueSize, AWSIoTPythonSDK.MQTTLib.DROP_NEWEST)


# Configure size of offlinePublishQueue to 5
myMQTTClient.configureOfflinePublishQueueing(5, AWSIoTPythonSDK.MQTTLib.DROP_NEWEST);


# Basic MQTT operations
myMQTTClient.connect(2000)
myMQTTClient.subscribe("iot-camera/shadow/update", 1, customCallback)
time.sleep(2)

# while 1:
myMQTTClient.publish("iot-camera/shadow/update", "hi leonela :)", 1)
time.sleep(2)
# myMQTTClient.unsubscribe("#aws/things/iot-camera/shadow/update")
# myMQTTClient.disconnect()

