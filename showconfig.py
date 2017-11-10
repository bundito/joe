import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QWidget
from ui_joeconfig import Ui_Configuration
import config
from config import cfg

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_Configuration()
ui.setupUi(window)


def save_and_close():
    cfg['mediadirs']['TV'] = ui.tvEdit.text()
    cfg['mediadirs']['Movies'] = ui.moviesEdit.text()
    cfg['mediadirs']['Downloads'] = ui.downloadEdit.text()

    cfg['system_vars']['ProgramName'] = ui.prognameEdit.text()
    cfg['system_vars']['ProgramVer'] = ui.versionEdit.text()
    cfg['system_vars']['FilebotLoc'] = ui.filebotLocEdit.text()
    cfg['system_vars']['LogDir'] = ui.logDirEntry.text()

    if ui.testmodeCheck.isChecked() == True:
        cfg['system_vars']['DebugMode'] = 'True'
    else:
        cfg['system_vars']['DebugMode'] = 'False'

    config.write_complete_config(cfg)

    window.close()



# Set labels and populate text boxes
ui.dialogTitle.setText("%s %s" % (cfg['system_vars']['ProgramName'], cfg['system_vars']['ProgramVer']))

ui.tvEdit.setText(cfg['mediadirs']['TV'])
ui.moviesEdit.setText(cfg['mediadirs']['Movies'])
ui.downloadEdit.setText(cfg['mediadirs']['Downloads'])

ui.prognameEdit.setText(cfg['system_vars']['ProgramName'])
ui.versionEdit.setText((cfg['system_vars']['ProgramVer']))
ui.filebotLocEdit.setText(cfg['system_vars']['FilebotLoc'])
ui.logDirEntry.setText(cfg['system_vars']['LogDir'])

debugCfg = cfg['system_vars']['DebugMode']
if debugCfg == "True":
    debugChecked = True
else:
    debugChecked = False
ui.testmodeCheck.setChecked(debugChecked)

# Behold the power of buttons
ui.tvChoose.clicked.connect(lambda checked, src="tv": chooseDir(src))
ui.moviesChoose.clicked.connect(lambda checked, src="movies": chooseDir(src))
ui.downloadChoose.clicked.connect(lambda checked, src="download": chooseDir(src))
ui.logLocationChooser.clicked.connect(lambda checked, src="log": chooseDir(src))
ui.filebotChooser.clicked.connect(lambda checked, src="fb": chooseFile(src))

ui.cancelButton.clicked.connect(window.close)
ui.okButton.clicked.connect(lambda checked, src="fb": save_and_close())

# Directory and file choose dialog popups
def chooseDir(loc):
    dirName = QFileDialog.getExistingDirectory()

    if loc == "tv":
        ui.tvEdit.setText(dirName)
    if loc == "movies":
        ui.moviesEdit.setText(dirName)
    if loc == "download":
        ui.downloadEdit.setText(dirName)
    if loc == "log":
        ui.logDirEntry.setText(dirName)


def chooseFile(src):
    filename = QFileDialog.getOpenFileName()

    if src == "fb":
        ui.filebotLocEdit.setText(filename[0])


# save the changed configread and close the dialog box.





window.show()
sys.exit(app.exec_())