# piCam-AWS-IOT-SDK-py
MLH Southwest Regional Hackathon Team Project

# What it does
It uses an ultrasonic sensor paired with a camera to detect any unusual activity or possible intruders in enclosed shared community spaces such as apartment hallways or corridors.

# How we built it
Connected Arduino reads ultrasonic sensor data and converts it into binary. This transfers to the Raspberry Pi by means of 8 digital io pins. That real time data is processed in Python on the Raspberry Pi to redetermine spatial data in order to detect a possible intruder at each metaphorical house / apartment door. That data is transmitted via MQTT protocols to Amazon Web Services Internet of Things (AWS IoT) with modified device SDKs for Python. AWS IoT, as broker and subscriber to the device, receives the incoming data and then triggers a message to both the camera and the mobile user endpoint. The camera receives the incoming signal which triggers a snapshot of the environment. The mobile user endpoint receives an SMS direct message alerting of a possible intruder via Amazon Simple Notification Service (SNS) which is configured to discern incoming spatial data and relates it to the specific resident (mobile user). The user then has the opportunity to either respond to the message with a security code to turn off the false alarm. If the user does not manage to do so, chooses or fails to shut it off otherwise, the end goal would be to alert authorities by VoIP means. However, this step was yet to be determined.

# Challenges we ran into
Various. Started off with IBM IoT Platform and Bluemix for starters, then decided against it and went with AWS.

# @leonel_ai role
I worked on configuring Amazon Web Services (AWS) IoT platform to successfully communicate with interconnected devices (things). From MQTT protocols and the application of an AWS IoT specific SDK for Python between the Raspberri Pi + Arduino module and camera to pushing data to subscribers via Amazon SNS, I worked on maintaining cohesion and data integrity throughout the project.
