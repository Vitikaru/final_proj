from page.AuthPage import AuthPage
from page.MainPage import MainPage


def test_ui(browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.login_as("viktoriya.przhanova.99@mail.ru", "CUG6eXUrEuv2&VQ")

    main_page = MainPage(browser)
    main_page.search("Автоматизация тестирования")

    to_be = main_page.add_like()
    as_is = main_page.my_books()
    assert as_is == to_be

    price = main_page.info_book()
    total = main_page.add_basket()
    assert total == price
