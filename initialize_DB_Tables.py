#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import sqlite3

# SQLite DB Name
DB_Name =  "IoTN.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists Sensor_Data ;
create table Sensor_Data (                  //For first sensor
  id integer primary key autoincrement,
  SensorID text,
  SensorData text,
  DateNTime text
);


drop table if exists Sensor2_Data ;
create table Sensor2_Data (                 //For second sensor if required
  id integer primary key autoincrement,
  SensorID text,
  SensorData text,
  DateNTime text
);
"""

#Connect or Create DB File
conn = sqlite3.connect('/home/user/IoTN.db')    // Set up as required
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
