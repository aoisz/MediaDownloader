from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QThread
from PySide6.QtCore import *

class DownloadThread(QtCore.QThread):
    progress_updated = QtCore.pyqtSignal(int)
    
    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.function(*self.args, **self.kwargs)

    def update_progress(self, progress):
        self.progress_updated.emit(progress)
