from urllib.parse import urljoin

import requests


class ApiClientException(Exception):
    ...


class ResponseStatusCodeException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url

        self.username = username
        self.password = password

        self.session = requests.Session()

    def _request(self, method, location, headers, data=None, json=None, params=None, allow_redirects=True,
                 expected_status=200, jsonify=True):
        url = urljoin(self.base_url, location)  # urljoin заменяет весь url на location при необходимости

        response = self.session.request(method=method, url=url, headers=headers, data=data, json=json, params=params,
                                        allow_redirects=allow_redirects)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Expected code {expected_status}, but got {response.status_code}\n'
                                              f'Response history - {response.history}')
        if jsonify:
            json_response: dict = response.json()
            if json_response.get('bStateError', False):
                error = json_response['sErrorMsg']
                raise RespondErrorException(f'Request {url} return error : "{error}"')
            return json_response
        # print(response.text)

        return response

    def post_login(self):
        headers = {
            # "Referer": self.base_url
        }

        data = {
            'username': self.username,
            'password': self.password,
        }

        location = urljoin(self.base_url, 'login')
        try:
            login_request = self._request(method='POST', location=location, headers=headers, data=data,
                                          jsonify=False, expected_status=200)
            return login_request
        except ResponseStatusCodeException as exc:
            assert False, exc

    def post_user_create(self, name, surname, username, password, email, middlename=None):
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "name": name,
            "surname": surname,
            "middle_name": middlename,
            "username": username,
            "password": password,
            "email": email
        }

        location = urljoin(self.base_url, 'api/user')
        create_user_request = self._request(method='POST', location=location, json=data, headers=headers,
                                            expected_status=210)

        return create_user_request
