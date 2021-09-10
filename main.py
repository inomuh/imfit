#!/usr/bin/env python3

import sys
import time
import ast
import json
import os
import re

from PySide6 import *
from modules import *
from widgets import *

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import QDir
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
	widgets = None
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)   

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		global widgets
		widgets = self.ui

		Settings.ENABLE_CUSTOM_TITLE_BAR = True

		#  APP NAME
		title = "IM-FIT"
		description = "IM-FIT"

		#  APPLY TEXTS
		self.setWindowTitle(title)
		widgets.titleRightInfo.setText(description)

		# TOGGLE MENU
		widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

		# SET UI DEFINITIONS
		UIFunctions.uiDefinitions(self)

		# DATAS
		self.placeForMutation = list()

		### FUNCTIONS
		
		# TAKE FILE FUNCTIONS
				
		# General files function
		def get_file(self):
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)

			if dialog.exec_():
				file_name = dialog.selectedFiles()

		# Take ".py" file function
		def get_file_py(self):
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setNameFilter(("*.py"))

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				if file_name[0].endswith('.py'):
					with open(file_name[0], 'r') as f:
						data = f.read()
						widgets.textEdit.setPlainText(data)
						f.close()

		# Take ".json" file function
		def get_file_json(self):
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setNameFilter(("*.json"))

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				if file_name[0].endswith('.json'):
					with open(file_name[0], 'r') as f:
						data = f.read()
						widgets.textEdit_3.setPlainText(data)
						f.close()
				
		# Take ".rosbag" file function
		def get_file_rosbag(self):
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setNameFilter(("*.bag"))

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				if file_name[0].endswith('.bag'):
					with open(file_name[0], 'r') as f:
						data = f.read()
						widgets.textEditor.setPlainText(data)
						f.close()

		# EDIT BUTTONS 
		
		# Source Code Edit Checkbox on START PAGE
		def editSourceCodes(self):
			if widgets.checkBox_8.isChecked()==True:
				widgets.textEdit.setReadOnly(False)
			else:
				widgets.textEdit.setReadOnly(True)
		
		# Workload Edit Checkbox on START PAGE
		def editWorkload(self):
			if widgets.checkBox_5.isChecked()==True:
				widgets.textEdit_3.setReadOnly(False)
			else:
				widgets.textEdit_3.setReadOnly(True)

		# Select Code Snippets wit One Click
		def selectWithOneClickedForCS(self):
			try:
				clickedItemText=widgets.listWidget_10.currentItem().text()

				with open('code_snippets.json') as codeSnippetsFromJson:
					codeSnippetNameList = json.load(codeSnippetsFromJson)
				
				lenOfCodeSnipList = (widgets.listWidget_10.count())-3

				for i in range(lenOfCodeSnipList):
					snippetName = codeSnippetNameList["code_snippets"][i]["Snippets"]["Snippet_Name"]

					if clickedItemText == snippetName:
						snippetDescription = codeSnippetNameList["code_snippets"][i]["Snippets"]["Process"]
						widgets.textEdit_24.setPlainText(snippetDescription)
			except AttributeError:
				pass
			
		# Select Snippet Button on Start Page
		def codeSnippetSelect(self):
			selectedRow = widgets.listWidget_10.currentItem().text()
			row=selectedRow.split("\n")
			widgets.listWidget_8.addItems(row)

		# Select Task on Create on Workload Page
		def taskSelect(self):
			selectedRow = widgets.listWidget_21.currentItem().text()
			row=selectedRow.split("\n")
			widgets.listWidget_22.addItems(row)

		# Select Task with One Click on Workload Page
		def taskInfoWithOneClick(self):
			clickedItemText = widgets.listWidget_21.currentItem().text()
			widgets.textEdit_14.clear()

			jsonTypeTasks = widgets.plainTextEdit.toPlainText()
			tasksJsonList = json.loads(jsonTypeTasks)

			for i in range(0,len(tasksJsonList['gorevler'])):
				taskName = str(tasksJsonList['gorevler'][i]['Task']['Task_ID'])
				if taskName == clickedItemText:
					taskDetails = str(tasksJsonList['gorevler'][i]['Task'])
					for i in taskDetails:
						widgets.textEdit_14.setPlainText(widgets.textEdit_14.toPlainText()+i)

		# Select Line For Mutation on FI Plan Page
		def selectPossibleMutationLine(self):
			possibleMutationLine = widgets.listWidget.currentItem().text()
			widgets.textEdit_13.setPlainText(possibleMutationLine)

		# Select Fault From Fault Library on FI Plan Page
		def faultSelectFromLibrary (self):
			if len(widgets.textEdit_13.toPlainText()) != 0:
				selectedRow = widgets.listWidget_3.currentItem().text()
				row = "Line: " + widgets.textEdit_13.toPlainText() + "\nFault: " + selectedRow
				text = row.split("\n")
				widgets.listWidget_7.addItems(text)
			else:
				pass

		# This Function Shows Fault's Information from Fault Library on FI Plan Page
		def selectWithOneClickedForFIPlan (self):
			clickedItemText=widgets.listWidget_3.currentItem().text()

			with open('faultLibrary.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)
			
			lenOfFaultList = widgets.listWidget_3.count()

			for i in range(lenOfFaultList):
				faultName = faultList["fault_library"][i]["fault"]["Fault_Name"]

				if clickedItemText == faultName:
					faultDescription = faultList["fault_library"][i]["fault"]["Explain"]
					widgets.textEdit_17.setPlainText(faultDescription)

		# LIST'S (listWidget's) CLICK CONNECTS

		# Line Selection For Mutation on FI Plan Page
		widgets.listWidget.itemClicked.connect(selectPossibleMutationLine)

		# Line Selection and Show Information About Fault on FI Plan Page
		widgets.listWidget_3.itemDoubleClicked.connect(faultSelectFromLibrary)
		widgets.listWidget_3.itemClicked.connect(selectWithOneClickedForFIPlan)
				
		# Code Snippet Selection on Start Page
		widgets.listWidget_10.itemDoubleClicked.connect(codeSnippetSelect)
		widgets.listWidget_10.itemClicked.connect(selectWithOneClickedForCS)

		# Select Task and Show Task's Details on Workload Page
		widgets.listWidget_21.itemClicked.connect(taskInfoWithOneClick)
		widgets.listWidget_21.itemDoubleClicked.connect(taskSelect)


		# BUTTONS CLICK CONNECTS

		# LEFT MENU BUTTON CONNECTS
		widgets.btn_home.clicked.connect(self.buttonClick)
		widgets.btn_start.clicked.connect(self.buttonClick)
		widgets.btn_scan.clicked.connect(self.buttonClick)
		widgets.btn_fiplan.clicked.connect(self.buttonClick)
		widgets.btn_execution.clicked.connect(self.buttonClick)
		widgets.btn_monitoring.clicked.connect(self.buttonClick)

		# GO TO BUTTON CONNECTS
		widgets.btn_go_start.clicked.connect(self.buttonClick)
		widgets.btn_go_scan.clicked.connect(self.buttonClick)
		widgets.btn_go_fiplan.clicked.connect(self.buttonClick)
		widgets.btn_go_exe.clicked.connect(self.buttonClick)
		widgets.btn_go_monitoring.clicked.connect(self.buttonClick)
		widgets.btn_new_one.clicked.connect(self.buttonClick)

		# START PAGE BUTTON CONNECTS
		widgets.btn_open_folder.clicked.connect(get_file_py)
		widgets.btn_select_workload.clicked.connect(get_file_json)
		widgets.btn_create_workload.clicked.connect(self.buttonClick)
		widgets.btn_save_workload.clicked.connect(self.buttonClick)
		widgets.checkBox_5.clicked.connect(self.buttonClick)
		widgets.btn_clear_codes.clicked.connect(self.buttonClick)
		widgets.btn_clear_workload.clicked.connect(self.buttonClick)
		widgets.btn_add_custom.clicked.connect(self.buttonClick)
		widgets.checkBox_8.clicked.connect(editSourceCodes)
		widgets.checkBox_5.clicked.connect(editWorkload)

		# CODE SNIPPET BUTTON CONNECTS
		widgets.btn_create_code.clicked.connect(self.buttonClick)
		widgets.btn_select_snippet.clicked.connect(codeSnippetSelect)
		widgets.btn_remove_snip.clicked.connect(self.buttonClick)

		# SCAN PAGE BUTTON CONNECTS
		widgets.btn_back_code.clicked.connect(self.buttonClick)
		widgets.btn_scan2.clicked.connect(self.buttonClick)
		
		# FI PLAN PAGE BUTTONS
		widgets.btn_random_fault.clicked.connect(self.buttonClick)
		widgets.btn_slct_fiplan.clicked.connect(get_file_json)
		widgets.btn_create_custom.clicked.connect(self.buttonClick)
		widgets.btn_select_fault.clicked.connect(faultSelectFromLibrary)
		widgets.btn_remove_fault.clicked.connect(self.buttonClick)
		widgets.btn_start_mutation.clicked.connect(self.buttonClick)
		widgets.btn_save_fiplan.clicked.connect(self.buttonClick)
		widgets.btn_remove_fiplan.clicked.connect(self.buttonClick)

		# EXECUTION PAGE BUTTONS
		widgets.btn_new_exe.clicked.connect(self.buttonClick)
		widgets.btn_remove_exe.clicked.connect(self.buttonClick)
		widgets.btn_select_metrics.clicked.connect(self.buttonClick)
		widgets.btn_start_exe.clicked.connect(self.buttonClick)

		# MONITORING PAGE BUTTONS
		widgets.btn_select_scenario.clicked.connect(get_file_rosbag)
		widgets.btn_run_scenario.clicked.connect(self.buttonClick)
		widgets.btn_create_report.clicked.connect(self.buttonClick)

		# SAVE WORKLOAD PAGE BUTTONS
		widgets.btn_workload_save.clicked.connect(self.buttonClick)
		widgets.btn_changeDir.clicked.connect(self.buttonClick)
		widgets.btn_back_start2.clicked.connect(self.buttonClick)
		
		# CREATE WORKLOAD PAGE BUTTONS
		widgets.btn_take_tasks.clicked.connect(self.buttonClick)
		widgets.btn_select_task.clicked.connect(self.buttonClick)
		widgets.btn_remove_task.clicked.connect(self.buttonClick)
		widgets.btn_save_task.clicked.connect(self.buttonClick)
		widgets.btn_back_start.clicked.connect(self.buttonClick)
		
		# CREATE CUSTOM SNIPPET PAGE BUTTONS
		widgets.btn_snip_location.clicked.connect(self.buttonClick)
		widgets.btn_save_snip.clicked.connect(self.buttonClick)
		widgets.back_snip.clicked.connect(self.buttonClick)

		#CREATE CUSTOM FAULT PAGE
		widgets.btn_back_fi.clicked.connect(self.buttonClick)
		widgets.btn_save_fault.clicked.connect(self.buttonClick)

		# METRICS PAGE BUTTONS
		widgets.saveMetrics.clicked.connect(self.buttonClick)
		widgets.btn_back_exe.clicked.connect(self.buttonClick)        

		# SHOW APP
		self.show()

		# SET CUSTOM THEME
		useCustomTheme = False

		# SET HOME PAGE AND SELECT MENU
		widgets.stackedWidget.setCurrentWidget(widgets.home)
		widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

		

	
	# BUTTONS CLICK FUNCTIONS

	def buttonClick(self):
		# GET BUTTON CLICKED
		btn = self.sender()
		btnName = btn.objectName()

		# HOME PAGE
		if btnName == "btn_home":
			widgets.stackedWidget.setCurrentWidget(widgets.home)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("HOME")	
		
		# START PAGE
		if btnName == "btn_start":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("START")

		# SCAN PAGE
		if btnName == "btn_scan":
			widgets.stackedWidget.setCurrentWidget(widgets.scan)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("SCAN")

		# CODE SNIPPETS PAGE
		if btnName == "btn_code":
			widgets.stackedWidget.setCurrentWidget(widgets.code)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("CODE SNIPPETS")

		# FIPLAN PAGE
		if btnName == "btn_fiplan":
			widgets.stackedWidget.setCurrentWidget(widgets.fiplan)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN")

		# EXECUTION PAGE
		if btnName == "btn_execution":
			widgets.stackedWidget.setCurrentWidget(widgets.execution)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("EXECUTION")

		# MONITORING PAGE
		if btnName == "btn_monitoring":
			widgets.stackedWidget.setCurrentWidget(widgets.monitoring)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("MONITORING")

		
		### PAGE CHANGE BUTTONS ###

		if btnName == "btn_go_start":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			UIFunctions.resetStyle(self,widgets.btn_home.styleSheet())
			widgets.btn_start.setStyleSheet(UIFunctions.selectMenu(widgets.btn_start.styleSheet()))
			widgets.titleRightInfo.setText("START")

		if btnName == "btn_go_scan":
			if widgets.checkBox_3.isChecked()==True:
				widgets.stackedWidget.setCurrentWidget(widgets.scan)
				UIFunctions.resetStyle(self,widgets.btn_start.styleSheet())
				widgets.btn_scan.setStyleSheet(UIFunctions.selectMenu(widgets.btn_scan.styleSheet()))
				widgets.titleRightInfo.setText("SCAN")
				widgets.textEdit_4.setPlainText(widgets.textEdit.toPlainText())
				widgets.textEdit_22.setPlainText(widgets.textEdit_3.toPlainText())

				if widgets.listWidget_8.count()!=0:
						csDatasList=[]
						for i in range(widgets.listWidget_8.count()):
							csDatas = widgets.listWidget_8.item(i).text()
							csDatasList.append(csDatas)

						widgets.listWidget_17.addItems(csDatasList)		
			
		if btnName == "btn_go_fiplan":
			widgets.stackedWidget.setCurrentWidget(widgets.fiplan)
			UIFunctions.resetStyle(self,widgets.btn_scan.styleSheet())
			widgets.btn_fiplan.setStyleSheet(UIFunctions.selectMenu(widgets.btn_fiplan.styleSheet()))
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN")

			for originalLine in self.placeForMutation:
				newLine = originalLine.lstrip()
				widgets.listWidget.addItem(newLine)
			
			lineNumber = widgets.listWidget.count()
			
			for number in range(0,lineNumber):
				if number%2==0:
					widgets.listWidget.item(number).setBackground(QtGui.QColor(128,128,128))

		if btnName == "btn_go_exe":
			widgets.stackedWidget.setCurrentWidget(widgets.execution)
			UIFunctions.resetStyle(self,widgets.btn_fiplan.styleSheet())
			widgets.btn_execution.setStyleSheet(UIFunctions.selectMenu(widgets.btn_execution.styleSheet()))
			widgets.titleRightInfo.setText("EXECUTION")

		if btnName == "btn_go_monitoring":
			widgets.stackedWidget.setCurrentWidget(widgets.monitoring)
			UIFunctions.resetStyle(self,widgets.btn_execution.styleSheet())
			widgets.btn_monitoring.setStyleSheet(UIFunctions.selectMenu(widgets.btn_monitoring.styleSheet()))
			widgets.titleRightInfo.setText("MONITORING")

		if btnName == "btn_new_one":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			UIFunctions.resetStyle(self,widgets.btn_monitoring.styleSheet())
			widgets.btn_start.setStyleSheet(UIFunctions.selectMenu(widgets.btn_start.styleSheet()))
			widgets.titleRightInfo.setText("START")

		### PAGES ###

		# START PAGE
		
		if btnName == "btn_create_workload":
			widgets.stackedWidget.setCurrentWidget(widgets.cWorkload)
			widgets.leftMenuBg.hide()
			widgets.toggleButton.show()
			widgets.titleRightInfo.setText("START - CREATE WORKLOAD")

		if btnName == "btn_save_workload":
			widgets.stackedWidget.setCurrentWidget(widgets.sWorkload)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("START - WORKLOAD SAVE")

		if btnName == "btn_add_custom":
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setNameFilter(("*.json"))

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				if file_name[0].endswith('.json'):
					with open(file_name[0], 'r') as f:
						data = f.read()
						widgets.textEdit_24.setPlainText(data)
						snippetsJsonList = json.loads(data)
						
						taskName = str(snippetsJsonList['Example_Python_Snippets']['Snippet_Name'])
						widgets.listWidget_8.addItem(taskName)
						widgets.listWidget_10.addItem(taskName)

						f.close()	

		if btnName == "btn_clear_codes":
			widgets.textEdit.clear()

		if btnName == "btn_clear_workload":
			widgets.textEdit_3.clear()

		# SAVE WORKLOAD PAGE FROM START PAGE
		
		if btnName == "btn_workload_save":
			workloadText=widgets.textEdit_12.toPlainText()
			workloadName=widgets.textEdit_8.toPlainText()
			pathName=widgets.textEdit_21.toPlainText()

			completeName = os.path.join(pathName, workloadName+".json")
			
			jsonFile = open(completeName, "w")
			jsonFile.write(workloadText)
			jsonFile.close()

		if btnName == "btn_changeDir":
			dialog = QFileDialog()
			pathName=response = QFileDialog.getExistingDirectory()
			widgets.textEdit_21.setPlainText(pathName)

		if btnName == "btn_back_start2":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("START")

		# CREATE WORKLOAD PAGE FROM START PAGE

		if btnName == "btn_take_tasks":
			try:
				dataSize = widgets.listWidget_21.count()
				jsonTypeTasks=widgets.plainTextEdit.toPlainText()
				loadTasks=json.loads(jsonTypeTasks)

				if dataSize == 0:

					for i in range(0,len(loadTasks['gorevler'])):
						workloadTask=str(loadTasks['gorevler'][i]['Task']['Task_ID'])
						workloadTask=workloadTask.split("\n")
						widgets.listWidget_21.addItems(workloadTask)
				else:
					widgets.listWidget_21.clear()

					for i in range(0,len(loadTasks['gorevler'])):
						workloadTask=str(loadTasks['gorevler'][i]['Task']['Task_ID'])
						workloadTask=workloadTask.split("\n")
						widgets.listWidget_21.addItems(workloadTask)
			except:
				print("Please, Edit Workload")
		
		if btnName == "btn_select_task":
			selectedTaskFromList=widgets.listWidget_21.currentItem().text()
			selectedTaskFromList=selectedTaskFromList.split("\n")
			widgets.listWidget_22.addItems(selectedTaskFromList)

		if btnName == "btn_save_task":
			allSelectedSnippets=""

			dataSizeOfSelected = widgets.listWidget_22.count()

			jsonTypeTasks=widgets.plainTextEdit.toPlainText()
			tasksJsonList = json.loads(jsonTypeTasks)

			if dataSizeOfSelected !=0:
				dialog = QFileDialog()
				pathName = QFileDialog.getExistingDirectory()

				taskName=widgets.textEdit_5.toPlainText()

				taskPathAndName = os.path.join(pathName, taskName+".json")				

				for i in range(0,len(tasksJsonList['gorevler'])):
					taskName = str(tasksJsonList['gorevler'][i]['Task']['Task_ID'])
					for j in range(0,widgets.listWidget_22.count()):
						listItem = widgets.listWidget_22.item(j).text()
						if taskName == listItem:
							taskDetails = str(tasksJsonList['gorevler'][i]['Task'])
							for i in taskDetails:
								allSelectedSnippets+=i

				
				jsonFile = open(taskPathAndName, "w")
				jsonFile.write(allSelectedSnippets)
				jsonFile.close()

				widgets.label_4.setText("SAVED!")

			else:
				pass
		
		if btnName == "btn_remove_task":
			row = widgets.listWidget_22.currentRow()
			widgets.listWidget_22.takeItem(row)

		if btnName == "btn_back_start":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("START")
		
		#  CODE SNIPPETS FROM START PAGE

		if btnName == "btn_create_code":
			widgets.stackedWidget.setCurrentWidget(widgets.cSnippets)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("CODE SNIPPETS - CREATE CUSTOM SNIPPETS")

		if btnName == "btn_remove_snip":
			row = widgets.listWidget_8.currentRow()
			widgets.listWidget_8.takeItem(row)
		
		# CREATE CUSTOM SNIPPETS FROM START PAGE
				
		if btnName == "btn_save_snip":
			if widgets.textEdit_25.toPlainText() == "":
				widgets.label_60.setText("Select Location To Save!")
			elif widgets.textEdit_16.toPlainText() == "":
				widgets.label_60.setText("Give a Snippet Name!")
			else:
				createdCodeCodeSnippet=widgets.textEdit_15.toPlainText()
				codeSnippetName=widgets.textEdit_16.toPlainText()
				codeSnippetLocation=widgets.textEdit_25.toPlainText()

				codeSnippetPathAndName = os.path.join(codeSnippetLocation, codeSnippetName+".json")
				
				jsonFile = open(codeSnippetPathAndName, "w")
				jsonFile.write(createdCodeCodeSnippet)
				jsonFile.close()
				label_60.setText("SAVED!")

		if btnName == "btn_snip_location":
			dialog = QFileDialog()
			pathName=response = QFileDialog.getExistingDirectory()
			widgets.textEdit_25.setPlainText(pathName)

		if btnName == "back_snip":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("START")
		
		#  SCAN PAGE

		if btnName == "btn_back_code":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			UIFunctions.resetStyle(self,widgets.btn_scan.styleSheet())
			widgets.btn_start.setStyleSheet(UIFunctions.selectMenu(widgets.btn_start.styleSheet()))
		
		patterns = list()
		csDatasList = list()
		paintedLines = list()
		jsonFonksiyonlari = list()
		codeSnippetsRegexCodes = list()
		csDataSequence = list()

		if btnName == "btn_scan2":
			if widgets.checkBox_2.isChecked()==True:
				isEmptyCodes=len(widgets.textEdit_4.toPlainText())
				isEmptyWorkloads=len(widgets.textEdit_22.toPlainText())
				if isEmptyCodes!=0:
					pureText=widgets.textEdit_4.toPlainText()
					tree=ast.dump(ast.parse(pureText))
					widgets.textEdit_23.setPlainText(tree)
					
					for i in range(100):
						time.sleep(0.01)
						widgets.progressBar_2.setValue(i+1) 

					splitText=pureText.split('\n')
					widgets.listWidget_2.addItems(splitText)
					if isEmptyWorkloads!=0:
						workloadText=widgets.textEdit_22.toPlainText()
						workloadData=json.loads(workloadText)
				
						try: 
							for i in range(0,len(workloadData['gorevler'])):
								fonksiyon_adi=workloadData['gorevler'][i]['Task']['Task_ID']
								fonksiyon_ara="def "+fonksiyon_adi
								jsonFonksiyonlari.append(fonksiyon_ara)
						
						except:
							print("Workload Build Error!")

						for number,line in enumerate(splitText):
							for j in jsonFonksiyonlari:
								if j in line:
									while number!=0:
											leading_spaces = len(splitText[number]) - len(splitText[number].lstrip())
											if leading_spaces!=0:
												widgets.listWidget_2.item(number).setBackground(QtGui.QColor(102,0,102))
												paintedLines.append(number)
												number+=1
											else:
												break

						if widgets.listWidget_8.count()!=0:
							
							for i in range(widgets.listWidget_8.count()):
								csDatas = widgets.listWidget_17.item(i).text()
								csDatasList.append(csDatas)

								
							with open('code_snippets.json') as codeSnippetsFromJson:
								codeSnippetRegexCode = json.load(codeSnippetsFromJson)

							for i in range(30):
								addedSnippetName=codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Snippet_Name"]
								for snippet in csDatasList:
									if snippet== addedSnippetName:
										addedSnippetRegex = codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Regex_Code"]
										patterns.append(addedSnippetRegex)

							for i in paintedLines:
								listOfCodes=widgets.listWidget_2.item(i).text()
								for pattern in patterns:
									result = re.findall(pattern,listOfCodes,re.MULTILINE)
									if result!=[]:
										widgets.listWidget_2.item(i).setBackground(QtGui.QColor(0,128,255))
										paintedLineForMutation = widgets.listWidget_2.item(i).text()
										self.placeForMutation.append(paintedLineForMutation)                   					

						else:
							pass
					
					else:
						with open('code_snippets.json') as codeSnippetsFromJson:
							codeSnippetRegexCode = json.load(codeSnippetsFromJson)

						for i in range(widgets.listWidget_8.count()):
								csDatas = widgets.listWidget_17.item(i).text()
								csDatasList.append(csDatas)

						for i in range(12):
							addedSnippetName=codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Snippet_Name"]
							for snippet in csDatasList:
								if snippet== addedSnippetName:
									addedSnippetRegex = codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Regex_Code"]
									patterns.append(addedSnippetRegex)
						else:
							with open('code_snippets.json') as codeSnippetsFromJson:
								codeSnippetRegexCode = json.load(codeSnippetsFromJson)
							for i in range(12):
								gerekli=codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Regex_Code"]
								patterns.append(gerekli)
							

						for i in range(widgets.listWidget_2.count()):
							listOfCodes=widgets.listWidget_2.item(i).text()
							for pattern in patterns:
								result = re.findall(pattern,listOfCodes,re.MULTILINE)
								itemsCount = len(re.findall(pattern,pureText,re.MULTILINE))
								if result!=[]:
									widgets.listWidget_2.item(i).setBackground(QtGui.QColor(102,0,102))
   
		# FAULT PLAN PAGE

		if btnName == "btn_random_fault":
			print("Random Fault Injection Under Development")

		if btnName == "btn_create_custom":
			widgets.stackedWidget.setCurrentWidget(widgets.customFault)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN - CREATE CUSTOM FAULT")

		if btnName == "btn_remove_fault":
			row = widgets.listWidget_7.currentRow()
			widgets.listWidget_7.takeItem(row)
			row = row - 1
			widgets.listWidget_7.takeItem(row)

		if btnName == "btn_start_mutation":
			lineForFaultInjection = widgets.textEdit_13.toPlainText()

			for i in range(100):
				time.sleep(0.01)
				widgets.progressBar.setValue(i+10)

			comparisonOperators = ["==","!=",">","<",">=","<="]
			temp = 0
			finalResult = ""
			
			for comparison in comparisonOperators:
				result = re.findall(comparison,lineForFaultInjection)
				if result != []:
					for i in result:
						if len(i) > temp:
							temp = len(i)
							finalResult = i
							
			comparisonOperators.remove(finalResult)

			for i in comparisonOperators:
				mutatedVersions = lineForFaultInjection.replace(finalResult,i)
				listForMutatedVersions = mutatedVersions.split("\n")
				widgets.listWidget_4.addItems(listForMutatedVersions)

		if btnName == "btn_save_fiplan":
			allMutations=""

			dataSizeOfSelected = widgets.listWidget_4.count()

			jsonTypeTasks=widgets.plainTextEdit.toPlainText()
			tasksJsonList = json.loads(jsonTypeTasks)

			if dataSizeOfSelected !=0:
				dialog = QFileDialog()
				pathName = QFileDialog.getExistingDirectory()

				taskName=widgets.textEdit_26.toPlainText()

				taskPathAndName = os.path.join(pathName, taskName+".json")
				
				for j in range(widgets.listWidget_4.count()):
					allMutations+=widgets.listWidget_4.item(j).text()
				
				jsonFile = open(taskPathAndName, "w")
				jsonFile.write(allMutations)
				jsonFile.close()

				text = widgets.textEdit_26.toPlainText()
				splitText = text.split("\n")
				widgets.listWidget_11.addItems(splitText)

				widgets.label_58.setText("SAVED!")

			else:
				pass

		if btnName == "btn_remove_fiplan":
			row = widgets.listWidget_11.currentRow()
			widgets.listWidget_11.takeItem(row)

		# CREATE CUSTOM FAULT FROM FI PLAN

		if btnName == "btn_back_fi":
			widgets.stackedWidget.setCurrentWidget(widgets.fiplan)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN")
		
		if btnName == "btn_save_fault":
			if widgets.textEdit_11.toPlainText() != "":
				dialog = QFileDialog()
				pathName = QFileDialog.getExistingDirectory()

				faultName=widgets.textEdit_10.toPlainText()

				taskPathAndName = os.path.join(pathName, faultName+".json")

				allFaults = widgets.textEdit_11.toPlainText()
								
				jsonFile = open(taskPathAndName, "w")
				jsonFile.write(allFaults)
				jsonFile.close()

				widgets.label_61.setText("SAVED!")

			else:
				widgets.label_61.setText("FAULT DOES NOT EXIST!")

		# EXECUTION PAGE
		
		if btnName == "btn_new_exe":
			print("New execution process!!!")
		
		if btnName == "btn_remove_exe":
			print("Remove execution!!!")
		
		if btnName == "btn_select_metrics":
			print("Select Execution Metrics")
			widgets.stackedWidget.setCurrentWidget(widgets.selectMetrics)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("EXECUTION - METRICS")

		if btnName == "btn_start_exe":
			print("Execution Process Started")

		# SELECT METRICS FROM EXECUTION PAGE

		if btnName == "saveMetrics":
			print("Metrics Saved!!!")

		if btnName == "btn_back_exe":
			widgets.stackedWidget.setCurrentWidget(widgets.execution)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("EXECUTION")
		
		# MONITORING PAGE
		
		if btnName == "btn_select_scenario":
			print("Scenario Selected")
		
		if btnName == "btn_run_scenario":
			print("Run The Scenario")

		if btnName == "btn_create_report":
			print("Report Created")

	# RESIZE EVENTS

	def resizeEvent(self, event):
		# UPDATE SIZE GRIPS
		UIFunctions.resize_grips(self)

	
	# MOUSE CLICK EVENTS

	def mousePressEvent(self, event):
		# SET DRAG POS WINDOW
		self.dragPos = event.globalPos()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	window = MainWindow()
	window.show()

	sys.exit(app.exec_())