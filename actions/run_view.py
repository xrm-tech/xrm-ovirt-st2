import base64
import os
import requests
import sys
from st2common.runners.base_action import Action

from lib.xrmcontroller import XRMBaseAction

__all__ = [
    'RunCmd'
]
CONTROLLER_ADDRESS = "http://st2:459Qdr_@xrm-controller:8080/ovirt/view/"

class RunDelete(XRMBaseAction):

    def run(self, plan_name):
        addr = ONTROLLER_ADDRESS
        if plan_name != "":
            addr = CONTROLLER_ADDRESS+plan_name+"/"
        req = self.session.get(addr)
        print("status", req.status_code)
        print(req.text)

        if req.status_code == 200:
            return True
        else:
            sys.exit(1)
            return False
