/*
 Basic ESP8266 MQTT example

 This sketch demonstrates the capabilities of the pubsub library in combination
 with the ESP8266 board/library.

 It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off

 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.

 To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <stdlib.h>
#include <ArduinoJson.h>
#include <MqttClient.h>
#include <WiFiUdp.h>
#include <NTPClient.h>

#define NTP_OFFSET   60 * 60      // Offset to Local Time in seconds
#define NTP_INTERVAL 60 * 1000    // Update time in miliseconds
#define NTP_ADDRESS  "europe.pool.ntp.org"

// Update these with values suitable for your network.

const char *ssid = "pieterse";
const char *password = "yours246";
const char *mqtt_server = "192.168.1.5";
const int sensor_pin = A0;
float sensorReading = 0;
float pubValue = 0;
float formattedTime = 0;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "2.za.pool.ntp.org", 7200, 60000);
WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {
      Serial.begin(115200);
      setup_wifi();
      client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
    // We start by connecting to a WiFi network
      delay(10);
      Serial.println();
      Serial.print("Connecting to Wifi - ");
      Serial.println(ssid);
      WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
}
      Serial.println("");
      Serial.println("WiFi connected");
      Serial.println("IP address: ");
      Serial.println(WiFi.localIP());
      timeClient.update();
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
      Serial.print("Attempting remote MQTT connection...");   // Connect to remote network
      client.setServer(mqtt_server, 1883);   
     
  // MQTT Connection Test Section
   if (client.connect("ESP8266Client")) {
      Serial.println("Connected to remote network ");
   }
    else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
         // Wait 5 seconds before retrying
      delay(5000);     
    }
  } 
    Sensor();
    Json();
}

float Sensor()  {  // Sensor Section  (Setup here for sensor)
  int sensor_analog;
      sensor_analog = analogRead(sensor_pin);
      sensorReading = ( 100 - ( (sensor_analog/1023.00) * 100 ) )/10;
      delay(5000); // delay 5 seconds before next write  
 
      pubValue = sensorReading;
      return pubValue; 
   }

void Json() {             //Json create Object script
     StaticJsonBuffer<300> jsonBuffer;
     JsonObject& root = jsonBuffer.createObject();
char JSONmessageBuffer[150];  // see https://techtutorialsx.com/2017/04/29/esp32-sending-json-messages-over-mqtt/  
 String formattedTime = timeClient.getFormattedTime();
     root["SensorID"] = "S_M";
     root["SensorData"] = pubValue;
     root["DateNTime"] = formattedTime;
     root.printTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
     client.publish("outTopic", JSONmessageBuffer);
     Serial.println(JSONmessageBuffer);            // prints Json string
 
  if (client.publish("outTopic", JSONmessageBuffer) == true) {
     Serial.println("Success sending message"); 
     Serial.println(" "); 
} 
  else {
     Serial.println("Error sending message");
     Serial.println("");
}
     client.loop();
  }  

void loop() {
     
  
  if (!client.connected()) {
     reconnect();
  }
  }
