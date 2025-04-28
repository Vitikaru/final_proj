from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.litres.ru/"
        self.__driver = driver

    def open(self):

        # Окрытие сайта "Литрес"
        self.__driver.get(self.__url)
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "div.CookieAcceptPopup_container__brIgd > button"))).click()

    def login_as(self, email, password):

        # Ожидание нажатия на кнопку "Войти"
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab-login"))
        ).click()

        # Ожидание появление поля "email"
        WebDriverWait(
            self.__driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#auth__input--enterEmailOrLogin"))
                ).send_keys(email)
        self._click_submit()

        # Ожидание появления поля "пароль"
        WebDriverWait(
            self.__driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[type=password]"))).send_keys(password)
        self._click_submit()

        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[class="Modal_close__pNO8c"]'))).click()

    def _click_submit(self):
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "div.AuthContent_form__submit__crvDj > button"))).click()
