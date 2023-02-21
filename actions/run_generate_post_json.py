import base64
import os
import requests
from st2common.runners.base_action import Action

from lib.xrmcontroller import XRMBaseAction

__all__ = [
    'RunCmd'
]


class RunGenerate(XRMBaseAction):

    def run(self, address):
        #self.login()
        data = {"site_primary_url": self.config['01_site_primary_url'],\
                "site_primary_username": self.config['02_site_primary_username'],\
                "site_primary_password": self.config['03_site_primary_password'],\
                "site_secondary_url": self.config['04_site_secondary_url'],\
                "site_secondary_username": self.config['05_site_secondary_username'], \
                "site_secondary_password": self.config['06_site_secondary_password']}
                
        req = self.session.post(address, data=data)
        print(req.text)

        #print (self.config['01_site_primary_url'])
        #print (self.config['02_site_primary_username'])
        #print (self.config['03_site_primary_password'])
        

        return True
