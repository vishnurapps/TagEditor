import logging
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QFileDialog, QLineEdit, QGridLayout
from PyQt5.QtGui import QPixmap
from subprocess import PIPE, Popen

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s ::  %(name)s :: %(funcName)s :: %(levelname)s :: %(message)s')
file_handler = logging.FileHandler("run.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ArtChanger(QDialog):
    def __init__(self, album, art):
        QDialog.__init__(self)
        self.album = album
        self.art = art
        logger.debug("Inside ArtChanger __init__")
        self.setWindowTitle("Change Album Art")
        self.btnWeb = QPushButton("From Web")
        self.btnLocal = QPushButton("From Local")
        self.btnCancel = QPushButton("Cancel")
        self.leImageBox = QLineEdit()
        self.leImageBox.setPlaceholderText("Enter image url")
        self.buttonLayout = QGridLayout()
        self.buttonLayout.addWidget(self.btnWeb, 0, 0)
        self.buttonLayout.addWidget(self.btnLocal, 0, 1)
        self.buttonLayout.addWidget(self.btnCancel, 0, 2)
        logger.debug("Layout created and elements added")
        self.btnWeb.clicked.connect(self.from_web)
        self.btnLocal.clicked.connect(self.from_local)
        self.btnCancel.clicked.connect(self.cancel_and_close)
        self.setLayout(self.buttonLayout)
        logger.debug("Buttons connected")

    def from_web(self):
        logger.debug("Inside ArtChanger from_web")
        self.buttonLayout.addWidget(self.leImageBox, 1, 0, 2, 0)

    def from_local(self):
        logger.debug("Inside ArtChanger from_local")
        filename, filter= QFileDialog.getOpenFileName(parent=self, caption='Open file', filter='*.jpg, *.jpeg, *.png')
        pixmap = QPixmap(filename)
        copy = Popen(['cp', filename, "/tmp/sample.jpg"], stdout=PIPE)
        copy.communicate()
        pixmap = pixmap.scaledToHeight(240)
        pixmap = pixmap.scaledToWidth(240)
        self.art.setPixmap(pixmap)

    def cancel_and_close(self):
        logger.debug(("Inside ArtChanger cancel_and_close"))
        self.close()