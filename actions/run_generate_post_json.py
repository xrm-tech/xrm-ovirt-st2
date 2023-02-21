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
        data = {"service": "1", "id": "2", "action": "3"}
        req = self.session.post(address, data=data)
        print(req)

        #print (self.config['01_site_primary_url'])
        #print (self.config['02_site_primary_username'])
        #print (self.config['03_site_primary_password'])

        return True
