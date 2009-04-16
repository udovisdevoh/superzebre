#-*- coding: iso-8859-1 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Projet import *
# Creer un serveur
server = SimpleXMLRPCServer(("localhost", 8006),
                            requestHandler=SimpleXMLRPCRequestHandler,allow_none = True)
server.register_introspection_functions()

class Serveur(object):
    def __init__(self):
        self.User = []
        self.bd = ""#SGBD()
        self.numUser = 0
    def connect(self):
        self.numUser+=1
        self.User.append(self.numUser)
        return self.numUser
    def deconnect(self,numClient):
        self.User.remove(numClient)
    def save(self,projet,nomfic):
        self.bd.save(nomfic,projet)
    def load(self,nomProjet):
        projet = self.bd.load(nomProjet)
        return projet

server.register_instance(Serveur())
print "Server on"
server.serve_forever()
 
        