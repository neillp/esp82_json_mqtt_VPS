#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler   # The SDH is in store_Sensor_Data_to_DB.py

# MQTT Settings 
MQTT_Broker = "VPS IP"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "outTopic"   # Edit to relevant topic

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, flags, rc):
	mqttc.subscribe(MQTT_Topic, 0)  # Edit topic

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "Sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print "MQTT Data Received..."
	print "MQTT Topic: " + msg.topic  
	print "Data: " + msg.payload
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
