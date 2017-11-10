import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from ui_joeconfig import Ui_Configuration

app = QApplication(sys.argv)  # <—- QApp doesn’t change
window = QMainWindow()            #  <—— WidgetClass from UI
ui = Ui_Configuration()         #   <—- imported file from ui_xxxx file
ui.setupUi(window)

window.show()
sys.exit(app.exec_())