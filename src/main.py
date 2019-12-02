###############################################################################
###
###    Utilitários oara: subir contêineres e subir/criar/testar bd
###
###############################################################################

import sys
import docker
import phoenixdb

class CrawlerManager:
    client = None #client = docker.from_env()
    dbconn = None
    dburl = 'http://localhost:8765/'
    
    def __init__(self):
        try:
            self.client = docker.from_env()
            self.dbconn = phoenixdb.connect(self.dburl, autocommit=True)
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            sys.exit(1)      
    
    def listRunningContainers(self):
        client = docker.from_env()
        for container in client.containers.list():
            print(container.id)
            
    #def createDatabase(self):
    
    #def startDatabase(self):
        
    #def testDatabase(self):
        
            