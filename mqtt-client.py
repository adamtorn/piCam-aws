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

# Progressive Reconect Backoff
# When non-client-side disconnect occurs, SDK will auto-reconnect
AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.configureAutoReconnectBackoffTime(baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond)
# Defaults:
# baseReconnectQuietTimeSecond = 1;
# maxReconnectQuietTimeSecond = 32;
# stableConnectionTimeSecond = 20;
