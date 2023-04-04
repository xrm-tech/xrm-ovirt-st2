import base64
import os
import requests
from st2common.runners.base_action import Action

from lib.xrmcontroller import XRMBaseAction

__all__ = [
    'RunCmd'
]


class RunGenerate(XRMBaseAction):

    def parse_storage_to_json(self,primary_storages,secondary_storages):
        """
        Sample output:

        [
        { primary_type: "nfs", primary_path: "/nfs_dom", primary_addr: "192.168.0.1", secondary_type: "nfs", secondary_path: "/nfs_dom_replica", secondary_addr: "192.168.0.1" },
        { primary_type: "nfs", primary_path: "/nfs_dom", primary_addr: "192.168.0.1", secondary_type: "nfs", secondary_path: "/nfs_dom_replica", secondary_addr: "192.168.0.1" }
        ]
        """
        ret = []
        item = {}
        for stg in primary_storages.split(";"):
            try:
                type= stg.split("://")[0]
                addr = stg.split("://")[1].split(":")[0]
                path = "/"+stg.split(":/")[2].split("/")[0]
                #print (type +" "+ addr+" "+path)
                item={"primary_type":type,"primary_addr":addr,"primary_path":path}
                ret.append(item)
            except Exception as e:
                print("Exception in parse_storage_to_json: " + str(e))
        idx = 0
        for stg in secondary_storages.split(";"):
            try:
                type= stg.split("://")[0]
                addr = stg.split("://")[1].split(":")[0]
                path = "/"+stg.split(":/")[2].split("/")[0]
                #print (str(idx)+" "+type +" "+ addr+" "+path)
                ret[idx]["secondary_type"] = type;
                ret[idx]["secondary_addr"] = addr;
                ret[idx]["secondary_path"] = path;
            except Exception as e:
                print("Exception in parse_storage_to_json: " + str(e))
            idx+=1
        print (ret)
        return ret

    def run(self, address):
        #self.login()
        data = {"site_primary_url": self.config['01_site_primary_url'],\
                "site_primary_username": self.config['02_site_primary_username'],\
                "site_primary_password": self.config['03_site_primary_password'],\
                "site_secondary_url": self.config['04_site_secondary_url'],\
                "site_secondary_username": self.config['05_site_secondary_username'], \
                "site_secondary_password": self.config['06_site_secondary_password']}
        storage_data =  self.parse_storage_to_json(self.config['07_primary_storage'],self.config['08_secondary_storage'])      
        data["storage_domains"]=storage_data
        req = self.session.post(address, data=data)
        print(req.text)

        #print (self.config['01_site_primary_url'])
        #print (self.config['02_site_primary_username'])
        #print (self.config['03_site_primary_password'])
        

        return True
