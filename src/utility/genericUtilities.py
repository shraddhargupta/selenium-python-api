import logging as logger
import configparser

def generate_randm_email_and_passport(domain=None,email_prefix=None):
    logger.debug("Generating random email and password")


def read_config_details(apiName, configFilePath):
    config = configparser.RawConfigParser()
    config.read(configFilePath)
    details_dict = dict(config.items(apiName))
    return details_dict



def write_response_file(filepath,filename,fileContent):
    f = open(filepath+filename, "w")
    f.write(fileContent)
    f.close()


def read_payload(filename):
    f = open(filename, "r")
    file_content=f.read()
    f.close()
    return file_content