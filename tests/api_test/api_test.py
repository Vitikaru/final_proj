from Api import BoardApi


url = BoardApi("https://api.litres.ru/foundation/api/")


def test_api():
    url.catalog()
    url.new()
    url.popular()
    url.find_name()
    url.find_genre()
    url.find_author()
    url.find_series()
