import re   #imported for regex
import time       
#from PySide6.QtWidgets import *
#from PyQt6 import QtGui, QtCore

import main

class ScanModule:
    widgets = None

    #This function scans the source codes with regex    
    def scanWithRegex():
        for i in range(100):
                time.sleep(0.01)
                widgets.progressBar_2.setValue(i+1)
        
        x=widgets.textEdit_4.toPlainText()
        x=x.split('\n')
        widgets.listWidget_2.addItems(x)

        patterns=["if.*:","elif.*:","def.*:","for.*:","while.*:","__init__","super(.*)","#!/usr/bin/env python","try: ","except .*:","finally:  ","else.*:"]

        for i in range(widgets.listWidget_2.count()):
            list=widgets.listWidget_2.item(i).text()
            for pattern in patterns:
                result = re.findall(pattern,list,re.MULTILINE)
                if result!=[]:
                    widgets.listWidget_2.item(i).setBackground(QtGui.QColor(102,0,102))


class ParseWithAST(ScanModule):
    
    #This class parses the possible place to do mutation testing
    
    def parseWithAST(self):
        pass
