#from SGDB import *
from sqlite3 import dbapi2 as SQLite
import xmlrpclib as XMLRPCLib
from SimpleXMLRPCServer import SimpleXMLRPCServer

#AUTH_CAN_READ = 0
#AUTH_CAN_WRITE_TEXTANALYSIS = 1
#AUTH_CAN_WRITE_CRCS = 2
#AUTH_CAN_WRITE_CALENDAR

class DataBaseController:
    def __init__(self, port, dataBaseName):
        self.port = port
        self.host = "localhost"
        self.server = SimpleXMLRPCServer((self.host, self.port))
        self.dataBase = SQLite.connect(dataBaseName + ".db")
        self.server.register_instance(self)
        self.cursor = self.dataBase.cursor()
        
    def connect(self,user,password):
        #CE BLOC N'EST QU'UN EXEMPLE DE L'UTILISATION
        cursor = self.dataBase.cursor()
        cursor.execute("SELECT id FROM users WHERE name = ? AND password = ?", (user, password))
        users = cursor.fetchall()
        if len(users) == 0:
            return False
        id = users[0]
        cursor.execute("SELECT project_id FROM project_auths WHERE user = ? AND auth = ?", (id, AUTH_CAN_READ))
        ids = []
        for row in cursor:
            ids.append(row['project_id'])
        cursor.execute("SELECT name FROM projects WHERE id IN(?)", (ids))
        return cursor.fetchall()
    
    def runCommand(self,text):
        self.cursor.execute(text);
        
    def save(self,project):
        pass
    
    def load(self,projectName):
        #return project from SQL
        pass
    
    def delete(self,projectName):
        pass
    
if __name__ == '__main__':
    dataBaseController = DataBaseController(127,"test");
    dataBaseController.runCommand("CREATE TABLE test (id INTEGER PRIMARY KEY, name VARCHAR(50), email VARCHAR(50))")
        