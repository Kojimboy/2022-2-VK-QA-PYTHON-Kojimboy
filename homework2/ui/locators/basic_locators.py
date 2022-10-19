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
    TOP_CAMPAIGN_CELL = (By.XPATH, "//*[contains(@class, 'nameCell-module-campaignNameLink')]")


class NewCampaignPageLocators(BasePageLocators):  # Страница создания новой компании
    SPECIAL_CAMPAIGN = (By.XPATH, "//*[contains(@class,'column-list-item _special')]")
    MAIN_URL_INPUT = (By.XPATH, "//*[contains(@class,'mainUrl-module-searchInput')]")
    TOP_CAMPAIGN_NAME_INPUT = (
        By.XPATH, "//*[contains(@class,'js-base-setting-campaign-name-wrap')]//*[contains(@class,'js-form-element')]")
    BANNER_NAME_INPUT = (By.XPATH, "//*[contains(@data-gtm-id, 'banner_form_text')]")
    BANNER_ADD_BUTTON = (
        By.XPATH, "//*[contains(@class,'js-banner-form-btn')]//*[contains(@class,'button button_submit')]")
    SAVE_CAMPAIGN_BUTTON = (
        By.XPATH,
        "//*[contains(@class,'footer__button js-save-button-wrap')]//*[contains(@class,'button button_submit')]")


class NewSegmentPageLocators(BasePageLocators):  # Страница создания сегмента
    APP_GAME_SEGMENT = (By.XPATH,
                        "//div[contains(text(),'Приложения и игры в соцсетях') or contains(text(),'Apps and games in "
                        "social networks')]")
    APPS_GAMES_CHECKBOX = (
        By.XPATH, "//*[contains(@class, 'adding-segments-source__checkbox js-main-source-checkbox')]")
    ADD_SEGMENT_BUTTON = (By.XPATH,
                          "//*[contains(@class,'adding-segments-modal__btn-wrap js-add-button')]//*[contains(@class, "
                          "'button button_submit')]")
    SEGMENT_NAME_INPUT = (By.XPATH,
                          "//*[contains(@class, 'input input_create-segment-form')]//*[contains(@class, 'input__inp "
                          "js-form-element')]")
    CREATE_SEGMENT_BUTTON = (By.XPATH,
                             "//*[contains(@class,'create-segment-form__btn-wrap js-create-segment-button-wrap')]//*["
                             "contains(@class, 'button button_submit')]")
    GROUP_VK_OK_SEGMENT = (By.XPATH,
                           "//div[contains(text(),'Группы ОК и VK') or contains(text(),'Groups OK and VK')]")
    SEARCH_GROUP_INPUT = (
        By.XPATH, "//*[contains(@class,'input input_sources-form')]//*[contains(@class,'input__inp js-form-element')]")
    CHECKBOX_WITH_SEARCH = (By.XPATH,
                            "//*[@class ='adding-segments-source']//*[contains(@class, "
                            "'adding-segments-source__checkbox js-main-source-checkbox')]")


class SegmentPageLocators(BasePageLocators):  # Страница сегментов
    TOP_SEGMENT_CELL = (By.XPATH, ".//*[contains(@class, 'cells-module-nameCell')]//a")
    TOP_SEGMENT_CHECKBOX = (By.XPATH, ".//*[contains(@class, 'main-module-CellFirst')]//input")
    VK_OK_GROUP_DATA_SOURCE_BUTTON = (
        By.XPATH, "//*[contains(@class, 'left-nav__item')]//a[contains(@href, '/segments/groups_list')]")
    VK_OK_GROUP_NAME_INPUT = (By.XPATH, "//*[contains(@class, 'multiSelectSuggester-module-searchInput')]")
    SHOW_GROUP_BUTTON = (
        By.XPATH, "//*[contains(@class, 'optionListTitle-module-control')]//*[contains(@data-test, 'show')]")
    VK_EDU_GROUP = (By.XPATH, "//*[contains(@title, 'VK Образование')]//*[contains(@class, 'optionsList-module-text')]")
    ADD_SELECTED_GROUP_BUTTON = (By.XPATH, "//*[contains(@class, 'button-module-textWrapper')]")
    VK_EDU_GROUP_TITLE_SEGMENT_CELL = (By.XPATH, "//span[@title='VK Образование']")
    SEGMENT_CHECKBOX = (
        By.XPATH, ".//*[contains(@type, 'checkbox')]")  # без точки не работает поиск внутри другого элемента
    SUCCESS_DELETE_MESSAGE = (
        By.XPATH,
        "//*[contains(@class, 'notify-module-content') and contains(@class,'undefined notify-module-success')]")
    ACTION_BUTTON = (By.XPATH,
                     "//*[contains(@class, 'select-module-selectWrap') and contains(@class,"
                     "'segmentsTable-module-controlItem')]")
    DELETE_SEGMENT_BUTTON = (By.XPATH, "//*[contains(@data-id, 'remove')]")
    SEGMENT_SEARCH_INPUT = (By.XPATH, "//*[contains(@class,'suggester-module-searchInput')]")
    SUGGESTED_SEGMENT = (By.XPATH, "//*[contains(@class,'optionsList-module-optionsList')]//li")
    SOURCE_SEARCH_INPUT = (By.XPATH, "//*[contains(@class,'suggester-ts__input')]")
    SUGGESTED_SOURCE = (By.XPATH, "//*[contains(@class,'suggester-ts__item__name')]")
    DELETE_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class,'remove-source-wrap js-remove-source')]")
    CONFIRM_DELETE_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class,'button button_confirm-remove button_general')]")
