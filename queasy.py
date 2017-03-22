import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_queasy import Ui_MainWindow

import os

UserHome = os.path.expanduser("~")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
   
    def assignWidgets(self):
        self.generateImage.clicked.connect(self.goPushed)
   
    def goPushed(self):
        ourFile = open("%s/%s.txt"%(UserHome, self.deckNameEntry.displayText()), "w")
        for line in self.deckListEntry.toPlainText().split("\n"):
            ourFile.write("%s\n"%line)
        
        ourFile.close()
        
        os.system('cd ../StackIt && python StackIt.py "%s/%s.txt"'%(UserHome, self.deckNameEntry.displayText()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
