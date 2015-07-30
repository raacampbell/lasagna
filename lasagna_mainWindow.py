# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designerFiles/lasagna_mainWindow.ui'
#
# Created: Thu Jul 30 17:34:08 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_lasagna_mainWindow(object):
    def setupUi(self, lasagna_mainWindow):
        lasagna_mainWindow.setObjectName(_fromUtf8("lasagna_mainWindow"))
        lasagna_mainWindow.resize(1002, 795)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lasagna_mainWindow.sizePolicy().hasHeightForWidth())
        lasagna_mainWindow.setSizePolicy(sizePolicy)
        lasagna_mainWindow.setMinimumSize(QtCore.QSize(540, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/lasagna_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        lasagna_mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(lasagna_mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView_3 = PlotWidget(self.centralwidget,viewBox=lasagna_viewBox())
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.gridLayout.addWidget(self.graphicsView_3, 1, 0, 1, 1)
        self.graphicsView_2 = PlotWidget(self.centralwidget,viewBox=lasagna_viewBox())
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_1 = PlotWidget(self.centralwidget,viewBox=lasagna_viewBox())
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_1.sizePolicy().hasHeightForWidth())
        self.graphicsView_1.setSizePolicy(sizePolicy)
        self.graphicsView_1.setObjectName(_fromUtf8("graphicsView_1"))
        self.gridLayout.addWidget(self.graphicsView_1, 0, 0, 1, 1)
        lasagna_mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(lasagna_mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen_recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_recent.setObjectName(_fromUtf8("menuOpen_recent"))
        self.menuLoad_ingredient = QtGui.QMenu(self.menuFile)
        self.menuLoad_ingredient.setObjectName(_fromUtf8("menuLoad_ingredient"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPlugins = QtGui.QMenu(self.menuBar)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        lasagna_mainWindow.setMenuBar(self.menuBar)
        self.mainDockWidget = QtGui.QDockWidget(lasagna_mainWindow)
        self.mainDockWidget.setMinimumSize(QtCore.QSize(250, 319))
        self.mainDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.mainDockWidget.setObjectName(_fromUtf8("mainDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.imageSettingsTab = QtGui.QWidget()
        self.imageSettingsTab.setObjectName(_fromUtf8("imageSettingsTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.imageSettingsTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.imageSettingsTab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.intensityHistogram = PlotWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intensityHistogram.sizePolicy().hasHeightForWidth())
        self.intensityHistogram.setSizePolicy(sizePolicy)
        self.intensityHistogram.setMaximumSize(QtCore.QSize(16777215, 180))
        self.intensityHistogram.setObjectName(_fromUtf8("intensityHistogram"))
        self.verticalLayout_3.addWidget(self.intensityHistogram)
        self.logYcheckBox = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logYcheckBox.sizePolicy().hasHeightForWidth())
        self.logYcheckBox.setSizePolicy(sizePolicy)
        self.logYcheckBox.setChecked(True)
        self.logYcheckBox.setObjectName(_fromUtf8("logYcheckBox"))
        self.verticalLayout_3.addWidget(self.logYcheckBox)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.imageSettingsTab, _fromUtf8(""))
        self.axisSetingsTab = QtGui.QWidget()
        self.axisSetingsTab.setObjectName(_fromUtf8("axisSetingsTab"))
        self.groupBoxAxisRatio = QtGui.QGroupBox(self.axisSetingsTab)
        self.groupBoxAxisRatio.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.groupBoxAxisRatio.setObjectName(_fromUtf8("groupBoxAxisRatio"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 110, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.axisRatioLabel_1 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_1.setSizePolicy(sizePolicy)
        self.axisRatioLabel_1.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axisRatioLabel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_1.setObjectName(_fromUtf8("axisRatioLabel_1"))
        self.horizontalLayout.addWidget(self.axisRatioLabel_1)
        self.axisRatioLineEdit_1 = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_1.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_1.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_1.setObjectName(_fromUtf8("axisRatioLineEdit_1"))
        self.horizontalLayout.addWidget(self.axisRatioLineEdit_1)
        self.layoutWidget1 = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 110, 22))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.axisRatioLabel_2 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_2.setSizePolicy(sizePolicy)
        self.axisRatioLabel_2.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_2.setObjectName(_fromUtf8("axisRatioLabel_2"))
        self.horizontalLayout_2.addWidget(self.axisRatioLabel_2)
        self.axisRatioLineEdit_2 = QtGui.QLineEdit(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_2.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_2.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_2.setObjectName(_fromUtf8("axisRatioLineEdit_2"))
        self.horizontalLayout_2.addWidget(self.axisRatioLineEdit_2)
        self.layoutWidget2 = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 70, 110, 22))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.axisRatioLabel_3 = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_3.setSizePolicy(sizePolicy)
        self.axisRatioLabel_3.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_3.setObjectName(_fromUtf8("axisRatioLabel_3"))
        self.horizontalLayout_3.addWidget(self.axisRatioLabel_3)
        self.axisRatioLineEdit_3 = QtGui.QLineEdit(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_3.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_3.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_3.setObjectName(_fromUtf8("axisRatioLineEdit_3"))
        self.horizontalLayout_3.addWidget(self.axisRatioLineEdit_3)
        self.groupBoxFlip = QtGui.QGroupBox(self.axisSetingsTab)
        self.groupBoxFlip.setEnabled(False)
        self.groupBoxFlip.setGeometry(QtCore.QRect(150, 10, 61, 121))
        self.groupBoxFlip.setToolTip(_fromUtf8(""))
        self.groupBoxFlip.setObjectName(_fromUtf8("groupBoxFlip"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBoxFlip)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 43, 83))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_FlipView1 = QtGui.QPushButton(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView1.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView1.setSizePolicy(sizePolicy)
        self.pushButton_FlipView1.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView1.setFont(font)
        self.pushButton_FlipView1.setCheckable(True)
        self.pushButton_FlipView1.setObjectName(_fromUtf8("pushButton_FlipView1"))
        self.verticalLayout.addWidget(self.pushButton_FlipView1)
        self.pushButton_FlipView2 = QtGui.QPushButton(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView2.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView2.setSizePolicy(sizePolicy)
        self.pushButton_FlipView2.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView2.setFont(font)
        self.pushButton_FlipView2.setObjectName(_fromUtf8("pushButton_FlipView2"))
        self.verticalLayout.addWidget(self.pushButton_FlipView2)
        self.pushButton_FlipView3 = QtGui.QPushButton(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView3.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView3.setSizePolicy(sizePolicy)
        self.pushButton_FlipView3.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView3.setFont(font)
        self.pushButton_FlipView3.setCheckable(True)
        self.pushButton_FlipView3.setObjectName(_fromUtf8("pushButton_FlipView3"))
        self.verticalLayout.addWidget(self.pushButton_FlipView3)
        self.tabWidget.addTab(self.axisSetingsTab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.mainDockWidget.setWidget(self.dockWidgetContents)
        lasagna_mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mainDockWidget)
        self.auxDockWidget = QtGui.QDockWidget(lasagna_mainWindow)
        self.auxDockWidget.setMinimumSize(QtCore.QSize(250, 150))
        self.auxDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.auxDockWidget.setObjectName(_fromUtf8("auxDockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.infoTextPanel = QtGui.QLabel(self.dockWidgetContents_2)
        self.infoTextPanel.setGeometry(QtCore.QRect(20, 10, 241, 131))
        self.infoTextPanel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.infoTextPanel.setFrameShadow(QtGui.QFrame.Raised)
        self.infoTextPanel.setText(_fromUtf8(""))
        self.infoTextPanel.setWordWrap(True)
        self.infoTextPanel.setObjectName(_fromUtf8("infoTextPanel"))
        self.auxDockWidget.setWidget(self.dockWidgetContents_2)
        lasagna_mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.auxDockWidget)
        self.toolBar = QtGui.QToolBar(lasagna_mainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        lasagna_mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(lasagna_mainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        lasagna_mainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(lasagna_mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAbout = QtGui.QAction(lasagna_mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(lasagna_mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.action_ARA_Explorer = QtGui.QAction(lasagna_mainWindow)
        self.action_ARA_Explorer.setCheckable(True)
        self.action_ARA_Explorer.setObjectName(_fromUtf8("action_ARA_Explorer"))
        self.actionResetAxes = QtGui.QAction(lasagna_mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/edit-redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionResetAxes.setIcon(icon3)
        self.actionResetAxes.setObjectName(_fromUtf8("actionResetAxes"))
        self.actionLoadOverlay = QtGui.QAction(lasagna_mainWindow)
        self.actionLoadOverlay.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/overlay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadOverlay.setIcon(icon4)
        self.actionLoadOverlay.setShortcut(_fromUtf8(""))
        self.actionLoadOverlay.setObjectName(_fromUtf8("actionLoadOverlay"))
        self.actionRemoveOverlay = QtGui.QAction(lasagna_mainWindow)
        self.actionRemoveOverlay.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/removeoverlay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveOverlay.setIcon(icon5)
        self.actionRemoveOverlay.setObjectName(_fromUtf8("actionRemoveOverlay"))
        self.actionNone = QtGui.QAction(lasagna_mainWindow)
        self.actionNone.setObjectName(_fromUtf8("actionNone"))
        self.actionOpen_2 = QtGui.QAction(lasagna_mainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.menuLoad_ingredient.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuLoad_ingredient.menuAction())
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionResetAxes)
        self.toolBar.addAction(self.actionRemoveOverlay)
        self.toolBar.addSeparator()

        self.retranslateUi(lasagna_mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lasagna_mainWindow)

    def retranslateUi(self, lasagna_mainWindow):
        lasagna_mainWindow.setWindowTitle(_translate("lasagna_mainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("lasagna_mainWindow", "&File", None))
        self.menuOpen_recent.setTitle(_translate("lasagna_mainWindow", "&Open recent", None))
        self.menuLoad_ingredient.setTitle(_translate("lasagna_mainWindow", "&Load ingredient", None))
        self.menuHelp.setTitle(_translate("lasagna_mainWindow", "Help", None))
        self.menuPlugins.setTitle(_translate("lasagna_mainWindow", "&Plugins", None))
        self.groupBox.setTitle(_translate("lasagna_mainWindow", "Intensity Histogram", None))
        self.logYcheckBox.setText(_translate("lasagna_mainWindow", "Log Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageSettingsTab), _translate("lasagna_mainWindow", "Image", None))
        self.groupBoxAxisRatio.setTitle(_translate("lasagna_mainWindow", "Axis ratios", None))
        self.axisRatioLabel_1.setText(_translate("lasagna_mainWindow", "View 1", None))
        self.axisRatioLineEdit_1.setText(_translate("lasagna_mainWindow", "1", None))
        self.axisRatioLabel_2.setText(_translate("lasagna_mainWindow", "View 2", None))
        self.axisRatioLineEdit_2.setText(_translate("lasagna_mainWindow", "2", None))
        self.axisRatioLabel_3.setText(_translate("lasagna_mainWindow", "View 3", None))
        self.axisRatioLineEdit_3.setText(_translate("lasagna_mainWindow", "0.5", None))
        self.groupBoxFlip.setTitle(_translate("lasagna_mainWindow", "Flip", None))
        self.pushButton_FlipView1.setText(_translate("lasagna_mainWindow", "View 1", None))
        self.pushButton_FlipView2.setText(_translate("lasagna_mainWindow", "View 2", None))
        self.pushButton_FlipView3.setText(_translate("lasagna_mainWindow", "View 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.axisSetingsTab), _translate("lasagna_mainWindow", "Axis", None))
        self.toolBar.setWindowTitle(_translate("lasagna_mainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("lasagna_mainWindow", "&New base stack", None))
        self.actionAbout.setText(_translate("lasagna_mainWindow", "About", None))
        self.actionQuit.setText(_translate("lasagna_mainWindow", "&Quit", None))
        self.action_ARA_Explorer.setText(_translate("lasagna_mainWindow", "&ARA Explorer", None))
        self.actionResetAxes.setText(_translate("lasagna_mainWindow", "resetAxes", None))
        self.actionResetAxes.setToolTip(_translate("lasagna_mainWindow", "reset axes", None))
        self.actionResetAxes.setShortcut(_translate("lasagna_mainWindow", "Ctrl+R", None))
        self.actionLoadOverlay.setText(_translate("lasagna_mainWindow", "&Load overlay", None))
        self.actionRemoveOverlay.setText(_translate("lasagna_mainWindow", "removeOverlay", None))
        self.actionRemoveOverlay.setToolTip(_translate("lasagna_mainWindow", "removeOverlay", None))
        self.actionNone.setText(_translate("lasagna_mainWindow", "none", None))
        self.actionOpen_2.setText(_translate("lasagna_mainWindow", "Open", None))

from pyqtgraph import PlotWidget
import mainWindow_rc
from lasagna_viewBox import lasagna_viewBox
