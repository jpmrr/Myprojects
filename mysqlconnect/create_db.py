#!/usr/bin/python
import sys
import socket
import re
import os
import datetime
from subprocess import PIPE, Popen
import mysql.connector
from mysql.connector import errorcode


class create_db:
	def __init__(self, DB_NAME):
		self.DB_NAME = DB_NAME
		self.cnx = mysql.connector.connect(user='root', password='Oracle@123', host='127.0.0.1')
		self.cursor = self.cnx.cursor()



	def create_database(self, cursor):
	    try:
	        cursor.execute(
	            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
	    except mysql.connector.Error as err:
	        print("Failed creating database")
	        exit(1)

	def use_db(self):
		try:
	    	    self.cursor.execute("USE {}".format(self.DB_NAME))
		except mysql.connector.Error as err:
	    	    print("Database does not exists")
	    	    if err.errno == errorcode.ER_BAD_DB_ERROR:
	        	self.create_database(self.cursor)
	        	print("Database created successfully.")
	        	self.cnx.database = self.DB_NAME
	    	    else:
	        	print(err)
	        	exit(1)


db1=create_db("test_db")
db1.use_db()
db2=create_db("jpm_db")
db3=create_db("oca_db")
db2.use_db()
db3.use_db()
