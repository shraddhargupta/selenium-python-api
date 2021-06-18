import pytest



@pytest.fixture(scope='module')
def my_setup():
    print(" ")
    print("<<<<>>>>>>>")


@pytest.mark.smoke
def test_login_page_valid_user(my_setup):
    print("Login with valid user")
    print("aaaaaaaa")

@pytest.mark.smoke
def test_login_page_invalid_user(my_setup):
    print("Login with in valid user")
    print("bbbbbbbb")