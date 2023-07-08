import os.path
import requests
from time import sleep
import threading, queue

from .config import DOWNLOAD_PATH, RUNTIME_DOWNLOAD_ERROR_LOG, DOWNLOAD_STATUS_LOG


class Downloader:
    def __init__(self, links, wait=0):
        self.links = links
        self.wait = wait
        self.q = self.fill_q(links)

    @staticmethod
    def fill_q(links):
        q = queue.Queue()
        for link in links:
            q.put(link)
        return q


    def download_single(self, link, title):
        try:
            song = requests.get(link)
            with open(DOWNLOAD_PATH + os.path.sep + title, 'wb') as f:
                f.write(song.content)
        except:
            with open(RUNTIME_DOWNLOAD_ERROR_LOG, "w+") as error_file:
                error_file.write(f"Download failed: {link}\n")

        return True

    def download_sample(self, link, title):
        try:
            print(link)
            sleep(5)
        except:
            with open(RUNTIME_DOWNLOAD_ERROR_LOG, "w+") as error_file:
                error_file.write(f"Download failed: {link}\n")

        return True

    def download_all(self):
        for song in self.links:
            # status = self.download_single(song, self.links[song]['title'])
            status = self.download_sample(song, self.links[song]['title'])
            if status:
                self.links[song]['downloaded'] = True
        return self.links

    # TODO: WRITE THE LAST SATUS AS JSON IN DOWNLOAD_STATUS_LOG

