from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.XPATH, "//*[contains(@class,'responseHead-module-button')]")
LOGIN_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.XPATH, "//*[contains(@class,'authForm-module-button')]")
AUTORIZED_USER_RIGHT_MODULE = (By.XPATH, "//*[contains(@class,'right-module-rightWrap')]")
LOGOUT_BUTTON = (By.XPATH, "//*[contains(@href,'/logout')]")
RIGHT_DROP_MENU = (By.XPATH, "//*[contains(@class,'rightMenu-module-visibleRightMenu')]")
INVALID_INPUT_ERROR_MESSAGE = (By.XPATH, "//*[contains(@class,'notify-module-error')]")
INVALID_LOGIN_PASSWORD_ERROR_MESSAGE = (By.CLASS_NAME, "formMsg_title")
EDIT_PROFILE_BUTTON = (By.XPATH, "//*[contains(@class,'center-module-profile')]")
EDIT_FIO_INPUT = (By.XPATH, "//*[contains(@data-name,'fio')]//input[contains(@type,'text')]")
EDIT_PHONE_INPUT = (By.XPATH, "//*[contains(@data-name,'phone')]//input[contains(@type,'text')]")
EDIT_SAVE_BUTTON = (By.XPATH, "//*[contains(@class,'button button_submit')]")
EDIT_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@data-class-name, 'SuccessView')]")
AUTORIZED_USER_NAME_IN_RIGHT_MODULE = (By.XPATH, "//*[contains(@class,'right-module-userNameWrap')]")