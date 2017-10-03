# esp82_json_mqtt_VPS
Built the system using an ESP12S to upload dynamic Json file data from a sensor to a MQTT server on a private VPS.
This project gives a working framework that could easily be configured to write data from any type of sensor. 
The data, in this case, will be written to an SQLite database, hence the need for a Json file. My Json help came from https://techtutorialsx.com/2017/04/29/esp32-sending-json-messages-over-mqtt/ and my SQLite inspiration comes from https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/comment-page-1/#comment-287, both of which have been a great help.

I am not a professional programmer, so apologies any "strange" coding! The main thing is that it works and was a great learning experience!

