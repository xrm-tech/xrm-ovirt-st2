import base64
import os
import requests
from st2common.runners.base_action import Action

__all__ = [
    'RunCmd'
]


class RunCmd(Action):

    def run(self, address):
        print (self.config['01_site_primary_url'])
        print (self.config['02_site_primary_username'])
        print (self.config['03_site_primary_password'])
        return True
