from selenium.webdriver.common.by import By

LOGIN_BUTTON_LOCATOR = (By.XPATH,
                        '/html/body/div[1]/div[1]/div[1]/div/div/'
                        'div/div/div/div[2]/div/div[1]')
LOGIN_INPUT_LOCATOR = (By.XPATH,
                       '/html/body/div[2]/div/div[2]/div/form/div/'
                       'div[1]/input')
PASS_INPUT_LOCATOR = (By.XPATH,
                      '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
LOGIN_SUBMIT_LOCATOR = (By.XPATH,
                        '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')

LOGOUT_MENU_LOCATOR = (By.XPATH,
                       '/html/body/div[1]/div/div[1]/div/div/div/div[3]')
LOGOUT_LINK_LOCATOR = (By.XPATH,
                       '/html/body/div[1]/div/div[1]/div/div/'
                       'div/div[3]/ul/li[2]/a')
