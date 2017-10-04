#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------


import json
import sqlite3

# SQLite DB Name
DB_Name =  "IoTN.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect('/home/neill/IoTN.db')  # Edit path as necessary
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save first sensor's data to DB Table
def sensor1_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['SensorID']
	Data_and_Time = json_Dict['Date_n_Time']
	SensorData = json_Dict['SensorData']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Sensor_Data (SensorID, Date_n_Time, SensorData) values (?,?,?)",[SensorID, Data_and_Time, SensorData])
	del dbObj
	print "Inserted First Sensor Data into Database."
	print ""

# Function to save second sensor's to DB Table
def sensor2_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['SensorID']
	Data_and_Time = json_Dict['Date_n_Time']
	Sensor2Data = json_Dict['Sensor2Data']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Sensor2_Data (SensorID, Date_n_Time, Sensor2Data) values (?,?,?)",[SensorID, Data_and_Time, Sensor2Data])
	del dbObj
	print "Inserted second sensor's data into Database."
	print ""
# Note Sensor_Data is the Table name, and SensorData is the field name.

#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "outTopic":
		sensor1_Data_Handler(jsonData)
	elif Topic =="outTopic2":
		sensor2_Data_Handler(jsonData)

#===============================================================
