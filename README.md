# esp82_json_mqtt_VPS
I built the system using an ESP12S to upload dynamic Json file data from a sensor to a MQTT server on a private VPS. The data was then written on an SQLite DB. It will also work on a local wireless network with a MQTT server and SQLite3.

This project gives a working framework that could easily be configured to write data from any type of sensor. 
The data, in this case, will be written to an SQLite database, hence the need for a Json file. My Json help came from https://techtutorialsx.com/2017/04/29/esp32-sending-json-messages-over-mqtt/ and my SQLite inspiration comes from Pradeesi at https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/comment-page-1/#comment-287, both of which have been a great help. 

For setting up the VPS files, I urge you to go the latter website for an excellent "How to..". The "Initialize, Listen and Store" files must be uploaded to the VPS. I placed them in my 'home/user/' directory (Ubuntu 16.04), but this is not strictly necessary.

Make sure that your data variables are the same from the ESP8266, to the DB and on to the "Store.." file on the VPS. Adjust the file variables for your specific sensor's data, although it will work 'as is'. NB: Make sure that all the data that is written to SQlite is in the correct ORDER (as in the DB) in all the files that handle it. If not, it will not write it to the relevant fields! 

"Initialise_.." creates the DB. In a terminal run "python store_..", then python mqtt_Listen_..". The latter will print out the data being written to the DB. 

I am not a professional programmer, so apologies any "strange" coding! The main thing is that it works and was a great learning experience! 

I never had a RTC, so I have used NTPClient to give the timestamp. It works well, although I still need to sort out the date.
