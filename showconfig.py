import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from ui_joeconfig import Ui_Configuration
from config import cfg

app = QApplication(sys.argv)  # <—- QApp doesn’t change
window = QMainWindow()            #  <—— WidgetClass from UI
ui = Ui_Configuration()         #   <—- imported file from ui_xxxx file
ui.setupUi(window)


print(cfg)

ui.tvEdit.setText(cfg['mediadirs']['TV'])
ui.moviesEdit.setText((cfg['mediadirs']['Movies']))
ui.downloadEdit.setText((cfg['mediadirs']['Downloads']))
#-----
ui.prognameEdit.setText(cfg['system_vars']['ProgramName'])
ui.versionEdit.setText((cfg['system_vars']['ProgramVer']))
ui.filebotLocEdit.setText(cfg['system_vars']['FilebotLoc'])
ui.binDirectory.setText(cfg['system_vars']['ProgramDir'])

debugCfg = cfg['system_vars']['DebugMode']
if debugCfg == "True":
    debugChecked = True
else:
    debugChecked = False
ui.testmodeCheck.setChecked(debugChecked)

window.show()
sys.exit(app.exec_())