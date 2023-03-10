# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import configparser
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom

a = []

tree = ET.parse("C:/Users/dnjsc/Desktop/GP/Radar Project/Radar.xml")
root = tree.getroot()
child = list(root)
#child = root.getchildren()
for x in root:
    a.append(x.attrib)
class Ui_MainWindow(object):

    def meas_Radar(self):
        items = []
        data = ET.Element('data')
        w=0
        f=1
        b=[]
        d=[]
        d1=[]
    
        for r in range(self.listWidget_Radar_Right.count()):
            items.append(self.listWidget_Radar_Right.item(r).text())
   
       
        for c in items:
            
            for x in root.findall("./List[@name='" + c + "']"):
                                    
                    Function = ET.SubElement(data, 'Function')
                    Type = ET.SubElement(Function, 'Type ')
                    Algorithm  = ET.SubElement(Function, 'Algorithm  ')
                    Input = ET.SubElement(Function, 'Input  ')
                    Output = ET.SubElement(Function, 'Output  ')
                    Function.set('name', c)
                    
                    for q in x.findall("Type[@name]"):
                        d.append(q.attrib)
                        
                        Type.set('name',d[w]["name"])
                    for p in x.findall("Algorithm[@name]"):
                        b.append(p.attrib)
                        
                        Algorithm.set('name',b[w]["name"])
                    
                    if w==0:
                        Input.set('name', 'None')
                    else:
                        w = w-1
                        Input.set('name', b[w]["name"])
                        w= w+1
                    
                    
                    if f < len(items):
                       for h in root.findall("./List[@name='" + items[f] + "']"):
                            for v in h.findall("Algorithm[@name]"):
                                d1.append(v.attrib)
                                Output.set('name',d1[w]["name"])
                    else:
                        Output.set('name',"None")          
                                
                    w=w+1
                    f=f+1




        mydata = ET.tostring(data)
        myfile = open("Output_Radar.xml", "wb")
        myfile.write(mydata)



    def meas_Conti(self):
        items = []
        data = ET.Element('data')
        w=0
        f=1
        b=[]
        d=[]
        d1=[]
    
        for r in range(self.listWidget_Conti_Right.count()):
            items.append(self.listWidget_Conti_Right.item(r).text())
   
       
        for c in items:
            
            for x in root.findall("./List[@name='" + c + "']"):
                                    
                    Function = ET.SubElement(data, 'Function')
                    Type = ET.SubElement(Function, 'Type ')
                    Algorithm  = ET.SubElement(Function, 'Algorithm  ')
                    Input = ET.SubElement(Function, 'Input  ')
                    Output = ET.SubElement(Function, 'Output  ')
                    Function.set('name', c)
                    
                    for q in x.findall("Type[@name]"):
                        d.append(q.attrib)
                        
                        Type.set('name',d[w]["name"])
                    for p in x.findall("Algorithm[@name]"):
                        b.append(p.attrib)
                        
                        Algorithm.set('name',b[w]["name"])
                    
                    if w==0:
                        Input.set('name', 'None')
                    else:
                        w = w-1
                        Input.set('name', b[w]["name"])
                        w= w+1
                    
                    
                    if f < len(items):
                       for h in root.findall("./List[@name='" + items[f] + "']"):
                            for v in h.findall("Algorithm[@name]"):
                                d1.append(v.attrib)
                                Output.set('name',d1[w]["name"])
                    else:
                        Output.set('name',"None")          
                                
                    w=w+1
                    f=f+1




        mydata = ET.tostring(data)
        myfile = open("Output_Conti.xml", "wb")
        myfile.write(mydata)

    def open_xml_Radar(self):
 
        __sortingEnabled = self.listWidget_Radar_Left.isSortingEnabled()
        self.listWidget_Radar_Left.setSortingEnabled(False)
        for i in range(len(a)):
            item = self.listWidget_Radar_Left.item(i)
            item.setText(a[i]["name"])
        self.listWidget_Radar_Left.setSortingEnabled(__sortingEnabled)

    def open_xml_Conti(self):
 
        __sortingEnabled = self.listWidget_Conti_Left.isSortingEnabled()
        self.listWidget_Conti_Left.setSortingEnabled(False)
        for i in range(len(a)):
            item = self.listWidget_Conti_Left.item(i)
            item.setText(a[i]["name"])
        self.listWidget_Conti_Left.setSortingEnabled(__sortingEnabled)

    def add_Radar(self):

        listItems = self.listWidget_Radar_Left.selectedItems()
        for item in listItems:

            self.listWidget_Radar_Right.addItem(self.listWidget_Radar_Left.takeItem(self.listWidget_Radar_Left.row(item)))
            for i in range(len(a)):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_Radar_Left.addItem(item)
            for i in range(len(a)):
                item = self.listWidget_Radar_Left.item(i)
                item.setText(a[i]["name"])

    def remove_Radar(self):
        listItems = self.listWidget_Radar_Right.selectedItems()
        for item in listItems:
            self.listWidget_Radar_Right.takeItem(self.listWidget_Radar_Right.row(item))

#########for conti########
    def add_Conti(self):

        listItems = self.listWidget_Conti_Left.selectedItems()
        for item in listItems:

            self.listWidget_Conti_Right.addItem(self.listWidget_Conti_Left.takeItem(self.listWidget_Conti_Left.row(item)))
            for i in range(len(a)):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_Conti_Left.addItem(item)
            for i in range(len(a)):
                item = self.listWidget_Conti_Left.item(i)
                item.setText(a[i]["name"])

    def remove_Conti(self):
        listItems = self.listWidget_Conti_Right.selectedItems()
        for item in listItems:
            self.listWidget_Conti_Right.takeItem(self.listWidget_Conti_Right.row(item))
        

        




        
    def open_dialog_box_Radar(self):
        filename = QFileDialog.getOpenFileName()
        path=filename[0]        
        file_config = path
        self.label_4_Radar.setText(self.load_config(file_config))
        

        with open(path,"r") as f:
            print(f.read())
            
    def open_dialog_box_Conti(self):
        filename = QFileDialog.getOpenFileName()
        path=filename[0]        
        file_config = path
        
        self.label_4_Conti.setText(self.load_config(file_config))

        with open(path,"r") as f:
            print(f.read())

    def load_config(self,file_config):
        global C, plottype, animationpath, colormap_vc, file, file_mean, file_simu, file_simu_saved, file_saved
        global NFFT_x, NFFT_y, NFFT_y, NFFT_v, velocity_channel, POS_TH_Value_Pos, POS_TH_Value_Vel, POS_TH_BT_Value
        global nrframes_init, nrframes_end, nrframes_end_complete, GeneratePositionGraph_Simulation, \
            GenerateVelocityGraph_Simulation, Generate_HD5_Matrix, Generate_Gif_Animation, AreaAnalysis, \
            Diogo_Analysis, Apply_backgroundreduction, Apply_normalization, Apply_gaussfilter, Apply_theshold, \
            Apply_oscfar, Apply_oscfar_inAnimation, GenerateWebcamVideo, GenerateVelocitygraph, \
            GeneratePositionGraph, Apply_Distance_threshold, Apply_dbV2W

        

        config = configparser.ConfigParser()
        config.sections()
        config.read(file_config)

        C = config['DEFAULT']['C']
        plottype = config['DEFAULT']['plottype']
        animationpath = config['DEFAULT']['animationpath']
        colormap_vc = config['DEFAULT']['colormap_vc']

        file = config['DATABASE']['file']
        file_mean = config['DATABASE']['file_mean']
        file_simu = config['DATABASE']['file_simu']
        file_simu_saved = config['DATABASE']['file_simu_saved']
        file_saved = config['DATABASE']['file_saved']

        NFFT_x = int(config['CALCULATION']['NFFT_x'])
        NFFT_y = int(config['CALCULATION']['NFFT_y'])
        NFFT_v = int(config['CALCULATION']['NFFT_v'])
        velocity_channel = int(config['CALCULATION']['velocity_channel'])
        POS_TH_Value_Pos = int(config['CALCULATION']['POS_TH_Value_Pos'])
        POS_TH_Value_Vel = int(config['CALCULATION']['POS_TH_Value_Vel'])
        POS_TH_BT_Value = int(config['CALCULATION']['POS_TH_BT_Value'])

        nrframes_init = int(config['EXECUTION']['nrframes_init'])
        nrframes_end = int(config['EXECUTION']['nrframes_end'])
        nrframes_end_complete = config['EXECUTION'].getboolean('nrframes_end_complete')
        GeneratePositionGraph_Simulation = config['EXECUTION'].getboolean('GeneratePositionGraph_Simulation')
        GenerateVelocityGraph_Simulation = config['EXECUTION'].getboolean('GenerateVelocityGraph_Simulation')
        Generate_HD5_Matrix = config['EXECUTION'].getboolean('Generate_HD5_Matrix')
        Generate_Gif_Animation = config['EXECUTION'].getboolean('Generate_Gif_Animation')
        AreaAnalysis = config['EXECUTION'].getboolean('AreaAnalysis')
        Diogo_Analysis = config['EXECUTION'].getboolean('Diogo_Analysis')
        Apply_backgroundreduction = config['EXECUTION'].getboolean('Apply_backgroundreduction')
        Apply_normalization = config['EXECUTION'].getboolean('Apply_normalization')
        Apply_gaussfilter = config['EXECUTION'].getboolean('Apply_gaussfilter')
        Apply_theshold = config['EXECUTION'].getboolean('Apply_theshold')
        Apply_Distance_threshold = config['EXECUTION'].getboolean('Apply_Distance_threshold')
        Apply_oscfar = config['EXECUTION'].getboolean('Apply_oscfar')
        Apply_dbV2W = config['EXECUTION'].getboolean('Apply_dbV2W')
        Apply_oscfar_inAnimation = config['EXECUTION'].getboolean('Apply_oscfar_inAnimation')
        GeneratePositionGraph = config['EXECUTION'].getboolean('GeneratePositionGraph')
        GenerateVelocitygraph = config['EXECUTION'].getboolean('GenerateVelocitygraph')
        GenerateWebcamVideo = config['EXECUTION'].getboolean('GenerateWebcamVideo')

        list=[str("NFFT_x = " + str(NFFT_x)),str("NFFT_y = " + str(NFFT_y)),str("NFFT_v = " + str(NFFT_v)),
                   "(velocity_channel = " + str(velocity_channel),"POS_TH_Value_Pos = " + str(POS_TH_Value_Pos),"POS_TH_Value_Vel = " + str(POS_TH_Value_Vel),
              "POS_TH_BT_Value = " + str(POS_TH_BT_Value)]
        join="\n".join(list)
        return join
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 981, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.listView = QtWidgets.QListView(self.Home)
        self.listView.setGeometry(QtCore.QRect(0, 0, 971, 531))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(300, 170, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Home, "")
        self.RadarLog = QtWidgets.QWidget()
        self.RadarLog.setObjectName("RadarLog")
        self.listView_2 = QtWidgets.QListView(self.RadarLog)
        self.listView_2.setGeometry(QtCore.QRect(0, 0, 971, 531))
        self.listView_2.setStyleSheet("")
        self.listView_2.setObjectName("listView_2")
        self.btn_Load_Config_Radar = QtWidgets.QPushButton(self.RadarLog)
        self.btn_Load_Config_Radar.setGeometry(QtCore.QRect(70, 110, 131, 41))
        self.btn_Load_Config_Radar.setObjectName("btn_Load_Config_Radar")


        self.btn_Load_Config_Radar.clicked.connect(self.open_dialog_box_Radar)

        
        self.btn_Load_xml_Radar = QtWidgets.QPushButton(self.RadarLog)
        self.btn_Load_xml_Radar.setGeometry(QtCore.QRect(550, 60, 131, 41))
        self.btn_Load_xml_Radar.setObjectName("btn_Load_xml_Radar")

        #self.btn_Load_xml_Radar.clicked.connect(self.open_xml_Radar)
        
        self.scrollArea = QtWidgets.QScrollArea(self.RadarLog)
        self.scrollArea.setGeometry(QtCore.QRect(30, 200, 211, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 220, 400))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_4_Radar = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4_Radar.setGeometry(QtCore.QRect(20, 10, 300, 101))
        
        
        
        self.label_4_Radar.setObjectName("label_4_Radar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.listWidget_Radar_Left = QtWidgets.QListWidget(self.RadarLog)
        self.listWidget_Radar_Left.setGeometry(QtCore.QRect(340, 180, 221, 211))
        self.listWidget_Radar_Left.setObjectName("listWidget_Radar_Left")

        for i in range(len(a)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_Radar_Left.addItem(item)

            
        self.btn_Radar_Add = QtWidgets.QPushButton(self.RadarLog)
        self.btn_Radar_Add.setGeometry(QtCore.QRect(580, 230, 71, 31))
        self.btn_Radar_Add.setObjectName("btn_Radar_Add")


        
        self.btn_Radar_Delete = QtWidgets.QPushButton(self.RadarLog)
        self.btn_Radar_Delete.setGeometry(QtCore.QRect(580, 290, 71, 31))
        self.btn_Radar_Delete.setObjectName("btn_Radar_Delete")
        self.listWidget_Radar_Right = QtWidgets.QListWidget(self.RadarLog)
        self.listWidget_Radar_Right.setGeometry(QtCore.QRect(670, 180, 221, 211))
        self.listWidget_Radar_Right.setObjectName("listWidget_Radar_Right")
        self.btn_Start_Mesurement_Radar = QtWidgets.QPushButton(self.RadarLog)
        self.btn_Start_Mesurement_Radar.setGeometry(QtCore.QRect(400, 460, 171, 41))
        self.btn_Start_Mesurement_Radar.setObjectName("btn_Start_Mesurement_Radar")

        self.btn_Start_Mesurement_Radar.clicked.connect(self.meas_Radar)

        
        self.Console_Radar = QtWidgets.QLabel(self.RadarLog)
        self.Console_Radar.setGeometry(QtCore.QRect(40, 420, 241, 41))
        self.Console_Radar.setObjectName("Console_Radar")
        self.tabWidget.addTab(self.RadarLog, "")
        self.Continental = QtWidgets.QWidget()
        self.Continental.setObjectName("Continental")
        self.listView_3 = QtWidgets.QListView(self.Continental)
        self.listView_3.setGeometry(QtCore.QRect(0, 0, 971, 531))
        self.listView_3.setStyleSheet("")
        self.listView_3.setObjectName("listView_3")
        self.Console_Conti = QtWidgets.QLabel(self.Continental)
        self.Console_Conti.setGeometry(QtCore.QRect(50, 420, 241, 41))
        self.Console_Conti.setObjectName("Console_Conti")
        self.listWidget_Conti_Left = QtWidgets.QListWidget(self.Continental)
        self.listWidget_Conti_Left.setGeometry(QtCore.QRect(350, 180, 221, 211))
        self.listWidget_Conti_Left.setObjectName("listWidget_Conti_Left")

        for i in range(len(a)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_Conti_Left.addItem(item)
            
        self.btn_Start_Mesurement_Conti = QtWidgets.QPushButton(self.Continental)
        self.btn_Start_Mesurement_Conti.setGeometry(QtCore.QRect(410, 460, 171, 41))
        self.btn_Start_Mesurement_Conti.setObjectName("btn_Start_Mesurement_Conti")

        self.btn_Start_Mesurement_Conti.clicked.connect(self.meas_Conti)

        
        self.listWidget_Conti_Right = QtWidgets.QListWidget(self.Continental)
        self.listWidget_Conti_Right.setGeometry(QtCore.QRect(680, 180, 221, 211))
        self.listWidget_Conti_Right.setObjectName("listWidget_Conti_Right")
        self.btn_Load_Config_Conti = QtWidgets.QPushButton(self.Continental)
        self.btn_Load_Config_Conti.setGeometry(QtCore.QRect(80, 110, 131, 41))
        self.btn_Load_Config_Conti.setObjectName("btn_Load_Config_Conti")

        self.btn_Load_Config_Conti.clicked.connect(self.open_dialog_box_Conti)
        
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Continental)
        self.scrollArea_2.setGeometry(QtCore.QRect(40, 200, 211, 121))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 188, 400))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 400))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_4_Conti = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4_Conti.setGeometry(QtCore.QRect(20, 10, 180, 101))
        
        self.label_4_Conti.setObjectName("label_4_Conti")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.btn_Load_xml_Conti = QtWidgets.QPushButton(self.Continental)
        self.btn_Load_xml_Conti.setGeometry(QtCore.QRect(560, 60, 131, 41))
        self.btn_Load_xml_Conti.setObjectName("btn_Load_xml_Conti")
        self.btn_Conti_Delete = QtWidgets.QPushButton(self.Continental)
        self.btn_Conti_Delete.setGeometry(QtCore.QRect(590, 290, 71, 31))
        self.btn_Conti_Delete.setObjectName("btn_Conti_Delete")
        self.btn_Conti_Add = QtWidgets.QPushButton(self.Continental)
        self.btn_Conti_Add.setGeometry(QtCore.QRect(590, 230, 71, 31))
        self.btn_Conti_Add.setObjectName("btn_Conti_Add")
        self.tabWidget.addTab(self.Continental, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Automotive Radar GUI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.btn_Load_Config_Radar.setText(_translate("MainWindow", "Load Configuration"))
        self.btn_Load_xml_Radar.setText(_translate("MainWindow", "Load xml"))
        self.btn_Radar_Add.setText(_translate("MainWindow", "Add"))
        self.btn_Radar_Delete.setText(_translate("MainWindow", "Delete"))
        self.btn_Start_Mesurement_Radar.setText(_translate("MainWindow", "Start Mesurement"))
        self.Console_Radar.setText(_translate("MainWindow", "Console:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RadarLog), _translate("MainWindow", "Radar Log"))
        self.Console_Conti.setText(_translate("MainWindow", "Console:"))
        self.btn_Start_Mesurement_Conti.setText(_translate("MainWindow", "Start Mesurement"))
        self.btn_Load_Config_Conti.setText(_translate("MainWindow", "Load Configuration"))
        self.btn_Load_xml_Conti.setText(_translate("MainWindow", "Load xml"))
        self.btn_Conti_Delete.setText(_translate("MainWindow", "Delete"))
        self.btn_Conti_Add.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Continental), _translate("MainWindow", "Continental"))
        self.btn_Load_xml_Radar.clicked.connect(self.open_xml_Radar)
        self.btn_Load_xml_Conti.clicked.connect(self.open_xml_Conti)
        self.btn_Radar_Add.clicked.connect(self.add_Radar)
        self.btn_Radar_Delete.clicked.connect(self.remove_Radar)
        self.btn_Conti_Add.clicked.connect(self.add_Conti)
        self.btn_Conti_Delete.clicked.connect(self.remove_Conti)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
