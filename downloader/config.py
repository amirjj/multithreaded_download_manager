import os

LINKS = [
    # 'https://ups.music-fa.com/tagdl/1402/',
    'https://ups.music-fa.com/tagdl/1401/',
    'https://ups.music-fa.com/tagdl/downloads/',
    'https://dls.music-fa.com/tagdl/ati/',
    'https://irsv.upmusics.com/AliBZ/'
]

ROOT = os.getcwd()
DOWNLOAD_PATH = os.path.join(ROOT, 'static', 'downloads')
LOG_DIR = os.path.join(ROOT, 'downloader', 'log')
RUNTIME_DOWNLOAD_ERROR_LOG = os.path.join(LOG_DIR, 'runtime_downloader_error.log')
DOWNLOAD_STATUS_LOG = os.path.join(LOG_DIR, 'download_status.json')

