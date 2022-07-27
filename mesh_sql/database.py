#!/usr/bin/python

import sqlite3

DEBUG = True


class database_connect:
    def __init__(self, db_name="test.db", parent=None):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)

    try:
        def start_db(self):
            DEBUG: print("create database")
            self.conn= sqlite3.connect(self.db_name)

        def create_db(self):
            # create database
            if self.conn != None:
                DEBUG: print("database is created")
                DEBUG: print("Opened database successfully")
            else:
                DEBUG: print("database is not created")
                DEBUG: print("database failed to open")

        def close_db(self):
            DEBUG: print("close database")
            self.conn.close()

        def create_table(self, table_name, content=[]):
            self.table_name = table_name.upper()
            self.keys = range(1)
            fields = {}
            for i in self.keys:
                DEBUG: print("index: ", i, "content: ", content)
                self.conn.execute(f'''CREATE TABLE {self.table_name}
                            ({content});''')
                # print("Table created successfully")

        def insert_to_db(self, table_name, table_fields, content=[]):
            self.table_name = table_name.upper()
            self.table_fields = table_fields.upper()
            self.conn.execute(f"INSERT INTO {self.table_name} ({self.table_fields}) \
                     VALUES ({content} );");
            self.conn.commit()
            DEBUG: print("Records created successfully")

        def update_table(self,table_name, table_fields, command_content=[]):
            self.table_name = table_name.upper()
            self.table_fields = table_fields.upper()
            self.conn.execute(f"UPDATE {self.table_name} set {self.table_fields} = {command_content};")
            self.conn.commit()
            print("Total number of rows updated :", self.conn.total_changes)

        def dalete_fields(self,table_name, command_content=[]):
            self.table_name = table_name.upper()
            self.conn.execute(f"DELETE from {self.table_name} {command_content};")
            self.conn.commit()
            print("Total number of rows deleted :", self.conn.total_changes)

    except sqlite3.OperationalError as e:
        DEBUG: print("database failed to open")
        DEBUG: print(e)
