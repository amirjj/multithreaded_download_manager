from downloader.link_maker import Linker
from downloader.downloader import Downloader
from downloader.config import LINKS


if __name__ == "__main__":
    l = Linker("https://ups.music-fa.com/tagdl/1402/")
    songs = l.create_music_links()
    # print(songs)
    d = Downloader(songs)
    d.download_all()
    # d.download_single('https://ups.music-fa.com/tagdl/1402/Valayar%20-%20Nafasam%20%28320%29.mp3', 'Valayar - Nafasam (320).mp3')

