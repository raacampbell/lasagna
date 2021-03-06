# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designerFiles/lasagna_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lasagna_mainWindow(object):
    def setupUi(self, lasagna_mainWindow):
        lasagna_mainWindow.setObjectName("lasagna_mainWindow")
        lasagna_mainWindow.resize(1002, 795)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lasagna_mainWindow.sizePolicy().hasHeightForWidth())
        lasagna_mainWindow.setSizePolicy(sizePolicy)
        lasagna_mainWindow.setMinimumSize(QtCore.QSize(540, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lasagna_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        lasagna_mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(lasagna_mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.graphicsView_1 = LasagnaPlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_1.sizePolicy().hasHeightForWidth())
        self.graphicsView_1.setSizePolicy(sizePolicy)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.graphicsView_2 = LasagnaPlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.graphicsView_3 = LasagnaPlotWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.frame_2 = QtWidgets.QFrame(self.splitter_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        lasagna_mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(lasagna_mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_recent = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_recent.setObjectName("menuOpen_recent")
        self.menuLoad_ingredient = QtWidgets.QMenu(self.menuFile)
        self.menuLoad_ingredient.setObjectName("menuLoad_ingredient")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlugins = QtWidgets.QMenu(self.menuBar)
        self.menuPlugins.setObjectName("menuPlugins")
        lasagna_mainWindow.setMenuBar(self.menuBar)
        self.mainDockWidget = QtWidgets.QDockWidget(lasagna_mainWindow)
        self.mainDockWidget.setMinimumSize(QtCore.QSize(380, 613))
        self.mainDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.mainDockWidget.setObjectName("mainDockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.imageSettingsTab = QtWidgets.QWidget()
        self.imageSettingsTab.setObjectName("imageSettingsTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.imageSettingsTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.intensityHistogram = PlotWidget(self.imageSettingsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intensityHistogram.sizePolicy().hasHeightForWidth())
        self.intensityHistogram.setSizePolicy(sizePolicy)
        self.intensityHistogram.setMinimumSize(QtCore.QSize(0, 180))
        self.intensityHistogram.setMaximumSize(QtCore.QSize(16777215, 180))
        self.intensityHistogram.setObjectName("intensityHistogram")
        self.verticalLayout_3.addWidget(self.intensityHistogram)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.logYcheckBox = QtWidgets.QCheckBox(self.imageSettingsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logYcheckBox.sizePolicy().hasHeightForWidth())
        self.logYcheckBox.setSizePolicy(sizePolicy)
        self.logYcheckBox.setMaximumSize(QtCore.QSize(16777215, 21))
        self.logYcheckBox.setChecked(True)
        self.logYcheckBox.setObjectName("logYcheckBox")
        self.horizontalLayout_13.addWidget(self.logYcheckBox)
        self.imageAlpha_horizontalSlider = QtWidgets.QSlider(self.imageSettingsTab)
        self.imageAlpha_horizontalSlider.setMinimumSize(QtCore.QSize(221, 0))
        self.imageAlpha_horizontalSlider.setMaximum(100)
        self.imageAlpha_horizontalSlider.setProperty("value", 100)
        self.imageAlpha_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageAlpha_horizontalSlider.setInvertedAppearance(False)
        self.imageAlpha_horizontalSlider.setInvertedControls(False)
        self.imageAlpha_horizontalSlider.setObjectName("imageAlpha_horizontalSlider")
        self.horizontalLayout_13.addWidget(self.imageAlpha_horizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.imageStackLayers_TreeView = QtWidgets.QTreeView(self.imageSettingsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageStackLayers_TreeView.sizePolicy().hasHeightForWidth())
        self.imageStackLayers_TreeView.setSizePolicy(sizePolicy)
        self.imageStackLayers_TreeView.setMinimumSize(QtCore.QSize(0, 271))
        self.imageStackLayers_TreeView.setRootIsDecorated(False)
        self.imageStackLayers_TreeView.setObjectName("imageStackLayers_TreeView")
        self.verticalLayout_3.addWidget(self.imageStackLayers_TreeView)
        spacerItem = QtWidgets.QSpacerItem(20, 162, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.imageSettingsTab, "")
        self.pointsSettingsTab = QtWidgets.QWidget()
        self.pointsSettingsTab.setObjectName("pointsSettingsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pointsSettingsTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.points_TreeView = QtWidgets.QTreeView(self.pointsSettingsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_TreeView.sizePolicy().hasHeightForWidth())
        self.points_TreeView.setSizePolicy(sizePolicy)
        self.points_TreeView.setMinimumSize(QtCore.QSize(0, 281))
        self.points_TreeView.setMaximumSize(QtCore.QSize(16777215, 330))
        self.points_TreeView.setObjectName("points_TreeView")
        self.verticalLayout_5.addWidget(self.points_TreeView)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBoxAxisRatio_2 = QtWidgets.QGroupBox(self.pointsSettingsTab)
        self.groupBoxAxisRatio_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAxisRatio_2.sizePolicy().hasHeightForWidth())
        self.groupBoxAxisRatio_2.setSizePolicy(sizePolicy)
        self.groupBoxAxisRatio_2.setMinimumSize(QtCore.QSize(131, 131))
        self.groupBoxAxisRatio_2.setMaximumSize(QtCore.QSize(131, 16777215))
        self.groupBoxAxisRatio_2.setObjectName("groupBoxAxisRatio_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 30, 106, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.axisRatioLabel_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_4.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_4.setSizePolicy(sizePolicy)
        self.axisRatioLabel_4.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_4.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axisRatioLabel_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_4.setObjectName("axisRatioLabel_4")
        self.horizontalLayout_5.addWidget(self.axisRatioLabel_4)
        self.view1Z_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view1Z_spinBox.sizePolicy().hasHeightForWidth())
        self.view1Z_spinBox.setSizePolicy(sizePolicy)
        self.view1Z_spinBox.setMinimum(1)
        self.view1Z_spinBox.setMaximum(99)
        self.view1Z_spinBox.setObjectName("view1Z_spinBox")
        self.horizontalLayout_5.addWidget(self.view1Z_spinBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 60, 106, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.axisRatioLabel_5 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_5.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_5.setSizePolicy(sizePolicy)
        self.axisRatioLabel_5.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_5.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_5.setObjectName("axisRatioLabel_5")
        self.horizontalLayout_6.addWidget(self.axisRatioLabel_5)
        self.view2Z_spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.view2Z_spinBox.setMinimum(1)
        self.view2Z_spinBox.setObjectName("view2Z_spinBox")
        self.horizontalLayout_6.addWidget(self.view2Z_spinBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 90, 106, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.axisRatioLabel_6 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_6.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_6.setSizePolicy(sizePolicy)
        self.axisRatioLabel_6.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_6.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_6.setObjectName("axisRatioLabel_6")
        self.horizontalLayout_7.addWidget(self.axisRatioLabel_6)
        self.view3Z_spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.view3Z_spinBox.setMinimum(1)
        self.view3Z_spinBox.setObjectName("view3Z_spinBox")
        self.horizontalLayout_7.addWidget(self.view3Z_spinBox)
        self.horizontalLayout_10.addWidget(self.groupBoxAxisRatio_2)
        self.frame = QtWidgets.QFrame(self.pointsSettingsTab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelMarker = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker.sizePolicy().hasHeightForWidth())
        self.labelMarker.setSizePolicy(sizePolicy)
        self.labelMarker.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker.setObjectName("labelMarker")
        self.horizontalLayout_4.addWidget(self.labelMarker)
        self.markerSymbol_comboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerSymbol_comboBox.sizePolicy().hasHeightForWidth())
        self.markerSymbol_comboBox.setSizePolicy(sizePolicy)
        self.markerSymbol_comboBox.setMaximumSize(QtCore.QSize(85, 24))
        self.markerSymbol_comboBox.setObjectName("markerSymbol_comboBox")
        self.horizontalLayout_4.addWidget(self.markerSymbol_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelMarker_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_2.sizePolicy().hasHeightForWidth())
        self.labelMarker_2.setSizePolicy(sizePolicy)
        self.labelMarker_2.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_2.setObjectName("labelMarker_2")
        self.horizontalLayout_8.addWidget(self.labelMarker_2)
        self.markerSize_spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerSize_spinBox.sizePolicy().hasHeightForWidth())
        self.markerSize_spinBox.setSizePolicy(sizePolicy)
        self.markerSize_spinBox.setMinimum(1)
        self.markerSize_spinBox.setMaximum(99)
        self.markerSize_spinBox.setProperty("value", 1)
        self.markerSize_spinBox.setObjectName("markerSize_spinBox")
        self.horizontalLayout_8.addWidget(self.markerSize_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelMarker_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_3.sizePolicy().hasHeightForWidth())
        self.labelMarker_3.setSizePolicy(sizePolicy)
        self.labelMarker_3.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_3.setObjectName("labelMarker_3")
        self.horizontalLayout_9.addWidget(self.labelMarker_3)
        self.markerAlpha_spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerAlpha_spinBox.sizePolicy().hasHeightForWidth())
        self.markerAlpha_spinBox.setSizePolicy(sizePolicy)
        self.markerAlpha_spinBox.setMinimum(0)
        self.markerAlpha_spinBox.setMaximum(255)
        self.markerAlpha_spinBox.setProperty("value", 255)
        self.markerAlpha_spinBox.setObjectName("markerAlpha_spinBox")
        self.horizontalLayout_9.addWidget(self.markerAlpha_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelMarker_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_5.sizePolicy().hasHeightForWidth())
        self.labelMarker_5.setSizePolicy(sizePolicy)
        self.labelMarker_5.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_5.setObjectName("labelMarker_5")
        self.horizontalLayout_12.addWidget(self.labelMarker_5)
        self.lineWidth_spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineWidth_spinBox.sizePolicy().hasHeightForWidth())
        self.lineWidth_spinBox.setSizePolicy(sizePolicy)
        self.lineWidth_spinBox.setMinimum(1)
        self.lineWidth_spinBox.setMaximum(25)
        self.lineWidth_spinBox.setProperty("value", 2)
        self.lineWidth_spinBox.setObjectName("lineWidth_spinBox")
        self.horizontalLayout_12.addWidget(self.lineWidth_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.markerColor_pushButton = QtWidgets.QPushButton(self.frame)
        self.markerColor_pushButton.setObjectName("markerColor_pushButton")
        self.verticalLayout_4.addWidget(self.markerColor_pushButton)
        self.markerColor_pushButton.raise_()
        self.horizontalLayout_10.addWidget(self.frame)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 204, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.points_TreeView.raise_()
        self.tabWidget.addTab(self.pointsSettingsTab, "")
        self.axisSetingsTab = QtWidgets.QWidget()
        self.axisSetingsTab.setObjectName("axisSetingsTab")
        self.groupBoxAxisRatio = QtWidgets.QGroupBox(self.axisSetingsTab)
        self.groupBoxAxisRatio.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.groupBoxAxisRatio.setObjectName("groupBoxAxisRatio")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 114, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.axisRatioLabel_1 = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_1.setSizePolicy(sizePolicy)
        self.axisRatioLabel_1.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axisRatioLabel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_1.setObjectName("axisRatioLabel_1")
        self.horizontalLayout.addWidget(self.axisRatioLabel_1)
        self.axisRatioLineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_1.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_1.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_1.setObjectName("axisRatioLineEdit_1")
        self.horizontalLayout.addWidget(self.axisRatioLineEdit_1)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 50, 114, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.axisRatioLabel_2 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_2.setSizePolicy(sizePolicy)
        self.axisRatioLabel_2.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_2.setObjectName("axisRatioLabel_2")
        self.horizontalLayout_2.addWidget(self.axisRatioLabel_2)
        self.axisRatioLineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_2.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_2.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_2.setObjectName("axisRatioLineEdit_2")
        self.horizontalLayout_2.addWidget(self.axisRatioLineEdit_2)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 70, 114, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.axisRatioLabel_3 = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_3.setSizePolicy(sizePolicy)
        self.axisRatioLabel_3.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_3.setObjectName("axisRatioLabel_3")
        self.horizontalLayout_3.addWidget(self.axisRatioLabel_3)
        self.axisRatioLineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_3.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_3.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_3.setObjectName("axisRatioLineEdit_3")
        self.horizontalLayout_3.addWidget(self.axisRatioLineEdit_3)
        self.groupBoxFlip = QtWidgets.QGroupBox(self.axisSetingsTab)
        self.groupBoxFlip.setEnabled(True)
        self.groupBoxFlip.setGeometry(QtCore.QRect(150, 10, 81, 121))
        self.groupBoxFlip.setToolTip("")
        self.groupBoxFlip.setObjectName("groupBoxFlip")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBoxFlip)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 20, 43, 95))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_FlipView1 = QtWidgets.QPushButton(self.layoutWidget6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView1.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView1.setSizePolicy(sizePolicy)
        self.pushButton_FlipView1.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView1.setFont(font)
        self.pushButton_FlipView1.setCheckable(True)
        self.pushButton_FlipView1.setObjectName("pushButton_FlipView1")
        self.verticalLayout.addWidget(self.pushButton_FlipView1)
        self.pushButton_FlipView2 = QtWidgets.QPushButton(self.layoutWidget6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView2.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView2.setSizePolicy(sizePolicy)
        self.pushButton_FlipView2.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView2.setFont(font)
        self.pushButton_FlipView2.setCheckable(True)
        self.pushButton_FlipView2.setObjectName("pushButton_FlipView2")
        self.verticalLayout.addWidget(self.pushButton_FlipView2)
        self.pushButton_FlipView3 = QtWidgets.QPushButton(self.layoutWidget6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView3.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView3.setSizePolicy(sizePolicy)
        self.pushButton_FlipView3.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView3.setFont(font)
        self.pushButton_FlipView3.setCheckable(True)
        self.pushButton_FlipView3.setObjectName("pushButton_FlipView3")
        self.verticalLayout.addWidget(self.pushButton_FlipView3)
        self.tabWidget.addTab(self.axisSetingsTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.mainDockWidget.setWidget(self.dockWidgetContents)
        lasagna_mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mainDockWidget)
        self.toolBar = QtWidgets.QToolBar(lasagna_mainWindow)
        self.toolBar.setObjectName("toolBar")
        lasagna_mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(lasagna_mainWindow)
        self.statusBar.setObjectName("statusBar")
        lasagna_mainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(lasagna_mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/icons/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout = QtWidgets.QAction(lasagna_mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(lasagna_mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/icons/window-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.action_ARA_Explorer = QtWidgets.QAction(lasagna_mainWindow)
        self.action_ARA_Explorer.setCheckable(True)
        self.action_ARA_Explorer.setObjectName("action_ARA_Explorer")
        self.actionResetAxes = QtWidgets.QAction(lasagna_mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/icons/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionResetAxes.setIcon(icon3)
        self.actionResetAxes.setObjectName("actionResetAxes")
        self.actionLoadOverlay = QtWidgets.QAction(lasagna_mainWindow)
        self.actionLoadOverlay.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/icons/overlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadOverlay.setIcon(icon4)
        self.actionLoadOverlay.setShortcut("")
        self.actionLoadOverlay.setObjectName("actionLoadOverlay")
        self.actionRemoveOverlay = QtWidgets.QAction(lasagna_mainWindow)
        self.actionRemoveOverlay.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/icons/removeoverlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveOverlay.setIcon(icon5)
        self.actionRemoveOverlay.setObjectName("actionRemoveOverlay")
        self.actionNone = QtWidgets.QAction(lasagna_mainWindow)
        self.actionNone.setObjectName("actionNone")
        self.actionOpen_2 = QtWidgets.QAction(lasagna_mainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.menuLoad_ingredient.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuLoad_ingredient.menuAction())
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionResetAxes)
        self.toolBar.addSeparator()

        self.retranslateUi(lasagna_mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lasagna_mainWindow)

    def retranslateUi(self, lasagna_mainWindow):
        _translate = QtCore.QCoreApplication.translate
        lasagna_mainWindow.setWindowTitle(_translate("lasagna_mainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("lasagna_mainWindow", "&File"))
        self.menuOpen_recent.setTitle(_translate("lasagna_mainWindow", "&Open recent"))
        self.menuLoad_ingredient.setTitle(_translate("lasagna_mainWindow", "&Load ingredient"))
        self.menuHelp.setTitle(_translate("lasagna_mainWindow", "Help"))
        self.menuPlugins.setTitle(_translate("lasagna_mainWindow", "&Plugins"))
        self.logYcheckBox.setText(_translate("lasagna_mainWindow", "Log Y"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageSettingsTab), _translate("lasagna_mainWindow", "Image"))
        self.groupBoxAxisRatio_2.setTitle(_translate("lasagna_mainWindow", "z-spread"))
        self.axisRatioLabel_4.setText(_translate("lasagna_mainWindow", "View 1"))
        self.axisRatioLabel_5.setText(_translate("lasagna_mainWindow", "View 2"))
        self.axisRatioLabel_6.setText(_translate("lasagna_mainWindow", "View 3"))
        self.labelMarker.setText(_translate("lasagna_mainWindow", "Marker"))
        self.labelMarker_2.setText(_translate("lasagna_mainWindow", "Size"))
        self.labelMarker_3.setText(_translate("lasagna_mainWindow", "Alpha"))
        self.labelMarker_5.setText(_translate("lasagna_mainWindow", "Width"))
        self.markerColor_pushButton.setText(_translate("lasagna_mainWindow", "Color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsSettingsTab), _translate("lasagna_mainWindow", "Points"))
        self.groupBoxAxisRatio.setTitle(_translate("lasagna_mainWindow", "Axis ratios"))
        self.axisRatioLabel_1.setText(_translate("lasagna_mainWindow", "View 1"))
        self.axisRatioLineEdit_1.setText(_translate("lasagna_mainWindow", "1"))
        self.axisRatioLabel_2.setText(_translate("lasagna_mainWindow", "View 2"))
        self.axisRatioLineEdit_2.setText(_translate("lasagna_mainWindow", "2"))
        self.axisRatioLabel_3.setText(_translate("lasagna_mainWindow", "View 3"))
        self.axisRatioLineEdit_3.setText(_translate("lasagna_mainWindow", "0.5"))
        self.groupBoxFlip.setTitle(_translate("lasagna_mainWindow", "Flip Stacks"))
        self.pushButton_FlipView1.setText(_translate("lasagna_mainWindow", "View 1"))
        self.pushButton_FlipView2.setText(_translate("lasagna_mainWindow", "View 2"))
        self.pushButton_FlipView3.setText(_translate("lasagna_mainWindow", "View 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.axisSetingsTab), _translate("lasagna_mainWindow", "Axis"))
        self.toolBar.setWindowTitle(_translate("lasagna_mainWindow", "toolBar"))
        self.actionOpen.setText(_translate("lasagna_mainWindow", "&New image stack"))
        self.actionOpen.setToolTip(_translate("lasagna_mainWindow", "New image stack"))
        self.actionAbout.setText(_translate("lasagna_mainWindow", "About"))
        self.actionQuit.setText(_translate("lasagna_mainWindow", "&Quit"))
        self.action_ARA_Explorer.setText(_translate("lasagna_mainWindow", "&ARA Explorer"))
        self.actionResetAxes.setText(_translate("lasagna_mainWindow", "resetAxes"))
        self.actionResetAxes.setToolTip(_translate("lasagna_mainWindow", "reset axes"))
        self.actionResetAxes.setShortcut(_translate("lasagna_mainWindow", "Ctrl+R"))
        self.actionLoadOverlay.setText(_translate("lasagna_mainWindow", "&Load overlay"))
        self.actionRemoveOverlay.setText(_translate("lasagna_mainWindow", "removeOverlay"))
        self.actionRemoveOverlay.setToolTip(_translate("lasagna_mainWindow", "removeOverlay"))
        self.actionNone.setText(_translate("lasagna_mainWindow", "none"))
        self.actionOpen_2.setText(_translate("lasagna_mainWindow", "Open"))


from lasagna.lasagnaplotwidget import LasagnaPlotWidget
from pyqtgraph import PlotWidget
import mainWindow_rc
