from PyQt5 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class ResolutionOption(QWidget):
    def __init__(self, parent=None):
        super(ResolutionOption, self).__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self.parent)
        self.centralwidget.setObjectName("centralwidget")
        layout = QHBoxLayout()
        layout.addWidget(self.centralwidget)

        self.setLayout(layout)

    
    def setup(self, youtubeObject):
        self.imageHolder = QPixmap(youtubeObject.thumbnail_url)
                
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.imageHolder)

        layout = QVBoxLayout()
        layout.addLayout(controlLayout)

        self.setLayout(layout)