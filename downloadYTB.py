from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QThread, Signal
from pytube import YouTube
import time

class DownloadThread1(QThread):
    progress_updated = Signal(float)

    def __init__(self, link):
        super().__init__()
        self.link = link

    def run(self):
        try:
            youtubeObj = YouTube(self.link)
        except :
            # Handle the error here
            print("Invalid YouTube link")
            return

        youtubeObj = youtubeObj.streams.get_highest_resolution()

        # Estimate the total duration based on the file size
        total_duration = youtubeObj.filesize / 1000000 # in MB

        # Start the download
        start_time = time.time()
        youtubeObj.download()
        end_time = time.time()

        # Emit the progress through the signal
        elapsed_duration = end_time - start_time
        elapsed_percent = elapsed_duration / total_duration * 100
        self.progress_updated.emit(elapsed_percent)
