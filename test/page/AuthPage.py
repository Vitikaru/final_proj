from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def go(self):

        # Окрытие сайта "Литрес"
        self.__driver.get("https://www.litres.ru/")

    def login_as(self, email, password):

        # Ожидание нажатия на кнопку "Войти"
        WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tab-login"))).click

        # Ожидание появление поля "email"
        WebDriverWait(
            self.__driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#auth__input--enterEmailOrLogin"))
                ).send_keys(email)
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.AuthContent_form__submit__crvDj > button"
            ).click()

        # Ожидание появления поля "пароль"
        WebDriverWait(
            self.__driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[type=password]"))).send_keys(password)
        self.__driver.find_element(
            By.CSS_SELECTOR, "div.AuthContent_form__submit__crvDj > button"
            ).click()
