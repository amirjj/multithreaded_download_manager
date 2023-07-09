import os.path
import requests
from .config import DOWNLOAD_PATH, RUNTIME_DOWNLOAD_ERROR_LOG


class Downloader:
    def __init__(self, links):
        self.links = links

    def download_single(self, link):
        title = self.links[link]['title']
        print(title)
        try:
            song = requests.get(link)
            with open(DOWNLOAD_PATH + os.path.sep + title, 'wb') as f:
                f.write(song.content)
        except:
            with open(RUNTIME_DOWNLOAD_ERROR_LOG, "w+") as error_file:
                error_file.write(f"Download failed: {link}\n")

        return True

    def download_all(self):
        for song in self.links:
            status = self.download_single(song)
            if status:
                self.links[song]['downloaded'] = True
        return self.links

