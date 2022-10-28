from urllib.parse import urljoin

import requests


class ApiClientException(Exception):
    ...


class ResponseStatusCodeException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ApiClient:
    PACKAGE_ID = 2266

    def __init__(self, base_url: str, email: str, password: str):
        self.base_url = base_url

        self.email = email
        self.password = password

        self.session = requests.Session()

    def _request(self, method, location, headers, data=None, json=None, params=None, allow_redirects=True,
                 expected_status=200,
                 jsonify=True):
        url = urljoin(self.base_url, location)  # urljoin заменяет весь url на location при необходимости

        response = self.session.request(method=method, url=url, headers=headers, data=data, json=json, params=params,
                                        allow_redirects=allow_redirects)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Expected {expected_status}, but got {response.status_code}')
        if jsonify:
            json_response: dict = response.json()
            if json_response.get('bStateError', False):
                error = json_response['sErrorMsg']
                raise RespondErrorException(f'Request {url} return error : "{error}"')

            return json_response
        return response

    def post_login(self):
        headers = {
            "Referer": "https://target.my.com/",  # с этим хедером работает авторизация
        }

        data = {
            'email': self.email,
            'password': self.password,
            'continue': 'https://target-sandbox.my.com/auth/',
            'failure': 'https://account.my.com/login/'
        }

        location = urljoin("https://auth-ac.my.com", "auth")
        login_request = self._request(method='POST', location=location, headers=headers, data=data, jsonify=False,
                                      expected_status=404)
        # s = open('files/res.html', 'w+')
        # s.write(login_request.text)
        # s.close()
        # print(login_request.history)
        # print(login_request.cookies.get_dict())
        # print(self.session.cookies)
        return login_request

    def post_campaign_create(self, campaign_name, banner_name):
        headers = {
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'
        }

        data = {
            "name": campaign_name,
            "objective": "special",
            "package_id": self.PACKAGE_ID,
            "banners": [
                {"textblocks": {"billboard_video": {"text": banner_name}}, "urls": {"primary": {"id": 52}},
                 "name": ""}]
        }

        location = urljoin(self.base_url, 'api/v2/campaigns.json')
        create_campaign_request = self._request(method='POST', location=location, json=data, headers=headers)
        return create_campaign_request

    def get_top_active_campaign_id(self):
        params = {"sorting": "-id",
                  "limit": 1,
                  '_status__in': 'active'}

        headers = {
        }

        location = urljoin(self.base_url, 'api/v2/campaigns.json')
        top_campaign_id_request = self._request(method='GET', location=location, headers=headers, params=params,
                                                data=None)

        return top_campaign_id_request

    def post_campaign_delete(self, campaign_id):
        headers = {
            "X-CSRFToken": f'{self.session.cookies["csrftoken"]}',
        }

        data = [
            {
                'id': campaign_id,
                'status': 'deleted',
            }
        ]

        location = urljoin(self.base_url, "api/v2/campaigns/mass_action.json")

        delete_request = self._request(method='POST', location=location, json=data, headers=headers,
                                       expected_status=204, jsonify=False)
        return delete_request

    def get_top_segment_id(self):
        headers = {

        }

        params = {
            "fields": "id",
            "sorting": "-id",
            "limit": 1,
        }

        location = urljoin(self.base_url, "api/v2/remarketing/segments.json")
        segments_request = self._request(method="GET", location=location, params=params, data=None, headers=headers)

        return segments_request

    def post_segment_create(self, segment_name, object_type, source_id=None):
        headers = {
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'
        }
        params = {
            'source_id': source_id,
            'type': 'positive',
        } if source_id else {
            'type': 'positive',
            'left': 365,
            'right': 0,
        }

        data = {
            'name': segment_name,
            'pass_condition': 1,
            'relations': [
                {
                    'object_type': object_type,
                    "params": params,
                },
            ],
        }

        location = urljoin(self.base_url, 'api/v2/remarketing/segments.json')
        create_segment_request = self._request(method='POST', location=location, json=data, headers=headers,
                                               expected_status=200)
        return create_segment_request

    def post_segment_delete(self, segment_id):
        headers = {
            "X-CSRFToken": f'{self.session.cookies["csrftoken"]}',
        }

        data = [
            {
                'source_id': segment_id,
                'source_type': 'segment',
            }
        ]

        location = urljoin(self.base_url, "api/v1/remarketing/mass_action/delete.json")

        delete_segment_request = self._request(method='POST', location=location, json=data, headers=headers,
                                               jsonify=False)
        return delete_segment_request

    def get_vk_source_id_in_search(self, url):
        headers = {

        }

        params = {
            '_q': url,
        }

        location = urljoin(self.base_url, "api/v2/vk_groups.json")
        vk_source_request = self._request(method="GET", location=location, params=params, data=None, headers=headers)

        return vk_source_request

    def post_vk_source_create(self, vk_id):
        headers = {
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'
        }

        data = {
            'items': [
                {
                    'object_id': vk_id,
                },
            ],
        }

        location = urljoin(self.base_url, 'api/v2/remarketing/vk_groups/bulk.json')
        create_source_request = self._request(method='POST', location=location, json=data, headers=headers,
                                              expected_status=201)
        return create_source_request

    def post_source_delete(self, vk_id):
        headers = {
            "X-CSRFToken": f'{self.session.cookies["csrftoken"]}',
        }

        location = urljoin(self.base_url, f"api/v2/remarketing/vk_groups/{vk_id}.json")

        delete_source_request = self._request(method='DELETE', location=location, headers=headers, expected_status=204,jsonify=False)
        return delete_source_request

    def get_vk_source_id_in_list(self):
        headers = {

        }

        params = {
            'fields': 'id',
            'limit': '50',
        }

        location = urljoin(self.base_url, "api/v2/remarketing/vk_groups.json")
        sources_request = self._request(method="GET", location=location, params=params, data=None, headers=headers)

        return sources_request
