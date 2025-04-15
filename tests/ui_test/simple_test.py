from page.AuthPage import AuthPage


def test_first(browser):
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.login_as("viktoriya.przhanova.99@mail.ru", "CUG6eXUrEuv2&VQ")
