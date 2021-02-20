import os
import sys
from shutil import move
from functions import time_check, new_folder
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random

try:
	with open(os.path.dirname(os.path.realpath(__file__)) + "/" + "folder.txt", "r") as f:
		folder = f.read()
		folder_dir = folder
except:
	folder_dir = "C:/"

try:
	with open(os.path.dirname(os.path.realpath(__file__)) + "/" + "file.txt", "r") as f:
		file_folder = f.read()
		file_dir = file_folder
except:
	file_dir = "C:/"


# Init values
rachunki = ["PRĄD", "GAZ", "BANK", "INNE", "SMIECI", "POLSAT", "TELEFON", "IZBA"]
dates = date.today()
os.chdir(folder_dir)
cytaty = ["Ziemia to kropka pod znakiem zapytania./Stanisław Jerzy Lec",
		  "Ziemia jest twoim okrętem, nie siedzibą./Św. Augustyn",
		  "Ziemia nigdy nie oddaje bez procentu tego, co otrzymała./Cyceron",
		  "Pokój na Ziemi nie może być osiągnięty bez pokoju z przyrodą./Anonim",
		  "Z orbity Ziemia jest piękna, błękitna, widać wszystko w cudownych kolorach./Mirosław Hermaszewski",
		  "Ziemia więcej mówi nam o nas niż wszystkie książki./Antoine de Saint-Exupéry"]
random_numb = random.randrange(0,len(cytaty))
cytat = cytaty[random_numb].split("/")[0]
autor = cytaty[random_numb].split("/")[1]

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.cytat = QtWidgets.QLabel(self.centralwidget)
		self.cytat.setGeometry(QtCore.QRect(0, 0, 800, 40))
		self.cytat.setObjectName("cytat")
		self.cytat.setFont(QFont("Arial", 15))
		self.autor = QtWidgets.QLabel(self.centralwidget)
		self.autor.setGeometry(QtCore.QRect(0, 40, 800, 40))
		self.autor.setObjectName("autor")
		self.autor.setFont(QFont("Arial", 15))
		self.prad = QtWidgets.QPushButton(self.centralwidget)
		self.prad.setGeometry(QtCore.QRect(100, 270, 100, 40))
		self.prad.setObjectName("prad")
		self.prad.clicked.connect(lambda: self.prad_file())
		self.gaz = QtWidgets.QPushButton(self.centralwidget)
		self.gaz.setGeometry(QtCore.QRect(250, 270, 100, 40))
		self.gaz.setObjectName("gaz")
		self.gaz.clicked.connect(lambda: self.gaz_file())
		self.bank = QtWidgets.QPushButton(self.centralwidget)
		self.bank.setGeometry(QtCore.QRect(400, 270, 100, 40))
		self.bank.setObjectName("bank")
		self.bank.clicked.connect(lambda: self.bank_file())
		self.inne = QtWidgets.QPushButton(self.centralwidget)
		self.inne.setGeometry(QtCore.QRect(550, 270, 100, 40))
		self.inne.setObjectName("inne")
		self.inne.clicked.connect(lambda: self.other_file())
		#
		self.smieci = QtWidgets.QPushButton(self.centralwidget)
		self.smieci.setGeometry(QtCore.QRect(100, 330, 100, 40))
		self.smieci.setObjectName("smieci")
		self.smieci.clicked.connect(lambda: self.smieci_file())
		#
		self.polsat = QtWidgets.QPushButton(self.centralwidget)
		self.polsat.setGeometry(QtCore.QRect(250, 330, 100, 40))
		self.polsat.setObjectName("polsat")
		self.polsat.clicked.connect(lambda: self.polsat_file())
		#
		self.telefon = QtWidgets.QPushButton(self.centralwidget)
		self.telefon.setGeometry(QtCore.QRect(400, 330, 100, 40))
		self.telefon.setObjectName("telefon")
		self.telefon.clicked.connect(lambda: self.telefon_file())
		#
		self.izba = QtWidgets.QPushButton(self.centralwidget)
		self.izba.setGeometry(QtCore.QRect(550, 330, 100, 40))
		self.izba.setObjectName("izba")
		self.izba.clicked.connect(lambda: self.izba_file())
		#
		self.zapytanie = QtWidgets.QLabel(self.centralwidget)
		self.zapytanie.setGeometry(QtCore.QRect(250, 100, 550, 100))
		self.zapytanie.setObjectName("zapytanie")
		self.zapytanie.setFont(QFont("Arial", 20))
		self.button_file_direct = QtWidgets.QPushButton(self.centralwidget)
		self.button_file_direct.setGeometry(QtCore.QRect(110, 510, 100, 40))
		self.button_file_direct.setObjectName("button_file_direct")
		self.button_file_direct.clicked.connect(lambda: self.select_file_direct())
		self.button_folder_direct = QtWidgets.QPushButton(self.centralwidget)
		self.button_folder_direct.setGeometry(QtCore.QRect(510, 510, 100, 40))
		self.button_folder_direct.setObjectName("button_folder_direct")
		self.button_folder_direct.clicked.connect(lambda: self.select_folder_direct())
		self.label_file_direct = QtWidgets.QLabel(self.centralwidget)
		self.label_file_direct.setGeometry(QtCore.QRect(110, 480, 250, 20))
		self.label_file_direct.setObjectName("label_file_direct")
		self.label_folder_direct = QtWidgets.QLabel(self.centralwidget)
		self.label_folder_direct.setGeometry(QtCore.QRect(510, 480, 250, 20))
		self.label_folder_direct.setObjectName("label_folder_direct")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.cytat.setText(_translate("MainWindow", cytat))
		self.autor.setText(_translate("MainWindow", autor))
		self.prad.setText(_translate("MainWindow", rachunki[0]))
		self.gaz.setText(_translate("MainWindow", rachunki[1]))
		self.bank.setText(_translate("MainWindow", rachunki[2]))
		self.inne.setText(_translate("MainWindow", rachunki[3]))
		self.smieci.setText(_translate("MainWindow", rachunki[4]))
		self.polsat.setText(_translate("MainWindow", rachunki[5]))
		self.telefon.setText(_translate("MainWindow", rachunki[6]))
		self.izba.setText(_translate("MainWindow", rachunki[7]))
		self.zapytanie.setText(_translate("MainWindow", "Jaki jest to rachunek?"))
		self.button_file_direct.setText(_translate("MainWindow", "Plik"))
		self.button_folder_direct.setText(_translate("MainWindow", "Folder"))
		self.label_file_direct.setText(_translate("MainWindow", file_dir))
		self.label_folder_direct.setText(_translate("MainWindow", folder_dir))

	def prad_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[0])
				move(file_dir + "/" + rachunki[0], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[0], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def gaz_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[1])
				move(file_dir + "/" + rachunki[1], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[1], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def bank_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[2])
				move(file_dir + "/" + rachunki[2], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[2], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def other_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				self.other, check = QInputDialog.getText(None, 'Input Dialog', 'Jaki to rachunek?')
				os.rename(self.file, self.other)
				move(file_dir + "/" + self.other, folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(self.other, self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def smieci_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[4])
				move(file_dir + "/" + rachunki[4], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[4], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def polsat_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[5])
				move(file_dir + "/" + rachunki[5], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[5], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def telefon_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[6])
				move(file_dir + "/" + rachunki[6], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[6], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def izba_file(self):
		try:
			if self.check() == True:
				global files_num
				self.file = time_check(os.listdir(file_dir), file_dir)
				os.rename(self.file, rachunki[7])
				move(file_dir + "/" + rachunki[7], folder_dir + "/" + dates.strftime("%m.%Y"))
				MainWindow.showMinimized()
				files_num = len(os.listdir(file_dir))
		except:
			os.rename(rachunki[7], self.file)
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Ten rachunek już istnieje")
			x = msg.exec_()
			pass

	def select_file_direct(self):
		global file_dir
		global files_num
		file_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose file Directory", "C:\\")
		files_num = len(os.listdir(file_dir))
		f = open(os.path.dirname(os.path.realpath(__file__)) + "/" + "file.txt", "w")
		f.write(file_dir)
		f.close()
		self.label_file_direct.setText(file_dir)

	def select_folder_direct(self):
		global folder_dir
		new_folder()
		folder_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose folder Directory", "C:\\")
		with open(os.path.dirname(os.path.realpath(__file__)) + "/" + "folder.txt", "w") as f:
			f.write(folder_dir)
		self.label_folder_direct.setText(folder_dir)

	def check(self):
		global files_num
		if files_num < len(os.listdir(file_dir)):
			return True
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setText("Brak nowych plików")
			x = msg.exec_()
			return False

# GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

new_folder()
files_num = len(os.listdir(file_dir))
MainWindow.showMinimized()
MainWindow.show()
sys.exit(app.exec_())


