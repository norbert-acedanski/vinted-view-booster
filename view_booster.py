import time
from typing import Literal, List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class ViewBooster:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    def __enter__(self):
        self.driver = webdriver.Chrome(service=Service("./chromedriver/chromedriver.exe"), options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.current_option = None
        self.current_user = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close_window()

# GENERAL

    def open_url(self, url: str) -> None:
        self.driver.get(url)
        if "Vinted" not in self.driver.title:
            f"Expected 'Vinted' in browser title, got '{self.driver.title}' instead, refreshing..."
            self.refresh_page()

    def decline_all_cookies(self) -> None:
        self.driver.find_element(by=By.XPATH, value="//*[@id='onetrust-reject-all-handler']").click()

    def refresh_page(self) -> None:
        self.driver.refresh()

    def close_window(self) -> None:
        self.driver.close()

# MAIN PAGE

    def choose_option_in_search_item(self, option: Literal["item", "user", "forum", "faq"]) -> None:
        self.driver.find_element(by=By.XPATH, value="//*[@id='search-item']").click()
        self.driver.find_element(by=By.XPATH, value=f"//*[@data-testid='search-bar-search-type-{option}']").click()
        self.current_option = option

    def search_phrase_in_search_bar(self, phrase: str) -> None:
        self.driver.find_element(by=By.XPATH, value="//*[@id='search_text']").send_keys(phrase)
        self.driver.find_element(by=By.XPATH, value="//*[@id='search_text']").send_keys(Keys.ENTER)

    def choose_searched_phrase(self, phrase: str) -> None:
        if self.current_option == "user":
            user_xpath = f"//*[@id='content']//a[@class='follow__name' and text()='{phrase}']"
            try:
                self.driver.find_element(by=By.XPATH, value=user_xpath).click()
            except NoSuchElementException:
                if self.driver.find_element(by=By.XPATH,
                                            value="//*[@id='content']//span[@class='empty-state__content']") \
                        .is_displayed():
                    raise NoSuchElementException("No match found!")
                else:
                    raise
            self.current_user = phrase
        else:
            raise ValueError("For now, search is defined only for 'user' option")

# USER PAGE

    def get_number_of_items_of_a_user(self) -> int:
        number_of_items_xpath = \
            "//*[@class='profile__items-wrapper']/div[contains(@class, 'Container__container')]//h2/span"
        return int(self.driver.find_element(by=By.XPATH, value=number_of_items_xpath).text.split(" ")[0])

    def all_visible_user_items(self) -> List[WebElement]:
        return self.driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'feed-grid__item ')]")

    def scroll_max_down(self) -> None:
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.5)

    def get_all_items_url(self) -> List[str]:
        items_xpath = "//*[contains(@class, 'feed-grid__item ')]//a"
        return [item.get_attribute('href') for item in self.driver.find_elements(by=By.XPATH, value=items_xpath)]

    def get_current_view_count(self) -> int:
        try:
            return int(self.driver.find_element(
                by=By.XPATH,
                value="//div[@class='details-list__item']/div[contains(text(), 'Liczba')]/following-sibling::div").text)
        except (NoSuchElementException, StaleElementReferenceException):
            self.refresh_page()
        