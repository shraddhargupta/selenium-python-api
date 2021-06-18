import json
import requests
from allapitest.src.utility import genericUtilities

#BaseTemplate: This will serve as Base for all api requests .

class BaseTemplate:

    def get(config_filename, response_filename):
        api_general_details = genericUtilities.read_config_details('API', config_filename)
        api_get_details = genericUtilities.read_config_details('GET-API', config_filename)
        base_url = api_general_details['base-url']
        get_uri = api_get_details['uri']
        param_list = api_get_details['parameter'].split(',')
        final_param = ''
        for param_pair in param_list:
            final_param += '&'+param_pair.replace(':', "=")
        url = base_url + get_uri + "?" + final_param
        rs_api = requests.get(url)
        genericUtilities.write_response_file(api_general_details['output-dir'], response_filename, rs_api.text)
        return rs_api.json()

    def post(config_filename,payload_filename,response_filename):
        api_general_details = genericUtilities.read_config_details('API', config_filename)
        api_post_details = genericUtilities.read_config_details('POST-API', config_filename)
        file_content = genericUtilities.read_payload(api_post_details['input-dir'] + payload_filename)
        json.loads(file_content)
        base_url = api_general_details['base-url']
        get_uri = api_post_details['uri']
        param_list = api_post_details['parameter'].split(',')
        final_param = ''
        for param_pair in param_list:
            final_param += param_pair.replace(':', "=")
        url = base_url + get_uri + "?" + final_param
        headers_list=api_post_details['headers'].split(',')
        headers={}
        for header in headers_list:
            key=header.split(':')[0]
            value=header.split(':')[1]
            headers[key]=value
        rs_api = requests.post(url=url, data=file_content, headers=headers)
        genericUtilities.write_response_file(api_general_details['output-dir'],response_filename, rs_api.text)
        return rs_api.json()



