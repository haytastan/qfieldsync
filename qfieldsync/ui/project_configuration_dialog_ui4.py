# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/project_configuration_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from qgis.PyQt import QtCore, QtGui

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

class Ui_QFieldProjectConfigurationBase(object):
    def setupUi(self, QFieldProjectConfigurationBase):
        QFieldProjectConfigurationBase.setObjectName(_fromUtf8("QFieldProjectConfigurationBase"))
        QFieldProjectConfigurationBase.resize(608, 510)
        self.gridLayout = QtGui.QGridLayout(QFieldProjectConfigurationBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(QFieldProjectConfigurationBase)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.layersTable = QtGui.QTableWidget(self.groupBox)
        self.layersTable.setObjectName(_fromUtf8("layersTable"))
        self.layersTable.setColumnCount(2)
        self.layersTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.layersTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.layersTable.setHorizontalHeaderItem(1, item)
        self.layersTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.layersTable, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QFieldProjectConfigurationBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(QFieldProjectConfigurationBase)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.createBaseMapGroupBox = QtGui.QGroupBox(self.tab)
        self.createBaseMapGroupBox.setCheckable(True)
        self.createBaseMapGroupBox.setChecked(False)
        self.createBaseMapGroupBox.setObjectName(_fromUtf8("createBaseMapGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.createBaseMapGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.mapThemeRadioButton = QtGui.QRadioButton(self.createBaseMapGroupBox)
        self.mapThemeRadioButton.setObjectName(_fromUtf8("mapThemeRadioButton"))
        self.buttonGroup = QtGui.QButtonGroup(QFieldProjectConfigurationBase)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.mapThemeRadioButton)
        self.gridLayout_3.addWidget(self.mapThemeRadioButton, 0, 1, 1, 1)
        self.baseMapTypeStack = QtGui.QStackedWidget(self.createBaseMapGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseMapTypeStack.sizePolicy().hasHeightForWidth())
        self.baseMapTypeStack.setSizePolicy(sizePolicy)
        self.baseMapTypeStack.setObjectName(_fromUtf8("baseMapTypeStack"))
        self.mapThemePage = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapThemePage.sizePolicy().hasHeightForWidth())
        self.mapThemePage.setSizePolicy(sizePolicy)
        self.mapThemePage.setObjectName(_fromUtf8("mapThemePage"))
        self.formLayout_2 = QtGui.QFormLayout(self.mapThemePage)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.mapThemePage)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.mapThemeComboBox = QtGui.QComboBox(self.mapThemePage)
        self.mapThemeComboBox.setObjectName(_fromUtf8("mapThemeComboBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.mapThemeComboBox)
        self.baseMapTypeStack.addWidget(self.mapThemePage)
        self.singleLayerPage = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleLayerPage.sizePolicy().hasHeightForWidth())
        self.singleLayerPage.setSizePolicy(sizePolicy)
        self.singleLayerPage.setObjectName(_fromUtf8("singleLayerPage"))
        self.formLayout = QtGui.QFormLayout(self.singleLayerPage)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.singleLayerPage)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.layerComboBox = QgsMapLayerComboBox(self.singleLayerPage)
        self.layerComboBox.setObjectName(_fromUtf8("layerComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.layerComboBox)
        self.baseMapTypeStack.addWidget(self.singleLayerPage)
        self.gridLayout_3.addWidget(self.baseMapTypeStack, 2, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.createBaseMapGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.tileSize = QtGui.QLineEdit(self.createBaseMapGroupBox)
        self.tileSize.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tileSize.setObjectName(_fromUtf8("tileSize"))
        self.gridLayout_3.addWidget(self.tileSize, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.createBaseMapGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)
        self.mapUnitsPerPixel = QtGui.QLineEdit(self.createBaseMapGroupBox)
        self.mapUnitsPerPixel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.mapUnitsPerPixel.setObjectName(_fromUtf8("mapUnitsPerPixel"))
        self.gridLayout_3.addWidget(self.mapUnitsPerPixel, 5, 1, 1, 1)
        self.singleLayerRadioButton = QtGui.QRadioButton(self.createBaseMapGroupBox)
        self.singleLayerRadioButton.setObjectName(_fromUtf8("singleLayerRadioButton"))
        self.buttonGroup.addButton(self.singleLayerRadioButton)
        self.gridLayout_3.addWidget(self.singleLayerRadioButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.createBaseMapGroupBox, 0, 0, 1, 1)
        self.singleLayerRadioButton.raise_()
        self.createBaseMapGroupBox.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.onlyOfflineCopyFeaturesInAoi = QtGui.QCheckBox(self.tab_2)
        self.onlyOfflineCopyFeaturesInAoi.setObjectName(_fromUtf8("onlyOfflineCopyFeaturesInAoi"))
        self.gridLayout_5.addWidget(self.onlyOfflineCopyFeaturesInAoi, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(QFieldProjectConfigurationBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QFieldProjectConfigurationBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QFieldProjectConfigurationBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QFieldProjectConfigurationBase)

    def retranslateUi(self, QFieldProjectConfigurationBase):
        QFieldProjectConfigurationBase.setWindowTitle(_translate("QFieldProjectConfigurationBase", "Configure Project for QField synchronisation", None))
        self.groupBox.setTitle(_translate("QFieldProjectConfigurationBase", "Layers", None))
        item = self.layersTable.horizontalHeaderItem(0)
        item.setText(_translate("QFieldProjectConfigurationBase", "Layer", None))
        item = self.layersTable.horizontalHeaderItem(1)
        item.setText(_translate("QFieldProjectConfigurationBase", "Action", None))
        self.createBaseMapGroupBox.setToolTip(_translate("QFieldProjectConfigurationBase", "A base map is fully rendered to a raster image. Attributes from layers on a base map are no longer accessible.", None))
        self.createBaseMapGroupBox.setTitle(_translate("QFieldProjectConfigurationBase", "Create base map", None))
        self.mapThemeRadioButton.setText(_translate("QFieldProjectConfigurationBase", "Map Theme", None))
        self.label.setText(_translate("QFieldProjectConfigurationBase", "Map Theme", None))
        self.label_2.setText(_translate("QFieldProjectConfigurationBase", "Layer", None))
        self.label_3.setText(_translate("QFieldProjectConfigurationBase", "Tile Size", None))
        self.tileSize.setToolTip(_translate("QFieldProjectConfigurationBase", "Rendering will happen in tiles. This number determines the width and height (in pixels) that will be rendered per tile.", None))
        self.tileSize.setText(_translate("QFieldProjectConfigurationBase", "1024", None))
        self.label_4.setText(_translate("QFieldProjectConfigurationBase", "Map Units/Pixel", None))
        self.mapUnitsPerPixel.setToolTip(_translate("QFieldProjectConfigurationBase", "This determines the spatial resolution of the resulting map image. It depends on the CRS of the map canvas. For map units in [m], a value of 1 means each pixel covers an area of 1x1 m, a value of 1000 means 1 pixel per square kilometer.", None))
        self.mapUnitsPerPixel.setText(_translate("QFieldProjectConfigurationBase", "100", None))
        self.singleLayerRadioButton.setText(_translate("QFieldProjectConfigurationBase", "Single Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QFieldProjectConfigurationBase", "Base map", None))
        self.onlyOfflineCopyFeaturesInAoi.setText(_translate("QFieldProjectConfigurationBase", "Only copy features in area of interest", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QFieldProjectConfigurationBase", "Offline editing", None))

from qgis.gui import QgsMapLayerComboBox
