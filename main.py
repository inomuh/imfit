#!/usr/bin/env python3

import sys
import time
import ast
import astpretty
import json
import os
import re
import subprocess
import coverage
import rospy
import yaml
import xml.etree.ElementTree as ET
import random
import astunparse
import inspect
import string

from PySide6 import *
from modules import *
from widgets import *

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import QDir
from ui_main import Ui_MainWindow

from fpdf import FPDF

class MainWindow(QMainWindow):
	widgets = None

	global zippedList
	zippedList = list()

	global zipped_list_yaml
	zipped_list_yaml = list()

	global sourceAndMutatedCode
	sourceAndMutatedCode = list()

	global sourceCode
	sourceCode = ""

	global mutatedCode
	mutatedCode = ""

	global lineNumberAndLineInfo
	lineNumberAndLineInfo = list()

	global killedMutants
	killedMutants = 0

	global survivorMutants
	survivorMutants = 0

	global equivalentMutants
	equivalentMutants = 0

	global listOfKilledMutants
	listOfKilledMutants = list()

	global listOfSurvivorMutants
	listOfSurvivorMutants = list()

	global listOfEquivalentMutants
	listOfEquivalentMutants = list()

	global errorCodeList	
	errorCodeList = list()

	global originalSourceCodeOutput
	originalSourceCodeOutput = ""

	global faultNameList
	faultNameList = list()

	global timeoutList
	timeoutList = list()

	global file_type
	file_type = ""

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
		self.lineNumberForMutation = list()


		### FUNCTIONS
		
		# TAKE FILE FUNCTIONS
				
		# General files function
		def get_file(self):
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				with open(file_name[0], 'r') as f:
						data = f.read()
						widgets.textEdit.setPlainText(data)
						f.close()
		
		def check_empty():
			length_file_content = widgets.listWidget_24.count()
			lentgh_mutation_library = widgets.listWidget_20.count()

			if length_file_content > 0 or lentgh_mutation_library > 0:
				widgets.listWidget_24.clear() # File Content
				widgets.listWidget_20.clear() # Mutation Library
				widgets.listWidget_23.clear() # Selected Line  & Fault
				widgets.listWidget_25.clear() # Mutation Applied Content
				widgets.textEdit_41.clear() # Selected Line

		def take_yaml_file(data):
			global file_type
			file_type = "yaml"
			split_data = data.split("\n")
			widgets.listWidget_24.addItems(split_data)
			with open('yaml_fault_library.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)
				for i in range(0,4):
					targetLineFromJson = faultList["all_faults"][i]["fault"]["Fault_Name"]
					adding_fault = targetLineFromJson.split("\n")
					widgets.listWidget_20.addItems(adding_fault)
					

		def take_launch_file(data):
			global file_type
			file_type = "launch"
			split_data = data.split("\n")
			widgets.listWidget_24.addItems(split_data)				
			with open('yaml_fault_library.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)
				for i in range(4,7):
					targetLineFromJson = faultList["all_faults"][i]["fault"]["Fault_Name"]
					adding_fault = targetLineFromJson.split("\n")
					widgets.listWidget_20.addItems(adding_fault)
		
		def take_srv_msg_file(data):
			global file_type
			split_data = data.split("\n")
			widgets.listWidget_24.addItems(split_data)
			file_type = "srv"
			with open('yaml_fault_library.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)
				for i in range(7,12):
					targetLineFromJson = faultList["all_faults"][i]["fault"]["Fault_Name"]
					adding_fault = targetLineFromJson.split("\n")
					widgets.listWidget_20.addItems(adding_fault)
					
		def check_file_type(file_name, data):
			if file_name.endswith('.yaml') or file_name.endswith('.yml'):
				take_yaml_file(data)
			elif file_name.endswith('.launch'):
				take_launch_file(data)
			elif file_name.endswith('.srv')  or file_name.endswith('.msg'):
				take_srv_msg_file(data)
			else:
				pass
			

		def get_yaml_file(self):	
			dialog = QFileDialog()
			dialog.setFileMode(QFileDialog.AnyFile)

			if dialog.exec_():
				file_name = dialog.selectedFiles()

				with open(file_name[0], 'r') as f:
						file_name = file_name[0]
						check_empty()
						data = f.read()
						check_file_type(file_name,data)
						f.close()

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

					for i in range(20):
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

		def selectPossibleMutationLine(self):
			""" Select Line For Mutation on FI Plan Page """
			possibleMutationLine = widgets.listWidget.currentItem().text()
			widgets.textEdit_13.setPlainText(possibleMutationLine)
		
		def selectPossibleMutationLineYAML(self):
			""" Select Line For Mutation on FI Plan Page """
			possibleMutationLine = widgets.listWidget_24.currentItem().text()
			widgets.textEdit_41.setPlainText(possibleMutationLine)

		def fault_select_from_yaml_lib (self):
			""" # Select Fault From Fault Library on YAML - LAUNCH Page """

			global zipped_list_yaml # yaml zipped list eklenecek
			
			if len(widgets.textEdit_41.toPlainText()) != 0:				

				selectedLine = widgets.textEdit_41.toPlainText()
				selectedFault = widgets.listWidget_20.currentItem().text()

				textSelectedLine = "Line: " + selectedLine
				textSelectedFault = "\tFault: " + selectedFault

				zipped_list_yaml.append(selectedLine)
				zipped_list_yaml.append(selectedFault)

				selectedLineAndFault = textSelectedLine+textSelectedFault

				lineAndFault = selectedLineAndFault.split("\n")

				widgets.listWidget_23.addItems(lineAndFault)

			else:
				pass

		
		def faultSelectFromLibrary (self):
			""" Select Fault From Fault Library on FI Plan Page """
			global zippedList

			if len(widgets.textEdit_13.toPlainText()) != 0:

				selectedLine = widgets.textEdit_13.toPlainText()
				selectedFault = widgets.listWidget_3.currentItem().text()

				textSelectedLine = "Line: " + selectedLine
				textSelectedFault = "\tFault: " + selectedFault

				zippedList.append(selectedLine)
				zippedList.append(selectedFault)

				selectedLineAndFault = textSelectedLine+textSelectedFault

				lineAndFault = selectedLineAndFault.split("\n")

				widgets.listWidget_7.addItems(lineAndFault)

			else:
				pass

		# This Function Shows Fault's Information from Fault Library on FI Plan Page
		def selectWithOneClickedForFIPlan (self):
			try:
				clickedItemText=widgets.listWidget_3.currentItem().text()

				with open('faultLibrary.json') as faultsFromJson:
					faultList = json.load(faultsFromJson)
				
				lenOfFaultList = widgets.listWidget_3.count()

				for i in range(lenOfFaultList):
					faultName = faultList["all_faults"][i]["fault"]["Fault_Name"]

					if clickedItemText == faultName:
						faultDescription = faultList["all_faults"][i]["fault"]["Explanation"]
						widgets.textEdit_17.setPlainText(faultDescription)
			except:
				IndexError()

		def mutationForFIPlan (self):
			widgets.btn_start_mutation.setEnabled(False)

			global zippedList
			global sourceCode
			global mutatedCode
			global sourceAndMutatedCode
			global faultNameList

			for i in range(100):
				time.sleep(0.01)
				widgets.progressBar.setValue(i+10)

			with open('faultLibrary.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)

			operators = list()
			opss = list()

			zippedListLength = len(zippedList)

			sizeOfFaultAndLineList = widgets.listWidget_7.count()

			lengthFaultList = len(faultList["all_faults"]) - 1

			lengthPossibleMutationLines = widgets.listWidget.count()

			lengthFaultLibrary = widgets.listWidget_3.count()		

			if widgets.checkBox_4.isChecked() == True:				
				
				for j in range(0,lengthPossibleMutationLines):
						lineWithInfo = widgets.listWidget.item(j).text()
											
						find_rospy = re.findall("rospy", lineWithInfo)

						if find_rospy != []:
							try:
								def mutate_function(code):
									""" Goes to the node to apply the mutation. """
									node = ast.parse(code)
									renamer = GeneralROSMutator()
									node2 = renamer.visit(node)
									codes_print(code,node2)

								def change_code(code):
									""" Adding random value to the source code line to be a mutant """
									list1 = list(code)
									random_number = random_value_generate()
									string_random_number = str(random_number)
									list1[-1] = string_random_number+")"
									str1 = ''.join(list1)
									# print(str1)
									mutated_rospy = str1.split("\n")
									widgets.listWidget_4.addItems(mutated_rospy)

								def random_value_generate():
									""" Creating the random value """
									random_number = random.randint(1, 20)
									return random_number

								def codes_print(code,node2):
									""" The function shows prime and mutated code after the process. """
									# print("\n######### Original Code ##########\n")
									# print(code)
									# print("\n######### Mutated Code ##########\n")
									unparsed_code = astunparse.unparse(node2)
									strip_code = code.strip()
									strip_unparsed_code = unparsed_code.strip()

									if strip_code == strip_unparsed_code:
										change_code(code)
									else:
									# print(unparsed_code)
										listForMutatedVersions = unparsed_code.split("\n")
										# print(listForMutatedVersions)
										for i in listForMutatedVersions:
											if i != "":
												mutated_rospy = i.split("\n")
												widgets.listWidget_4.addItems(mutated_rospy)


								class GeneralROSMutator(ast.NodeTransformer):
									""" This class mutates for Initializing ROS Node """
									def __init__(self):
										self._arg_count = 0

									def visit_Constant(self,node):
										""" The visitor function. """
										if isinstance(node.value,str):
											node.value="MUTANT"
											self.generic_visit(node)
											return node

										if isinstance(node.value, bool):
											if node.value is True:
												node.value = False
												self.generic_visit(node)
												return node
											node.value = True
											self.generic_visit(node)
											return node
										node.value = random.randint(1, 20)
										self.generic_visit(node)
										return node

									def visit_FunctionDef(self, node):
										""" The visitor function. """
										node.name= "MUTANT"
										self.generic_visit(node)
										return node

									def visit_arg(self, node):
										""" The visitor function. """
										node.arg = "arg_{}".format(self._arg_count)
										self._arg_count += 1
										self.generic_visit(node)
										return node

									def visit_Return(self, node):
										""" The visitor function. """
										node.value = None
										self.generic_visit(node)
										return node

								mutate_function(lineWithInfo)
							except:
								pass

							

						else:
							for faultNumber in range(0 , lengthFaultList):									
									operatorsFromLibrary = faultList["all_faults"][faultNumber]["fault"]["Target_to_Change"]
									opssFromLibrary = faultList["all_faults"][faultNumber]["fault"]["Changed"]

									operators = operatorsFromLibrary.split(",")
									opss = opssFromLibrary.split(",")

									text = lineWithInfo
												
									findOperator = re.findall("\W", text)

									try:

										if findOperator != []:
											temp = 0
											uzunluk = 0
											target = ""
											kelime = ""

											for i in findOperator:
												if i == " ":
													findOperator.remove(i)

											targetWord = ""

											for i in range(0,len(findOperator)):
												targetWord = targetWord+(findOperator[i])

											for i in operators:
												result = re.findall(i,text)
												if len(result) != 2:
													for i in result:
														uzunluk = len(i)
														if uzunluk > temp:
															temp = uzunluk
															target = result
											
											if target[0] == targetWord:
												if uzunluk == 3:
													for j in opss:
														if target[0] != j:
															if target[0] == "**=":
																kelime = ""
																kelime = "\\" + target[0]
																mutatedVersions = re.sub(kelime,j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)
															else:
																mutatedVersions = re.sub(target[0],j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)

												elif uzunluk == 2:
													for j in opss:
														if target[0] != j:
															if target[0] == "+="or"*="or"^="or"**":
																kelime = ""
																kelime = "[\\" + target[0] + "]{2}"
																mutatedVersions = re.sub(kelime,j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)
															else:
																mutatedVersions = re.sub(target[0],j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)

												else :
													for j in opss:
														if target[0] != j:
															if target[0] == "+"or"-"or"*"or"/":
																kelime = ""
																kelime = "\\" + target[0]
																mutatedVersions = re.sub(kelime,j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)

															else:
																mutatedVersions = re.sub(target[0],j,text)
																listForMutatedVersions = mutatedVersions.split("\n")
																widgets.listWidget_4.addItems(listForMutatedVersions)
																faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																faultNameList.append(faultNameForMonitoring)
																sourceCode = lineWithInfo
																mutatedCode = mutatedVersions

																sourceAndMutatedCode.append(sourceCode)
																sourceAndMutatedCode.append(mutatedCode)

											elif target[0] == "or"or" and "or" not ":
													for j in opss:
														if target[0] != j:
															mutatedVersions = re.sub(target[0],j,text)
															listForMutatedVersions = mutatedVersions.split("\n")
															widgets.listWidget_4.addItems(listForMutatedVersions)
															faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
															faultNameList.append(faultNameForMonitoring)
															sourceCode = lineWithInfo
															mutatedCode = mutatedVersions

															sourceAndMutatedCode.append(sourceCode)
															sourceAndMutatedCode.append(mutatedCode)

											elif target[0] == " is "or" is not ":
													for j in opss:
														if target[0] != j:
															mutatedVersions = re.sub(target[0],j,text)
															listForMutatedVersions = mutatedVersions.split("\n")
															widgets.listWidget_4.addItems(listForMutatedVersions)
															faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
															faultNameList.append(faultNameForMonitoring)
															sourceCode = lineWithInfo
															mutatedCode = mutatedVersions

															sourceAndMutatedCode.append(sourceCode)
															sourceAndMutatedCode.append(mutatedCode)

											elif target[0] == " in "or" not in ":
													for j in opss:
														if target[0] != j:
															mutatedVersions = re.sub(target[0],j,text)
															listForMutatedVersions = mutatedVersions.split("\n")
															widgets.listWidget_4.addItems(listForMutatedVersions)
															faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
															faultNameList.append(faultNameForMonitoring)
															sourceCode = lineWithInfo
															mutatedCode = mutatedVersions

															sourceAndMutatedCode.append(sourceCode)
															sourceAndMutatedCode.append(mutatedCode)

											elif target[0] == "&"or"|"or"^"or"~"or"<<"or">>":
													for j in opss:
														if target[0] != j:
															mutatedVersions = re.sub(target[0],j,text)
															listForMutatedVersions = mutatedVersions.split("\n")
															widgets.listWidget_4.addItems(listForMutatedVersions)
															faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
															faultNameList.append(faultNameForMonitoring)
															sourceCode = lineWithInfo
															mutatedCode = mutatedVersions

															sourceAndMutatedCode.append(sourceCode)
															sourceAndMutatedCode.append(mutatedCode)

											else:
												pass

										else:
												for j in opss:
													mutatedVersions = re.sub(operators,j,text)
													listForMutatedVersions = mutatedVersions.split("\n")
													widgets.listWidget_4.addItems(listForMutatedVersions)
													faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
													faultNameList.append(faultNameForMonitoring)
													sourceCode = lineWithInfo
													mutatedCode = mutatedVersions

													sourceAndMutatedCode.append(sourceCode)
													sourceAndMutatedCode.append(mutatedCode)
										
									except:
										pass

			else:

				if sizeOfFaultAndLineList != 0:
					try:
						for j in range(0,zippedListLength):
							if j % 2 == 0:
								lineWithInfo = zippedList[j]
							else:
								faultWithInfo = zippedList[j]
								find_rospy = re.findall("rospy", lineWithInfo)
								if find_rospy != []:
									def mutate_function(code):
										""" Goes to the node to apply the mutation. """
										node = ast.parse(code)
										renamer = GeneralROSMutator()
										node2 = renamer.visit(node)
										codes_print(code,node2)

									def change_code(code):
										""" Adding random value to the source code line to be a mutant """
										list1 = list(code)
										random_number = random_value_generate()
										string_random_number = str(random_number)
										list1[-1] = string_random_number+")"
										str1 = ''.join(list1)
										# print(str1)
										mutated_rospy = str1.split("\n")
										widgets.listWidget_4.addItems(mutated_rospy)

									def random_value_generate():
										""" Creating the random value """
										random_number = random.randint(1, 20)
										return random_number

									def codes_print(code,node2):
										""" The function shows prime and mutated code after the process. """
										# print("\n######### Original Code ##########\n")
										# print(code)
										# print("\n######### Mutated Code ##########\n")
										unparsed_code = astunparse.unparse(node2)
										strip_code = code.strip()
										strip_unparsed_code = unparsed_code.strip()

										if strip_code == strip_unparsed_code:
											change_code(code)
										else:
										# print(unparsed_code)
											listForMutatedVersions = unparsed_code.split("\n")
											# print(listForMutatedVersions)
											for i in listForMutatedVersions:
												if i != "":
													mutated_rospy = i.split("\n")
													widgets.listWidget_4.addItems(mutated_rospy)


									class GeneralROSMutator(ast.NodeTransformer):
										""" This class mutates for Initializing ROS Node """
										def __init__(self):
											self._arg_count = 0

										def visit_Constant(self,node):
											""" The visitor function. """
											if isinstance(node.value,str):
												node.value="MUTANT"
												self.generic_visit(node)
												return node

											if isinstance(node.value, bool):
												if node.value is True:
													node.value = False
													self.generic_visit(node)
													return node
												node.value = True
												self.generic_visit(node)
												return node
											node.value = random.randint(1, 20)
											self.generic_visit(node)
											return node

										def visit_FunctionDef(self, node):
											""" The visitor function. """
											node.name= "mutated_function"
											self.generic_visit(node)
											return node

										def visit_arg(self, node):
											""" The visitor function. """
											node.arg = "arg_{}".format(self._arg_count)
											self._arg_count += 1
											self.generic_visit(node)
											return node

										def visit_Return(self, node):
											""" The visitor function. """
											node.value = None
											self.generic_visit(node)
											return node

									mutate_function(lineWithInfo)
								else:
									for faultNumber in range(0 , lengthFaultList):
											faultName = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
											if faultName == faultWithInfo:
												operatorsFromLibrary = faultList["all_faults"][faultNumber]["fault"]["Target_to_Change"]
												opssFromLibrary = faultList["all_faults"][faultNumber]["fault"]["Changed"]

												operators = operatorsFromLibrary.split(",")
												opss = opssFromLibrary.split(",")


												text = lineWithInfo

														
												findOperator = re.findall("\W", text)

												if findOperator != []:
													temp = 0
													uzunluk = 0
													target = ""
													kelime = ""

													for i in findOperator:
														if i == " ":
															findOperator.remove(i)

													targetWord = ""

													for i in range(0,len(findOperator)):
														targetWord = targetWord+(findOperator[i])

													for i in operators:
														result = re.findall(i,text)
														if len(result) != 2:
															for i in result:
																uzunluk = len(i)
																if uzunluk > temp:
																	temp = uzunluk
																	target = result


													if target[0] == targetWord:
														if uzunluk == 3:
															for j in opss:
																if target[0] != j:
																	if target[0] == "**=":
																		kelime = ""
																		kelime = "\\" + target[0]
																		mutatedVersions = re.sub(kelime,j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)
																	else:
																		mutatedVersions = re.sub(target[0],j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)

														elif uzunluk == 2:
															for j in opss:
																if target[0] != j:
																	if target[0] == "+="or"*="or"^="or"**":
																		kelime = ""
																		kelime = "[\\" + target[0] + "]{2}"
																		mutatedVersions = re.sub(kelime,j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)
																	else:
																		mutatedVersions = re.sub(target[0],j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)
														else :
															for j in opss:
																if target[0] != j:
																	if target[0] == "+"or"-"or"*"or"/":
																		kelime = ""
																		kelime = "\\" + target[0]
																		mutatedVersions = re.sub(kelime,j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)
																	else:
																		mutatedVersions = re.sub(target[0],j,text)
																		listForMutatedVersions = mutatedVersions.split("\n")
																		widgets.listWidget_4.addItems(listForMutatedVersions)
																		faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																		faultNameList.append(faultNameForMonitoring)

													elif target[0] == "or"or" and "or" not ":
															for j in opss:
																if target[0] != j:
																	mutatedVersions = re.sub(target[0],j,text)
																	listForMutatedVersions = mutatedVersions.split("\n")
																	widgets.listWidget_4.addItems(listForMutatedVersions)
																	faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																	faultNameList.append(faultNameForMonitoring)

													elif target[0] == " is "or" is not ":
															for j in opss:
																if target[0] != j:
																	mutatedVersions = re.sub(target[0],j,text)
																	listForMutatedVersions = mutatedVersions.split("\n")
																	widgets.listWidget_4.addItems(listForMutatedVersions)
																	faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																	faultNameList.append(faultNameForMonitoring)

													elif target[0] == " in "or" not in ":
															for j in opss:
																if target[0] != j:
																	mutatedVersions = re.sub(target[0],j,text)
																	listForMutatedVersions = mutatedVersions.split("\n")
																	widgets.listWidget_4.addItems(listForMutatedVersions)
																	faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																	faultNameList.append(faultNameForMonitoring)

													elif target[0] == "&"or"|"or"^"or"~"or"<<"or">>":
															for j in opss:
																if target[0] != j:
																	mutatedVersions = re.sub(target[0],j,text)
																	listForMutatedVersions = mutatedVersions.split("\n")
																	widgets.listWidget_4.addItems(listForMutatedVersions)
																	faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
																	faultNameList.append(faultNameForMonitoring)

													else:
														pass

												else:
														for j in opss:
															mutatedVersions = re.sub(operators,j,text)
															listForMutatedVersions = mutatedVersions.split("\n")
															widgets.listWidget_4.addItems(listForMutatedVersions)
															faultNameForMonitoring = faultList["all_faults"][faultNumber]["fault"]['Fault_Name']
															faultNameList.append(faultNameForMonitoring)
					except:
						pass
			
			# # Mutasyon işlemi sonucunda oluşturulan mutantların sayısını 
			# # listenin içindeki elemanların sayısını alarak gösterir.
			# totalMutantsNumber = widgets.listWidget_4.count()
			# widgets.label_76.setText("Number of Total Mutants: " + str(totalMutantsNumber))


		def executionModule(self):
			global killedMutants
			global survivorMutants
			global equivalentMutants
			global faultNameList
			global timeoutList
			global sourceAndMutatedCode

			start_time = time.time()

			timeoutCounter = 0

			sourceCodeData = widgets.textEdit.toPlainText()

			fname = "original_code.py"
			data = sourceCodeData
			with open(fname, 'w') as f:
				f.write(data)

			lengthMutatedLines = widgets.listWidget_4.count()
			timeLimitPerProcess = widgets.textEdit_18.toPlainText()

			subprocess.run("python3 original_code.py", shell=True)
			# cmd = ["python3", "original_code.py"]
			# try:
			# 	subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, timeout=int(timeLimitPerProcess))
			# except subprocess.TimeoutExpired:
			# 	pass

			print("############################################################################")
			print("########################         Original Code     #########################")
			print("############################################################################")

			with open('faultPlans.json') as faultsFromJson:
				faultList = json.load(faultsFromJson)


			print(lengthMutatedLines)

			for i in range(0,lengthMutatedLines):
				targetLineFromJson = faultList["fault_plans"][i]["Fault"]["Source_Code"]
				mutatedCodeFromJson = faultList["fault_plans"][i]["Fault"]["Mutate_Code"]

				mutationProcess = sourceCodeData.replace(targetLineFromJson, mutatedCodeFromJson)
				fname = "fault"+str(i)+".py"
				data = mutationProcess
				with open(fname, 'w') as f:
					f.write(data)

				print("\n\nFault Number: ",i)
				print("\n############################################################################")

				cmd = ["python3", "fault"+str(i)+".py"]
				try:
					res = subprocess.run(cmd, stdout=subprocess.PIPE, timeout=int(timeLimitPerProcess))
				except subprocess.TimeoutExpired:
					timeoutCounter += 1
					timeoutList.append("python3 fault"+str(i)+".py")
					killedMutants += 1
					listOfKilledMutants.append("python3 fault"+str(i)+".py")
					# errorCodeList.append(mutantCodeOutput)
					continue      
				else:

					mutantCodeExecution = "python3 fault"+str(i)+".py"

					statusOfOutput = subprocess.getstatusoutput(mutantCodeExecution) # Mutant kodları çalıştırıp çıktılarını alır.
					mutantCodeOutput = statusOfOutput[1]
					errorCodeList.append(mutantCodeOutput)


					coverageRun = "coverage run fault"+str(i)+".py" # Çalıştırılacak "fault"ların isimleri oluşturulur.
					coverageReport = "coverage report" 

					os.system(coverageRun) # Faultlar ayrı ayrı çalıştırılır
					os.system(coverageReport) # Çalıştırılan "fault"un coverage raporunu oluşturur.


					if statusOfOutput[0] != 0:
						print(mutantCodeOutput)
						print("############################################################################")
						print("######################       Killed Mutant            ######################")
						print("############################################################################")
						killedMutants += 1
						listOfKilledMutants.append(mutantCodeExecution)
						errorCodeList.append(mutantCodeOutput)
						
					else:

						if mutantCodeOutput == originalSourceCodeOutput:
							print(mutantCodeOutput)
							print("############################################################################")
							print("######################       Equivalent Mutant        ######################")
							print("############################################################################")
							equivalentMutants +=1
							listOfEquivalentMutants.append(mutantCodeExecution)

						else:
							print(mutantCodeOutput)
							print("############################################################################")
							print("######################       Survivor Mutant          ######################")
							print("############################################################################")
							survivorMutants +=1
							listOfSurvivorMutants.append(mutantCodeExecution)

			end_time = time.time()

			print("\n\n")
			print("############################################################################")
			print("#                                RESULTS                                   #")
			print("############################################################################")
			print("\n")

			print("Process Time: ",end_time-start_time)
			widgets.listWidget_9.addItem("Process Time:"+str(end_time-start_time))
			print("\n")

			mutationScore = (killedMutants / (killedMutants + survivorMutants)) * 100

			print("Mutation Score: %",mutationScore)
			widgets.listWidget_9.addItem("Mutation Score: %" + str(mutationScore))
			print("\n")
			print("Number of Total Mutants:", killedMutants + survivorMutants + equivalentMutants)
			widgets.listWidget_9.addItem("All Mutants: " + str(killedMutants + survivorMutants + equivalentMutants))
			print("\n")
			print("Killed Mutants: ",killedMutants)
			widgets.listWidget_9.addItem("Killed: " + str(killedMutants))
			print("Survivor Mutants: ",survivorMutants)
			widgets.listWidget_9.addItem("Survived: " + str(survivorMutants))
			print("Equivalent Mutants: ",equivalentMutants)
			widgets.listWidget_9.addItem("Equivalent: " + str(equivalentMutants))
			print("Timeout: ",timeoutCounter)
			widgets.listWidget_9.addItem("Timeout: " + str(timeoutCounter))

			print("\n")
			print("############################################################################")
			print("#                                DETAILS                                   #")
			print("############################################################################")
			print("\n")

			lengthOfKilledMutantsList = len(listOfKilledMutants)

			print("Killed Mutants List: ")
			widgets.listWidget_16.addItem("Killed Mutants List: ")
			for i in range(lengthOfKilledMutantsList):
				print(listOfKilledMutants[i])
				widgets.listWidget_16.addItem(str(listOfKilledMutants[i]))

			print("\n")

			print("Survivor Mutants List: ")
			widgets.listWidget_16.addItem("Survivor Mutants List: ")
			for i in listOfSurvivorMutants:
				print(i)
				widgets.listWidget_16.addItem(str(i))

			print("\n")

			print("Equivalent Mutants List: ")
			widgets.listWidget_16.addItem("Equivalent Mutants List: ")
			for i in listOfEquivalentMutants:
				print(i)
				widgets.listWidget_16.addItem(str(i))

			print("Timeout List: ")
			widgets.listWidget_16.addItem("Timeout Mutants List: ")
			for i in timeoutList:
				print(i)
				widgets.listWidget_16.addItem(str(i))

			print("\n")
			print("############################################################################")
			print("#                     Outputs of Killed Mutants                            #")
			print("############################################################################")

			for i in range(lengthOfKilledMutantsList):
				print("\n")
				print("############################################################################")
				print(listOfKilledMutants[i])
				widgets.listWidget_19.addItem(str(listOfKilledMutants[i]))
				print("----------------------------------------------------------------------------")
				errorOutput = errorCodeList[i]
				onlyError = errorOutput.split("\n")
				print(onlyError[-1])
				widgets.listWidget_19.addItem(str(onlyError[-1]))
				print("############################################################################")
			print("\n")

			if widgets.checkBox_7.isChecked() is True:
				for  i in range(0,lengthMutatedLines):
					path = "fault"+str(i)+".py"
					os.remove(path)
					
				os.remove("original_code.py")
				os.remove(".coverage")
			else:
				pass

			widgets.label_10.setText("Mutation Score: %" + str(mutationScore))

			lenfaultNameList = len(faultNameList)
			for i in range(0,lenfaultNameList):
				widgets.listWidget_14.addItem("fault" + str(i) + ".py --> " + str(faultNameList[i]))
				print(str(faultNameList[i]))

			# lenSourceAndMutatedCode = len(sourceAndMutatedCode)

			# for i in (0,lenSourceAndMutatedCode):
			# 	if i % 2 == 0:
			# 		continue
			# 	else:
			# 		sourceCode = sourceAndMutatedCode[i-1]
			# 		mutatedCode = sourceAndMutatedCode[i]
			# 		widgets.listWidget_14.addItem(sourceCode + " --> " + mutatedCode)

		def selectedMetricInformations():
			try:
				clickedItemText = widgets.listWidget_18.currentItem().text()
				selectedMetric = widgets.listWidget_18.currentItem().text()

				with open('metricList.json') as metricsFromJson:
					faultList = json.load(metricsFromJson)
				
				lenOfMetricList = widgets.listWidget_18.count()

				for i in range(0,lenOfMetricList):
					metricName = faultList["Metrics"][i]["Metric"]["Name"]

					if clickedItemText == metricName:
						metricInfo = faultList["Metrics"][i]["Metric"]["Info"]
						widgets.textEdit_9.setPlainText(metricInfo)
			except:
				IndexError()

		
		def selectMetricFromListDoubleClick():
			selectedMetric = widgets.listWidget_18.currentItem().text()
			widgets.listWidget_15.addItem(selectedMetric)

		# LIST'S (listWidget's) CLICK CONNECTS

		# Line Selection For Mutation on FI Plan Page
		widgets.listWidget.itemClicked.connect(selectPossibleMutationLine)

		# Line Selection For Mutation on YAML - LAUNCH FI Plan Page
		widgets.listWidget_24.itemClicked.connect(selectPossibleMutationLineYAML)

		# Line Selection and Show Information About Fault on FI Plan Page
		widgets.listWidget_3.itemDoubleClicked.connect(faultSelectFromLibrary)
		widgets.listWidget_3.itemClicked.connect(selectWithOneClickedForFIPlan)
				
		# Code Snippet Selection on Start Page
		widgets.listWidget_10.itemDoubleClicked.connect(codeSnippetSelect)
		widgets.listWidget_10.itemClicked.connect(selectWithOneClickedForCS)

		# Select Task and Show Task's Details on Workload Page
		widgets.listWidget_21.itemClicked.connect(taskInfoWithOneClick)
		widgets.listWidget_21.itemDoubleClicked.connect(taskSelect)

		# Select Metric
		widgets.listWidget_18.itemClicked.connect(selectedMetricInformations)
		widgets.listWidget_18.itemDoubleClicked.connect(selectMetricFromListDoubleClick)


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
		widgets.btn_go_start_2.clicked.connect(self.buttonClick)
		widgets.btn_go_scan.clicked.connect(self.buttonClick)
		widgets.btn_go_fiplan.clicked.connect(self.buttonClick)
		widgets.btn_go_exe.clicked.connect(self.buttonClick)
		widgets.btn_go_exe_2.clicked.connect(self.buttonClick)
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
		widgets.btn_prepare_plan.clicked.connect(self.buttonClick)

		# CODE SNIPPET BUTTON CONNECTS
		widgets.btn_create_code.clicked.connect(self.buttonClick)
		widgets.btn_select_snippet.clicked.connect(codeSnippetSelect)
		widgets.btn_remove_snip.clicked.connect(self.buttonClick)

		# ROS PAGE BUTTON CONNECTS  
		widgets.open_ros_btn.clicked.connect(self.buttonClick)
		widgets.rosrun_btn.clicked.connect(self.buttonClick)
		widgets.topics_btn.clicked.connect(self.buttonClick)
		widgets.services_btn.clicked.connect(self.buttonClick)
		widgets.params_btn.clicked.connect(self.buttonClick)
		widgets.add_order_btn.clicked.connect(self.buttonClick)

		# SCAN PAGE BUTTON CONNECTS
		widgets.btn_back_code.clicked.connect(self.buttonClick)
		widgets.btn_scan2.clicked.connect(self.buttonClick)
		
		# FI PLAN PAGE BUTTONS
		widgets.btn_random_fault.clicked.connect(self.buttonClick)
		widgets.btn_slct_fiplan.clicked.connect(get_file_json)
		widgets.btn_create_custom.clicked.connect(self.buttonClick)
		widgets.btn_select_fault.clicked.connect(faultSelectFromLibrary)
		widgets.btn_remove_fault.clicked.connect(self.buttonClick)
		widgets.btn_start_mutation.clicked.connect(mutationForFIPlan)
		widgets.btn_save_fiplan.clicked.connect(self.buttonClick)
		widgets.btn_remove_fiplan.clicked.connect(self.buttonClick)

		# EXECUTION PAGE BUTTONS
		widgets.btn_new_exe.clicked.connect(self.buttonClick)
		widgets.btn_remove_exe.clicked.connect(self.buttonClick)
		widgets.btn_select_metrics.clicked.connect(self.buttonClick)
		widgets.btn_start_exe.clicked.connect(executionModule)

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
		widgets.btn_create_snip.clicked.connect(self.buttonClick)
		widgets.btn_save_snip.clicked.connect(self.buttonClick)
		widgets.back_snip.clicked.connect(self.buttonClick)
		widgets.btn_delete_snip.clicked.connect(self.buttonClick)

		# CREATE CUSTOM FAULT PAGE
		widgets.btn_back_fi.clicked.connect(self.buttonClick)
		widgets.btn_save_fault.clicked.connect(self.buttonClick)
		widgets.btn_create_fault.clicked.connect(self.buttonClick)
		widgets.btn_delete_fault.clicked.connect(self.buttonClick)
		widgets.btn_remove_createdFault.clicked.connect(self.buttonClick)

		# METRICS PAGE BUTTONS
		widgets.btn_metric_list.clicked.connect(selectMetricFromListDoubleClick)
		widgets.saveMetrics.clicked.connect(self.buttonClick)
		widgets.btn_back_exe.clicked.connect(self.buttonClick)

		# YAML-LAUNCH FILE PAGE BUTTONS
		widgets.btn_open_yaml.clicked.connect(get_yaml_file)
		widgets.btn_clear_yaml.clicked.connect(check_empty)
		widgets.btn_yaml_fault.clicked.connect(fault_select_from_yaml_lib)
		widgets.btn_apply_yaml.clicked.connect(self.buttonClick)
		widgets.btn_remove_yaml.clicked.connect(self.buttonClick)
		widgets.btn_save_yaml.clicked.connect(self.buttonClick)
		widgets.checkBox_10.clicked.connect(self.buttonClick)

		# SHOW APP
		self.show()

		# SET CUSTOM THEME
		useCustomTheme = False

		# SET HOME PAGE AND SELECT MENU
		widgets.stackedWidget.setCurrentWidget(widgets.home)
		widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

		

	
	# BUTTONS CLICK FUNCTIONS

	def buttonClick(self):
		global file_type
		# GET BUTTON CLICKED
		btn = self.sender()
		btnName = btn.objectName()

		# HOME PAGE
		if btnName == "btn_home":
			widgets.stackedWidget.setCurrentWidget(widgets.ros_page)
			UIFunctions.resetStyle(self, btnName)
			btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
			widgets.titleRightInfo.setText("HOME")	
		
		# START PAGE
		if btnName == "btn_start":
			# widgets.stackedWidget.setCurrentWidget(widgets.start)
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

		if btnName == "btn_go_start_2":
			widgets.stackedWidget.setCurrentWidget(widgets.start)
			UIFunctions.resetStyle(self,widgets.btn_home.styleSheet())
			widgets.btn_start.setStyleSheet(UIFunctions.selectMenu(widgets.btn_start.styleSheet()))
			widgets.titleRightInfo.setText("START")

		if btnName == "btn_go_scan":
			widgets.btn_go_scan.setEnabled(False)
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
			widgets.btn_go_fiplan.setEnabled(False)
			widgets.stackedWidget.setCurrentWidget(widgets.fiplan)
			UIFunctions.resetStyle(self,widgets.btn_scan.styleSheet())
			widgets.btn_fiplan.setStyleSheet(UIFunctions.selectMenu(widgets.btn_fiplan.styleSheet()))
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN")

			for originalLine in self.placeForMutation:
				if type(originalLine) == int:
					pass
				else:
					newLine = originalLine.lstrip()
					widgets.listWidget.addItem(newLine)
			
			lineNumber = widgets.listWidget.count()
			
			for number in range(0,lineNumber):
				if number%2==0:
					widgets.listWidget.item(number).setBackground(QtGui.QColor(52, 59, 72)) # Gri
				else:
					widgets.listWidget.item(number).setBackground(QtGui.QColor(40, 44, 52)) #Arka plan rengi

		if btnName == "btn_go_exe":
			widgets.stackedWidget.setCurrentWidget(widgets.execution)
			UIFunctions.resetStyle(self,widgets.btn_fiplan.styleSheet())
			widgets.btn_execution.setStyleSheet(UIFunctions.selectMenu(widgets.btn_execution.styleSheet()))
			widgets.titleRightInfo.setText("EXECUTION")

		if btnName == "btn_go_exe_2":
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

		if btnName == "btn_prepare_plan":
			widgets.stackedWidget.setCurrentWidget(widgets.yaml_launch)
		
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
						
						taskName = str(snippetsJsonList['Snippet_Name'])
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

		# ROS PAGE at START PAGE
		
		if btnName == "open_ros_btn":
			dialog = QFileDialog()
			pathName = QFileDialog.getExistingDirectory()
			widgets.textEdit_42.setPlainText(pathName)

			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Warning)
			msgBox.setText("Dikkat")
			msgBox.setWindowTitle("Warning")
			msgBox.setStandardButtons(QMessageBox.Ok)
			msgBox.exec()

			model = QFileSystemModel()
			model.setRootPath(pathName)

			widgets.treeView.setModel(model)
			widgets.treeView.setRootIndex(model.index(pathName))
			widgets.treeView.setSortingEnabled(True)

		if btnName == "rosrun_btn":
			# Çalıştırmaya başlamak istiyor musunuz -Evet -Hayır gibi bir doğrulama yapılacak

			os.system("gnome-terminal -x killall roscore")

			os.system("gnome-terminal -x roscore")

			time.sleep(3) # condition
			os.system("gnome-terminal -x rosrun deneme_paket talker.py")

			time.sleep(3)
			os.system("gnome-terminal -x rosrun deneme_paket listener.py")

			time.sleep(3)
			os.system("gnome-terminal -x rostopic list")

		if btnName == "add_order_btn":
			path = widgets.textEdit_42.toPlainText()
			length_roslist = widgets.listWidget_26.count()
			file_from_tree = str(widgets.treeView.selectedIndexes()[0].data())
			adding_item = str(length_roslist + 1) + ". " + file_from_tree
			widgets.listWidget_26.addItem(adding_item)

		if btnName == "topics_btn":
			pass

		if btnName == "services_btn":
			pass

		if btnName == "params_btn":
			pass
		
		#  CODE SNIPPETS FROM START PAGE

		if btnName == "btn_create_code":
			widgets.stackedWidget.setCurrentWidget(widgets.cSnippets)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("CODE SNIPPETS - CREATE CUSTOM SNIPPETS")

		if btnName == "btn_remove_snip":
			row = widgets.listWidget_8.currentRow()
			widgets.listWidget_8.takeItem(row)
		
		# CREATE CUSTOM SNIPPETS FROM START PAGE

		if btnName == "btn_create_snip":
			snippetName = widgets.textEdit_2.toPlainText()
			snippetTitle = widgets.textEdit_27.toPlainText()
			snippetProcess = widgets.textEdit_29.toPlainText()
			snippetRegex = widgets.textEdit_28.toPlainText()

			codeSnippetJson ={
				"Snippet_Name": snippetName,
				"Title": snippetTitle,
				"Process": snippetProcess,
				"Regex_Code": snippetRegex
			}

			jsonSnippet = json.dumps(codeSnippetJson, indent = 4)

			widgets.textEdit_25.setPlainText(jsonSnippet)

		if btnName == "btn_delete_snip":
			widgets.textEdit_2.clear()
			widgets.textEdit_27.clear()
			widgets.textEdit_29.clear()
			widgets.textEdit_28.clear()
			widgets.textEdit_25.clear()
			widgets.textEdit_16.clear()
				
		if btnName == "btn_save_snip":

			isEmptyCodeSnip = widgets.textEdit_25.toPlainText()

			if isEmptyCodeSnip != "" and widgets.checkBox_6.isChecked() == True:

				snippetName = widgets.textEdit_2.toPlainText()
				snippetTitle = widgets.textEdit_27.toPlainText()
				snippetProcess = widgets.textEdit_29.toPlainText()
				snippetRegex = widgets.textEdit_28.toPlainText()

				createdSnippet ={
					"Snippets": {
						"Snippet_Name": snippetName,
						"Title": snippetTitle,
						"Process": snippetProcess,
						"Regex_Code": snippetRegex
					}
				}

				with open("code_snippets.json",'r+') as file:
					# First we load existing data into a dict.
					file_data = json.load(file)
					# Join new_data with file_data inside emp_details
					file_data["code_snippets"].append(createdSnippet)
					# Sets file's current position at offset.
					file.seek(0)
					# convert back to json.
					json.dump(file_data, file, indent = 4)

					codeSnippetFileName=widgets.textEdit_16.toPlainText()

					dialog = QFileDialog()
					pathName = QFileDialog.getExistingDirectory()

					codeSnippetPathAndName = os.path.join(pathName, codeSnippetFileName + ".json")

					createdCodeSnippets = widgets.textEdit_25.toPlainText()
					
					jsonFile = open(codeSnippetPathAndName, "w")
					jsonFile.write(createdCodeSnippets)
					jsonFile.close()

					widgets.label_60.setText("SAVED!")
				
				widgets.listWidget_10.addItem(snippetName)

			else:
				pass
			

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
			widgets.btn_scan2.setEnabled(False)

			if widgets.checkBox_2.isChecked()==True:
				isEmptyCodes=len(widgets.textEdit_4.toPlainText())
				isEmptyWorkloads=len(widgets.textEdit_22.toPlainText())
				if isEmptyCodes!=0:
					pureText=widgets.textEdit_4.toPlainText()
					tree=ast.dump(ast.parse(pureText))
					tree = astpretty.pprint(ast.parse(pureText).body[0], indent='  ')
					widgets.textEdit_23.setPlainText(tree)
					
					# for i in range(100):
					# 	time.sleep(0.01)
					# 	widgets.progressBar_2.setValue(i+1) 

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
												widgets.listWidget_2.item(number).setBackground(QtGui.QColor(102,0,102)) # Mavi renk
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

							for i in range(20):
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
										widgets.listWidget_2.item(i).setBackground(QtGui.QColor(0,128,255)) # Açık mavi
										paintedLineForMutation = widgets.listWidget_2.item(i).text()
										self.placeForMutation.append(i)
										self.placeForMutation.append(paintedLineForMutation)                   					
						else:
							pass
					
					else:
						with open('code_snippets.json') as codeSnippetsFromJson:
							codeSnippetRegexCode = json.load(codeSnippetsFromJson)

						for i in range(widgets.listWidget_8.count()):
								csDatas = widgets.listWidget_17.item(i).text()
								csDatasList.append(csDatas)

						for i in range(20):
							addedSnippetName=codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Snippet_Name"]
							for snippet in csDatasList:
								if snippet== addedSnippetName:
									addedSnippetRegex = codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Regex_Code"]
									patterns.append(addedSnippetRegex)
						else:
							with open('code_snippets.json') as codeSnippetsFromJson:
								codeSnippetRegexCode = json.load(codeSnippetsFromJson)
							for i in range(20):
								gerekli=codeSnippetRegexCode["code_snippets"][i]["Snippets"]["Regex_Code"]
								patterns.append(gerekli)
							
						for i in range(widgets.listWidget_2.count()):
							listOfCodes=widgets.listWidget_2.item(i).text()
							for pattern in patterns:
								result = re.findall(pattern,listOfCodes,re.MULTILINE)
								itemsCount = len(re.findall(pattern,pureText,re.MULTILINE))
								if result!=[]:
									paintedLineForMutation = widgets.listWidget_2.item(i).setBackground(QtGui.QColor(102,0,102)) # Mor
									purple_line_for_mutation = widgets.listWidget_2.item(i).text()
									selectedCodeSnippetCount = widgets.listWidget_17.count()
									if selectedCodeSnippetCount == 0 and widgets.textEdit_22.toPlainText() == "":
										listOfCodes = listOfCodes.lstrip()
										widgets.listWidget.addItem(listOfCodes)
										


		# FAULT PLAN PAGE

		if btnName == "btn_random_fault":
			print("Random Fault Injection Under Development")

		if btnName == "btn_create_custom":
			widgets.stackedWidget.setCurrentWidget(widgets.customFault)
			widgets.leftMenuBg.hide()
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN - CREATE CUSTOM FAULT")

		if btnName == "btn_remove_fault":
			global zippedList

			row = widgets.listWidget_7.currentRow()
			widgets.listWidget_7.takeItem(row)
			print(row)
			
			for i in range(2):
				del zippedList[row]

			print(zippedList)

		if btnName == "btn_save_fiplan":

			dataSizeOfSelected = widgets.listWidget_4.count()

			if dataSizeOfSelected != widgets.checkBox_4.isChecked() == True:
				dialog = QFileDialog()
				pathName = QFileDialog.getExistingDirectory()

				FIPlanName=widgets.textEdit_26.toPlainText()

				taskPathAndName = os.path.join(pathName, FIPlanName+".json")

				global sourceAndMutatedCode

				lengthMutatedList = len(sourceAndMutatedCode)

				for i in range(0,lengthMutatedList):
					if i % 2 == 0:
						originalCode = sourceAndMutatedCode[i]
					else:
						mutantCode = sourceAndMutatedCode[i]

						createdFault ={
							"Fault": {
								"Source_Code": originalCode,
								"Mutate_Code": mutantCode
							}
						}

						with open("faultPlans.json",'r+') as file:
							# First we load existing data into a dict.
							file_data = json.load(file)
							# Join new_data with file_data inside emp_details
							file_data["fault_plans"].append(createdFault)
							# Sets file's current position at offset.
							file.seek(0)
							# convert back to json.
							json.dump(file_data, file, indent = 4)

						# with open(taskPathAndName, "a") as outfile:
						# 	# createdFaultData = json.load(outfile)
						# 	# # Join new_data with file_data inside emp_details
						# 	# createdFaultData["fault_plans"].append(createdFault)
						# 	outfile.seek(0)
						# 	json.dump(createdFault, outfile,  indent = 4)

				text = widgets.textEdit_26.toPlainText()
				splitText = text.split("\n")
				widgets.listWidget_11.addItems(splitText)


		if btnName == "btn_remove_fiplan":
			row = widgets.listWidget_11.currentRow()
			widgets.listWidget_11.takeItem(row)

		# CREATE CUSTOM FAULT FROM FI PLAN

		if btnName == "btn_back_fi":
			widgets.stackedWidget.setCurrentWidget(widgets.fiplan)
			widgets.leftMenuBg.show()
			widgets.titleRightInfo.setText("FAULT INJECTION PLAN")
			
			lengthCreatedFaultsList = widgets.listWidget_5.count()

			if lengthCreatedFaultsList != 0:
				for i in range(0,lengthCreatedFaultsList):
					createdFaultFromList =  widgets.listWidget_5.item(i).text()
					widgets.listWidget_3.addItem(createdFaultFromList)

		if btnName == "btn_create_fault":
			faultName = widgets.textEdit_11.toPlainText()
			target = widgets.textEdit_30.toPlainText()
			changed = widgets.textEdit_31.toPlainText()
			explanation = widgets.textEdit_32.toPlainText()

			createdFaultJson ={
				"fault": {
					"Fault_Name": faultName,
					"Target_to_Change": target,
					"Changed": changed,
					"Explanation": explanation
				}
			}

			jsonFault = json.dumps(createdFaultJson, indent = 4)

			widgets.textEdit_34.setPlainText(jsonFault)

		if btnName == "btn_delete_fault":
			widgets.textEdit_11.clear()
			widgets.textEdit_30.clear()
			widgets.textEdit_31.clear()
			widgets.textEdit_32.clear()
			widgets.textEdit_34.clear()

		
		if btnName == "btn_save_fault":
			if widgets.textEdit_11.toPlainText() != "" and widgets.textEdit_30.toPlainText() != "" and widgets.textEdit_31.toPlainText() != "" and widgets.textEdit_32.toPlainText() != "":
				faultName = widgets.textEdit_11.toPlainText()
				target = widgets.textEdit_30.toPlainText()
				changed = widgets.textEdit_31.toPlainText()
				explanation = widgets.textEdit_32.toPlainText()

				createdFaultJson ={
				"fault": {
					"Fault_Name": faultName,
					"Target_to_Change": target,
					"Changed": changed,
					"Explanation": explanation
				}
			}

				with open("faultLibrary.json",'r+') as file:
					# First we load existing data into a dict.
					file_data = json.load(file)
					# Join new_data with file_data inside emp_details
					file_data["all_faults"].append(createdFaultJson)
					# Sets file's current position at offset.
					file.seek(0)
					# convert back to json.
					json.dump(file_data, file, indent = 4)

					jsonFault = json.dumps(createdFaultJson, indent = 4)

					faultFileName=widgets.textEdit_10.toPlainText()

					dialog = QFileDialog()
					pathName = QFileDialog.getExistingDirectory()

					taskPathAndName = os.path.join(pathName, faultFileName+".json")

					createdFault = widgets.textEdit_34.toPlainText()
									
					jsonFile = open(taskPathAndName, "w")
					jsonFile.write(createdFault)
					jsonFile.close()

					widgets.label_61.setText("SAVED!")

				widgets.listWidget_5.addItem(faultName)

				widgets.textEdit_11.clear()
				widgets.textEdit_30.clear()
				widgets.textEdit_31.clear()
				widgets.textEdit_32.clear()
				widgets.textEdit_34.clear()

			else:
				widgets.label_61.setText("FAULT DOES NOT EXIST!")

		if btnName == "btn_remove_createdFault":
			row = widgets.listWidget_5.currentRow()
			widgets.listWidget_5.takeItem(row)

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
			pass


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

			# save FPDF() class into a 
			# variable pdf
			pdf = FPDF()
			
			# Add a page
			pdf.add_page()
			
			# set style and size of font 
			# that you want in the pdf
			pdf.set_font("Arial", size = 9)

			txt = """
			The V&V Report Created by IM-FIT
			This reports shows information about AST Diagram of Source Codes, Fault List, Metric List, Rosbag Scenarios, etc.
			Therefore the user can learn about its source codes.
			IM-FIT
			"""
			pdf.cell(200, 10, txt = txt,ln = 1, align = 'C')

			# contents
			# ast diagram
			astText = widgets.textEdit_23.toPlainText()
			pdf.cell(200, 10, txt = astText,ln = 1, align = 'L')
			
			lenMetricList = widgets.listWidget_9.count()
			for i in range(0,lenMetricList):
				# create a cell
				line = widgets.listWidget_9.item(i).text()
				pdf.cell(200, 10, txt = line, ln = 2, align = 'L')

			lenMetricList = widgets.listWidget_16.count()
			for i in range(0,lenMetricList):
				# create a cell
				line = widgets.listWidget_16.item(i).text()
				pdf.cell(200, 10, txt = line, ln = 3, align = 'L')

			lenMetricList = widgets.listWidget_19.count()
			for i in range(0,lenMetricList):
				# create a cell
				line = widgets.listWidget_19.item(i).text()
				pdf.cell(200, 10, txt = line, ln = 4, align = 'L')

			lenMetricList = widgets.listWidget_14.count()
			for i in range(0,lenMetricList):
				# create a cell
				line = widgets.listWidget_14.item(i).text()
				pdf.cell(200, 10, txt = line, ln = 5, align = 'L')

			lenMetricList = widgets.listWidget_12.count()
			for i in range(0,lenMetricList):
				# create a cell
				line = widgets.listWidget_12.item(i).text()
				pdf.cell(200, 10, txt = line, ln = 6, align = 'L')
			
			# # save the pdf with name .pdf
			pdf.output("V&V_Report_by_IM-FIT.pdf")
			widgets.label_77.setText("V&V Report is Created")

		if btnName == "btn_apply_yaml":
			applied_mutation_list_count = widgets.listWidget_25.count()
			if applied_mutation_list_count > 0:
				widgets.listWidget_25.clear()
			if widgets.checkBox_10.isChecked() == True:
				if file_type == "yaml":
					def mutate_all_value (yaml_value):
						""" Define the data to apply mutation testing for yaml files """
						len_yaml_value_list = len(yaml_value)

						for i in range (0,len_yaml_value_list):
							if type(yaml_value[i]) == str:
								yaml_value[i] = "MUTANT"
							elif type(yaml_value[0]) == int:
								yaml_value[0] = 310911711697110116
							elif type(yaml_value[0]) == float:
								yaml_value[0] = 0.310911711697110116
							elif type(yaml_value[0]) == bool:
								if yaml_value[0] == False:
									yaml_value[0] = True
								else:
									yaml_value[0] = False
							else:
								yaml_value[0]
						return yaml_value

					content_list_length = widgets.listWidget_24.count()
					for i in range(0,content_list_length):
						row_info = widgets.listWidget_24.item(i).text()
						yaml_data_line = yaml.full_load(row_info)
						if row_info == "":
							pass
						else:					
							try:
								dict_values = yaml_data_line.values()
								dict_values = list(dict_values)

								dict_keys = yaml_data_line.keys()
								dict_keys = list(dict_keys)
								
								zipped = zip(dict_keys,mutate_all_value(dict_values))

								zipped_list = dict(zipped)

								dict_yaml = yaml.dump(zipped_list)
								# print(dict_yaml)

								split_dict_yaml = dict_yaml.split("\n")
								mutated_yaml_data = split_dict_yaml[0]
								split_data = mutated_yaml_data.split("\n")

								widgets.listWidget_25.addItems(split_data)					
									
							except:
								AttributeError()
				
				elif file_type == "launch":
					key_list = ["name","pkg","type","args","default","file",
					"respawn","output","command","ns","from","to","if","group"]

					def mutate_all_keys(key_data_list):
						""" Mutation testing applies to  the all possible nodes """
						tree = ET.parse('ornek_launch.launch')
						root = tree.getroot()
						lenroot = len(root)
						for i in range(0,lenroot):
							dictof = root[i].attrib
							for key in key_data_list:
								if key in dictof:
									dictof[key] = "mutated_data"
									split_data = str(dictof).split("\n")
									widgets.listWidget_25.addItems(split_data)

					mutate_all_keys(key_list)

				elif file_type == "msg" or "srv":
					content_list_length = widgets.listWidget_24.count()
					data_types_list = ["string","float32","int8","uint32","int32"]

					for i in range (0,content_list_length):
						SRV_CODE = widgets.listWidget_24.item(i).text()
						for i in data_types_list:
							result = re.findall(i, SRV_CODE)
							if result != []:
								for j in data_types_list:
									if result[0] != j:
										MUTATED_SRV_CODE = SRV_CODE.replace(result[0], j)
										split_data = MUTATED_SRV_CODE.split("\n")
										widgets.listWidget_25.addItems(split_data)
				else:
					pas

			else:
				if file_type == "yaml":
					def mutate_all_value (yaml_value, secim):
						""" Define the data to apply mutation testing for yaml files """
						old_value = yaml_value

						if type(yaml_value[0]) == str and secim == "YAML String Mutator":
							yaml_value[0] = "MUTANT"

						elif type(yaml_value[0]) == int and secim == "YAML Integer Mutator":
							yaml_value[0] = 310911711697110116

						elif type(yaml_value[0]) == float and secim == "YAML Float Mutator":
							yaml_value[0] = 0.310911711697110116

						elif type(yaml_value[0]) == bool and secim == "YAML Boolean Mutator":
							if yaml_value[0] == False:
								yaml_value[0] = True
							else:
								yaml_value[0] = False
						else:
							yaml_value[0]

						return yaml_value


					def analyze_yaml_line(YAML_DOCUMENT, secim):
						try:
							yaml_data_line = yaml.full_load(YAML_DOCUMENT)

							dict_values = yaml_data_line.values()
							dict_values = list(dict_values)

							dict_keys = yaml_data_line.keys()
							dict_keys = list(dict_keys)

							zipped = zip(dict_keys,mutate_all_value(dict_values, secim))

							zipped_list = dict(zipped)

							dict_yaml = yaml.dump(zipped_list)

							new_yaml = dict_yaml.split("\n")

							mutated_yaml_line = new_yaml[0]

							check_lines(YAML_DOCUMENT, mutated_yaml_line)
						except:
							pass

					def check_lines(YAML_DOCUMENT, mutated_yaml_line):
						if YAML_DOCUMENT != mutated_yaml_line:
							# Success mutation
							split_data = mutated_yaml_line.split("\n")
							widgets.listWidget_25.addItems(split_data)
							
					zipped_yaml_list_length = len(zipped_list_yaml)
					selected_list_length = widgets.listWidget_23.count() 
					if zipped_yaml_list_length != 0 and selected_list_length != 0:
						for i in range(0,zipped_yaml_list_length):
							if i % 2 == 0:
								lineWithInfo = zipped_list_yaml[i]
							else:
								fault = zipped_list_yaml[i]
								analyze_yaml_line(lineWithInfo,fault)

				if file_type == "srv":
					def analyze_srv_line (line, selected_fault):
						if selected_fault == "SRV - MSG string Mutator":
							target = "string"
							apply_srv_line_mutation(line,target)
						elif selected_fault == "SRV - MSG float32 Mutator":
							target = "float32"
							apply_srv_line_mutation(line,target)
						elif selected_fault == "SRV - MSG int8 Mutator":
							target = "int8"
							apply_srv_line_mutation(line,target)
						elif selected_fault == "SRV - MSG uint32 Mutator":
							target = "uint32"
							apply_srv_line_mutation(line,target)
						elif selected_fault == "SRV - MSG int32 Mutator":
							target = "int32"
							apply_srv_line_mutation(line,target)
						else:
							pass
					
					def apply_srv_line_mutation(line,target):
						SRV_CODE = line
						data_types_list = ["string","float32","int8","uint32","int32"]
						for i in data_types_list:
							result = re.findall(i, SRV_CODE)
							if result != [] and result[0] != target:
								MUTATED_SRV_CODE = SRV_CODE.replace(result[0], target)
								# Success Mutation
								split_data = MUTATED_SRV_CODE.split("\n")
								widgets.listWidget_25.addItems(split_data)

					zipped_yaml_list_length = len(zipped_list_yaml)
					selected_list_length = widgets.listWidget_23.count() 
					if zipped_yaml_list_length != 0 and selected_list_length != 0:
						for i in range(0,zipped_yaml_list_length):
							if i % 2 == 0:
								lineWithInfo = zipped_list_yaml[i]
							else:
								fault = zipped_list_yaml[i]
								analyze_srv_line (lineWithInfo, fault)
						
						

		if btnName == "btn_remove_yaml":
			pass

		if btnName == "btn_save_yaml":
			pass

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