import sys
sys.path.append("C:\\Users\\drapi\\OneDrive\\Bureau\\GitHub\\network")

import sqlite3
import database

class database_test():
    def __init__(self):
        self.database = database.Database()

    def create_database(self):
        self.database.create_database_and_table()
    
    def insert_user(self, user_name, ip, port):
        self.database.insert_user( user_name, ip, port)
    
    def delete_user(self, ip):
        self.database.delete_user(ip)
    
    def check_user_name(self, name):
        self.database.check_username(name)
    
    def delete_table(self, name_of_table):
        self.database.delete_table(name_of_table)
    
    def search_port_by_user_name(self, name):
        print(self.database.search_port_by_user_name(name))

objet = database_test()
objet.create_database()
# objet.insert_user("Thomas", "192.168.160.12", 5000)
# objet.delete_user("192.168.1.60.12")
# objet.check_user_néame("Tfhomas")
# objet.delete_table('active_users')
# objet.search_port_by_user_name("mathis")