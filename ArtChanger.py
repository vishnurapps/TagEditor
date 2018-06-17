import logging
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QDialog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s ::  %(name)s :: %(funcName)s :: %(levelname)s :: %(message)s')
file_handler = logging.FileHandler("run.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ArtChanger(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        logger.debug("Inside ArtChanger __init__")
        self.setWindowTitle("Change Album Art")
        self.btnWeb = QPushButton("From Web")
        self.btnLocal = QPushButton("From Local")
        self.btnCancel = QPushButton("Cancel")
        layout = QHBoxLayout()
        layout.addWidget(self.btnWeb)
        layout.addWidget(self.btnLocal)
        layout.addWidget(self.btnCancel)
        logger.debug("Layout created and elements added")
        self.btnWeb.clicked.connect(self.from_web)
        self.btnLocal.clicked.connect(self.from_local)
        self.btnCancel.clicked.connect(self.cancel_and_close)
        self.setLayout(layout)
        logger.debug("Buttons connected")

    def from_web(self):
        logger.debug("Inside ArtChanger from_web")

    def from_local(self):
        logger.debug("Inside ArtChanger from_local")

    def cancel_and_close(self):
        logger.debug(("Inside ArtChanger cancel_and_close"))
        self.close()