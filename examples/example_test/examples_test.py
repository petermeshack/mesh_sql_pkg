from mesh_sql.database import database_connect


class Test:
    def __init__(self):
        super().__init__()

        self.db = database_connect("ltd_my_jobs.db")
        self.db.create_db()
        self.table_name = "table_test"
        if self.db:
            try:

                self.db.create_table(self.table_name,
                                     "ID INT PRIMARY KEY NOT NULL," +
                                     "NAME TEXT NOT NULL," +
                                     "AGE INT NOT NULL," +
                                     "ADDRESS CHAR(50)," +
                                     "SALARY REAL")
                print(f"table doesnt exist \n created new table: {self.table_name}\n")
                self.add_to_database()
                self.update_exisiting_data()
            except:
                print("table already exists")
                self.add_to_database()
                self.update_exisiting_data()
                self.delete_values()
                self.display()

        self.db.close_db()

    def add_to_database(self):
        try:
            self.db.insert_to_db(table_name=self.table_name,
                                 table_fields="ID,NAME,AGE,ADDRESS,SALARY",
                                 content="4,'Paul',32,'California',20000.00")
        except:
            print("command error:add")
            print("error: the ID of Primary Key already exists or \n some fields are left empty or\n omission and "
                  "misspelled table fields\n")


    def update_exisiting_data(self):
        try:
            self.db.update_table(table_name=self.table_name,
                                 table_fields="SALARY",
                                 command_content="26000.00 where ID = 1")

        except Exception as e:
            print("command error:update")
            print("error: the ID of Primary Key DOESN'T exists or \n some fields are left empty or\n omission and "
                  "misspelled table fields\n")
            print(e)


    def delete_values(self):
        try:
            self.db.dalete_fields(table_name=self.table_name,
                                  command_content="where ID = 2")
        except:
            print("command error:delete")
            print("error: the ID/RECORD of Primary Key DOESN'T exists or \n some fields are left empty or\n omission "
                  "and misspelled table fields\n")


    def display(self):
        try:
          self.display_all_db_info(table_name=self.table_name, command_content="SELECT id, name, address, salary")

        except:
            print("command error: display")

    """display what is on db to console"""
    def display_all_db_info(self,table_name,command_content=[]):
            self.table_name = table_name.upper()
            cursor = self.db.conn.execute(f"{command_content} from {self.table_name}")
            for row in cursor:
                print("----------------------------------------------------------------")
                print("ID = ", row[0], "|", "NAME = ", row[1], "|", "ADDRESS = ", row[2], "|", "SALARY = ", row[3])
                print("----------------------------------------------------------------")
            print("Operation done successfully")