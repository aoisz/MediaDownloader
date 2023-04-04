from PyQt5 import QtCore, QtGui, QtWidgets
class MyQTextEdit(QtWidgets.QTextEdit):

    def focusInEvent(self, e):
        self.setPlainText("")
        super(MyQTextEdit, self).focusInEvent(e)

    def focusOutEvent(self, e):
        self.setPlainText("Paste link here")
        super(MyQTextEdit, self).focusOutEvent(e)