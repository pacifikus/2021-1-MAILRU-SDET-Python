import allure
import pytest

import test_settings


class TestAPI:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, auth_socket_client, mysql_builder):
        self.client = auth_socket_client
        self.mysql_builder = mysql_builder

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with valid data')
    @pytest.mark.API
    def test_add_user(self, userdata):
        headers = {'Content-Type': 'application/json'}
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert userdata['username'] in self.mysql_builder.get_users()
        assert response['status_code'] == 201

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with invalid username')
    @pytest.mark.API
    @pytest.mark.parametrize('invalid_username', ['', '11', 'q' * 17])
    def test_add_user_with_invalid_name(self, userdata, invalid_username):
        headers = {'Content-Type': 'application/json'}
        userdata['username'] = invalid_username
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert userdata['username'] not in self.mysql_builder.get_users()
        assert response['status_code'] == 400

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with invalid password')
    @pytest.mark.API
    @pytest.mark.parametrize('invalid_pass', ['', 'q' * 300])
    def test_add_user_with_invalid_pass(self, userdata, invalid_pass):
        headers = {'Content-Type': 'application/json'}
        userdata['password'] = invalid_pass
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert userdata['username'] not in self.mysql_builder.get_users()
        assert response['status_code'] == 400

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with invalid email')
    @pytest.mark.API
    @pytest.mark.parametrize('invalid_email', ['', 'qwe', '@qweqweqwe.ru', '.qwe@mail.ru', 'q' * 65])
    def test_add_user_with_invalid_email(self, userdata, invalid_email):
        headers = {'Content-Type': 'application/json'}
        userdata['email'] = invalid_email
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert userdata['username'] not in self.mysql_builder.get_users()
        assert response['status_code'] == 400

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with already existed email')
    @pytest.mark.API
    def test_add_user_with_exists_email(self, userdata):
        headers = {'Content-Type': 'application/json'}
        userdata['email'] = test_settings.ADMIN_EMAIL
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert userdata['username'] not in self.mysql_builder.get_users()
        assert response['status_code'] == 400

    @allure.epic('API tests')
    @allure.feature('User adding')
    @allure.title('Add user with already existed username')
    @pytest.mark.API
    def test_add_exists_user(self, userdata):
        headers = {'Content-Type': 'application/json'}
        userdata['username'] = test_settings.ADMIN_USER
        response = self.client.request(
            '/api/add_user',
            'POST',
            headers=headers,
            data=userdata
        )
        assert response['status_code'] == 304

    @allure.epic('API tests')
    @allure.feature('Application status')
    @allure.title('Try to obtain app status')
    @pytest.mark.API
    def test_status(self):
        response = self.client.request(
            '/status',
            'GET'
        )
        assert response['status_code'] == 200

    @allure.epic('API tests')
    @allure.feature('User deleting')
    @allure.title('Delete existed user')
    @pytest.mark.API
    def test_delete_user(self, added_user):
        response = self.client.request(
            f'/api/del_user/{added_user["username"]}',
            'GET'
        )
        assert added_user['username'] not in self.mysql_builder.get_users()
        assert response['status_code'] == 204

    @allure.epic('API tests')
    @allure.feature('User deleting')
    @allure.title('Delete unexisted user')
    @pytest.mark.API
    def test_delete_unexisting_user(self):
        invalid_username = 'user_does_not_exist'
        response = self.client.request(
            f'/api/del_user/{invalid_username}',
            'GET'
        )
        assert response['status_code'] == 404

    @allure.epic('API tests')
    @allure.feature('User blocking')
    @allure.title('Block unblocked user')
    @pytest.mark.API
    def test_block_user(self, added_user):
        response = self.client.request(
            f'/api/block_user/{added_user["username"]}',
            'GET'
        )
        assert self.mysql_builder.get_user_by_name(added_user['username']).access == 0
        assert response['status_code'] == 200

    @allure.epic('API tests')
    @allure.feature('User blocking')
    @allure.title('Block already blocked user')
    @pytest.mark.API
    def test_block_already_blocked_user(self, blocked_user):
        response = self.client.request(
            f'/api/block_user/{blocked_user["username"]}',
            'GET'
        )

        assert self.mysql_builder.get_user_by_name(blocked_user['username']).access == 0
        assert response['status_code'] == 304

    @allure.epic('API tests')
    @allure.feature('User unblocking')
    @allure.title('Unlock blocked user')
    @pytest.mark.API
    def test_unblock_user(self, blocked_user):
        response = self.client.request(
            f'/api/accept_user/{blocked_user["username"]}',
            'GET'
        )
        print(self.mysql_builder.get_user_by_name(blocked_user['username']))
        assert self.mysql_builder.get_user_by_name(blocked_user['username']).access == 1
        assert response['status_code'] == 200

    @allure.epic('API tests')
    @allure.feature('User unblocking')
    @allure.title('Unlock unblocked user')
    @pytest.mark.API
    def test_unblock_added_user(self, added_user):
        response = self.client.request(
            f'/api/accept_user/{added_user["username"]}',
            'GET'
        )
        assert self.mysql_builder.get_user_by_name(added_user['username']).access == 1
        assert response['status_code'] == 304

    @allure.epic('API tests')
    @allure.feature('Login')
    @allure.title('Try to login')
    @pytest.mark.API
    def test_login(self, socket_client):
        socket_client.login_mode = True
        response = socket_client.login()
        assert response['status_code'] == 302
        assert response['cookies'] != ''
