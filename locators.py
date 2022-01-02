from selenium.webdriver.common.by import By

class Search:
	category = By.ID, 'ddlMainCategories',
	support_type = By.ID, "ddlSubCategories",
	distance = By.ID, "ddlDistance",
	zipcode = By.XPATH, '//*[@id="p_lt_zoneContent_pageplaceholder_p_lt_ctl01_CarelikePartnerProviderSearch_txtPostalCode"]',
	search_btn = By.ID, 'btnSearch',
	popup = By.CSS_SELECTOR, 'a[title=Close]',


class Article:
	article = By.CSS_SELECTOR, '.tile-row article.tile',
	provider_name = By.CSS_SELECTOR, 'h3.provider-name',
	provider_affiliation = By.CSS_SELECTOR, 'h4.provider-affiliation',
	address = By.CSS_SELECTOR, 'div.provider-location .address',
	tel = By.CSS_SELECTOR, 'div.provider-location .tel',
	distance = By.CSS_SELECTOR, 'div.provider-distance',
