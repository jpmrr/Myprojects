#!/usr/bin/python
import sys
import socket
import re
import os
import datetime
from subprocess import PIPE, Popen
import mysql.connector
from mysql.connector import errorcode
from create_db import *


TABLES = {}
#dbname="jpm_db"
class create_tb:
    def __init__(self, DB_NAME):
	self.DB_NAME = DB_NAME
        self.cnx = mysql.connector.connect(user='root', password='Oracle@123', host='127.0.0.1')
        self.cursor = self.cnx.cursor()

    def create_table(self):
	TABLES[self.DB_NAME] = ("CREATE TABLE `v_backups` (""id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY," "bbox VARCHAR(30) NOT NULL," "bbox_id int(11) NOT NULL," "server VARCHAR(30) NOT NULL," "server_id int(11) NOT NULL," "lvs  VARCHAR(60) NOT NULL"")")
	print TABLES

	for table_name in TABLES:
    	    table_description = TABLES[table_name]
    	    try:
       		print("Creating table")
		self.cursor.execute("USE {}".format(self.DB_NAME))
        	self.cursor.execute(table_description)
    	    except mysql.connector.Error as err:
        	if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            	    print("already exists.")
        	else:
            	    print(err.msg)
    	    else:
        	print("OK")

	self.cursor.close()
	self.cnx.close()



db1=create_db("jpm3_db")
db1.use_db()
db=create_tb("jpm3_db")
db.create_table()
	
