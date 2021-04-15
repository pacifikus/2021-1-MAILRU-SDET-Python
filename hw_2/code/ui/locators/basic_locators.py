from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'responseHead-module-button')]"
    )
    LOGIN_INPUT_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'authForm-module-input')]"
    )
    PASS_INPUT_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'authForm-module-inputPassword')]"
    )
    LOGIN_SUBMIT_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'authForm-module-button')]"
    )


class DashboardPageLocators:
    LOGOUT_MENU_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'right-module-rightButton')]"
    )
    LOGOUT_LINK_LOCATOR = (
        By.LINK_TEXT,
        "ВЫЙТИ"
    )
    SEGMENTS_LINK_LOCATOR = (
        By.LINK_TEXT,
        "АУДИТОРИИ"
    )
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'dashboard-module-createButtonWrap')]"
    )
    CLEAR_CAMPAIGN_TITLE_LOCATOR = (
        By.XPATH,
        "//div[@class='input__clear js-input-clear']"
    )
    TITLE_CAMPAIGN_INPUT_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'input__inp')]"
    )
    TRAFFIC_TYPE_ITEM_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, '_traffic')]"
    )
    URL_INPUT_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'mainUrl-module-searchInput')]"
    )
    ADV_FORMAT_LOCATOR = (
        By.ID,
        "patterns_57_58"
    )
    TITLE_INPUT_LOCATOR = (
        By.XPATH,
        "//input[@placeholder='Введите заголовок объявления']"
    )
    DESCRIPTION_INPUT_LOCATOR = (
        By.XPATH,
        "//textarea[contains(@class, 'roles-module-roleTextarea')]"
    )
    UPLOAD_IMAGE_INPUT_LOCATOR = (
        By.XPATH,
        "//input[@data-test='image_90x75']"
    )
    CREATE_CAMPAIGN_SUBMIT_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'js-save-button-wrap')]"
    )
    CAMPAIGNS_TABLE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'main-module-TableWrapper')]"
    )
    CHECKBOX_CAMPAIGN_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'name-module-checkbox')]"
    )
    CAMPAIGN_CONTROLS_MODULE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'tableControls-module-selectItem')]"
    )
    REMOVE_CAMPAIGN_LOCATOR = (
        By.XPATH,
        "//li[@data-id='8']"
    )

    def create_campaign_cell_locator(self, campaign_name):
        return (
            By.XPATH,
            f"//a[contains(@class, 'nameCell-module-campaignNameLink') "
            f"and @title='{campaign_name}']"
        )


class SegmentsPageLocators:
    NEW_SEGMENT_LINK_LOCATOR = (
        By.LINK_TEXT,
        "Создайте"
    )
    SEGMENT_SOURCE_CHECKBOX_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'adding-segments-source__checkbox')]"
    )
    ADD_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'adding-segments-modal__btn')]"
    )
    CREATE_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'button_submit')]"
    )
    SEGMENTS_TABLE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'page_segments__tbl-wrap')]"
    )
    REMOVE_SEGMENT_ICON_LOCATOR = (
        By.XPATH,
        "//span[contains(@class, 'cells-module-removeCell')]"
    )
    REMOVE_SEGMENT_CONFIRM_BUTTON_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'button_confirm-remove')]"
    )
