# uncompyle6 version 2.13.3
# Python bytecode 3.5 (3350)
# Decompiled from: Python 3.5.2 (default, Sep 14 2017, 22:51:06)
# [GCC 5.4.0 20160609]
# Embedded file name: /home/bundito/PycharmProjects/joe/showconfig.py
# Compiled at: 2017-11-17 07:21:56
# Size of source mod 2**32: 3756 bytes
import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog, QApplication

from aborted.Ui_config_dialog import Ui_configDialog
from config import cfg

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_configDialog()
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
    window.hide()
else:
    cfg['system_vars']['DebugMode'] = 'False'
    window.hide()



window.setObjectName("Dialog")
ui.progNameTitle.setText('%s %s' % (cfg['system_vars']['ProgramName'], cfg['system_vars']['ProgramVer']))
ui.tvEdit.setText(cfg['mediadirs']['TV'])
ui.moviesEdit.setText(cfg['mediadirs']['Movies'])
ui.downloadEdit.setText(cfg['mediadirs']['Downloads'])
ui.prognameEdit.setText(cfg['system_vars']['ProgramName'])
ui.versionEdit.setText(cfg['system_vars']['ProgramVer'])
ui.filebotLocEdit.setText(cfg['system_vars']['FilebotLoc'])
ui.logDirEntry.setText(cfg['system_vars']['LogDir'])
debugCfg = cfg['system_vars']['DebugMode']

if debugCfg == 'True':
    debugChecked = True
else:
    debugChecked = False

ui.testmodeCheck.setChecked(debugChecked)
ui.tvChoose.clicked.connect(lambda checked, src='tv': chooseDir(src))
ui.moviesChoose.clicked.connect(lambda checked, src='movies': chooseDir(src))
ui.downloadChoose.clicked.connect(lambda checked, src='download': chooseDir(src))
ui.logLocationChooser.clicked.connect(lambda checked, src='log': chooseDir(src))
ui.filebotChooser.clicked.connect(lambda checked, src='fb': chooseFile(src))
ui.cancelButton.clicked.connect(lambda checked, src='cancel': window.hide())
ui.saveButton.clicked.connect(save_and_close)


def chooseDir(loc):
    dirName = QFileDialog.getExistingDirectory()
    if loc == 'tv':
        if dirName:
            ui.tvEdit.setText(dirName)
        else:
            ui.tvEdit.setText(cfg['mediadirs']['TV'])
        if loc == 'movies':
            if dirName:
                ui.moviesEdit.setText(dirName)
            else:
                ui.moviesEdit.setText(cfg['mediadirs']['Movies'])
            if loc == 'download':
                if dirName:
                    ui.downloadEdit.setText(dirName)
                else:
                    ui.downloadEdit.setText(cfg['mediadirs']['Downloads'])
                if loc == 'log':
                    if dirName:
                        ui.logDirEntry.setText(dirName)
                    else:
                        ui.logDirEntry.setText(cfg['system_vars']['LogDir'])

def chooseFile(src):
    filename = QFileDialog.getOpenFileName()

    if src == 'fb':
        ui.filebotLocEdit.setText(filename[0])



