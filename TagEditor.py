from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import eyed3
import logging
from ClickableQLabel import ClickableQLabel
from ArtChanger import ArtChanger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s ::  %(name)s :: %(funcName)s :: %(levelname)s :: %(message)s')
file_handler = logging.FileHandler("run.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class TagEditor(QDialog):

    def openAndLoad(self):
        logger.debug("Inside the TagEditor openAndLoad")
        filename, filter= QFileDialog.getOpenFileName(parent=self, caption='Open file', filter='*.mp3')
        logger.debug(filename)
        self.audiofile = eyed3.load(filename)
        self.leTrackNumber.setText(str(self.audiofile.tag.track_num[0]))
        self.leTitle.setText(self.audiofile.tag.title)
        self.leArtist.setText(self.audiofile.tag.artist)
        self.leAlbumArtist.setText(self.audiofile.tag.album_artist)
        logger.debug(type(self.audiofile.tag.genre))
        self.leGenre.setText(str(self.audiofile.tag.genre))
        self.btnApply.setEnabled(True)
        self.btnOpen.setEnabled(False)

    def cancelAndClear(self):
        logger.debug("Inside TagEditor cancelAndClear")
        self.leTrackNumber.clear()
        self.leTitle.clear()
        self.leArtist.clear()
        self.leAlbumArtist.clear()
        self.leGenre.clear()
        self.btnOpen.setEnabled(True)

    def applyChanges(self):
        logger.debug("Inside TagEditor applyChanges")
        self.audiofile.tag.track_num = int(self.leTrackNumber.text())
        self.audiofile.tag.title = self.leTitle.text()
        self.audiofile.tag.artist = self.leArtist.text()
        self.audiofile.tag.album_artist = self.leAlbumArtist.text()
        self.audiofile.tag.genre = self.leGenre.text()
        self.audiofile.tag.save()

    def __init__(self):
        QDialog.__init__(self)
        logger.debug("Inside TagEditor __init__")
        self.setWindowTitle("Mp3 Tag Editor")
        self.lblTrackNumber = QLabel("Track Number :")
        self.leTrackNumber = QLineEdit()
        self.lblArt = ClickableQLabel()
        pixmap = QPixmap("/home/vishnu/study/Music-icon.png")
        pixmap = pixmap.scaledToHeight(240)
        pixmap = pixmap.scaledToWidth(240)
        #self.lblArt.setPixmap(QPixmap("/home/vishnu/study/Music-icon.png"))
        self.lblArt.setPixmap(pixmap)
        self.lblTitle = QLabel("Title :")
        self.leTitle = QLineEdit()
        self.lblArtist = QLabel("Artist :")
        self.leArtist = QLineEdit()
        self.lblAlbum = QLabel("Album :")
        self.leAlbum = QLineEdit()
        self.lblAlbumArtist = QLabel("Album Artist:")
        self.leAlbumArtist = QLineEdit()
        self.lblGenre = QLabel("Genre")
        self.leGenre = QLineEdit()
        self.btnOpen = QPushButton("Open")
        self.btnApply = QPushButton("Apply")
        self.btnCancel = QPushButton("Cancel")
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.dataBox = QGroupBox()

        self.dataBoxLayout = QGridLayout()
        self.dataBox.setLayout(self.dataBoxLayout)
        self.songDataLayout = QHBoxLayout()
        self.buttonBoxLayout = QHBoxLayout()

        self.dataBoxLayout.addWidget(self.lblTrackNumber, 0, 0)
        self.dataBoxLayout.addWidget(self.leTrackNumber, 0, 1)
        self.dataBoxLayout.addWidget(self.lblTitle, 1, 0)
        self.dataBoxLayout.addWidget(self.leTitle, 1, 1)
        self.dataBoxLayout.addWidget(self.lblArtist, 2, 0)
        self.dataBoxLayout.addWidget(self.leArtist, 2, 1)
        self.dataBoxLayout.addWidget(self.lblAlbum, 3, 0)
        self.dataBoxLayout.addWidget(self.leAlbum, 3, 1)
        self.dataBoxLayout.addWidget(self.lblAlbumArtist, 4, 0)
        self.dataBoxLayout.addWidget(self.leAlbumArtist, 4, 1)
        self.dataBoxLayout.addWidget(self.lblGenre, 5, 0)
        self.dataBoxLayout.addWidget(self.leGenre, 5, 1)

        self.songDataLayout.addWidget(self.dataBox)
        self.songDataLayout.addWidget(self.lblArt)
        self.buttonBoxLayout.addSpacerItem(self.horizontalSpacer)
        self.buttonBoxLayout.addWidget(self.btnOpen)
        self.buttonBoxLayout.addWidget(self.btnApply)
        self.buttonBoxLayout.addWidget(self.btnCancel)

        layout = QVBoxLayout()
        layout.addLayout(self.songDataLayout)
        layout.addLayout(self.buttonBoxLayout)

        self.setLayout(layout)
        self.btnOpen.clicked.connect(self.openAndLoad)
        self.btnApply.clicked.connect(self.applyChanges)
        self.btnCancel.clicked.connect(self.cancelAndClear)
        self.lblArt.clicked.connect(self.change_art)
        
    def change_art(self):
        logger.debug("Inside TagEditor change_art")
        dia = ArtChanger(self.leAlbum.text(), self.lblArt)
        dia.exec_()

app = QApplication(sys.argv)
#app.exec_()
dialog = TagEditor()
dialog.show()
app.exec_()
