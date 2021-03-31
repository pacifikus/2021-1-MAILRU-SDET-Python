from selenium.webdriver.common.by import By

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
LOGOUT_MENU_LOCATOR = (
    By.XPATH,
    "//div[contains(@class, 'right-module-rightButton')]"
)
LOGOUT_LINK_LOCATOR = (
    By.LINK_TEXT,
    "ВЫЙТИ"
)
