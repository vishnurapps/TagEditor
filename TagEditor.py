from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import eyed3
 
class TagEditor(QDialog):

    def openAndLoad(self):
        print("Inside the openAndLoad")
        filename, filter= QFileDialog.getOpenFileName(parent=self, caption='Open file', filter='*.mp3')
        print(filename)
        self.audiofile = eyed3.load(filename)
        self.leTrackNumber.setText(str(self.audiofile.tag.track_num[0]))
        self.leTitle.setText(self.audiofile.tag.title)
        self.leArtist.setText(self.audiofile.tag.artist)
        self.leAlbumArtist.setText(self.audiofile.tag.album_artist)
        print(type(self.audiofile.tag.genre))
        self.leGenre.setText(str(self.audiofile.tag.genre))
        self.btnApply.setEnabled(True)
        self.btnOpen.setEnabled(False)

    def cancelAndClear(self):
        self.leTrackNumber.clear()
        self.leTitle.clear()
        self.leArtist.clear()
        self.leAlbumArtist.clear()
        self.leGenre.clear()
        self.btnOpen.setEnabled(True)

    def applyChanges(self):
        self.audiofile.tag.track_num = int(self.leTrackNumber.text())
        self.audiofile.tag.title = self.leTitle.text()
        self.audiofile.tag.artist = self.leArtist.text()
        self.audiofile.tag.album_artist = self.leAlbumArtist.text()
        self.audiofile.tag.genre = self.leGenre.text()
        self.audiofile.tag.save()

    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Mp3 Tag Editor")
        self.lblTrackNumber = QLabel("Track Number :")
        self.leTrackNumber = QLineEdit()
        self.leArt = QLabel()
        self.leArt.setPixmap(QPixmap("/home/vishnu/study/Music-icon.png"))
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
        self.groupBox1 = QGroupBox()
        self.group_layout = QGridLayout()
        self.groupBox1.setLayout(self.group_layout)

        self.group_layout.addWidget(self.lblTrackNumber, 0, 0)
        self.group_layout.addWidget(self.leTrackNumber, 0, 1)
        self.group_layout.addWidget(self.lblTitle, 1, 0)
        self.group_layout.addWidget(self.leTitle, 1, 1)
        self.group_layout.addWidget(self.lblArtist, 2, 0)
        self.group_layout.addWidget(self.leArtist, 2, 1)
        self.group_layout.addWidget(self.lblAlbum, 3, 0)
        self.group_layout.addWidget(self.leAlbum, 3, 1)
        self.group_layout.addWidget(self.lblAlbumArtist, 4, 0)
        self.group_layout.addWidget(self.leAlbumArtist, 4, 1)
        self.group_layout.addWidget(self.lblGenre, 5, 0)
        self.group_layout.addWidget(self.leGenre, 5, 1)
 
        layout = QGridLayout()
        layout.addWidget(self.groupBox1, 0, 0)
        layout.addWidget(self.leArt, 0, 1)
        layout.addWidget(self.btnOpen, 6, 0)
        layout.addWidget(self.btnApply, 6, 1)
        layout.addWidget(self.btnCancel, 6, 2)
        self.setLayout(layout)
        self.btnOpen.clicked.connect(self.openAndLoad)
        self.btnApply.clicked.connect(self.applyChanges)
        self.btnCancel.clicked.connect(self.cancelAndClear)


		
		
		
app = QApplication(sys.argv)
#app.exec_()
dialog = TagEditor()
dialog.show()
app.exec_()
