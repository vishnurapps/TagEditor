from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s ::  %(name)s :: %(funcName)s :: %(levelname)s :: %(message)s')
file_handler = logging.FileHandler("run.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ClickableQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self):
        QLabel.__init__(self)
        logger.debug("Inside the ClickableQlabel __init__")

    def mousePressEvent(self, QMouseEvent):
        logger.debug("Inside the ClickableQlabel mousePressEvent")
        self.clicked.emit()