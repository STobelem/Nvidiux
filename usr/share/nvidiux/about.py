# -*- coding: utf-8 -*-
#!/usr/bin/python2

# Copyright 2014 Payet Guillaume
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_About(QWidget):
	
	def __init__(self,parent=None):
		super (Ui_About, self).__init__(parent)
		self.createWidgets()
		
	def createWidgets(self):
		self.setObjectName(_fromUtf8("About Nvidiux"))
		self.setWindowTitle("A propos Nvidiux")
		self.resize(600, 530)
		self.Img = QtGui.QLabel(self)
		self.Img.move(190,5)
		self.Img.setPixmap(QtGui.QPixmap("/usr/share/nvidiux/img/drivers_nvidia_linux.png"))	
		self.title = QtGui.QLabel(self)
		self.title.move(210,142)
		font = QtGui.QFont()
		font.setPointSize(40)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		font.setStrikeOut(False)
		font.setStyleStrategy(QtGui.QFont.PreferAntialias)
		self.title.setFont(font)
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setText("Nvidiux")
		self.labelInfo = QtGui.QLabel(self)
		self.labelInfo.move(90,200)
		self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		font.setStyleStrategy(QtGui.QFont.PreferAntialias)
		self.labelInfo.setFont(font)
		self.labelInfo.setText(_fromUtf8("Permet d'underclocker ou d'overclocker votre gpu nvidia\nVersion 0.9 Beta 1 (11/03/15)\n(C) 2014 Payet Guillaume\nNvidiux n'est en aucun cas affilié à Nvidia"))
		self.textBrowser = QtGui.QTextBrowser(self)
		self.textBrowser.setGeometry(QtCore.QRect(10, 280, 580, 240))
		txtFile = open('/usr/share/nvidiux/gpl-3.0.txt', 'r')
		if txtFile != None:
			self.textBrowser.setText(_fromUtf8(txtFile.read()))
		else:
			self.textBrowser.setText(_fromUtf8("Programme distribué sous license GPL V3\nVoir http://www.gnu.org/licenses/gpl-3.0.txt"))
		
		def retranslateUi(self):
			self.setWindowTitle(_translate("About", "À Propos Nvidiux", None))
			self.setWindowTitle(_translate("About", "Permet d'underclocker ou d'overclocker votre gpu nvidia\nVersion 0.9 Beta 1 (11/03/15)\n(C) 2014 Payet Guillaume\nNvidiux n'est en aucun cas affilié à Nvidia", None))
