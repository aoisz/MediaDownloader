from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import youtube_dl
from pytube import YouTube
from youtube_dl.utils import RegexNotFoundError

class DownloadThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, link, download_func):
        super().__init__()
        self.link = link
        self.download_func = download_func

    def run(self):
        self.download_func(self.link, self.progress)

