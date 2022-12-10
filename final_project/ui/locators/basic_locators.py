from selenium.webdriver.common.by import By


class BasePageLocators:  # то что на всех страницах есть (logged)
    AUTHORIZED_USER_RIGHT_MODULE = (By.XPATH, "//*[contains(@class,'right-module-rightButton')]")


class LoginPageLocators(BasePageLocators):  # то что на главной(not logged)

    USER_NAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "submit")
