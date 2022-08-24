import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as chrome_options
import allure
from allure_commons.types import AttachmentType

driver = webdriver.Chrome()

driver.get('https://api.ratio2.dev2uit.ru/backend/user/index')
print('Страница открыта')
log = driver.find_element_by_id('loginform-username')
log.click()
log.send_keys("webmaster")
print('Поле логин успешно заполнено')
passw = driver.find_element_by_id('loginform-password')
passw.click()
passw.send_keys("7e3NoXAx")
print('Поле пароль успешно заполнено')
login_but = driver.find_element_by_xpath('//*[@id="login-form"]/button')
login_but.click()
print('Пользователь авторизирован. Редирект на главную страницу\n')
driver.save_screenshot('test.png')



