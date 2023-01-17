import base64
import os
import requests



from st2common.runners.base_action import Action

__all__ = [
    'RunCmd'
]


class RunCmd(Action):

    def run(self, status, media):
        return True
