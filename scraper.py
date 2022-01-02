from os import devnull
from pathlib import Path
from itertools import count
import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

from logger import logger
from locators import *
from csvwriter import CSVWriter


def close_popups() -> None:
	# Check and close up any possible popup
	logger.info("Check and close up any possible popup")
	popups = driver.find_elements(*Search.popup)
	if popups and popups[-1].is_displayed():
		popups[-1].click()


def select_category(category: str = '1') -> None:
	# select categories
	Select(driver.find_element(*Search.category)).select_by_value(category)


def select_support_type(support : str = '1') -> None:
	# select support type
	Select(driver.find_element(*Search.support_type)).select_by_value(support)


def select_distance(distance: str = "250") -> None:
	# select distance
	Select(driver.find_element(*Search.distance)).select_by_value(distance)


def select_zipcode(zipcode: int = 84321) -> None:
	# input the zipcode 
	driver.find_element(*Search.zipcode).send_keys(zipcode)


def search() -> None:
	# click the search button
	search_button = driver.find_element(*Search.search_btn)
	driver.execute_script("arguments[0].click();", search_button)
	multiple_page_operation()

def parse_article_element(article):
	provider_name = article.find_element(*Article.provider_name).text.strip()
	provider_affiliation = article.find_elements(*Article.provider_affiliation)
	affiliation = provider_affiliation[-1].text.strip() if provider_affiliation else '-'
	address = article.find_element(*Article.address).text.replace('\n', '. ').strip()
	tel = article.find_element(*Article.tel).text.strip()
	distance = article.find_element(*Article.distance).text.strip()
	logger.info(f"{provider_name}, {affiliation}, {address}, {tel}, {distance}")
	return {
		'provider_name': provider_name, 
		'affiliation': affiliation,
		'address': address, 
		'tel': tel, 
		'distance': distance,
	}


def one_page_operation() -> None:
	articles = driver.find_elements(*Article.article)
	if articles:
		for article in articles:
			data = parse_article_element(article)
			writer.writerow(data)


def multiple_page_operation() -> None:
	# select the cards and extract out info
	logger.info("Name, Affiliation, Address, Tel, Distance")
	current_url = driver.current_url
	# work on first page
	input("Press enter to start")
	one_page_operation()

	# this pages it traverses is limited for demo purposes only
	for page_number in range(2, 4):
		# next page
		next_url = f"{current_url}&page={page_number}"
		logger.debug(next_url)	
		driver.get(next_url)
		one_page_operation()


def main() -> None:
	url: str = "https://www.nationalmssociety.org/Resources-Support/Find-Doctors-Resources?"
	driver.get(url)
	close_popups()
	select_category()
	select_support_type()
	select_distance()
	select_zipcode()
	search()


def make_driver(timeout : int = 30) -> None:
	name = 'chromedriver' if platform.system() == 'Linux' else 'chromedriver.exe'
	driver_path = Path.cwd() / 'chromedriver' / name
	options = webdriver.ChromeOptions()
	options.add_argument("log-level=3")
	# the following two options are used to disable chrome browser infobar
	options.add_experimental_option("useAutomationExtension", False)
	options.add_experimental_option("excludeSwitches",["enable-automation"])
	driver = webdriver.Chrome(service=Service(driver_path), service_log_path=devnull, options=options)
	driver.implicitly_wait(timeout)
	return driver


writer = CSVWriter()
driver = make_driver()
main()