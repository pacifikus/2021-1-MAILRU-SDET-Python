import logging

import requests

logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 500


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        print(base_url)
        self.base_url = base_url
        self.session = requests.Session()

        self.csrf_token = None
        self.sessionid_gtp = None

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: '
                            f'COLLAPSED due to response size > '
                            f'{MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

    def _request(self, method, url, headers=None, data=None, json=None):
        res = self.session.request(method,
                                   url,
                                   data=data,
                                   json=json,
                                   headers=headers)
        return res

    @property
    def post_headers(self):
        return {'X-CSRFToken': self.csrf_token}

    @property
    def post_headers_1(self):
        return {'Content-Type': 'application/json; charset=UTF-8'}

    def get_token(self):
        url = 'https://target.my.com/csrf/'
        return self._request('GET', url).cookies['csrftoken']

    def post_login(self, user, password):
        url = 'https://auth-ac.my.com/auth'

        headers = {
            'Referer': 'https://target.my.com/',
        }

        data = {
            'email': user,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_'
                        'login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', url, headers=headers, data=data)

        self.csrf_token = self.get_token()
        return result

    def add_segment(self, name):
        url = 'https://target.my.com/api/v2/remarketing/segments.json'

        data = {
            'logicType': "or",
            'name': name,
            'pass_condition': 1,
            'relations': [
                {
                    'object_type': "remarketing_player",
                    'params': {
                        'type': "positive",
                        'left': 365,
                        'right': 0
                    }
                }
            ]
        }
        res = self._request('POST', url, headers=self.post_headers, json=data)
        print(res.json())
        return res

    def is_segment_exists(self, name):
        res = self._request('GET',
                            'https://target.my.com/api/v2'
                            '/remarketing/segments.json?limit=500')
        return name in [x['name'] for x in res.json()['items']]

    def remove_segment(self, name):
        res = self._request('GET',
                            'https://target.my.com/api/v2'
                            '/remarketing/segments.json?limit=500')
        segment_id = [x['id'] for x in res.json()['items']
                      if x['name'] == name][0]
        return self._request('DELETE',
                             f'https://target.my.com/api/v2'
                             f'/remarketing/segments/{segment_id}.json',
                             headers=self.post_headers)
