import os, sys, ntpath
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.OpenWorkspaceDialog import openworkspacedialog
sys.path.insert(1, "./")
sys.path.insert(1, "../../")

from PyQt5 import QtCore, QtGui, QtWidgets
'''
Author: Ernesto Vazquez
Dialog to browse files to open a workspace
'''

class Ui_OpenWorkspaceDialog(object):

    def setupUi(self, OpenWorkspaceDialog):
        OpenWorkspaceDialog.setObjectName("OpenWorkspaceDialog")
        OpenWorkspaceDialog.resize(576, 121)
        OpenWorkspaceDialog.setMinimumSize(QtCore.QSize(576, 121))
        OpenWorkspaceDialog.setWindowTitle("")
        self.label = QtWidgets.QLabel(OpenWorkspaceDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 411, 17))
        self.label.setObjectName("label")
        self.linePath = QtWidgets.QLineEdit(OpenWorkspaceDialog)
        self.linePath.setGeometry(QtCore.QRect(30, 40, 391, 25))
        self.linePath.setObjectName("linePath")
        self.browseButton = QtWidgets.QPushButton(OpenWorkspaceDialog)
        self.browseButton.setGeometry(QtCore.QRect(440, 40, 83, 25))
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.openworkspace)
        self.addButton = QtWidgets.QDialogButtonBox(OpenWorkspaceDialog)
        self.addButton.setGeometry(QtCore.QRect(440, 70, 83, 25))
        self.addButton.setObjectName("addButton")
        self.addButton.accepted.connect(OpenWorkspaceDialog.accept)
        self.retranslateUi(OpenWorkspaceDialog)
        QtCore.QMetaObject.connectSlotsByName(OpenWorkspaceDialog)

    def openworkspace(self):
        '''
        Open the selected workspace file
        '''
        try:
            title = "Please select Workspace"
            directory = "./"
            #Look for files with pdbws extension only
            ftype = "JSON files (*.pdbws)"
            dialog = QtWidgets.QFileDialog(None, title, directory, ftype)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.filename = str(dialog.selectedFiles()[0])
                print(self.filename)
                self.linePath.setText(self.filename)
        except:
            print("Fix")

    def retranslateUi(self, OpenWorkspaceDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("OpenWorkspaceDialog", "Create a New Workspace / Open New Workspace"))
        self.browseButton.setText(_translate("OpenWorkspaceDialog", "Browse"))
        self.addButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
