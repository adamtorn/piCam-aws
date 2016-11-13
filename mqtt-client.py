# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")

# Basic MQTT operations
myMQTTClient.connect()
myMQTTClient.publish("myTopic", "myPayload", 0)
myMQTTClient.subscribe("myTopic", 1, customCallback)
myMQTTClient.unsubscribe("myTopic")
myMQTTClient.disconnect()
