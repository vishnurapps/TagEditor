from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
 
class TagEditor(QDialog):
    def __init__(self):
        QDialog.__init__(self)
 
        self.lblTrackNumber = QLabel("Track Number :")
        self.leTrackNumber = QLineEdit()
        self.lblTitle = QLabel("Track Number :")
        self.leTitle = QLineEdit()
        self.lblArtist = QLabel("Artist :")
        self.leArtist = QLineEdit()
        self.lblAlbumArtist = QLabel("Album Artist:")
        self.leAlbumArtist = QLineEdit()
        self.lblGenre = QLabel("Genre")
        self.leGenre = QLineEdit()
        self.btnOpen = QPushButton("Open")
        self.btnApply = QPushButton("Apply")
        self.btnCancel = QPushButton("Cancel")
 
 
        layout = QGridLayout()
        layout.addWidget(self.lblTrackNumber, 0, 0)
        layout.addWidget(self.leTrackNumber, 0, 1)
        layout.addWidget(self.lblTitle, 1, 0)
        layout.addWidget(self.leTitle, 1, 1)
        layout.addWidget(self.lblArtist, 2, 0)
        layout.addWidget(self.leArtist, 2, 1)
        layout.addWidget(self.lblAlbumArtist, 3, 0)
        layout.addWidget(self.leAlbumArtist, 3, 1)
        layout.addWidget(self.lblGenre, 4, 0)
        layout.addWidget(self.leGenre, 4, 1)
        layout.addWidget(self.btnOpen, 5, 0)
        layout.addWidget(self.btnApply, 5, 1)
        layout.addWidget(self.btnCancel, 5, 2)
        self.setLayout(layout)


app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
#app.exec_()
dialog = TagEditor()
dialog.show()
app.exec_()
