from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

# For certificate based connection
myShadowClient = AWSIoTMQTTShadowClient("myClientID")

# Basic operations
myShadowClient.connect()

# Create a device shadow instance using persistent subscription
myDeviceShadow = myShadowClient.createShadowHandlerWithName("Bot", True)

# Shadow operations
myDeviceShadow.shadowGet(customCallback, 5)
myDeviceShadow.shadowUpdate(myJSONPayload, customCallback, 5)
myDeviceShadow.shadowDelete(customCallback, 5)
myDeviceShadow.shadowRegisterDeltaCallback(customCallback)
myDeviceShadow.shadowUnregisterDeltaCallback()
