import os
import sys

import allure
from allure_commons.types import AttachmentType
from jproperties import Properties
from pytest import fixture
from selenium import webdriver

PROJECT_ROOT = os.path.dirname(__file__)

CHROME_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdriver/chrome/chromedriver_lin'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdriver/chrome/chromedriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'webdriver/chrome/chromedriver_win.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdriver/chrome/chromedriver_win.exe')
}

OPERA_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdriver/opera/operadriver_lin'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdriver/opera/operadriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'webdriver/opera/operadriver_win.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdriver/opera/operadriver_win.exe')
}

YANDEX_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdriver/yandex/yandexdriver_lin'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdriver/yandex/yandexdriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'webdriver/yandex/yandexdriver_win.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdriver/yandex/yandexdriver_win.exe')
}

@fixture
def start_browser():
    configs = Properties()

    configs.load(open(os.path.join(PROJECT_ROOT, 'app.properties'), 'rb'))

    browser_name = configs.get("browser").data

    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--window-size=1920,1080')
    option.add_argument('lang=ru')

    if browser_name == 'Chrome':
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=option)
    elif browser_name == 'Opera':
        driver = webdriver.Opera(executable_path=OPERA_DRIVER_DICT[sys.platform], options=option)
    elif browser_name == 'Yandex':
        driver = webdriver.Opera(executable_path=YANDEX_DRIVER_DICT[sys.platform], options=option)
    else:
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=option)

    yield driver

    if sys.exc_info():
        allure.attach(body=driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    driver.quit()