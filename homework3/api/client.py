import requests


class ApiClientException(Exception):
    ...


class ApiClient:

    def __init__(self, base_url: str, email: str, password: str):
        self.base_url = base_url

        self.email = email
        self.password = password

        self.session = requests.Session()

    # def get_ssdc(self):
    #     headers = requests.get(url=self.base_url).headers
    #     ssdc = [h for h in headers if 'ssdc']
    #     if not ssdc:
    #         raise ApiClientException('Expected ssdc in Cookie')
    #     ssdc = ssdc[0].split('=')[-1]
    #     return ssdc

    def get_token(self):
        headers = requests.get(url=self.base_url).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrf_token']
        if not token_header:
            raise ApiClientException('Expected csrftoken in Set-Cookie')
        token_header = token_header[0].split('=')[-1]
        return token_header

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
        login_request = self.session.post(url='https://auth-ac.my.com/auth', headers=headers,
                                          data=data)

        s = open('files/res.html', 'w+')
        s.write(login_request.text)
        s.close()
        print(login_request.history)
        print(login_request.cookies.get_dict())
        print(self.session.cookies)
        return login_request

#
# client = ApiClient("https://auth-ac.my.com/auth", "mr-nicko2011@Yandex.ru", "Test_password123!")
# client.post_login()
#
# check = client.session.get("https://target-sandbox.my.com/profile/contacts")
# print(check.url)

