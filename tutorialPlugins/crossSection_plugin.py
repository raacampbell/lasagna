


"""
Creates a plugin that is composed of a new window with a pyqtgraph PlotWidget
On this graph we plot an x-axis cross-section of the image at the level which the 
mouse cursor is at. 
"""

from lasagna_plugin import lasagna_plugin
import cross_section_plot_UI
from PyQt4 import QtGui, QtCore
import sys


import lasagna_helperFunctions            # A potentially temporary module that houses general-purpose helper functions

class plugin(lasagna_plugin, QtGui.QWidget, cross_section_plot_UI.Ui_xSection): #must inherit lasagna_plugin first

    def __init__(self,lasagna,parent=None):
        super(plugin,self).__init__(lasagna) #This calls the lasagna_plugin constructor which in turn calls subsequent constructors

        #re-define some default properties that were originally defined in lasagna_plugin
        self.pluginShortName='Cross Section' #Appears on the menu
        self.pluginLongName='displays cross section in a new window' #Can be used for other purposes (e.g. tool-tip)
        self.pluginAuthor='Rob Campbell'


        #Create widgets defined in the designer file
        self.setupUi(self)
        self.show()

        #Set up the close button by linking it to the same slot as the normal window close button
        self.closeButton.released.connect(self.closePlugin)




    #self.lasagna.updateMainWindowOnMouseMove is run each time the axes are updated. So we can hook into it 
    #to update this window also
    def hook_updateMainWindowOnMouseMove_End(self):
        X = self.lasagna.mouseX
        Y = self.lasagna.mouseY

        #Get the widget that the mouse is currently in 
        pos = QtGui.QCursor.pos()
        PlotWidget = QtGui.qApp.widgetAt(pos).parent()

        #TODO: AXIS we may change the way things are named
        ImageItem = lasagna_helperFunctions.findPyQtGraphObjectNameInPlotWidget(PlotWidget,itemName='baseImage',regex=True)

        if ImageItem != None:
            xData = ImageItem.image[:,Y,0]

            self.graphicsView.clear()
            self.graphicsView.plot(xData)


    #The following methods are involved in shutting down the plugin window
    def closePlugin(self):
        """
        This method is called by lasagna when the user unchecks the plugin in the menu.
        """
        self.detachHooks() 
        self.close()


    #We define this here because we can't assume all plugins will have QWidget::closeEvent
    def closeEvent(self, event):
        """
        This event is execute when the user presses the close window (cross) button in the title bar
        """
        self.lasagna.stopPlugin(self.__module__) #This will call self.closePlugin
        self.lasagna.pluginActions[self.__module__].setChecked(False) #Uncheck the menu item associated with this plugin's name
        self.deleteLater()
        event.accept()
