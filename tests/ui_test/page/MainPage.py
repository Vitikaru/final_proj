from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self) -> str:
        return self.__driver.current_url

    def search(self, text):

        # поиск по названию
        WebDriverWait(self.__driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "form > div > input"))
                ).send_keys(text, Keys.RETURN)

        # отобразить все найденные книги
        WebDriverWait(self.__driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.ArtsGrid_grid__K8Emb > div")))

    def add_like(self):

        # добавление всех найденых книг в отложенное
        buttons = self.__driver.find_elements(
            By.CSS_SELECTOR, "div.Art_content__rightTop__sO9tF")

        counter = 0
        for add in buttons:
            add.click()
            counter += 1

        return counter

    def my_books(self):

        # нажатие на кнопку мои книги
        WebDriverWait(self.__driver, 5).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tab-myBooks > a"))).click()

        # переход к отложенным книгам
        WebDriverWait(self.__driver, 5).until(
          EC.element_to_be_clickable(
             (By.CSS_SELECTOR,
              "div > div.TabNavigation_item__7tFtK.TabNavigation_item_active__dP5tW"
              ))).click()

        # нати количество добавленных книг в отложенное
        txt = self.__driver.find_element(
            By.CSS_SELECTOR,
            "div.TabNavigation_item__7tFtK.TabNavigation_item_active__dP5tW"
            ).find_element(By.CSS_SELECTOR,
                           '[class="TabNavigation_counter__bNviM"]').text

        return int(txt)

    def info_book(self):

        # переход к информации о книге
        WebDriverWait(self.__driver, 5).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "div.ArtsGrid_artsGrid__rA8I8.ArtsGrid_artsGrid__adaptive__308LV > div:nth-child(1)"
             ))).click()

        # отобразить цену книги
        price = self.__driver.find_element(
            By.CSS_SELECTOR,
            '[class="SaleBlock_button__2RO0T SaleBlockPpd_shortInfoButtonContainer__TGe6r"]'
            ).find_element(
                By.CSS_SELECTOR,
                "div.SaleBlock_button__2RO0T.SaleBlockPpd_shortInfoButtonContainer__TGe6r > button > div > div > div > div"
                    ).text

        return str(price)

    def add_basket(self):

        # добавление книги в корзину
        WebDriverWait(self.__driver, 5).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div:nth-child(4) > button > div"))).click()

        # закрыть всплывающее окно
        WebDriverWait(self.__driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.Modal_content__header__tME5H > div"))
                ).click()

        # переход в корзину
        WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tab-basket > a"))
            ).click()

        # отобразить сумму к покупке
        total = self.__driver.find_element(
            By.CSS_SELECTOR, "div.CheckoutBox_costs__76eA2"
            ).find_element(
                By.CSS_SELECTOR,
                "div.CheckoutBox_costs__price__dTMFO.CheckoutBox_costs__info_total__Lbs00"
                ).text

        return str(total)
