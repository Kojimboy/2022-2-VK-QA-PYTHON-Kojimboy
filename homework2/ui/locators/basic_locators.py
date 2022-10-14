from selenium.webdriver.common.by import By


class BasePageLocators:  # то что на всех страницах есть (logged)
    AUTHORIZED_USER_RIGHT_MODULE = (By.XPATH, "//*[contains(@class,'right-module-rightButton')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@href,'/logout')]")
    RIGHT_DROP_MENU = (By.XPATH, "//*[contains(@class,'rightMenu-module-visibleRightMenu')]")
    AUTHORIZED_USER_NAME_IN_RIGHT_MODULE = (By.XPATH, "//*[contains(@class,'right-module-userNameWrap')]")
    # фио в правом верхнем углу

    PROFILE_BUTTON = (By.XPATH, "//*[contains(@class,'center-module-profile')]")  # Профиль
    AUDITIONS_BUTTON = (By.XPATH, "//*[contains(@class,'center-module-segments')]")  # Аудитории
    BILLING_BUTTON = (By.XPATH, "//*[contains(@class,'center-module-billing')]")  # Баланс


class MainPageLocators(BasePageLocators):  # то что на главной(not logged)
    LOGIN_FORM_BUTTON = (By.XPATH, "//*[contains(@class,'responseHead-module-button')]")
    LOGIN_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@class,'authForm-module-button')]")

    INVALID_INPUT_ERROR_MESSAGE = (By.XPATH, "//*[contains(@class,'notify-module-error')]")
    # сообщение о невалидном вводе

    # INVALID_LOGIN_PASSWORD_ERROR_MESSAGE = (By.CLASS_NAME, "formMsg_title") сообщение о несовпадении
    # зарегистрированного или незарегистрированного пользователя и пароля(открывается другая страница)

#
# class ProfilePageLocators(BasePageLocators):  # Страниц профиля
#     EDIT_FIO_INPUT = (By.XPATH, "//*[contains(@data-name,'fio')]//input[contains(@type,'text')]")
#     EDIT_PHONE_INPUT = (By.XPATH, "//*[contains(@data-name,'phone')]//input[contains(@type,'text')]")
#     EDIT_SAVE_BUTTON = (By.XPATH, "//*[contains(@class,'button button_submit')]")
#     EDIT_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@data-class-name, 'SuccessView')]")


class CampaignPageLocators(BasePageLocators):  # Страница компании
    OBJECTIVE = (By.XPATH, "//*[contains(@class,'progress__item js-progress-item-objective')]")


class NewCampaignPageLocators(BasePageLocators):  # Страница создания новой компании
    OBJECTIVE = (By.XPATH, "//*[contains(@class,'progress__item js-progress-item-objective')]")
