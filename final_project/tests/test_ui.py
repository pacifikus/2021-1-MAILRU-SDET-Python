import allure
import pytest

import test_settings
from base_case import BaseCase


@pytest.mark.usefixtures("screenshot_on_failure")
class TestAuthorization(BaseCase):
    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with correct data')
    @pytest.mark.UI
    def test_correct_login(self):
        username, password = test_settings.ADMIN_USER, test_settings.ADMIN_PASSWORD
        self.base_page.login(username, password)
        assert f'Logged as {test_settings.ADMIN_USER}' in self.driver.page_source
        assert self.mysql_builder.is_active(username)

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with incorrect login')
    @pytest.mark.UI
    def test_incorrect_login(self, random_string):
        username, password = random_string, test_settings.ADMIN_PASSWORD
        self.base_page.login(username, password)
        assert 'Invalid username or password'

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Try to auth with incorrect password')
    @pytest.mark.UI
    def test_incorrect_pass(self, random_string):
        username, password = test_settings.ADMIN_USER, random_string
        self.base_page.login(username, password)
        assert 'Invalid username or password'


@pytest.mark.usefixtures("screenshot_on_failure")
class TestRegistration(BaseCase):
    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with correct data')
    @pytest.mark.UI
    def test_correct_registration(self, userdata):
        self.registration_page.register(userdata)
        assert f'Logged as {userdata["username"]}' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with invalid username')
    @pytest.mark.UI
    @pytest.mark.parametrize('invalid_username', ['11', 'q' * 17])
    def test_incorrect_username(self, userdata, invalid_username):
        userdata['username'] = invalid_username
        self.registration_page.register(userdata)
        assert f'Incorrect username length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with too long password')
    @pytest.mark.UI
    def test_incorrect_password_length(self, userdata):
        userdata['password'] = 'q' * 300
        self.registration_page.register(userdata)
        assert f'Incorrect password length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with incorrect email')
    @pytest.mark.UI
    @pytest.mark.parametrize('invalid_email', ['qweqwe', '@qweqweqwe.ru', '.qwe@mail.ru'])
    def test_incorrect_email(self, userdata, invalid_email):
        userdata['email'] = invalid_email
        self.registration_page.register(userdata)
        assert f'Invalid email address' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with already existed email')
    @pytest.mark.UI
    def test_doubled_email(self, userdata):
        userdata['email'] = test_settings.ADMIN_EMAIL
        self.registration_page.register(userdata)
        assert f'Passwords must match' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with invalid email length')
    @pytest.mark.UI
    @pytest.mark.parametrize('invalid_email', ['', 'q.ru', 'q' * 65])
    def test_invalid_email_length(self, userdata, invalid_email):
        userdata['email'] = invalid_email
        self.registration_page.register(userdata)
        assert f'Incorrect email length' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with different password and confirmation')
    @pytest.mark.UI
    def test_different_password_confirmation(self, userdata, random_string):
        userdata['pass_repeat'] = random_string
        self.registration_page.register(userdata)
        assert f'Passwords must match' in self.driver.page_source

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register without accept')
    @pytest.mark.UI
    def test_if_not_accept(self, userdata):
        self.registration_page.register_without_accept(userdata)
        assert self.registration_page.is_registration_page()

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Try to register with empty required fields')
    @pytest.mark.UI
    @pytest.mark.parametrize('empty_field', ['username', 'password', 'email', 'pass_repeat'])
    def test_empty_fields(self, userdata, empty_field):
        userdata[empty_field] = ''
        self.registration_page.register(userdata)
        assert self.registration_page.is_registration_page()

    @allure.epic('UI tests')
    @allure.feature('Registration')
    @allure.title('Go to login page')
    @pytest.mark.UI
    def test_go_to_login(self):
        self.registration_page.go_to_login()
        assert self.driver.current_url == \
               f'http://{test_settings.APP_HOST}:{test_settings.APP_PORT}/login'


@pytest.mark.usefixtures("screenshot_on_failure")
class TestMainPage(BaseCase):

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to api page')
    @pytest.mark.UI
    def test_go_to_api(self):
        self.account_page.go_to_api()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://en.wikipedia.org/wiki/API'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to internet page')
    @pytest.mark.UI
    def test_go_to_internet(self):
        self.account_page.go_to_internet()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               "https://www.popularmechanics.com/" \
               "technology/infrastructure/a29666802/future-of-the-internet/"

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to SMTP page')
    @pytest.mark.UI
    def test_go_to_smtp(self):
        self.account_page.go_to_smtp()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               "https://ru.wikipedia.org/wiki/SMTP"

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to home page')
    @pytest.mark.UI
    def test_go_to_home(self):
        self.account_page.go_to_home()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               f'http://{test_settings.APP_HOST}:{test_settings.APP_PORT}/welcome/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to python page')
    @pytest.mark.UI
    def test_go_to_python(self):
        self.account_page.go_to_python()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://www.python.org/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to python history page')
    @pytest.mark.UI
    def test_go_to_python_history(self):
        self.account_page.go_to_python_history()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://en.wikipedia.org/wiki/History_of_Python'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to flask page')
    @pytest.mark.UI
    def test_go_to_flask(self):
        self.account_page.go_to_flask()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://flask.palletsprojects.com/en/1.1.x/#'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to centos page')
    @pytest.mark.UI
    def test_go_to_centos(self):
        self.account_page.go_to_centos()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert 'Centos7' in self.driver.title

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to news page')
    @pytest.mark.UI
    def test_go_to_news(self):
        self.account_page.go_to_news()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://www.wireshark.org/news/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to download page')
    @pytest.mark.UI
    def test_go_to_download(self):
        self.account_page.go_to_download()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://www.wireshark.org/#download'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Go to examples page')
    @pytest.mark.UI
    def test_go_to_examples(self):
        self.account_page.go_to_examples()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == \
               'https://hackertarget.com/tcpdump-examples/'

    @allure.epic('UI tests')
    @allure.feature('Main page')
    @allure.title('Check vk api on page')
    @pytest.mark.UI
    def test_vk_id_appear(self):
        assert 'VK ID: 0' in self.driver.page_source
