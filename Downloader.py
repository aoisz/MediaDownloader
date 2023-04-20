from PyQt5.QtCore import QThread, pyqtSignal
from pytube import YouTube

class Downloader(QThread):
    processSignal = pyqtSignal(float)

    def __init__(self, parent=None):
        super(Downloader, self).__init__(parent=parent)
        self.path = None
        self.url = None
        self.video = None
        self.stream = None

    def download_video(self, url, path):
        self.path = path
        self.url = url
        
        self.start()

    def run(self):
        self.video = YouTube(self.url)
        self.video.register_on_progress_callback(self.return_progress)
        self.stream = self.video.streams.get_highest_resolution()
        self.stream.download()
        # self.stream = highest_res.first()
        # self.stream.download(self.path)
        
    def return_progress(self, chunk, file_handle, bytes_remaining):
        percentage = 1 - bytes_remaining / self.stream.filesize
        self.processSignal.emit(percentage)