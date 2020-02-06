
#!/usr/bin/python
import sys
import socket
import re
import os
import datetime
from subprocess import PIPE, Popen
import mysql.connector
from create_db import *
from mk_table import *

class backup_data(create_db):

        def __init__(self,DB_NAME, bbox, bbox_id, server='gator4001', mounts = 2):
		create_db.__init__(self, DB_NAME)
                self.bbox = bbox
                self.bbox_id = bbox_id
                self.server = server
                self.mounts = mounts
                self.node = "test"


        def     get_server_id(self):
                self.server_id = self.server[-4:]
                return (self.server_id)

        def get_lvs(self):
                lvs = []
                for i in range(mounts):
                    lvs.append(self.server+"_lve"+str(i))
                    self.lvs1 = ", ".join(lvs)



        def add_box_details(self):
                cnx = mysql.connector.connect(user='root', password='Oracle@123', host='127.0.0.1', database = self.DB_NAME )
                cursor = cnx.cursor()
                add_box = ("INSERT INTO v_backups " "(bbox, bbox_id, server, server_id, lvs)" "values ( %s, %s, %s, %s, %s)")
                data_box = (self.bbox, self.bbox_id, self.server, self.server_id, self.lvs1 )
                cursor.execute(add_box, data_box)
                cnx.commit()
                cursor.close()
                cnx.close()



db1=create_db("jpm3_db")
db1.use_db()
db=create_tb("jpm3_db")
db.create_table()

bbox = raw_input("Enter the backup server name: ")
bbox_id = raw_input("Enter the backup box id: ")
server = raw_input("Enter the server name: ")
mounts = int(raw_input("Enter the no.of mounts: "))

server_1 = backup_data("jpm3_db", bbox, bbox_id, server, mounts)
server_1.get_server_id()
server_1.get_lvs()
server_1.add_box_details()

