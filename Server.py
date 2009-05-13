#-*- coding: iso-8859-1 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from DataBaseController import *
import pickle

class Server:
    def __init__(self):
        self.dataBaseController = DataBaseController(127,"superzebre")
    
    def sendProject(self, serializedProject):
        project = pickle.loads(serializedProject)
        self.saveProject(project)
    
    def requestProjectLoad(self,projectName):
        serializedProject = self.dataBaseController.readValueFromKey("project",projectName)
        return serializedProject
    
    def saveProject(self,project):
        key = project.name
        value = pickle.dumps(project)
        self.dataBaseController.writeKeyValue("project",key,value)
    
    def getProjectNameList(self):
        return self.dataBaseController.getAllKeys("project")
    
if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8006),
                            requestHandler=SimpleXMLRPCRequestHandler,allow_none = True)
    server.register_introspection_functions()
    server.register_instance(Server())
    print "Server on"
    server.serve_forever()