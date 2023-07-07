import requests
from bs4 import BeautifulSoup


class Linker:
    def __init__(self, link):
        self.root_link = link

    def create_music_links(self):
        response = requests.get(self.root_link)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        soup = BeautifulSoup(response.content, 'html.parser')
        a_list = soup.find_all('a')

        songs = dict()
        for element in a_list:
            href = element.get('href')
            text = element.text
            if '../' not in href:
                key = self.root_link + href
                songs[key] = {
                    'title': text,
                    'downloaded': False
                }

        return songs
