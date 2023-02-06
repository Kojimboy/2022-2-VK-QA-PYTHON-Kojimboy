from selenium.webdriver.common.by import By


class MainPageLocators:  # то что на главной странице (logged)
    HOME_BUTTON = (By.XPATH, ".//li//a[@href='/']")
    BUG_BUTTON = (By.XPATH, ".//ul/a[@href='/']")
    PYTHON_BUTTON = (By.XPATH, ".//a[contains(@href, 'https://www.python.org/') and contains(text(), 'Python')]")
    PYTHON_HISTORY_BUTTON = (By.XPATH, ".//a[contains(@href,'https://en.wikipedia.org/wiki/History_of_Python')]")
    FLASK_BUTTON = (By.XPATH, ".//a[contains(@href,'https://flask.palletsprojects.com/en/1.1.x/#')]")

    LINUX_BUTTON = (By.XPATH, ".//a[contains(@href, 'javascript') and contains(text(), 'Linux')]")
    NETWORK_BUTTON = (By.XPATH, ".//a[contains(@href, 'javascript') and contains(text(), 'Network')]")

    API_BUTTON = (By.XPATH, ".//a[contains(@href,'https://en.wikipedia.org/wiki/Application_programming_interface')]")
    FUTURE_BUTTON = (By.XPATH, ".//a[contains(@href,'https://www.popularmechanics.com/technology/infrastructure"
                               "/a29666802/future-of-the-internet/')]")
    SMTP_BUTTON = (By.XPATH, ".//a[contains(@href,'https://ru.wikipedia.org/wiki/SMTP')]")

    AUTHORIZED_USER_RIGHT_MODULE = (By.XPATH, ".//div[@id='login-name']")
    NICKNAME = (By.XPATH, ".//div[@id='login-name']//li[contains(text(),'Logged as')]")
    NAME_SURNAME = (By.XPATH, ".//div[@id='login-name']//li[contains(text(),'User:')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@href, '/logout')]")


class LoginPageLocators:  # то что на странице логина(not logged)

    USER_NAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "submit")

    REGISTER_BUTTON = (By.XPATH, "//a[contains(@href, '/reg')]")


class RegPageLocators:  # то что на странице регистрации(not logged)

    NAME_INPUT = (By.ID, "user_name")
    SURNAME_INPUT = (By.ID, "user_surname")
    MIDDLE_NAME_INPUT = (By.ID, "user_middle_name")
    USER_NAME_INPUT = (By.ID, "username")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm")

    TERM_CHECKBOX = (By.ID, "term")
    REGISTER_BUTTON = (By.ID, "submit")

    LOGIN_BUTTON = (By.XPATH, "//a[contains(@href, '/login')]")
