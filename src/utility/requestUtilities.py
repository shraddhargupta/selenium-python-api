
from allapitest.src.configs.hosts_config import API_HOSTS
import os
import  requests
class RequestUtilities(object):

    def __init__(self):

        self.env=os.environ.get('ENV','test')
        self.base_url=API_HOSTS[self.env]

    def post(self,endpoint,payload=None,headers=None,expected_status_code=200):

        if not headers:
            headers={"Content-Type":"application/json"}
        url=self.base_url+endpoint
        rs_api=requests.post(url=url,data=payload, headers=headers)
        self.status_code=rs_api.status_code
        assert self.status_code==int(expected_status_code),\
        f'Expected status code{expected_status_code} but actual {self.status_code}'
        return rs_api.json()


    def get(self):
        pass

    def delete(self):
        pass


