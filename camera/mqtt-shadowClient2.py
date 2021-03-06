from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

# For certificate based connection
myShadowClient = AWSIoTMQTTShadowClient("myClientID")

# Basic ops
myShadowClient.connect()

# Create a device shadow instance using persistent subscription
myDeviceShadow = myShadowClient.createShadowHandlerWithName("Bot", True)

# Shadow operations
myDeviceShadow.shadowGet(customCallback, 5)
myDeviceShadow.shadowUpdate(myJSONPayload, customCallback, 5)
myDeviceShadow.shadowDelete(customCallback, 5)
myDeviceShadow.shadowRegisterDeltaCallback(customCallback)
myDeviceShadow.shadowUnregisterDeltaCallback()

# To retrieve MQTTClient to perform plain MQTT ops along with shadow ops
myMQTTClient = myShadowClient.getMQTTConnection()
myMQTTClient.publish("plainMQTTTopic", "Payload", 1)

# Progressive Reconect Backoff
# When non-client-side disconnect occurs, SDK will auto-reconnect
AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTShadowClient.configureAutoReconnectBackoffTime(baseReconnectQuietTimeSecond, maxReconnectQuietTimeSecond, stableConnectionTimeSecond)
# Defaults:
# baseReconnectQuietTimeSecond = 1;
# maxReconnectQuietTimeSecond = 32;
# stableConnectionTimeSecond = 20;
