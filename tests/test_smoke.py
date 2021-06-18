import pytest
import logging as logger

from allapitest.src.main.BaseTemplate import BaseTemplate


class TestNewFeature:
    def test_new(self):
        logger.debug('new class ')

        @pytest.mark.smoke
        def test_get_gmap():
            logger.info("Get Request for GMAP API is initiated ")
            print("Get Request for GMAP API is initiated ")
            config_file_path = '/Users/shraddha/Documents/api-testing-python/allapitest/src/configs/host_config.cfg'
            api_response = BaseTemplate.get(config_file_path, 'new_get_response.txt')
            print("Response is generated from api ", api_response)
            # post_response=BaseTemplate.post(config_file_path,'payload.txt','new_post_response.txt')


        @pytest.mark.smoke
        def test_login_page_invalid_user():
            print("Login with in valid user")
            print("bbbbbbbb")
