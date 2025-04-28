import requests


class BoardApi:
    def __init__(self, url: str, headers={
            "Authorization": (
                "viktoriya.przhanova.99@mail.ru, CUG6eXUrEuv2&VQ"),
            "Content-Type": "application/json"
            }) -> None:
        self.url = url
        self.auth = headers

    def catalog(self):
        catalog = requests.get(self.url + "genres?subgenre_depth=3",
                               headers=self.auth)
        assert catalog.status_code == 200

    def new(self):
        new = requests.get(self.url + ("genres/5028/arts/facets?is_for_pda=false&limit=20&o=new&offset=0&show_unavailable=false"),
                           headers=self.auth)
        assert new.status_code == 200

    def popular(self):
        popular = requests.get(self.url + "genres/5028/arts/facets?is_for_pda=false&limit=20&o=popular&offset=0&show_unavailable=false",
                               headers=self.auth)
        assert popular.status_code == 200

    def find_name(self):
        name = requests.get(self.url + "search?is_for_pda=false&limit=24&offset=0&q=%D0%B3%D0%B0%D1%80%D1%80%D0%B8%20%D0%BF%D0%BE%D1%82%D1%82%D0%B5%D1%80&show_unavailable=false&types=text_book&types=audiobook&types=podcast&types=podcast_episode",
                            headers=self.auth)
        assert name.status_code == 200

    def find_genre(self):
        ganre = requests.get(self.url + "genres/5006/arts/facets?is_for_pda=false&limit=24&o=popular&offset=0&show_unavailable=false",
                             headers=self.auth)
        assert ganre.status_code == 200

    def find_author(self):
        author = requests.get(self.url + "search?is_for_pda=false&limit=12&o=popular&offset=0&q=%D1%80%D0%BE%D1%83%D0%BB%D0%B8%D0%BD%D0%B3&types=person",
                              headers=self.auth)
        assert author.status_code == 200

    def find_series(self):
        series = requests.get(self.url + "search?is_for_pda=false&limit=12&o=popular&offset=0&q=%D0%BA%D0%B8%D0%BF%D0%BB%D0%B8%D0%BD%D0%B3&types=series",
                              headers=self.auth)
        assert series.status_code == 200
