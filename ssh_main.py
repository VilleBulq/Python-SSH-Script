import paramiko
import logging
import sys
import time

logging.basicConfig(filename=sys.argv[1],level=logging.DEBUG)
class SSH:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    def connect(self):
        try:
            self.ssh.connect(self.host, 22, self.username, self.password)
            print "[*] Connection to:", self.host
            logging.debug("SSH yhteys:" + str(self.host))
            
        except Exception, e:
            print e, logging.warning(e)

    def ex_command(self, command):
        stdin , stdout, stderr = self.ssh.exec_command(command)
        try:
            output = stdout.readlines()
            if output:
                for f in output:
                    print f.strip("\n")

            self.ssh.close()
        except Exception, e:
            e, logging.warning(e)

def config(file):
    f = open(file, "r")
    cred = []
    for j in f:
        cred.append(j)
    SSH(cred[0], cred[1], cred[2])
            


    


