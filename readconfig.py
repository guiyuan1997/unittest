import os
import configparser
prodir = os.path.split(os.path.abspath(__file__))[0]
configpath = os.path.join(prodir,"config")
class read_config():
    cf = configparser.ConfigParser()
    cf.read(configpath)
    def get_http(self):
        host = self.cf.get("HTTP","host")
        port = self.cf.get("HTTP","port")
        return dict(host = host , port =port)