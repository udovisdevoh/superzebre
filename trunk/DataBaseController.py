#from SGDB import *
from sqlite3 import dbapi2 as SQLite
import xmlrpclib as XMLRPCLib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import base64

class DataBaseController:
    def __init__(self, port, dataBaseName):
        self.port = port
        self.host = "localhost"
        self.dataBase = SQLite.connect(dataBaseName + ".db")
        self.cursor = self.dataBase.cursor()
        try:
            self.runCommand("CREATE TABLE project (id TEXT, data TEXT)")
        except SQLite.OperationalError:
            print "warning! couldn't create table"
        
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
        
    def readValueFromKey(self,tableName,key):
        print "reading table " + tableName
        key = key.strip()
        key = key.lower()
        self.cursor.execute("SELECT data FROM '" + tableName + "' WHERE id = '" + key + "'")
        row = self.cursor.fetchone()
        if row == None:
            print "key " + key + " not found in table " + tableName
            return -1
        print "key " + key + " found in table " + tableName
        value = str(row[0])
        value = base64.urlsafe_b64decode(value)
        return value
    
    def writeKeyValue(self,tableName,key,value):
        value = base64.urlsafe_b64encode(value)
        key = key.strip()
        key = key.lower()
        self.cursor.execute("DELETE from '" + tableName + "' WHERE id = '" + key + "'");
        self.cursor.execute("REPLACE into '" + tableName + "' (id,data) values ('" + key + "','" + value + "');");
        self.dataBase.commit()
        
    def getAllKeys(self,tableName):
        keyList = []
        self.cursor.execute("SELECT id FROM '" + tableName + "' ORDER BY id")
        for row in self.cursor:
            print row[0]
            keyList.append(row[0])
        return keyList
    
if __name__ == '__main__':
    dataBaseController = DataBaseController(127,"superzebre");
    #dataBaseController.runCommand("CREATE TABLE test (id INTEGER PRIMARY KEY, name VARCHAR(50), email VARCHAR(50))")
    dataBaseController.readValueFromKey("project","mofo")
    dataBaseController.writeKeyValue("project", "mofo", "fdgfdghfd  fsg fdghfdhd fd")
    dataBaseController.getAllKeys("project")
    
    