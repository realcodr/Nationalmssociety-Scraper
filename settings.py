import platform
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

wait_time = 45
miles = [5, 10, 25, 50, 100, 250]
ignored_exceptions = NoSuchElementException, StaleElementReferenceException,

# TODO: I ought to use the webdriver manager to handle this but I have some reservations on the library
name = 'chromedriver' if platform.system() == 'Linux' else 'chromedriver.exe'
driver_path = Path('chromedriver') / name

driver = webdriver.Chrome(executable_path=driver_path)
webdriverwait = WebDriverWait(driver, wait_time, ignored_exceptions=ignored_exceptions)
