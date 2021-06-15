from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'uk-button')]"
    )
    LOGIN_INPUT_LOCATOR = (
        By.XPATH,
        '//input[@class="uk-input uk-form-large"]'
    )
    PASS_INPUT_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'uk-input uk-form-large uk-icon-eye')]"
    )
    CREATE_ACC_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="/reg"]'
    )


class AccountPageLocators:
    GO_TO_API_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://en.wikipedia.org/'
        'wiki/Application_programming_interface"]'
    )
    GO_TO_INTERNET_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://www.popularmechanics.com/'
        'technology/infrastructure/a29666802/future-of-the-internet/"]'
    )
    GO_TO_SMTP_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]'
    )
    LOGOUT_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="/logout"]'
    )
    HOME_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="/"]'
    )
    PYTHON_LINK_LOCATOR = (
        By.XPATH,
        '//a[contains(text(),"Python")]'
    )
    PYTHON_HISTORY_LINK_LOCATOR = (
        By.XPATH,
        '//a[contains(text(),"Python history")]'
    )
    FLASK_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://flask.palletsprojects.com/en/1.1.x/#"]'
    )
    LINUX_LINK_LOCATOR = (
        By.XPATH,
        '//a[contains(text(),"Linux")]'
    )
    CENTOS_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://getfedora.org/ru/workstation/download/"]'
    )
    NETWORK_LINK_LOCATOR = (
        By.XPATH,
        '//a[contains(text(),"Network")]'
    )
    NEWS_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://www.wireshark.org/news/"]'
    )
    DOWNLOAD_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://www.wireshark.org/#download"]'
    )
    EXAMPLES_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="https://hackertarget.com/tcpdump-examples/"]'
    )


class RegistrationPageLocators:
    CREATE_ACC_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="/reg"]'
    )
    USERNAME_INPUT_LOCATOR = (
        By.XPATH,
        "//input[@id='username']"
    )
    PASS_INPUT_LOCATOR = (
        By.XPATH,
        '//input[@id="password"]'
    )
    REPEAT_PASS_INPUT_LOCATOR = (
        By.XPATH,
        "//input[@name='confirm']"
    )
    EMAIL_INPUT_LOCATOR = (
        By.XPATH,
        '//input[@id="email"]'
    )
    ACCEPT_LOCATOR = (
        By.XPATH,
        '//input[@id="term"]'
    )
    REGISTER_BUTTON_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'uk-button')]"
    )
    GO_TO_LOGIN_LINK_LOCATOR = (
        By.XPATH,
        '//a[@href="/login"]'
    )
