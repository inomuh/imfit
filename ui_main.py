# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1442, 721)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 650))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMen"
                        "u .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInf"
                        "o { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus"
                        " */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pr"
                        "essed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ///////////////////////////////"
                        "//////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radi"
                        "us: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:ver"
                        "tical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    "
                        "background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertic"
                        "al {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}"
                        "\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-w"
                        "idth: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	bord"
                        "er-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: "
                        "5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_46 = QLabel(self.topLogoInfo)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 0, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy1)
        self.label_46.setMinimumSize(QSize(50, 50))
        self.label_46.setMaximumSize(QSize(16777215, 50))
        self.label_46.setSizeIncrement(QSize(-1, 0))
        self.label_46.setPixmap(QPixmap(u"images/images/ros-icon.png"))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy2)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_start = QPushButton(self.topMenu)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy2.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy2)
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.LeftToRight)
        self.btn_start.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-data-transfer-down.png);")

        self.verticalLayout_8.addWidget(self.btn_start)

        self.btn_scan = QPushButton(self.topMenu)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy2.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy2)
        self.btn_scan.setMinimumSize(QSize(0, 45))
        self.btn_scan.setFont(font)
        self.btn_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan.setLayoutDirection(Qt.LeftToRight)
        self.btn_scan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_scan)

        self.btn_fiplan = QPushButton(self.topMenu)
        self.btn_fiplan.setObjectName(u"btn_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_fiplan.setSizePolicy(sizePolicy2)
        self.btn_fiplan.setMinimumSize(QSize(0, 45))
        self.btn_fiplan.setFont(font)
        self.btn_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fiplan.setLayoutDirection(Qt.LeftToRight)
        self.btn_fiplan.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_fiplan)

        self.btn_execution = QPushButton(self.topMenu)
        self.btn_execution.setObjectName(u"btn_execution")
        sizePolicy2.setHeightForWidth(self.btn_execution.sizePolicy().hasHeightForWidth())
        self.btn_execution.setSizePolicy(sizePolicy2)
        self.btn_execution.setMinimumSize(QSize(0, 45))
        self.btn_execution.setFont(font)
        self.btn_execution.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_execution.setLayoutDirection(Qt.LeftToRight)
        self.btn_execution.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-terminal.png);")

        self.verticalLayout_8.addWidget(self.btn_execution)

        self.btn_monitoring = QPushButton(self.topMenu)
        self.btn_monitoring.setObjectName(u"btn_monitoring")
        sizePolicy2.setHeightForWidth(self.btn_monitoring.sizePolicy().hasHeightForWidth())
        self.btn_monitoring.setSizePolicy(sizePolicy2)
        self.btn_monitoring.setMinimumSize(QSize(0, 45))
        self.btn_monitoring.setFont(font)
        self.btn_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_monitoring.setLayoutDirection(Qt.LeftToRight)
        self.btn_monitoring.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-check.png);")

        self.verticalLayout_8.addWidget(self.btn_monitoring)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 63 13pt \"URW Gothic\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_5 = QVBoxLayout(self.home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(20)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1280, 400))
        self.label_2.setPixmap(QPixmap(u"images/images/IM-FIT_Mimari.jpg"))
        self.label_2.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(20)
        self.textEdit_35 = QTextEdit(self.home)
        self.textEdit_35.setObjectName(u"textEdit_35")
        self.textEdit_35.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_35.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.textEdit_35, 0, 1, 1, 1)

        self.textEdit_36 = QTextEdit(self.home)
        self.textEdit_36.setObjectName(u"textEdit_36")
        self.textEdit_36.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_36.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.textEdit_36, 0, 3, 1, 1)

        self.textEdit_37 = QTextEdit(self.home)
        self.textEdit_37.setObjectName(u"textEdit_37")
        self.textEdit_37.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_37.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.textEdit_37, 0, 4, 1, 1)

        self.textEdit_38 = QTextEdit(self.home)
        self.textEdit_38.setObjectName(u"textEdit_38")
        self.textEdit_38.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_38.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.textEdit_38, 0, 0, 1, 1)

        self.textEdit_39 = QTextEdit(self.home)
        self.textEdit_39.setObjectName(u"textEdit_39")
        self.textEdit_39.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_39.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_24.addWidget(self.textEdit_39, 0, 2, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_24, 1, 0, 1, 3)


        self.verticalLayout_5.addLayout(self.gridLayout_15)

        self.btn_go_start = QPushButton(self.home)
        self.btn_go_start.setObjectName(u"btn_go_start")
        sizePolicy.setHeightForWidth(self.btn_go_start.sizePolicy().hasHeightForWidth())
        self.btn_go_start.setSizePolicy(sizePolicy)
        self.btn_go_start.setMinimumSize(QSize(300, 30))
        self.btn_go_start.setMaximumSize(QSize(16777215, 30))
        self.btn_go_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_start.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_go_start.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.btn_go_start)

        self.stackedWidget.addWidget(self.home)
        self.start = QWidget()
        self.start.setObjectName(u"start")
        self.start.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.start)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.textEdit = QTextEdit(self.start)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 1, 1, 6, 3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_50 = QLabel(self.start)
        self.label_50.setObjectName(u"label_50")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy4)
        self.label_50.setMinimumSize(QSize(0, 30))
        self.label_50.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.verticalLayout_12.addWidget(self.label_50)

        self.label_81 = QLabel(self.start)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_12.addWidget(self.label_81)

        self.btn_open_folder = QPushButton(self.start)
        self.btn_open_folder.setObjectName(u"btn_open_folder")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_open_folder.sizePolicy().hasHeightForWidth())
        self.btn_open_folder.setSizePolicy(sizePolicy5)
        self.btn_open_folder.setMinimumSize(QSize(200, 30))
        self.btn_open_folder.setFont(font)
        self.btn_open_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_folder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_folder.setIcon(icon5)

        self.verticalLayout_12.addWidget(self.btn_open_folder)

        self.btn_clear_codes = QPushButton(self.start)
        self.btn_clear_codes.setObjectName(u"btn_clear_codes")
        sizePolicy5.setHeightForWidth(self.btn_clear_codes.sizePolicy().hasHeightForWidth())
        self.btn_clear_codes.setSizePolicy(sizePolicy5)
        self.btn_clear_codes.setMinimumSize(QSize(200, 30))
        self.btn_clear_codes.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_codes.setIcon(icon6)

        self.verticalLayout_12.addWidget(self.btn_clear_codes)

        self.checkBox_8 = QCheckBox(self.start)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy5.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy5)
        self.checkBox_8.setMinimumSize(QSize(200, 30))
        self.checkBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_8.setIcon(icon7)

        self.verticalLayout_12.addWidget(self.checkBox_8)

        self.label_85 = QLabel(self.start)
        self.label_85.setObjectName(u"label_85")

        self.verticalLayout_12.addWidget(self.label_85)

        self.btn_prepare_plan = QPushButton(self.start)
        self.btn_prepare_plan.setObjectName(u"btn_prepare_plan")
        sizePolicy5.setHeightForWidth(self.btn_prepare_plan.sizePolicy().hasHeightForWidth())
        self.btn_prepare_plan.setSizePolicy(sizePolicy5)
        self.btn_prepare_plan.setMinimumSize(QSize(200, 30))
        self.btn_prepare_plan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prepare_plan.setIcon(icon8)

        self.verticalLayout_12.addWidget(self.btn_prepare_plan)

        self.label_51 = QLabel(self.start)
        self.label_51.setObjectName(u"label_51")
        sizePolicy4.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy4)
        self.label_51.setMinimumSize(QSize(0, 30))
        self.label_51.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.verticalLayout_12.addWidget(self.label_51)

        self.btn_select_workload = QPushButton(self.start)
        self.btn_select_workload.setObjectName(u"btn_select_workload")
        self.btn_select_workload.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.btn_select_workload.sizePolicy().hasHeightForWidth())
        self.btn_select_workload.setSizePolicy(sizePolicy5)
        self.btn_select_workload.setMinimumSize(QSize(200, 30))
        self.btn_select_workload.setFont(font)
        self.btn_select_workload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_workload.setIcon(icon5)

        self.verticalLayout_12.addWidget(self.btn_select_workload, 0, Qt.AlignHCenter)

        self.btn_create_workload = QPushButton(self.start)
        self.btn_create_workload.setObjectName(u"btn_create_workload")
        sizePolicy5.setHeightForWidth(self.btn_create_workload.sizePolicy().hasHeightForWidth())
        self.btn_create_workload.setSizePolicy(sizePolicy5)
        self.btn_create_workload.setMinimumSize(QSize(200, 30))
        self.btn_create_workload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_workload.setIcon(icon9)

        self.verticalLayout_12.addWidget(self.btn_create_workload, 0, Qt.AlignHCenter)

        self.btn_save_workload = QPushButton(self.start)
        self.btn_save_workload.setObjectName(u"btn_save_workload")
        sizePolicy5.setHeightForWidth(self.btn_save_workload.sizePolicy().hasHeightForWidth())
        self.btn_save_workload.setSizePolicy(sizePolicy5)
        self.btn_save_workload.setMinimumSize(QSize(200, 30))
        self.btn_save_workload.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save_workload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_workload.setIcon(icon10)

        self.verticalLayout_12.addWidget(self.btn_save_workload, 0, Qt.AlignHCenter)

        self.btn_clear_workload = QPushButton(self.start)
        self.btn_clear_workload.setObjectName(u"btn_clear_workload")
        sizePolicy5.setHeightForWidth(self.btn_clear_workload.sizePolicy().hasHeightForWidth())
        self.btn_clear_workload.setSizePolicy(sizePolicy5)
        self.btn_clear_workload.setMinimumSize(QSize(200, 30))
        self.btn_clear_workload.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_workload.setIcon(icon6)

        self.verticalLayout_12.addWidget(self.btn_clear_workload)

        self.checkBox_5 = QCheckBox(self.start)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy5.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy5)
        self.checkBox_5.setMinimumSize(QSize(200, 30))
        self.checkBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.checkBox_5.setIcon(icon7)

        self.verticalLayout_12.addWidget(self.checkBox_5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 0, 7, 1)

        self.label_9 = QLabel(self.start)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 3)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(20)
        self.gridLayout_22.setVerticalSpacing(10)
        self.textEdit_3 = QTextEdit(self.start)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(0, 150))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_3.setReadOnly(True)

        self.gridLayout_22.addWidget(self.textEdit_3, 1, 0, 2, 4)

        self.label_55 = QLabel(self.start)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.label_55, 3, 2, 1, 2)

        self.btn_create_code = QPushButton(self.start)
        self.btn_create_code.setObjectName(u"btn_create_code")
        self.btn_create_code.setMinimumSize(QSize(0, 30))
        self.btn_create_code.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_code.setIcon(icon11)

        self.gridLayout_22.addWidget(self.btn_create_code, 8, 0, 1, 1)

        self.label_42 = QLabel(self.start)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 30))
        self.label_42.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.label_42, 0, 0, 1, 4)

        self.btn_add_custom = QPushButton(self.start)
        self.btn_add_custom.setObjectName(u"btn_add_custom")
        self.btn_add_custom.setMinimumSize(QSize(0, 30))
        self.btn_add_custom.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.btn_add_custom.setIcon(icon9)

        self.gridLayout_22.addWidget(self.btn_add_custom, 8, 1, 1, 1)

        self.label_54 = QLabel(self.start)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.label_54, 3, 0, 1, 2)

        self.label_56 = QLabel(self.start)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.label_56, 5, 2, 1, 2)

        self.btn_select_snippet = QPushButton(self.start)
        self.btn_select_snippet.setObjectName(u"btn_select_snippet")
        self.btn_select_snippet.setMinimumSize(QSize(0, 30))
        self.btn_select_snippet.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-hand-point-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_snippet.setIcon(icon12)

        self.gridLayout_22.addWidget(self.btn_select_snippet, 7, 0, 1, 2)

        self.textEdit_24 = QTextEdit(self.start)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")

        self.gridLayout_22.addWidget(self.textEdit_24, 4, 2, 1, 2)

        self.listWidget_10 = QListWidget(self.start)
        font5 = QFont()
        font5.setPointSize(20)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem.setFont(font5);
        __qlistwidgetitem.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem1.setFont(font5);
        __qlistwidgetitem1.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_10)
        __qlistwidgetitem2.setFont(font5);
        __qlistwidgetitem2.setFlags(Qt.NoItemFlags);
        self.listWidget_10.setObjectName(u"listWidget_10")
        sizePolicy.setHeightForWidth(self.listWidget_10.sizePolicy().hasHeightForWidth())
        self.listWidget_10.setSizePolicy(sizePolicy)
        self.listWidget_10.setMinimumSize(QSize(0, 0))
        self.listWidget_10.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_10.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_22.addWidget(self.listWidget_10, 4, 0, 3, 2)

        self.checkBox_3 = QCheckBox(self.start)
        self.checkBox_3.setObjectName(u"checkBox_3")
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(False)
        self.checkBox_3.setFont(font6)
        self.checkBox_3.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_22.addWidget(self.checkBox_3, 9, 0, 1, 2, Qt.AlignHCenter)

        self.listWidget_8 = QListWidget(self.start)
        self.listWidget_8.setObjectName(u"listWidget_8")
        self.listWidget_8.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")

        self.gridLayout_22.addWidget(self.listWidget_8, 6, 2, 3, 2)

        self.btn_remove_snip = QPushButton(self.start)
        self.btn_remove_snip.setObjectName(u"btn_remove_snip")
        self.btn_remove_snip.setMinimumSize(QSize(0, 30))
        self.btn_remove_snip.setMaximumSize(QSize(16777215, 16777215))
        self.btn_remove_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_snip.setIcon(icon13)

        self.gridLayout_22.addWidget(self.btn_remove_snip, 9, 2, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_22, 0, 4, 7, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setHorizontalSpacing(50)
        self.gridLayout_35.setVerticalSpacing(6)
        self.btn_go_scan = QPushButton(self.start)
        self.btn_go_scan.setObjectName(u"btn_go_scan")
        sizePolicy5.setHeightForWidth(self.btn_go_scan.sizePolicy().hasHeightForWidth())
        self.btn_go_scan.setSizePolicy(sizePolicy5)
        self.btn_go_scan.setMinimumSize(QSize(200, 30))
        self.btn_go_scan.setMaximumSize(QSize(200, 30))
        self.btn_go_scan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_scan.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_scan.setIcon(icon4)

        self.gridLayout_35.addWidget(self.btn_go_scan, 0, 1, 1, 1, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.start)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy5.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy5)
        self.pushButton_5.setMinimumSize(QSize(200, 30))
        self.pushButton_5.setMaximumSize(QSize(200, 30))
        self.pushButton_5.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon14)

        self.gridLayout_35.addWidget(self.pushButton_5, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout.addLayout(self.gridLayout_35)

        self.stackedWidget.addWidget(self.start)
        self.ros_page = QWidget()
        self.ros_page.setObjectName(u"ros_page")
        self.verticalLayout_32 = QVBoxLayout(self.ros_page)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_90 = QLabel(self.ros_page)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_10.addWidget(self.label_90, 2, 1, 1, 1)

        self.label_91 = QLabel(self.ros_page)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_10.addWidget(self.label_91, 2, 0, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.topics_btn = QPushButton(self.ros_page)
        self.topics_btn.setObjectName(u"topics_btn")
        self.topics_btn.setMinimumSize(QSize(0, 30))
        self.topics_btn.setMaximumSize(QSize(16777215, 30))
        self.topics_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.topics_btn, 0, 0, 1, 1)

        self.params_btn = QPushButton(self.ros_page)
        self.params_btn.setObjectName(u"params_btn")
        self.params_btn.setMinimumSize(QSize(0, 30))
        self.params_btn.setMaximumSize(QSize(16777215, 30))
        self.params_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.params_btn, 0, 2, 1, 1)

        self.services_btn = QPushButton(self.ros_page)
        self.services_btn.setObjectName(u"services_btn")
        self.services_btn.setMinimumSize(QSize(0, 30))
        self.services_btn.setMaximumSize(QSize(16777215, 30))
        self.services_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.services_btn, 0, 1, 1, 1)

        self.listWidget_27 = QListWidget(self.ros_page)
        self.listWidget_27.setObjectName(u"listWidget_27")
        self.listWidget_27.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_31.addWidget(self.listWidget_27, 1, 0, 1, 3)


        self.gridLayout_10.addLayout(self.gridLayout_31, 3, 0, 1, 1)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.rosrun_btn = QPushButton(self.ros_page)
        self.rosrun_btn.setObjectName(u"rosrun_btn")
        self.rosrun_btn.setMinimumSize(QSize(0, 30))
        self.rosrun_btn.setMaximumSize(QSize(16777215, 30))
        self.rosrun_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.rosrun_btn, 3, 0, 1, 2)

        self.treeView = QTreeView(self.ros_page)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.treeView, 2, 0, 1, 2)

        self.textEdit_42 = QTextEdit(self.ros_page)
        self.textEdit_42.setObjectName(u"textEdit_42")
        self.textEdit_42.setMaximumSize(QSize(16777215, 30))
        self.textEdit_42.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_42.setReadOnly(True)

        self.gridLayout_32.addWidget(self.textEdit_42, 1, 0, 1, 1)

        self.open_ros_btn = QPushButton(self.ros_page)
        self.open_ros_btn.setObjectName(u"open_ros_btn")
        self.open_ros_btn.setMinimumSize(QSize(200, 30))
        self.open_ros_btn.setMaximumSize(QSize(200, 16777215))
        self.open_ros_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.open_ros_btn, 1, 1, 1, 1)

        self.label_92 = QLabel(self.ros_page)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_32.addWidget(self.label_92, 0, 0, 1, 2)

        self.listWidget_26 = QListWidget(self.ros_page)
        self.listWidget_26.setObjectName(u"listWidget_26")
        self.listWidget_26.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_32.addWidget(self.listWidget_26, 4, 0, 1, 2)


        self.gridLayout_10.addLayout(self.gridLayout_32, 1, 0, 1, 1)

        self.textEdit_43 = QTextEdit(self.ros_page)
        self.textEdit_43.setObjectName(u"textEdit_43")

        self.gridLayout_10.addWidget(self.textEdit_43, 1, 1, 1, 1)


        self.verticalLayout_32.addLayout(self.gridLayout_10)

        self.stackedWidget.addWidget(self.ros_page)
        self.scan = QWidget()
        self.scan.setObjectName(u"scan")
        self.verticalLayout_30 = QVBoxLayout(self.scan)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setSpacing(10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_15 = QLabel(self.scan)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_19.addWidget(self.label_15, 2, 0, 1, 1)

        self.textEdit_22 = QTextEdit(self.scan)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_22.setReadOnly(True)

        self.gridLayout_19.addWidget(self.textEdit_22, 3, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.scan)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_19.addWidget(self.textEdit_4, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_19, 1, 0, 13, 1)

        self.checkBox_2 = QCheckBox(self.scan)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(120, 30))
        self.checkBox_2.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.checkBox_2, 10, 1, 4, 2)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_49 = QLabel(self.scan)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_21.addWidget(self.label_49, 0, 0, 1, 1)

        self.listWidget_2 = QListWidget(self.scan)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_21.addWidget(self.listWidget_2, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_21, 0, 4, 14, 1)

        self.label_59 = QLabel(self.scan)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.label_59, 0, 1, 1, 3)

        self.listWidget_17 = QListWidget(self.scan)
        self.listWidget_17.setObjectName(u"listWidget_17")
        sizePolicy.setHeightForWidth(self.listWidget_17.sizePolicy().hasHeightForWidth())
        self.listWidget_17.setSizePolicy(sizePolicy)
        self.listWidget_17.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_17.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_4.addWidget(self.listWidget_17, 1, 1, 7, 3)

        self.label_48 = QLabel(self.scan)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_4.addWidget(self.label_48, 0, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.scan)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy5.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy5)
        self.progressBar_2.setMinimumSize(QSize(315, 30))
        self.progressBar_2.setStyleSheet(u"background-color:black;")
        self.progressBar_2.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar_2, 9, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 8, 1, 1, 3)

        self.btn_scan2 = QPushButton(self.scan)
        self.btn_scan2.setObjectName(u"btn_scan2")
        sizePolicy5.setHeightForWidth(self.btn_scan2.sizePolicy().hasHeightForWidth())
        self.btn_scan2.setSizePolicy(sizePolicy5)
        self.btn_scan2.setMinimumSize(QSize(150, 30))
        self.btn_scan2.setFont(font)
        self.btn_scan2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scan2.setStyleSheet(u"background-color:black;\n"
"color:white;")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scan2.setIcon(icon15)

        self.gridLayout_4.addWidget(self.btn_scan2, 10, 3, 4, 1)


        self.verticalLayout_30.addLayout(self.gridLayout_4)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setHorizontalSpacing(50)
        self.btn_go_fiplan = QPushButton(self.scan)
        self.btn_go_fiplan.setObjectName(u"btn_go_fiplan")
        sizePolicy5.setHeightForWidth(self.btn_go_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_go_fiplan.setSizePolicy(sizePolicy5)
        self.btn_go_fiplan.setMinimumSize(QSize(200, 30))
        self.btn_go_fiplan.setMaximumSize(QSize(200, 30))
        self.btn_go_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_fiplan.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_fiplan.setIcon(icon4)

        self.gridLayout_38.addWidget(self.btn_go_fiplan, 0, 1, 1, 1, Qt.AlignRight)

        self.btn_back_code = QPushButton(self.scan)
        self.btn_back_code.setObjectName(u"btn_back_code")
        sizePolicy5.setHeightForWidth(self.btn_back_code.sizePolicy().hasHeightForWidth())
        self.btn_back_code.setSizePolicy(sizePolicy5)
        self.btn_back_code.setMinimumSize(QSize(200, 30))
        self.btn_back_code.setMaximumSize(QSize(200, 30))
        self.btn_back_code.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_code.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_back_code.setIcon(icon14)

        self.gridLayout_38.addWidget(self.btn_back_code, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_30.addLayout(self.gridLayout_38)

        self.stackedWidget.addWidget(self.scan)
        self.fiplan = QWidget()
        self.fiplan.setObjectName(u"fiplan")
        self.verticalLayout_40 = QVBoxLayout(self.fiplan)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(20)
        self.gridLayout_7.setVerticalSpacing(10)
        self.btn_start_mutation = QPushButton(self.fiplan)
        self.btn_start_mutation.setObjectName(u"btn_start_mutation")
        self.btn_start_mutation.setMinimumSize(QSize(0, 30))
        self.btn_start_mutation.setMaximumSize(QSize(16777215, 30))
        self.btn_start_mutation.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 13pt \"Ubuntu\";")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_mutation.setIcon(icon16)

        self.gridLayout_7.addWidget(self.btn_start_mutation, 9, 2, 1, 1)

        self.label_30 = QLabel(self.fiplan)
        self.label_30.setObjectName(u"label_30")
        sizePolicy4.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy4)
        self.label_30.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_30, 0, 1, 1, 2)

        self.progressBar = QProgressBar(self.fiplan)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 30))
        self.progressBar.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.progressBar.setValue(0)

        self.gridLayout_7.addWidget(self.progressBar, 10, 1, 1, 2)

        self.label_12 = QLabel(self.fiplan)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.btn_random_fault = QPushButton(self.fiplan)
        self.btn_random_fault.setObjectName(u"btn_random_fault")
        self.btn_random_fault.setMinimumSize(QSize(0, 30))
        self.btn_random_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-laptop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_random_fault.setIcon(icon17)

        self.gridLayout_7.addWidget(self.btn_random_fault, 1, 1, 1, 1)

        self.btn_create_custom = QPushButton(self.fiplan)
        self.btn_create_custom.setObjectName(u"btn_create_custom")
        sizePolicy2.setHeightForWidth(self.btn_create_custom.sizePolicy().hasHeightForWidth())
        self.btn_create_custom.setSizePolicy(sizePolicy2)
        self.btn_create_custom.setMinimumSize(QSize(0, 30))
        self.btn_create_custom.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_custom.setIcon(icon11)

        self.gridLayout_7.addWidget(self.btn_create_custom, 1, 2, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(6)
        self.gridLayout_25.setVerticalSpacing(10)
        self.label_16 = QLabel(self.fiplan)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_25.addWidget(self.label_16, 0, 0, 1, 1)

        self.btn_remove_fault = QPushButton(self.fiplan)
        self.btn_remove_fault.setObjectName(u"btn_remove_fault")
        self.btn_remove_fault.setMinimumSize(QSize(0, 30))
        self.btn_remove_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_fault.setIcon(icon13)

        self.gridLayout_25.addWidget(self.btn_remove_fault, 2, 0, 1, 1)

        self.listWidget_7 = QListWidget(self.fiplan)
        self.listWidget_7.setObjectName(u"listWidget_7")
        self.listWidget_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_25.addWidget(self.listWidget_7, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_25, 6, 2, 3, 1)

        self.label_34 = QLabel(self.fiplan)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)
        self.label_34.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_7.addWidget(self.label_34, 0, 3, 1, 3)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setHorizontalSpacing(6)
        self.gridLayout_30.setVerticalSpacing(10)
        self.listWidget = QListWidget(self.fiplan)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_30.addWidget(self.listWidget, 0, 0, 1, 1)

        self.label_5 = QLabel(self.fiplan)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_30.addWidget(self.label_5, 1, 0, 1, 1)

        self.textEdit_13 = QTextEdit(self.fiplan)
        self.textEdit_13.setObjectName(u"textEdit_13")
        sizePolicy2.setHeightForWidth(self.textEdit_13.sizePolicy().hasHeightForWidth())
        self.textEdit_13.setSizePolicy(sizePolicy2)
        self.textEdit_13.setMaximumSize(QSize(16777215, 30))
        self.textEdit_13.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_13.setReadOnly(True)

        self.gridLayout_30.addWidget(self.textEdit_13, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_30, 1, 0, 10, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_52 = QLabel(self.fiplan)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 30))
        self.label_52.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_26.addWidget(self.label_52, 0, 0, 1, 1)

        self.textEdit_17 = QTextEdit(self.fiplan)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setMinimumSize(QSize(300, 0))
        self.textEdit_17.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_17.setReadOnly(True)

        self.gridLayout_26.addWidget(self.textEdit_17, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_26, 2, 2, 4, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(6)
        self.gridLayout_27.setVerticalSpacing(10)
        self.label_6 = QLabel(self.fiplan)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_27.addWidget(self.label_6, 0, 0, 1, 1)

        self.listWidget_3 = QListWidget(self.fiplan)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem3.setFont(font5);
        __qlistwidgetitem3.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4.setFont(font5);
        __qlistwidgetitem4.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem5.setFont(font5);
        __qlistwidgetitem5.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem6.setFont(font5);
        __qlistwidgetitem6.setFlags(Qt.NoItemFlags);
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(300, 0))
        self.listWidget_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_27.addWidget(self.listWidget_3, 1, 0, 1, 1)

        self.btn_select_fault = QPushButton(self.fiplan)
        self.btn_select_fault.setObjectName(u"btn_select_fault")
        self.btn_select_fault.setMinimumSize(QSize(0, 30))
        self.btn_select_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_fault.setIcon(icon12)

        self.gridLayout_27.addWidget(self.btn_select_fault, 2, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.fiplan)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu"])
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setItalic(False)
        self.checkBox_4.setFont(font7)
        self.checkBox_4.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 11pt \"Ubuntu\";\n"
"")

        self.gridLayout_27.addWidget(self.checkBox_4, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_27, 2, 1, 8, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(18)
        self.gridLayout_23.setVerticalSpacing(6)
        self.pushButton = QPushButton(self.fiplan)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon13)

        self.gridLayout_23.addWidget(self.pushButton, 2, 0, 3, 2)

        self.btn_slct_fiplan = QPushButton(self.fiplan)
        self.btn_slct_fiplan.setObjectName(u"btn_slct_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_slct_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_slct_fiplan.setSizePolicy(sizePolicy2)
        self.btn_slct_fiplan.setMinimumSize(QSize(0, 30))
        self.btn_slct_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_slct_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_slct_fiplan.setIcon(icon5)

        self.gridLayout_23.addWidget(self.btn_slct_fiplan, 7, 0, 1, 1)

        self.textEdit_26 = QTextEdit(self.fiplan)
        self.textEdit_26.setObjectName(u"textEdit_26")
        sizePolicy2.setHeightForWidth(self.textEdit_26.sizePolicy().hasHeightForWidth())
        self.textEdit_26.setSizePolicy(sizePolicy2)
        self.textEdit_26.setMaximumSize(QSize(16777215, 30))
        self.textEdit_26.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.textEdit_26, 6, 1, 1, 1)

        self.label_76 = QLabel(self.fiplan)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 30))
        self.label_76.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_76, 5, 0, 1, 2)

        self.btn_save_fiplan = QPushButton(self.fiplan)
        self.btn_save_fiplan.setObjectName(u"btn_save_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_save_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_save_fiplan.setSizePolicy(sizePolicy2)
        self.btn_save_fiplan.setMinimumSize(QSize(0, 0))
        self.btn_save_fiplan.setMaximumSize(QSize(16777215, 30))
        self.btn_save_fiplan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_fiplan.setIcon(icon10)

        self.gridLayout_23.addWidget(self.btn_save_fiplan, 7, 1, 1, 1)

        self.label_33 = QLabel(self.fiplan)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_33, 6, 0, 1, 1)

        self.listWidget_11 = QListWidget(self.fiplan)
        self.listWidget_11.setObjectName(u"listWidget_11")
        sizePolicy.setHeightForWidth(self.listWidget_11.sizePolicy().hasHeightForWidth())
        self.listWidget_11.setSizePolicy(sizePolicy)
        self.listWidget_11.setMinimumSize(QSize(0, 0))
        self.listWidget_11.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.listWidget_11, 5, 2, 2, 1)

        self.btn_remove_fiplan = QPushButton(self.fiplan)
        self.btn_remove_fiplan.setObjectName(u"btn_remove_fiplan")
        sizePolicy2.setHeightForWidth(self.btn_remove_fiplan.sizePolicy().hasHeightForWidth())
        self.btn_remove_fiplan.setSizePolicy(sizePolicy2)
        self.btn_remove_fiplan.setMinimumSize(QSize(0, 30))
        self.btn_remove_fiplan.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_fiplan.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_fiplan.setIcon(icon13)

        self.gridLayout_23.addWidget(self.btn_remove_fiplan, 7, 2, 1, 1)

        self.label_44 = QLabel(self.fiplan)
        self.label_44.setObjectName(u"label_44")
        sizePolicy4.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy4)
        self.label_44.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_23.addWidget(self.label_44, 2, 2, 3, 1)

        self.listWidget_4 = QListWidget(self.fiplan)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_23.addWidget(self.listWidget_4, 1, 0, 1, 3)


        self.gridLayout_7.addLayout(self.gridLayout_23, 1, 3, 10, 3)


        self.verticalLayout_40.addLayout(self.gridLayout_7)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setHorizontalSpacing(50)
        self.pushButton_7 = QPushButton(self.fiplan)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy5.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy5)
        self.pushButton_7.setMinimumSize(QSize(200, 30))
        self.pushButton_7.setMaximumSize(QSize(200, 30))
        self.pushButton_7.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.pushButton_7.setIcon(icon14)

        self.gridLayout_39.addWidget(self.pushButton_7, 0, 0, 1, 1, Qt.AlignLeft)

        self.btn_go_exe = QPushButton(self.fiplan)
        self.btn_go_exe.setObjectName(u"btn_go_exe")
        sizePolicy5.setHeightForWidth(self.btn_go_exe.sizePolicy().hasHeightForWidth())
        self.btn_go_exe.setSizePolicy(sizePolicy5)
        self.btn_go_exe.setMinimumSize(QSize(200, 30))
        self.btn_go_exe.setMaximumSize(QSize(200, 30))
        self.btn_go_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_exe.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_exe.setIcon(icon4)

        self.gridLayout_39.addWidget(self.btn_go_exe, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_40.addLayout(self.gridLayout_39)

        self.stackedWidget.addWidget(self.fiplan)
        self.execution = QWidget()
        self.execution.setObjectName(u"execution")
        self.verticalLayout_20 = QVBoxLayout(self.execution)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.execution)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 30))
        self.label_57.setMaximumSize(QSize(16777215, 30))
        self.label_57.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_57, 0, 1, 1, 5, Qt.AlignHCenter)

        self.pushButton_9 = QPushButton(self.execution)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(0, 30))
        self.pushButton_9.setMaximumSize(QSize(16777215, 30))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_9.setIcon(icon12)

        self.gridLayout_6.addWidget(self.pushButton_9, 3, 0, 1, 1)

        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setSpacing(20)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_39 = QLabel(self.execution)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_40.addWidget(self.label_39, 3, 2, 1, 1)

        self.comboBox_8 = QComboBox(self.execution)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 30))
        self.comboBox_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.comboBox_8, 2, 1, 1, 1)

        self.textEdit_19 = QTextEdit(self.execution)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setMinimumSize(QSize(0, 30))
        self.textEdit_19.setMaximumSize(QSize(16777215, 30))
        self.textEdit_19.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.textEdit_19, 5, 3, 1, 1)

        self.comboBox_7 = QComboBox(self.execution)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(0, 30))
        self.comboBox_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.btn_new_exe = QPushButton(self.execution)
        self.btn_new_exe.setObjectName(u"btn_new_exe")
        sizePolicy.setHeightForWidth(self.btn_new_exe.sizePolicy().hasHeightForWidth())
        self.btn_new_exe.setSizePolicy(sizePolicy)
        self.btn_new_exe.setMinimumSize(QSize(0, 0))
        self.btn_new_exe.setMaximumSize(QSize(16777215, 30))
        self.btn_new_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_exe.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_new_exe.setIcon(icon9)

        self.gridLayout_40.addWidget(self.btn_new_exe, 6, 0, 1, 2)

        self.label_72 = QLabel(self.execution)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_40.addWidget(self.label_72, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_40.addItem(self.verticalSpacer_2, 8, 0, 3, 4)

        self.label_84 = QLabel(self.execution)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_40.addWidget(self.label_84, 4, 0, 1, 1)

        self.textEdit_18 = QTextEdit(self.execution)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setMaximumSize(QSize(16777215, 30))
        self.textEdit_18.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.textEdit_18, 3, 1, 1, 1)

        self.label_28 = QLabel(self.execution)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_40.addWidget(self.label_28, 2, 0, 1, 1)

        self.label_24 = QLabel(self.execution)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_40.addWidget(self.label_24, 1, 2, 1, 1)

        self.btn_start_exe = QPushButton(self.execution)
        self.btn_start_exe.setObjectName(u"btn_start_exe")
        sizePolicy.setHeightForWidth(self.btn_start_exe.sizePolicy().hasHeightForWidth())
        self.btn_start_exe.setSizePolicy(sizePolicy)
        self.btn_start_exe.setMinimumSize(QSize(150, 30))
        self.btn_start_exe.setMaximumSize(QSize(16777215, 30))
        self.btn_start_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_exe.setStyleSheet(u"background-color:black;\n"
"color:white;")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_exe.setIcon(icon18)

        self.gridLayout_40.addWidget(self.btn_start_exe, 7, 0, 1, 4)

        self.label_38 = QLabel(self.execution)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_40.addWidget(self.label_38, 5, 0, 1, 1)

        self.checkBox = QCheckBox(self.execution)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy5.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy5)
        self.checkBox.setMinimumSize(QSize(200, 30))
        self.checkBox.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.checkBox, 0, 3, 1, 1)

        self.comboBox_6 = QComboBox(self.execution)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy4.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy4)
        self.comboBox_6.setMinimumSize(QSize(0, 30))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.comboBox_6, 1, 3, 1, 1)

        self.label_20 = QLabel(self.execution)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setBaseSize(QSize(0, 0))

        self.gridLayout_40.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_82 = QLabel(self.execution)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_40.addWidget(self.label_82, 0, 2, 1, 1)

        self.comboBox_11 = QComboBox(self.execution)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMinimumSize(QSize(0, 30))
        self.comboBox_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.comboBox_11, 3, 3, 1, 1)

        self.label_26 = QLabel(self.execution)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_40.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_75 = QLabel(self.execution)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_40.addWidget(self.label_75, 3, 0, 1, 1)

        self.textEdit_7 = QTextEdit(self.execution)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy6)
        self.textEdit_7.setMinimumSize(QSize(0, 30))
        self.textEdit_7.setMaximumSize(QSize(16777215, 30))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.textEdit_7, 5, 1, 1, 1)

        self.label_36 = QLabel(self.execution)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_40.addWidget(self.label_36, 2, 2, 1, 1)

        self.label_83 = QLabel(self.execution)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_40.addWidget(self.label_83, 5, 2, 1, 1)

        self.comboBox_9 = QComboBox(self.execution)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(0, 30))
        self.comboBox_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.comboBox_9, 2, 3, 1, 1)

        self.textEdit_6 = QTextEdit(self.execution)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy2.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy2)
        self.textEdit_6.setMinimumSize(QSize(150, 30))
        self.textEdit_6.setMaximumSize(QSize(16777215, 30))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.textEdit_6, 0, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.execution)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(200, 30))
        self.checkBox_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_40.addWidget(self.checkBox_7, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.execution)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_3.setIcon(icon10)

        self.gridLayout_40.addWidget(self.pushButton_3, 6, 2, 1, 2)

        self.btn_select_metrics = QPushButton(self.execution)
        self.btn_select_metrics.setObjectName(u"btn_select_metrics")
        sizePolicy.setHeightForWidth(self.btn_select_metrics.sizePolicy().hasHeightForWidth())
        self.btn_select_metrics.setSizePolicy(sizePolicy)
        self.btn_select_metrics.setMinimumSize(QSize(0, 30))
        self.btn_select_metrics.setMaximumSize(QSize(16777215, 30))
        self.btn_select_metrics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_metrics.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-equalizer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_metrics.setIcon(icon19)

        self.gridLayout_40.addWidget(self.btn_select_metrics, 4, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_40, 1, 1, 3, 5)

        self.label_40 = QLabel(self.execution)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 30))
        self.label_40.setMaximumSize(QSize(16777215, 30))
        self.label_40.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_11 = QLabel(self.execution)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.label_11, 0, 6, 1, 1)

        self.btn_remove_exe = QPushButton(self.execution)
        self.btn_remove_exe.setObjectName(u"btn_remove_exe")
        sizePolicy.setHeightForWidth(self.btn_remove_exe.sizePolicy().hasHeightForWidth())
        self.btn_remove_exe.setSizePolicy(sizePolicy)
        self.btn_remove_exe.setMinimumSize(QSize(150, 30))
        self.btn_remove_exe.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_exe.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_exe.setIcon(icon1)

        self.gridLayout_6.addWidget(self.btn_remove_exe, 3, 6, 1, 1)

        self.listWidget_6 = QListWidget(self.execution)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        QListWidgetItem(self.listWidget_6)
        self.listWidget_6.setObjectName(u"listWidget_6")
        sizePolicy.setHeightForWidth(self.listWidget_6.sizePolicy().hasHeightForWidth())
        self.listWidget_6.setSizePolicy(sizePolicy)
        self.listWidget_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.listWidget_6, 1, 0, 2, 1)

        self.listWidget_13 = QListWidget(self.execution)
        QListWidgetItem(self.listWidget_13)
        QListWidgetItem(self.listWidget_13)
        QListWidgetItem(self.listWidget_13)
        self.listWidget_13.setObjectName(u"listWidget_13")
        sizePolicy.setHeightForWidth(self.listWidget_13.sizePolicy().hasHeightForWidth())
        self.listWidget_13.setSizePolicy(sizePolicy)
        self.listWidget_13.setMinimumSize(QSize(0, 0))
        self.listWidget_13.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_6.addWidget(self.listWidget_13, 1, 6, 2, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_6)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_43.setHorizontalSpacing(50)
        self.gridLayout_43.setContentsMargins(0, -1, -1, -1)
        self.btn_go_monitoring = QPushButton(self.execution)
        self.btn_go_monitoring.setObjectName(u"btn_go_monitoring")
        sizePolicy.setHeightForWidth(self.btn_go_monitoring.sizePolicy().hasHeightForWidth())
        self.btn_go_monitoring.setSizePolicy(sizePolicy)
        self.btn_go_monitoring.setMinimumSize(QSize(200, 30))
        self.btn_go_monitoring.setMaximumSize(QSize(200, 30))
        self.btn_go_monitoring.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_go_monitoring.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.btn_go_monitoring.setIcon(icon4)

        self.gridLayout_43.addWidget(self.btn_go_monitoring, 0, 1, 1, 1, Qt.AlignRight)

        self.pushButton_6 = QPushButton(self.execution)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy5.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy5)
        self.pushButton_6.setMinimumSize(QSize(200, 30))
        self.pushButton_6.setMaximumSize(QSize(200, 30))
        self.pushButton_6.setStyleSheet(u"font: 11pt \"Ubuntu\";\n"
"background-color: rgb(52, 59, 72);")
        self.pushButton_6.setIcon(icon14)

        self.gridLayout_43.addWidget(self.pushButton_6, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_20.addLayout(self.gridLayout_43)

        self.stackedWidget.addWidget(self.execution)
        self.monitoring = QWidget()
        self.monitoring.setObjectName(u"monitoring")
        self.verticalLayout_10 = QVBoxLayout(self.monitoring)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(20)
        self.gridLayout_20.setVerticalSpacing(10)
        self.listWidget_14 = QListWidget(self.monitoring)
        self.listWidget_14.setObjectName(u"listWidget_14")
        self.listWidget_14.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_20.addWidget(self.listWidget_14, 5, 1, 1, 1)

        self.label_10 = QLabel(self.monitoring)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_8 = QLabel(self.monitoring)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_74 = QLabel(self.monitoring)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_74, 2, 1, 1, 1)

        self.listWidget_19 = QListWidget(self.monitoring)
        self.listWidget_19.setObjectName(u"listWidget_19")
        self.listWidget_19.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_20.addWidget(self.listWidget_19, 3, 1, 1, 1)

        self.label_7 = QLabel(self.monitoring)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_45 = QLabel(self.monitoring)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_45, 4, 1, 1, 1)

        self.textEdit_23 = QTextEdit(self.monitoring)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_20.addWidget(self.textEdit_23, 1, 0, 3, 1)

        self.label_73 = QLabel(self.monitoring)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_20.addWidget(self.label_73, 0, 1, 1, 1)

        self.listWidget_9 = QListWidget(self.monitoring)
        self.listWidget_9.setObjectName(u"listWidget_9")
        self.listWidget_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_20.addWidget(self.listWidget_9, 5, 0, 1, 1)

        self.listWidget_16 = QListWidget(self.monitoring)
        self.listWidget_16.setObjectName(u"listWidget_16")
        self.listWidget_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_20.addWidget(self.listWidget_16, 1, 1, 1, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setSpacing(20)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.btn_run_scenario = QPushButton(self.monitoring)
        self.btn_run_scenario.setObjectName(u"btn_run_scenario")
        sizePolicy5.setHeightForWidth(self.btn_run_scenario.sizePolicy().hasHeightForWidth())
        self.btn_run_scenario.setSizePolicy(sizePolicy5)
        self.btn_run_scenario.setMinimumSize(QSize(200, 30))
        self.btn_run_scenario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_run_scenario.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.btn_run_scenario.setIcon(icon16)

        self.gridLayout_44.addWidget(self.btn_run_scenario, 3, 1, 1, 1)

        self.label_87 = QLabel(self.monitoring)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_44.addWidget(self.label_87, 4, 1, 1, 1)

        self.btn_create_report = QPushButton(self.monitoring)
        self.btn_create_report.setObjectName(u"btn_create_report")
        sizePolicy5.setHeightForWidth(self.btn_create_report.sizePolicy().hasHeightForWidth())
        self.btn_create_report.setSizePolicy(sizePolicy5)
        self.btn_create_report.setMinimumSize(QSize(200, 50))
        self.btn_create_report.setFont(font)
        self.btn_create_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_report.setStyleSheet(u"background-color: black;\n"
"color:white;")
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/cil-task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_report.setIcon(icon20)

        self.gridLayout_44.addWidget(self.btn_create_report, 5, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_44.addItem(self.verticalSpacer_5, 8, 1, 1, 1)

        self.listWidget_12 = QListWidget(self.monitoring)
        QListWidgetItem(self.listWidget_12)
        QListWidgetItem(self.listWidget_12)
        QListWidgetItem(self.listWidget_12)
        QListWidgetItem(self.listWidget_12)
        QListWidgetItem(self.listWidget_12)
        self.listWidget_12.setObjectName(u"listWidget_12")
        sizePolicy.setHeightForWidth(self.listWidget_12.sizePolicy().hasHeightForWidth())
        self.listWidget_12.setSizePolicy(sizePolicy)
        self.listWidget_12.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_44.addWidget(self.listWidget_12, 2, 0, 7, 1)

        self.btn_select_scenario = QPushButton(self.monitoring)
        self.btn_select_scenario.setObjectName(u"btn_select_scenario")
        sizePolicy5.setHeightForWidth(self.btn_select_scenario.sizePolicy().hasHeightForWidth())
        self.btn_select_scenario.setSizePolicy(sizePolicy5)
        self.btn_select_scenario.setMinimumSize(QSize(200, 30))
        self.btn_select_scenario.setFont(font)
        self.btn_select_scenario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_scenario.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_scenario.setIcon(icon5)

        self.gridLayout_44.addWidget(self.btn_select_scenario, 2, 1, 1, 1)

        self.label_77 = QLabel(self.monitoring)
        self.label_77.setObjectName(u"label_77")
        sizePolicy1.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy1)

        self.gridLayout_44.addWidget(self.label_77, 7, 1, 1, 1)

        self.label_47 = QLabel(self.monitoring)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setPixmap(QPixmap(u"images/images/graphic.png"))
        self.label_47.setScaledContents(True)

        self.gridLayout_44.addWidget(self.label_47, 0, 0, 1, 2)

        self.label_3 = QLabel(self.monitoring)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_44.addWidget(self.label_3, 1, 0, 1, 2)

        self.btn_new_one = QPushButton(self.monitoring)
        self.btn_new_one.setObjectName(u"btn_new_one")
        sizePolicy5.setHeightForWidth(self.btn_new_one.sizePolicy().hasHeightForWidth())
        self.btn_new_one.setSizePolicy(sizePolicy5)
        self.btn_new_one.setMinimumSize(QSize(200, 50))
        self.btn_new_one.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_one.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon21 = QIcon()
        icon21.addFile(u":/icons/images/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_one.setIcon(icon21)

        self.gridLayout_44.addWidget(self.btn_new_one, 6, 1, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_44, 1, 2, 5, 1)


        self.gridLayout_9.addLayout(self.gridLayout_20, 0, 0, 7, 5)


        self.verticalLayout_10.addLayout(self.gridLayout_9)

        self.stackedWidget.addWidget(self.monitoring)
        self.sWorkload = QWidget()
        self.sWorkload.setObjectName(u"sWorkload")
        self.verticalLayout_51 = QVBoxLayout(self.sWorkload)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(20)
        self.gridLayout_12.setVerticalSpacing(10)
        self.textEdit_20 = QTextEdit(self.sWorkload)
        self.textEdit_20.setObjectName(u"textEdit_20")
        sizePolicy5.setHeightForWidth(self.textEdit_20.sizePolicy().hasHeightForWidth())
        self.textEdit_20.setSizePolicy(sizePolicy5)
        self.textEdit_20.setMaximumSize(QSize(50, 30))
        self.textEdit_20.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.textEdit_20.setReadOnly(True)

        self.gridLayout_12.addWidget(self.textEdit_20, 3, 2, 1, 1)

        self.btn_workload_save = QPushButton(self.sWorkload)
        self.btn_workload_save.setObjectName(u"btn_workload_save")
        sizePolicy5.setHeightForWidth(self.btn_workload_save.sizePolicy().hasHeightForWidth())
        self.btn_workload_save.setSizePolicy(sizePolicy5)
        self.btn_workload_save.setMinimumSize(QSize(120, 30))
        self.btn_workload_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_workload_save.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_workload_save.setIcon(icon10)

        self.gridLayout_12.addWidget(self.btn_workload_save, 3, 3, 1, 1)

        self.textEdit_8 = QTextEdit(self.sWorkload)
        self.textEdit_8.setObjectName(u"textEdit_8")
        sizePolicy2.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy2)
        self.textEdit_8.setMaximumSize(QSize(16777215, 30))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")

        self.gridLayout_12.addWidget(self.textEdit_8, 3, 1, 1, 1)

        self.label_18 = QLabel(self.sWorkload)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)
        self.label_18.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_17 = QLabel(self.sWorkload)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)
        self.label_17.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_27 = QLabel(self.sWorkload)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_12.addWidget(self.label_27, 3, 4, 1, 1)

        self.btn_changeDir = QPushButton(self.sWorkload)
        self.btn_changeDir.setObjectName(u"btn_changeDir")
        sizePolicy5.setHeightForWidth(self.btn_changeDir.sizePolicy().hasHeightForWidth())
        self.btn_changeDir.setSizePolicy(sizePolicy5)
        self.btn_changeDir.setMinimumSize(QSize(120, 30))
        self.btn_changeDir.setMaximumSize(QSize(16777215, 30))
        self.btn_changeDir.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon22 = QIcon()
        icon22.addFile(u":/icons/images/icons/cil-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_changeDir.setIcon(icon22)

        self.gridLayout_12.addWidget(self.btn_changeDir, 0, 4, 1, 1)

        self.textEdit_12 = QTextEdit(self.sWorkload)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_12.addWidget(self.textEdit_12, 1, 0, 2, 5)

        self.textEdit_21 = QTextEdit(self.sWorkload)
        self.textEdit_21.setObjectName(u"textEdit_21")
        sizePolicy2.setHeightForWidth(self.textEdit_21.sizePolicy().hasHeightForWidth())
        self.textEdit_21.setSizePolicy(sizePolicy2)
        self.textEdit_21.setMaximumSize(QSize(16777215, 30))
        self.textEdit_21.setFont(font)
        self.textEdit_21.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.textEdit_21.setReadOnly(True)

        self.gridLayout_12.addWidget(self.textEdit_21, 0, 1, 1, 3)


        self.verticalLayout_51.addLayout(self.gridLayout_12)

        self.btn_back_start2 = QPushButton(self.sWorkload)
        self.btn_back_start2.setObjectName(u"btn_back_start2")
        sizePolicy5.setHeightForWidth(self.btn_back_start2.sizePolicy().hasHeightForWidth())
        self.btn_back_start2.setSizePolicy(sizePolicy5)
        self.btn_back_start2.setMinimumSize(QSize(200, 30))
        self.btn_back_start2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_start2.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.btn_back_start2.setIcon(icon14)

        self.verticalLayout_51.addWidget(self.btn_back_start2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.sWorkload)
        self.selectMetrics = QWidget()
        self.selectMetrics.setObjectName(u"selectMetrics")
        self.selectMetrics.setMinimumSize(QSize(200, 300))
        self.verticalLayout_52 = QVBoxLayout(self.selectMetrics)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(20)
        self.gridLayout_14.setVerticalSpacing(10)
        self.label_37 = QLabel(self.selectMetrics)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)
        self.label_37.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.label_37, 0, 1, 1, 1)

        self.textEdit_9 = QTextEdit(self.selectMetrics)
        self.textEdit_9.setObjectName(u"textEdit_9")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy7)
        self.textEdit_9.setMinimumSize(QSize(500, 0))
        self.textEdit_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_14.addWidget(self.textEdit_9, 5, 0, 1, 2, Qt.AlignHCenter)

        self.label_25 = QLabel(self.selectMetrics)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.label_25, 0, 0, 1, 1)

        self.btn_metric_list = QPushButton(self.selectMetrics)
        self.btn_metric_list.setObjectName(u"btn_metric_list")
        sizePolicy5.setHeightForWidth(self.btn_metric_list.sizePolicy().hasHeightForWidth())
        self.btn_metric_list.setSizePolicy(sizePolicy5)
        self.btn_metric_list.setMinimumSize(QSize(120, 30))
        self.btn_metric_list.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_metric_list.setIcon(icon12)

        self.gridLayout_14.addWidget(self.btn_metric_list, 3, 0, 1, 1, Qt.AlignHCenter)

        self.saveMetrics = QPushButton(self.selectMetrics)
        self.saveMetrics.setObjectName(u"saveMetrics")
        sizePolicy5.setHeightForWidth(self.saveMetrics.sizePolicy().hasHeightForWidth())
        self.saveMetrics.setSizePolicy(sizePolicy5)
        self.saveMetrics.setMinimumSize(QSize(120, 30))
        self.saveMetrics.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveMetrics.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.saveMetrics.setIcon(icon10)

        self.gridLayout_14.addWidget(self.saveMetrics, 3, 1, 1, 1, Qt.AlignHCenter)

        self.label_35 = QLabel(self.selectMetrics)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_14.addWidget(self.label_35, 4, 0, 1, 2, Qt.AlignHCenter)

        self.listWidget_18 = QListWidget(self.selectMetrics)
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(True)
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_18)
        __qlistwidgetitem7.setFont(font8);
        __qlistwidgetitem7.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_18)
        __qlistwidgetitem8.setFont(font8);
        __qlistwidgetitem8.setFlags(Qt.NoItemFlags);
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        QListWidgetItem(self.listWidget_18)
        self.listWidget_18.setObjectName(u"listWidget_18")
        sizePolicy.setHeightForWidth(self.listWidget_18.sizePolicy().hasHeightForWidth())
        self.listWidget_18.setSizePolicy(sizePolicy)
        self.listWidget_18.setMaximumSize(QSize(500, 16777215))
        self.listWidget_18.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_14.addWidget(self.listWidget_18, 1, 0, 2, 1)

        self.listWidget_15 = QListWidget(self.selectMetrics)
        self.listWidget_15.setObjectName(u"listWidget_15")
        sizePolicy7.setHeightForWidth(self.listWidget_15.sizePolicy().hasHeightForWidth())
        self.listWidget_15.setSizePolicy(sizePolicy7)
        self.listWidget_15.setMinimumSize(QSize(400, 200))
        self.listWidget_15.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_14.addWidget(self.listWidget_15, 1, 1, 2, 1)


        self.verticalLayout_52.addLayout(self.gridLayout_14)

        self.verticalSpacer_62 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_52.addItem(self.verticalSpacer_62)

        self.btn_back_exe = QPushButton(self.selectMetrics)
        self.btn_back_exe.setObjectName(u"btn_back_exe")
        sizePolicy5.setHeightForWidth(self.btn_back_exe.sizePolicy().hasHeightForWidth())
        self.btn_back_exe.setSizePolicy(sizePolicy5)
        self.btn_back_exe.setMinimumSize(QSize(200, 30))
        self.btn_back_exe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_exe.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.btn_back_exe.setIcon(icon14)

        self.verticalLayout_52.addWidget(self.btn_back_exe, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.selectMetrics)
        self.customFault = QWidget()
        self.customFault.setObjectName(u"customFault")
        self.verticalLayout_19 = QVBoxLayout(self.customFault)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(6)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(6)
        self.btn_create_fault = QPushButton(self.customFault)
        self.btn_create_fault.setObjectName(u"btn_create_fault")
        self.btn_create_fault.setMinimumSize(QSize(0, 30))
        self.btn_create_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_fault.setIcon(icon9)

        self.gridLayout_3.addWidget(self.btn_create_fault, 0, 0, 1, 1)

        self.btn_delete_fault = QPushButton(self.customFault)
        self.btn_delete_fault.setObjectName(u"btn_delete_fault")
        self.btn_delete_fault.setMinimumSize(QSize(0, 30))
        self.btn_delete_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_delete_fault.setIcon(icon6)

        self.gridLayout_3.addWidget(self.btn_delete_fault, 0, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_3, 5, 1, 2, 7)

        self.label_67 = QLabel(self.customFault)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_16.addWidget(self.label_67, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_4, 7, 1, 1, 7)

        self.textEdit_10 = QTextEdit(self.customFault)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy4.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy4)
        self.textEdit_10.setMinimumSize(QSize(0, 0))
        self.textEdit_10.setMaximumSize(QSize(16777215, 30))
        self.textEdit_10.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_10, 8, 2, 1, 1)

        self.label_66 = QLabel(self.customFault)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_16.addWidget(self.label_66, 2, 1, 1, 1)

        self.btn_back_fi = QPushButton(self.customFault)
        self.btn_back_fi.setObjectName(u"btn_back_fi")
        sizePolicy2.setHeightForWidth(self.btn_back_fi.sizePolicy().hasHeightForWidth())
        self.btn_back_fi.setSizePolicy(sizePolicy2)
        self.btn_back_fi.setMinimumSize(QSize(200, 30))
        self.btn_back_fi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_fi.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.btn_back_fi.setIcon(icon14)

        self.gridLayout_16.addWidget(self.btn_back_fi, 8, 8, 1, 1)

        self.textEdit_31 = QTextEdit(self.customFault)
        self.textEdit_31.setObjectName(u"textEdit_31")
        self.textEdit_31.setMaximumSize(QSize(16777215, 30))
        self.textEdit_31.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_31, 3, 2, 1, 6)

        self.textEdit_30 = QTextEdit(self.customFault)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setMaximumSize(QSize(16777215, 30))
        self.textEdit_30.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_30, 2, 2, 1, 6)

        self.label_69 = QLabel(self.customFault)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_65 = QLabel(self.customFault)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_16.addWidget(self.label_65, 1, 1, 1, 1)

        self.textEdit_32 = QTextEdit(self.customFault)
        self.textEdit_32.setObjectName(u"textEdit_32")
        self.textEdit_32.setMaximumSize(QSize(16777215, 30))
        self.textEdit_32.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_32, 4, 2, 1, 6)

        self.label_62 = QLabel(self.customFault)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_62, 0, 1, 1, 7)

        self.label_68 = QLabel(self.customFault)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_16.addWidget(self.label_68, 4, 1, 1, 1)

        self.textEdit_33 = QTextEdit(self.customFault)
        self.textEdit_33.setObjectName(u"textEdit_33")
        self.textEdit_33.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_33, 1, 0, 8, 1)

        self.textEdit_11 = QTextEdit(self.customFault)
        self.textEdit_11.setObjectName(u"textEdit_11")
        sizePolicy2.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy2)
        self.textEdit_11.setMaximumSize(QSize(16777215, 30))
        self.textEdit_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.textEdit_11, 1, 2, 1, 6)

        self.label_61 = QLabel(self.customFault)
        self.label_61.setObjectName(u"label_61")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy8)

        self.gridLayout_16.addWidget(self.label_61, 8, 6, 1, 2)

        self.label_41 = QLabel(self.customFault)
        self.label_41.setObjectName(u"label_41")
        sizePolicy5.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy5)
        self.label_41.setMaximumSize(QSize(100, 30))

        self.gridLayout_16.addWidget(self.label_41, 8, 1, 1, 1)

        self.btn_save_fault = QPushButton(self.customFault)
        self.btn_save_fault.setObjectName(u"btn_save_fault")
        sizePolicy5.setHeightForWidth(self.btn_save_fault.sizePolicy().hasHeightForWidth())
        self.btn_save_fault.setSizePolicy(sizePolicy5)
        self.btn_save_fault.setMinimumSize(QSize(120, 30))
        self.btn_save_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_fault.setIcon(icon10)

        self.gridLayout_16.addWidget(self.btn_save_fault, 8, 4, 1, 2)

        self.label_43 = QLabel(self.customFault)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(40, 30))
        self.label_43.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_16.addWidget(self.label_43, 8, 3, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(10)
        self.listWidget_5 = QListWidget(self.customFault)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_8.addWidget(self.listWidget_5, 3, 0, 1, 1)

        self.textEdit_34 = QTextEdit(self.customFault)
        self.textEdit_34.setObjectName(u"textEdit_34")
        self.textEdit_34.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_8.addWidget(self.textEdit_34, 0, 0, 2, 1)

        self.label_71 = QLabel(self.customFault)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_8.addWidget(self.label_71, 2, 0, 1, 1)

        self.btn_remove_createdFault = QPushButton(self.customFault)
        self.btn_remove_createdFault.setObjectName(u"btn_remove_createdFault")
        self.btn_remove_createdFault.setMinimumSize(QSize(0, 30))
        self.btn_remove_createdFault.setMaximumSize(QSize(16777215, 30))
        self.btn_remove_createdFault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_createdFault.setIcon(icon13)

        self.gridLayout_8.addWidget(self.btn_remove_createdFault, 4, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_8, 1, 8, 7, 1)

        self.label_70 = QLabel(self.customFault)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_16.addWidget(self.label_70, 0, 8, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_16)

        self.stackedWidget.addWidget(self.customFault)
        self.cWorkload = QWidget()
        self.cWorkload.setObjectName(u"cWorkload")
        self.verticalLayout_18 = QVBoxLayout(self.cWorkload)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(20)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(6)
        self.label_32 = QLabel(self.cWorkload)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.cWorkload)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_5.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.btn_take_tasks = QPushButton(self.cWorkload)
        self.btn_take_tasks.setObjectName(u"btn_take_tasks")
        sizePolicy5.setHeightForWidth(self.btn_take_tasks.sizePolicy().hasHeightForWidth())
        self.btn_take_tasks.setSizePolicy(sizePolicy5)
        self.btn_take_tasks.setMinimumSize(QSize(180, 30))
        self.btn_take_tasks.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon23 = QIcon()
        icon23.addFile(u":/icons/images/icons/cil-vertical-align-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_take_tasks.setIcon(icon23)

        self.gridLayout_5.addWidget(self.btn_take_tasks, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 0, 8, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_53 = QLabel(self.cWorkload)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_17.addWidget(self.label_53, 0, 0, 1, 1)

        self.textEdit_14 = QTextEdit(self.cWorkload)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_17.addWidget(self.textEdit_14, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_17, 4, 1, 4, 3)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(20)
        self.gridLayout_18.setVerticalSpacing(6)
        self.label_31 = QLabel(self.cWorkload)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.label_31, 0, 0, 1, 1)

        self.listWidget_21 = QListWidget(self.cWorkload)
        self.listWidget_21.setObjectName(u"listWidget_21")
        sizePolicy7.setHeightForWidth(self.listWidget_21.sizePolicy().hasHeightForWidth())
        self.listWidget_21.setSizePolicy(sizePolicy7)
        self.listWidget_21.setMinimumSize(QSize(0, 200))
        self.listWidget_21.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_18.addWidget(self.listWidget_21, 1, 0, 3, 1)

        self.btn_select_task = QPushButton(self.cWorkload)
        self.btn_select_task.setObjectName(u"btn_select_task")
        sizePolicy5.setHeightForWidth(self.btn_select_task.sizePolicy().hasHeightForWidth())
        self.btn_select_task.setSizePolicy(sizePolicy5)
        self.btn_select_task.setMinimumSize(QSize(180, 30))
        self.btn_select_task.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_task.setIcon(icon12)

        self.gridLayout_18.addWidget(self.btn_select_task, 4, 0, 3, 1, Qt.AlignHCenter)

        self.label_29 = QLabel(self.cWorkload)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.label_29, 0, 1, 1, 4)

        self.label = QLabel(self.cWorkload)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.label, 3, 1, 1, 5)

        self.btn_save_task = QPushButton(self.cWorkload)
        self.btn_save_task.setObjectName(u"btn_save_task")
        sizePolicy5.setHeightForWidth(self.btn_save_task.sizePolicy().hasHeightForWidth())
        self.btn_save_task.setSizePolicy(sizePolicy5)
        self.btn_save_task.setMinimumSize(QSize(120, 30))
        self.btn_save_task.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_task.setIcon(icon10)

        self.gridLayout_18.addWidget(self.btn_save_task, 5, 1, 1, 2)

        self.label_4 = QLabel(self.cWorkload)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_18.addWidget(self.label_4, 5, 3, 1, 2)

        self.btn_remove_task = QPushButton(self.cWorkload)
        self.btn_remove_task.setObjectName(u"btn_remove_task")
        sizePolicy5.setHeightForWidth(self.btn_remove_task.sizePolicy().hasHeightForWidth())
        self.btn_remove_task.setSizePolicy(sizePolicy5)
        self.btn_remove_task.setMinimumSize(QSize(120, 30))
        self.btn_remove_task.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_task.setIcon(icon13)

        self.gridLayout_18.addWidget(self.btn_remove_task, 5, 5, 1, 1)

        self.listWidget_22 = QListWidget(self.cWorkload)
        self.listWidget_22.setObjectName(u"listWidget_22")
        sizePolicy.setHeightForWidth(self.listWidget_22.sizePolicy().hasHeightForWidth())
        self.listWidget_22.setSizePolicy(sizePolicy)
        self.listWidget_22.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_18.addWidget(self.listWidget_22, 1, 1, 2, 5)

        self.textEdit_5 = QTextEdit(self.cWorkload)
        self.textEdit_5.setObjectName(u"textEdit_5")
        sizePolicy2.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy2)
        self.textEdit_5.setMinimumSize(QSize(0, 0))
        self.textEdit_5.setMaximumSize(QSize(16777215, 30))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_18.addWidget(self.textEdit_5, 4, 1, 1, 5)


        self.gridLayout_13.addLayout(self.gridLayout_18, 0, 1, 4, 3)


        self.verticalLayout_18.addLayout(self.gridLayout_13)

        self.btn_back_start = QPushButton(self.cWorkload)
        self.btn_back_start.setObjectName(u"btn_back_start")
        sizePolicy5.setHeightForWidth(self.btn_back_start.sizePolicy().hasHeightForWidth())
        self.btn_back_start.setSizePolicy(sizePolicy5)
        self.btn_back_start.setMinimumSize(QSize(200, 30))
        self.btn_back_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_start.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.btn_back_start.setIcon(icon14)

        self.verticalLayout_18.addWidget(self.btn_back_start, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.cWorkload)
        self.yaml_launch = QWidget()
        self.yaml_launch.setObjectName(u"yaml_launch")
        self.verticalLayout_31 = QVBoxLayout(self.yaml_launch)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setSpacing(20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setSpacing(20)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_78 = QLabel(self.yaml_launch)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_29.addWidget(self.label_78, 0, 0, 1, 2)

        self.textEdit_40 = QTextEdit(self.yaml_launch)
        self.textEdit_40.setObjectName(u"textEdit_40")
        self.textEdit_40.setMaximumSize(QSize(16777215, 30))
        self.textEdit_40.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_29.addWidget(self.textEdit_40, 2, 0, 1, 1)

        self.listWidget_25 = QListWidget(self.yaml_launch)
        self.listWidget_25.setObjectName(u"listWidget_25")
        self.listWidget_25.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_29.addWidget(self.listWidget_25, 1, 0, 1, 2)

        self.btn_save_yaml = QPushButton(self.yaml_launch)
        self.btn_save_yaml.setObjectName(u"btn_save_yaml")
        self.btn_save_yaml.setMinimumSize(QSize(150, 30))
        self.btn_save_yaml.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_yaml.setIcon(icon10)

        self.gridLayout_29.addWidget(self.btn_save_yaml, 2, 1, 2, 1)


        self.gridLayout_28.addLayout(self.gridLayout_29, 0, 4, 3, 2)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setSpacing(20)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_58 = QLabel(self.yaml_launch)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(16777215, 30))
        self.label_58.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_36.addWidget(self.label_58, 1, 0, 1, 2)

        self.btn_clear_yaml = QPushButton(self.yaml_launch)
        self.btn_clear_yaml.setObjectName(u"btn_clear_yaml")
        self.btn_clear_yaml.setMinimumSize(QSize(150, 30))
        self.btn_clear_yaml.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_yaml.setIcon(icon6)

        self.gridLayout_36.addWidget(self.btn_clear_yaml, 0, 1, 1, 1)

        self.textEdit_41 = QTextEdit(self.yaml_launch)
        self.textEdit_41.setObjectName(u"textEdit_41")
        self.textEdit_41.setMinimumSize(QSize(0, 30))
        self.textEdit_41.setMaximumSize(QSize(16777215, 30))
        self.textEdit_41.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_36.addWidget(self.textEdit_41, 4, 0, 1, 2)

        self.label_88 = QLabel(self.yaml_launch)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_36.addWidget(self.label_88, 3, 0, 1, 2)

        self.btn_open_yaml = QPushButton(self.yaml_launch)
        self.btn_open_yaml.setObjectName(u"btn_open_yaml")
        self.btn_open_yaml.setMinimumSize(QSize(150, 30))
        self.btn_open_yaml.setMaximumSize(QSize(16777215, 16777215))
        self.btn_open_yaml.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_open_yaml.setIcon(icon5)

        self.gridLayout_36.addWidget(self.btn_open_yaml, 0, 0, 1, 1)

        self.listWidget_24 = QListWidget(self.yaml_launch)
        self.listWidget_24.setObjectName(u"listWidget_24")
        self.listWidget_24.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_36.addWidget(self.listWidget_24, 2, 0, 1, 2)


        self.gridLayout_34.addLayout(self.gridLayout_36, 1, 0, 1, 2)

        self.label_80 = QLabel(self.yaml_launch)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(16777215, 30))
        self.label_80.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_34.addWidget(self.label_80, 0, 0, 1, 2)


        self.gridLayout_28.addLayout(self.gridLayout_34, 0, 0, 3, 2)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setSpacing(20)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.listWidget_23 = QListWidget(self.yaml_launch)
        self.listWidget_23.setObjectName(u"listWidget_23")
        self.listWidget_23.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_33.addWidget(self.listWidget_23, 4, 0, 1, 2)

        self.label_79 = QLabel(self.yaml_launch)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_33.addWidget(self.label_79, 0, 0, 1, 2)

        self.btn_remove_yaml = QPushButton(self.yaml_launch)
        self.btn_remove_yaml.setObjectName(u"btn_remove_yaml")
        self.btn_remove_yaml.setMinimumSize(QSize(0, 30))
        self.btn_remove_yaml.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_yaml.setIcon(icon13)

        self.gridLayout_33.addWidget(self.btn_remove_yaml, 6, 1, 1, 1)

        self.btn_yaml_fault = QPushButton(self.yaml_launch)
        self.btn_yaml_fault.setObjectName(u"btn_yaml_fault")
        self.btn_yaml_fault.setMinimumSize(QSize(0, 30))
        self.btn_yaml_fault.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_yaml_fault.setIcon(icon12)

        self.gridLayout_33.addWidget(self.btn_yaml_fault, 2, 0, 1, 2)

        self.listWidget_20 = QListWidget(self.yaml_launch)
        self.listWidget_20.setObjectName(u"listWidget_20")
        self.listWidget_20.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_33.addWidget(self.listWidget_20, 1, 0, 1, 2)

        self.btn_apply_yaml = QPushButton(self.yaml_launch)
        self.btn_apply_yaml.setObjectName(u"btn_apply_yaml")
        self.btn_apply_yaml.setMinimumSize(QSize(0, 30))
        self.btn_apply_yaml.setMaximumSize(QSize(16777215, 30))
        self.btn_apply_yaml.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_apply_yaml.setIcon(icon11)

        self.gridLayout_33.addWidget(self.btn_apply_yaml, 6, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.yaml_launch)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 13pt \"Ubuntu\";")

        self.gridLayout_33.addWidget(self.checkBox_10, 5, 0, 1, 2)

        self.label_86 = QLabel(self.yaml_launch)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_33.addWidget(self.label_86, 3, 0, 1, 2)


        self.gridLayout_28.addLayout(self.gridLayout_33, 0, 2, 3, 2)


        self.verticalLayout_31.addLayout(self.gridLayout_28)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setHorizontalSpacing(50)
        self.btn_go_start_2 = QPushButton(self.yaml_launch)
        self.btn_go_start_2.setObjectName(u"btn_go_start_2")
        self.btn_go_start_2.setMinimumSize(QSize(200, 30))
        self.btn_go_start_2.setMaximumSize(QSize(200, 30))
        self.btn_go_start_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_go_start_2.setIcon(icon14)

        self.gridLayout_37.addWidget(self.btn_go_start_2, 0, 0, 1, 1, Qt.AlignLeft)

        self.btn_go_exe_2 = QPushButton(self.yaml_launch)
        self.btn_go_exe_2.setObjectName(u"btn_go_exe_2")
        self.btn_go_exe_2.setMinimumSize(QSize(200, 30))
        self.btn_go_exe_2.setMaximumSize(QSize(200, 30))
        self.btn_go_exe_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_go_exe_2.setIcon(icon4)

        self.gridLayout_37.addWidget(self.btn_go_exe_2, 0, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_31.addLayout(self.gridLayout_37)

        self.stackedWidget.addWidget(self.yaml_launch)
        self.cSnippets = QWidget()
        self.cSnippets.setObjectName(u"cSnippets")
        self.verticalLayout_54 = QVBoxLayout(self.cSnippets)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(20)
        self.gridLayout_11.setVerticalSpacing(6)
        self.label_23 = QLabel(self.cSnippets)
        self.label_23.setObjectName(u"label_23")
        sizePolicy8.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy8)

        self.gridLayout_11.addWidget(self.label_23, 15, 7, 1, 2)

        self.label_13 = QLabel(self.cSnippets)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_13, 0, 5, 1, 2)

        self.btn_save_snip = QPushButton(self.cSnippets)
        self.btn_save_snip.setObjectName(u"btn_save_snip")
        sizePolicy.setHeightForWidth(self.btn_save_snip.sizePolicy().hasHeightForWidth())
        self.btn_save_snip.setSizePolicy(sizePolicy)
        self.btn_save_snip.setMinimumSize(QSize(0, 30))
        self.btn_save_snip.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        font9.setKerning(False)
        self.btn_save_snip.setFont(font9)
        self.btn_save_snip.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_snip.setIcon(icon10)

        self.gridLayout_11.addWidget(self.btn_save_snip, 15, 10, 1, 1)

        self.checkBox_6 = QCheckBox(self.cSnippets)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_11.addWidget(self.checkBox_6, 14, 7, 1, 4, Qt.AlignHCenter)

        self.textEdit_15 = QTextEdit(self.cSnippets)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setMinimumSize(QSize(400, 0))
        self.textEdit_15.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_15.setReadOnly(True)

        self.gridLayout_11.addWidget(self.textEdit_15, 1, 0, 17, 5)

        self.label_60 = QLabel(self.cSnippets)
        self.label_60.setObjectName(u"label_60")
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QSize(200, 30))
        self.label_60.setMaximumSize(QSize(16777215, 30))
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_60, 16, 7, 1, 4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(10)
        self.label_21 = QLabel(self.cSnippets)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 2)

        self.label_64 = QLabel(self.cSnippets)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_64, 4, 0, 1, 2)

        self.textEdit_28 = QTextEdit(self.cSnippets)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setMaximumSize(QSize(16777215, 30))
        self.textEdit_28.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.textEdit_28, 7, 0, 1, 2)

        self.btn_create_snip = QPushButton(self.cSnippets)
        self.btn_create_snip.setObjectName(u"btn_create_snip")
        sizePolicy.setHeightForWidth(self.btn_create_snip.sizePolicy().hasHeightForWidth())
        self.btn_create_snip.setSizePolicy(sizePolicy)
        self.btn_create_snip.setMinimumSize(QSize(200, 30))
        self.btn_create_snip.setMaximumSize(QSize(16777215, 30))
        self.btn_create_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_create_snip.setIcon(icon9)

        self.gridLayout_2.addWidget(self.btn_create_snip, 8, 0, 1, 1)

        self.label_19 = QLabel(self.cSnippets)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 2)

        self.btn_delete_snip = QPushButton(self.cSnippets)
        self.btn_delete_snip.setObjectName(u"btn_delete_snip")
        sizePolicy.setHeightForWidth(self.btn_delete_snip.sizePolicy().hasHeightForWidth())
        self.btn_delete_snip.setSizePolicy(sizePolicy)
        self.btn_delete_snip.setMinimumSize(QSize(200, 0))
        self.btn_delete_snip.setMaximumSize(QSize(16777215, 30))
        self.btn_delete_snip.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_delete_snip.setIcon(icon6)

        self.gridLayout_2.addWidget(self.btn_delete_snip, 8, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.cSnippets)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 30))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.textEdit_2, 1, 0, 1, 2)

        self.label_22 = QLabel(self.cSnippets)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_22, 6, 0, 1, 2)

        self.textEdit_27 = QTextEdit(self.cSnippets)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setMaximumSize(QSize(16777215, 30))
        self.textEdit_27.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.textEdit_27, 3, 0, 1, 2)

        self.textEdit_29 = QTextEdit(self.cSnippets)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setMaximumSize(QSize(16777215, 30))
        self.textEdit_29.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_2.addWidget(self.textEdit_29, 5, 0, 1, 2)


        self.gridLayout_11.addLayout(self.gridLayout_2, 1, 5, 4, 2)

        self.textEdit_16 = QTextEdit(self.cSnippets)
        self.textEdit_16.setObjectName(u"textEdit_16")
        sizePolicy2.setHeightForWidth(self.textEdit_16.sizePolicy().hasHeightForWidth())
        self.textEdit_16.setSizePolicy(sizePolicy2)
        self.textEdit_16.setMaximumSize(QSize(16777215, 30))
        self.textEdit_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout_11.addWidget(self.textEdit_16, 15, 9, 1, 1)

        self.label_63 = QLabel(self.cSnippets)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_63, 0, 0, 1, 5)

        self.label_14 = QLabel(self.cSnippets)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.label_14, 0, 7, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 5, 5, 13, 2)

        self.textEdit_25 = QTextEdit(self.cSnippets)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setMinimumSize(QSize(300, 0))
        self.textEdit_25.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.textEdit_25.setReadOnly(True)

        self.gridLayout_11.addWidget(self.textEdit_25, 1, 7, 13, 4)

        self.back_snip = QPushButton(self.cSnippets)
        self.back_snip.setObjectName(u"back_snip")
        sizePolicy2.setHeightForWidth(self.back_snip.sizePolicy().hasHeightForWidth())
        self.back_snip.setSizePolicy(sizePolicy2)
        self.back_snip.setMinimumSize(QSize(0, 30))
        self.back_snip.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_snip.setStyleSheet(u"background-color: black;\n"
"color:white;")
        self.back_snip.setIcon(icon14)

        self.gridLayout_11.addWidget(self.back_snip, 17, 7, 1, 4)


        self.verticalLayout_54.addLayout(self.gridLayout_11)

        self.stackedWidget.addWidget(self.cSnippets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy2.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy2)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy2.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy2)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy2.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy2)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setBold(False)
        font10.setItalic(False)
        self.creditsLabel.setFont(font10)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"IM-FIT", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Fault Injection Tool", None))
        self.label_46.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_fiplan.setText(QCoreApplication.translate("MainWindow", u"FI Plan", None))
        self.btn_execution.setText(QCoreApplication.translate("MainWindow", u"Execution", None))
        self.btn_monitoring.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"IM-FIT", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.home.setStyleSheet("")
        self.label_2.setText("")
        self.textEdit_35.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/images/icons/cil-magnifying-glass.png\" /><span style=\" font-weight:600;\"> Scan</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IM-FIT scans the source code according to selected workload and code snippets. The user can the place of workload on the source code with purple color. The blue color show the lines for applying to mutation testing.</p></body></html>", None))
        self.textEdit_36.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/images/icons/cil-terminal.png\" /><span style=\" font-weight:600;\"> Execute</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user selects the operating condition for the mutation process. If the user does not want to change anything, it can use deafult settings. After user completed the settings, it can start the execution process. This process runs the mutation codes.</p></body></html>", None))
        self.textEdit_37.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/images/icons/cil-check.png\" /><span style=\" font-weight:600;\"> Monitoring</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After the execution, the user can see the all results about the mutation process. User can see the faults, metrics, codes' AST diagram, mutation state graphic and rosbag scenarios. If the user wants to take a V&amp;V report, IM-FIT gives one V&amp;V report including all details.</p></body></html>", None))
        self.textEdit_38.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/images/icons/cil-data-transfer-down.png\" /><span style=\" font-weight:600;\"> Start</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IM-FIT needs the source code added by the user. User can upload its workload and if it wants to create a new one, it can do it. The user can select the code snippets for customizing the process.</p></body></html>", None))
        self.textEdit_39.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/images/icons/cil-clipboard.png\" /><span style=\" font-weight:600;\"> FI Plan</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user creates the fault injection plans to execution. All possible lines and all faults are shown to the user to select and create the plan. After completed the selection lines and faults, applies mutation for the lines from the source codes. After all, the user saves the &quot;FI Plan&quot; to u"
                        "se in execution.</p></body></html>", None))
        self.btn_go_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Source Codes Settings", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Python - ROS", None))
        self.btn_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Source Code", None))
        self.btn_clear_codes.setText(QCoreApplication.translate("MainWindow", u"Clear Source Codes", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Edit Codes", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Other F\u0130le Types", None))
        self.btn_prepare_plan.setText(QCoreApplication.translate("MainWindow", u"Prepare FI Plan", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Workload Settings", None))
        self.btn_select_workload.setText(QCoreApplication.translate("MainWindow", u"Open Workload", None))
        self.btn_create_workload.setText(QCoreApplication.translate("MainWindow", u"Create Workload", None))
        self.btn_save_workload.setText(QCoreApplication.translate("MainWindow", u"Save Workload", None))
        self.btn_clear_workload.setText(QCoreApplication.translate("MainWindow", u"Clear Workload", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Edit Workload", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Source Codes", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Specifications Of Selected Code Snippets:", None))
        self.btn_create_code.setText(QCoreApplication.translate("MainWindow", u"Create Code Snippets", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Workload", None))
        self.btn_add_custom.setText(QCoreApplication.translate("MainWindow", u"Add Custom Snippet", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Code Snippets List", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Selected Code Snippets:", None))
        self.btn_select_snippet.setText(QCoreApplication.translate("MainWindow", u"Select Snippet", None))

        __sortingEnabled = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_10.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"GENERAL SNIPPETS", None));
        ___qlistwidgetitem1 = self.listWidget_10.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"if", None));
        ___qlistwidgetitem2 = self.listWidget_10.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"elif", None));
        ___qlistwidgetitem3 = self.listWidget_10.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"else", None));
        ___qlistwidgetitem4 = self.listWidget_10.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"for", None));
        ___qlistwidgetitem5 = self.listWidget_10.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"while", None));
        ___qlistwidgetitem6 = self.listWidget_10.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"break", None));
        ___qlistwidgetitem7 = self.listWidget_10.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"continue", None));
        ___qlistwidgetitem8 = self.listWidget_10.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"pass", None));
        ___qlistwidgetitem9 = self.listWidget_10.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"return", None));
        ___qlistwidgetitem10 = self.listWidget_10.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"lambda function", None));
        ___qlistwidgetitem11 = self.listWidget_10.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"__init__", None));
        ___qlistwidgetitem12 = self.listWidget_10.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"__main__", None));
        ___qlistwidgetitem13 = self.listWidget_10.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"class", None));
        ___qlistwidgetitem14 = self.listWidget_10.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Try/Except", None));
        ___qlistwidgetitem15 = self.listWidget_10.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Try/Except/Else", None));
        ___qlistwidgetitem16 = self.listWidget_10.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Try/Except/Finally", None));
        ___qlistwidgetitem17 = self.listWidget_10.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Try/Except/Else/Finally", None));
        ___qlistwidgetitem18 = self.listWidget_10.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Shebang", None));
        ___qlistwidgetitem19 = self.listWidget_10.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ROS SNIPPETS", None));
        ___qlistwidgetitem20 = self.listWidget_10.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ROS Initializing Node", None));
        ___qlistwidgetitem21 = self.listWidget_10.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ROS Publishers", None));
        ___qlistwidgetitem22 = self.listWidget_10.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ROS Subscribers", None));
        ___qlistwidgetitem23 = self.listWidget_10.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ROS Time Values", None));
        ___qlistwidgetitem24 = self.listWidget_10.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"ROS Services", None));
        ___qlistwidgetitem25 = self.listWidget_10.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"ROS Parameters", None));
        ___qlistwidgetitem26 = self.listWidget_10.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ROS Logs", None));
        ___qlistwidgetitem27 = self.listWidget_10.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"CUSTOM SNIPPETS", None));
        self.listWidget_10.setSortingEnabled(__sortingEnabled)

        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Codes/Workload Ready", None))
        self.btn_remove_snip.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btn_go_scan.setText(QCoreApplication.translate("MainWindow", u"Scan Page", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Processes", None))
        self.topics_btn.setText(QCoreApplication.translate("MainWindow", u"Topics", None))
        self.params_btn.setText(QCoreApplication.translate("MainWindow", u"Params", None))
        self.services_btn.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.rosrun_btn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.open_ros_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Folder Tree", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Workload", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Ready To Scan", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Detected Parts", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Selected Code Snippets", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Source Codes", None))
        self.btn_scan2.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_go_fiplan.setText(QCoreApplication.translate("MainWindow", u"FI Plan Page", None))
        self.btn_back_code.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.btn_start_mutation.setText(QCoreApplication.translate("MainWindow", u"Start Mutation", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fault Settings", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Possible Lines", None))
        self.btn_random_fault.setText(QCoreApplication.translate("MainWindow", u"Use Random Fault", None))
        self.btn_create_custom.setText(QCoreApplication.translate("MainWindow", u"Create Custom Fault", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Selected Line & Fault", None))
        self.btn_remove_fault.setText(QCoreApplication.translate("MainWindow", u"Remove L\u0130ne Fault", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Mutation List", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selected Line", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Fault Information", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fault Library", None))

        __sortingEnabled1 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem28 = self.listWidget_3.item(0)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"OPERATORS", None));
        ___qlistwidgetitem29 = self.listWidget_3.item(1)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"(AOM) Arithmetic Operator Missing", None));
        ___qlistwidgetitem30 = self.listWidget_3.item(2)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"(AOW) Arithmetic Operator Wrong", None));
        ___qlistwidgetitem31 = self.listWidget_3.item(3)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"(AOE) Arithmetic Operator Extraneous", None));
        ___qlistwidgetitem32 = self.listWidget_3.item(4)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"(COM) Comparison Operator Missing", None));
        ___qlistwidgetitem33 = self.listWidget_3.item(5)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"(COW) Comparison Operator Wrong", None));
        ___qlistwidgetitem34 = self.listWidget_3.item(6)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"(COE) Comparison Operator Extraneous", None));
        ___qlistwidgetitem35 = self.listWidget_3.item(7)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"(AOM) Assignment Operator Missing", None));
        ___qlistwidgetitem36 = self.listWidget_3.item(8)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"(AOW) Assignment Operator Wrong", None));
        ___qlistwidgetitem37 = self.listWidget_3.item(9)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"(AOE) Assignment Operator Extraneous", None));
        ___qlistwidgetitem38 = self.listWidget_3.item(10)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"(LOM) Logical Operator Missing", None));
        ___qlistwidgetitem39 = self.listWidget_3.item(11)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"(LOW) Logical Operator Wrong", None));
        ___qlistwidgetitem40 = self.listWidget_3.item(12)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"(LOE) Logical Operator Extraneous", None));
        ___qlistwidgetitem41 = self.listWidget_3.item(13)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"(MOM) Membership Operator Missing", None));
        ___qlistwidgetitem42 = self.listWidget_3.item(14)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"(MOW) Membership Operator Wrong", None));
        ___qlistwidgetitem43 = self.listWidget_3.item(15)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"(MOE) Membership Operator Extraneous", None));
        ___qlistwidgetitem44 = self.listWidget_3.item(16)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"(IOM) Identity Operator Missing", None));
        ___qlistwidgetitem45 = self.listWidget_3.item(17)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"(IOW) Identity  Operator Wrong", None));
        ___qlistwidgetitem46 = self.listWidget_3.item(18)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"(IOE) Identity Operator Extraneous", None));
        ___qlistwidgetitem47 = self.listWidget_3.item(19)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"STATEMENTS", None));
        ___qlistwidgetitem48 = self.listWidget_3.item(20)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"(bM) break Missing", None));
        ___qlistwidgetitem49 = self.listWidget_3.item(21)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"(bW) break Wrong", None));
        ___qlistwidgetitem50 = self.listWidget_3.item(22)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"(bE) break Extraneous", None));
        ___qlistwidgetitem51 = self.listWidget_3.item(23)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("MainWindow", u"(cM) continue Missing", None));
        ___qlistwidgetitem52 = self.listWidget_3.item(24)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("MainWindow", u"(cW) continue Wrong", None));
        ___qlistwidgetitem53 = self.listWidget_3.item(25)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("MainWindow", u"(cE) continue Extraneous", None));
        ___qlistwidgetitem54 = self.listWidget_3.item(26)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("MainWindow", u"(FM) False Missing", None));
        ___qlistwidgetitem55 = self.listWidget_3.item(27)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("MainWindow", u"(FW) False Wrong", None));
        ___qlistwidgetitem56 = self.listWidget_3.item(28)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("MainWindow", u"(FE) False Extraneous", None));
        ___qlistwidgetitem57 = self.listWidget_3.item(29)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("MainWindow", u"(pM) pass Missing", None));
        ___qlistwidgetitem58 = self.listWidget_3.item(30)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("MainWindow", u"(pW) pass Wrong", None));
        ___qlistwidgetitem59 = self.listWidget_3.item(31)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("MainWindow", u"(pE) pass Extraneous", None));
        ___qlistwidgetitem60 = self.listWidget_3.item(32)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("MainWindow", u"(TM) True Missing", None));
        ___qlistwidgetitem61 = self.listWidget_3.item(33)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("MainWindow", u"(TW) True Wrong", None));
        ___qlistwidgetitem62 = self.listWidget_3.item(34)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("MainWindow", u"(TE) True Extraneous", None));
        ___qlistwidgetitem63 = self.listWidget_3.item(35)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("MainWindow", u"ROS FAULTS", None));
        ___qlistwidgetitem64 = self.listWidget_3.item(36)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("MainWindow", u"ROS Initializing Node Mutation", None));
        ___qlistwidgetitem65 = self.listWidget_3.item(37)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("MainWindow", u"ROS Pub-Sub Mutation ", None));
        ___qlistwidgetitem66 = self.listWidget_3.item(38)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("MainWindow", u"ROS Time Mutation", None));
        ___qlistwidgetitem67 = self.listWidget_3.item(39)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("MainWindow", u"ROS Service Mutation", None));
        ___qlistwidgetitem68 = self.listWidget_3.item(40)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("MainWindow", u"ROS Parameter Mutation", None));
        ___qlistwidgetitem69 = self.listWidget_3.item(41)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("MainWindow", u"ROS Log Mutation", None));
        ___qlistwidgetitem70 = self.listWidget_3.item(42)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("MainWindow", u"CREATED FAULTS", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled1)

        self.btn_select_fault.setText(QCoreApplication.translate("MainWindow", u"Select Fault", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Apply Mutation for All Possible Line", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove Mutant Code Line", None))
        self.btn_slct_fiplan.setText(QCoreApplication.translate("MainWindow", u"Select FI Plan", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Total Mutants:", None))
#if QT_CONFIG(tooltip)
        self.btn_save_fiplan.setToolTip(QCoreApplication.translate("MainWindow", u"Save Button", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_fiplan.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"FI Plan Name:", None))
        self.btn_remove_fiplan.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"FI Plan List", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Scan Page", None))
        self.btn_go_exe.setText(QCoreApplication.translate("MainWindow", u"Execution Page", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Execution Settings", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Select FI Plan", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Memory Size(GB):", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"ROS Noetic", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"ROS Melodic", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"ROS Kinetic", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"ROS will not be used", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Python 3.9", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Python 3.8.5", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Python 2.8", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"Python 2.7", None))

        self.btn_new_exe.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Metrics:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Delete / Keep:", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ROS:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"OS:", None))
        self.btn_start_exe.setText(QCoreApplication.translate("MainWindow", u"Start Execution", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Selected FI Plan:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Use Default Settings", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Ubuntu 20.04", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Ubuntu 18.04", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Ubuntu 16.04", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"W\u0130ndows 10", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Windows 8.1", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Windows 8", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Default Settings:", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"16", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Python:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Time Limit:", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plan03</p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Gazebo:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Selected Metrics:", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Gazebo will be used", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Gazebo will not be used", None))

        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Execution03</p></body></html>", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Delete Mutants", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_select_metrics.setText(QCoreApplication.translate("MainWindow", u"Select Metrics", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"FI Plan List", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Execution Plan List", None))
        self.btn_remove_exe.setText(QCoreApplication.translate("MainWindow", u"Remove", None))

        __sortingEnabled2 = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        ___qlistwidgetitem71 = self.listWidget_6.item(0)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Plan01", None));
        ___qlistwidgetitem72 = self.listWidget_6.item(1)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Plan02", None));
        ___qlistwidgetitem73 = self.listWidget_6.item(2)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Plan03", None));
        ___qlistwidgetitem74 = self.listWidget_6.item(3)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Plan04", None));
        ___qlistwidgetitem75 = self.listWidget_6.item(4)
        ___qlistwidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Plan05", None));
        self.listWidget_6.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.listWidget_13.isSortingEnabled()
        self.listWidget_13.setSortingEnabled(False)
        ___qlistwidgetitem76 = self.listWidget_13.item(0)
        ___qlistwidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Execution01", None));
        ___qlistwidgetitem77 = self.listWidget_13.item(1)
        ___qlistwidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Execution02", None));
        ___qlistwidgetitem78 = self.listWidget_13.item(2)
        ___qlistwidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Execution03", None));
        self.listWidget_13.setSortingEnabled(__sortingEnabled3)

        self.btn_go_monitoring.setText(QCoreApplication.translate("MainWindow", u"Monitoring Page", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"FI Plan Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Mutation Score", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"AST Daigram", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Killed Mutants Output:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Metrics:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Faults:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Mutant Lists:", None))
        self.btn_run_scenario.setText(QCoreApplication.translate("MainWindow", u"Run The Scenario", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"V&V Report", None))
        self.btn_create_report.setText(QCoreApplication.translate("MainWindow", u"Create Report", None))

        __sortingEnabled4 = self.listWidget_12.isSortingEnabled()
        self.listWidget_12.setSortingEnabled(False)
        ___qlistwidgetitem79 = self.listWidget_12.item(0)
        ___qlistwidgetitem79.setText(QCoreApplication.translate("MainWindow", u"rosbag_record01.bag", None));
        ___qlistwidgetitem80 = self.listWidget_12.item(1)
        ___qlistwidgetitem80.setText(QCoreApplication.translate("MainWindow", u"rosbag_record02.bag", None));
        ___qlistwidgetitem81 = self.listWidget_12.item(2)
        ___qlistwidgetitem81.setText(QCoreApplication.translate("MainWindow", u"rosbag_rercord03.bag", None));
        ___qlistwidgetitem82 = self.listWidget_12.item(3)
        ___qlistwidgetitem82.setText(QCoreApplication.translate("MainWindow", u"rosbag_record04.bag", None));
        ___qlistwidgetitem83 = self.listWidget_12.item(4)
        ___qlistwidgetitem83.setText(QCoreApplication.translate("MainWindow", u"rosbag_record05.bag", None));
        self.listWidget_12.setSortingEnabled(__sortingEnabled4)

        self.btn_select_scenario.setText(QCoreApplication.translate("MainWindow", u"Select Scenario", None))
        self.label_77.setText("")
        self.label_47.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rosbag Scenarios", None))
        self.btn_new_one.setText(QCoreApplication.translate("MainWindow", u"Start To The New One", None))
        self.sWorkload.setStyleSheet("")
        self.textEdit_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">.json</p></body></html>", None))
        self.btn_workload_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"F\u0130le Name:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Look In:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"NOT SAVED!", None))
        self.btn_changeDir.setText(QCoreApplication.translate("MainWindow", u"Select Directory", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_back_start2.setText(QCoreApplication.translate("MainWindow", u"Back To Start Step", None))
        self.selectMetrics.setStyleSheet("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Select Metrics & States", None))
        self.btn_metric_list.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.saveMetrics.setText(QCoreApplication.translate("MainWindow", u"Save Metrics", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Information", None))

        __sortingEnabled5 = self.listWidget_18.isSortingEnabled()
        self.listWidget_18.setSortingEnabled(False)
        ___qlistwidgetitem84 = self.listWidget_18.item(0)
        ___qlistwidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Metrics", None));
        ___qlistwidgetitem85 = self.listWidget_18.item(1)
        ___qlistwidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Detected", None));
        ___qlistwidgetitem86 = self.listWidget_18.item(2)
        ___qlistwidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Undetected", None));
        ___qlistwidgetitem87 = self.listWidget_18.item(3)
        ___qlistwidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Covered", None));
        ___qlistwidgetitem88 = self.listWidget_18.item(4)
        ___qlistwidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Valid", None));
        ___qlistwidgetitem89 = self.listWidget_18.item(5)
        ___qlistwidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Total Mutants", None));
        ___qlistwidgetitem90 = self.listWidget_18.item(6)
        ___qlistwidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Mutant States", None));
        ___qlistwidgetitem91 = self.listWidget_18.item(7)
        ___qlistwidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Killed", None));
        ___qlistwidgetitem92 = self.listWidget_18.item(8)
        ___qlistwidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Survived", None));
        ___qlistwidgetitem93 = self.listWidget_18.item(9)
        ___qlistwidgetitem93.setText(QCoreApplication.translate("MainWindow", u"No Coverage", None));
        ___qlistwidgetitem94 = self.listWidget_18.item(10)
        ___qlistwidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Timeout", None));
        ___qlistwidgetitem95 = self.listWidget_18.item(11)
        ___qlistwidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Runtime Error", None));
        ___qlistwidgetitem96 = self.listWidget_18.item(12)
        ___qlistwidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Compile Error", None));
        ___qlistwidgetitem97 = self.listWidget_18.item(13)
        ___qlistwidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Ignored", None));
        self.listWidget_18.setSortingEnabled(__sortingEnabled5)

        self.btn_back_exe.setText(QCoreApplication.translate("MainWindow", u"Back To Execution Step", None))
        self.customFault.setStyleSheet("")
        self.btn_create_fault.setText(QCoreApplication.translate("MainWindow", u"Create Fault", None))
        self.btn_delete_fault.setText(QCoreApplication.translate("MainWindow", u"Delete Fault", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Changed:", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Target to Change:", None))
        self.btn_back_fi.setText(QCoreApplication.translate("MainWindow", u"Back To FI Plan Page", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Fault Example", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Fault Name:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Create Custom Fault", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Explanation:", None))
        self.textEdit_33.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">&quot;fault&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">:{</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">            </span><span style"
                        "=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">&quot;Fault_Name&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">: </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;(AOW) Arithmetic Operator Wrong&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">&quot;Target_to_Change&quot;</span><span "
                        "style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">: </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;\\\\+,\\\\-,\\\\*,\\\\/,[%]{1},[**]{2},[\\//]{2}&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">&quot;Changed&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">:</span><span style=\""
                        " font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;+,-,*,/,%,**,//&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">            </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">&quot;Explanation&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">:</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;Arithmetic Operators Wrong\\nOriginal Code: x + y\\nMu"
                        "tated Code: x - y&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">            }</span></p></body></html>", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:130.769%;\"><br /></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"NOT SAVED!", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.btn_save_fault.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u".json", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Created Fault List", None))
        self.btn_remove_createdFault.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Created Fault", None))
        self.cWorkload.setStyleSheet("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Codes:", None))
        self.plainTextEdit.setPlainText("")
        self.btn_take_tasks.setText(QCoreApplication.translate("MainWindow", u"Take Task IDs", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Task Details", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"All Tasks:", None))
        self.btn_select_task.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Selected Tasks:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WP Name:", None))
        self.btn_save_task.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"NOT SAVED!", None))
        self.btn_remove_task.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_back_start.setText(QCoreApplication.translate("MainWindow", u"Back To Start Step", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Mutation Applied Lines", None))
        self.btn_save_yaml.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"File Content", None))
        self.btn_clear_yaml.setText(QCoreApplication.translate("MainWindow", u"Clear All Contents", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Selected Line", None))
        self.btn_open_yaml.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"File Settings", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Mutation Library", None))
        self.btn_remove_yaml.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btn_yaml_fault.setText(QCoreApplication.translate("MainWindow", u"Select Fault", None))
        self.btn_apply_yaml.setText(QCoreApplication.translate("MainWindow", u"Apply Mutation", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Apply Mutation for All Possiple Lines", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Selected Line & Fault List", None))
        self.btn_go_start_2.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.btn_go_exe_2.setText(QCoreApplication.translate("MainWindow", u"Execution Page", None))
        self.cSnippets.setStyleSheet("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Your Code Snippet", None))
        self.btn_save_snip.setText(QCoreApplication.translate("MainWindow", u"Save Code Snippet", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Use The Created Code Snippet", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">{</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">    &quot;Snippet_Name&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">: </span><span style"
                        "=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;if&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">    &quot;Title&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">:</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#ce9178;\">&quot;Python if Statement Syntax&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; color:#9cdcfe;\">    &quot;Process&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; color:#d4d4d4;\">:</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; color:#ce9178;\">&quot;if test expression:\\n\\tstatement(s)&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#9cdcfe;\">    &quot;Regex_Code&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">:</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback';"
                        " font-size:14px; color:#ce9178;\">&quot;if.*:&quot;</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace','Droid Sans Fallback'; font-size:14px; color:#d4d4d4;\">}</span></p></body></html>", None))
        self.label_60.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Process:", None))
        self.btn_create_snip.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Snippet Name:", None))
        self.btn_delete_snip.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Regex Code:", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Example Code Snippet", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Created Code Snipet", None))
        self.back_snip.setText(QCoreApplication.translate("MainWindow", u"Back To Code Snippets Step", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Inovasyon Muhendislik", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

