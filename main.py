from downloader.link_maker import Linker
from downloader.downloader import Downloader
from downloader.config import LINKS
import threading


def download_link(link):
    print(link)
    link_obj = Linker(link)
    songs = link_obj.create_music_links()
    d = Downloader(songs)
    d.download_all()


def multithread_download():
    threads = list()
    for link in LINKS:
        t = threading.Thread(target=download_link, args=(link,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    multithread_download()
    # l = Linker("https://ups.music-fa.com/tagdl/1402/")
    # songs = l.create_music_links()
    # d = Downloader(songs)
    # d.download_all()
    # d.multi_thread_download_all()

