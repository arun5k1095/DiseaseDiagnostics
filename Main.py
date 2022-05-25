
# Tool = "Human Clinical Diagnosis"
# Version = "1.0"
# LastModifiedOn : "24th April 2022"
#______________________________________________________________________

import serial
import sys
import Resources
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui ,QtCore
import time
import smtplib
from threading import*

PatientName = 'Test_Subject'  # user should input
PatientAge = '38'  # user should input
WeightPAtient = "72"

def showUserInfo(message):
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText(message)
   msgBox.setWindowTitle("Status Info")
   msgBox.setStandardButtons(QMessageBox.Ok)
   msgBox.show()

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok: pass
   else: pass

if __name__ == "__main__":
    Aplication = QApplication(sys.argv)
    MainWindowGUI = QWidget()
    MainWindowGUI.setFixedSize(780, 400)
    MainWindowGUI.setWindowTitle('Human Clinical Diagnosis')
    MainWindowGUI.setStyleSheet("background-color: black;")
    MainWindowGUI.setObjectName("MainMenu");
    IconFilepath = ":/resources/Icon.ico"
    MainWindowGUI.setStyleSheet("QWidget#MainMenu{background-image: url(Wallpeper1.jpg);}");
    MainWindowGUI.setWindowIcon(QtGui.QIcon(IconFilepath))
    LogTable = QTableWidget(MainWindowGUI)
    LogTable.setRowCount(500)
    LogTable.setColumnCount(7)
    LogTable.move(35, 50)
    LogTable.setFixedSize(700, 200)
    LogTable.setStyleSheet("background-color: 	white" "")
    Header1 = QTableWidgetItem("Temperature")
    Header2 = QTableWidgetItem("SugarLevel")
    Header3 = QTableWidgetItem("BloodPreassure")
    Header4 = QTableWidgetItem("SOP2Level")
    Header5 = QTableWidgetItem("HeartRate")
    Header6 = QTableWidgetItem("Report")
    Header7 = QTableWidgetItem("FuncExecTime")

    LogTable.setHorizontalHeaderItem(0, Header1)
    LogTable.setHorizontalHeaderItem(1, Header2)
    LogTable.setHorizontalHeaderItem(2, Header3)
    LogTable.setHorizontalHeaderItem(3, Header4)
    LogTable.setHorizontalHeaderItem(4, Header5)
    LogTable.setHorizontalHeaderItem(5, Header6)
    LogTable.setHorizontalHeaderItem(6, Header7)



    for row in range(100):
        LogTable.setVerticalHeaderItem(row , QTableWidgetItem("Day "+str(row)))

    import pandas

    Database = pandas.DataFrame()

    DataBaseLoaded = 0
    def ReadPatientDatabase():
        global Database , DataBaseLoaded
        try:
            FilePath, _ =QFileDialog.getOpenFileName\
                (MainWindowGUI, 'Select Patient Diagnosis Rules File', r"", '*.xlsx')
        except: pass
        Database = pandas.read_excel(FilePath)
        if len(Database) > 1:
            DataBaseLoaded = 1

    import random


    class Person:
        def __init__(self, Temperature = 38, HeartRate = 100,SPO2Level = 98,BloodPreassure = 90,BloodGlucose = 130):
            self.Temperature = Temperature
            self.HeartRate = HeartRate
            self.SPO2Level = SPO2Level
            self.BloodPreassure = BloodPreassure
            self.BloodGlucose = BloodGlucose

    Patient = Person()

    import time

    def SimulateDays():
        global Patient
        if DataBaseLoaded: pass
        else :
            showUserInfo("Please load the Diagnosis rules database")
            return
        StartTime = time.time()
        #Randomly simulate patiens Condition
        Patient.Temperature = random.randint(int(Database.loc[0,["MIN1"]])-5 , int(Database.loc[0,["MAX2"]])+5)
        Patient.HeartRate = random.randint( int(Database.loc[1,["MIN1"]])-5 , int(Database.loc[1,["MAX2"]])+5 )
        Patient.SPO2Level = random.randint( int(Database.loc[2,["MIN1"]])-5 , int(Database.loc[2,["MAX2"]])+5 )
        Patient.BloodPreassure = random.randint( int(Database.loc[3,["MIN1"]])-5 , int(Database.loc[3,["MAX2"]])+5 )
        Patient.BloodGlucose = random.randint( int(Database.loc[4,["MIN1"]])-30 , int(Database.loc[4,["MAX2"]])+100 )
        EndTime = time.time()

        ExecutionTime = EndTime - StartTime

        DiagnosisReport = ""
        if (Patient.Temperature > int(Database.loc[0,["MAX2"]])):
            DiagnosisReport += " Temp :" + Database.loc[0, ["MAX2_COND"]].values

        elif  (Patient.Temperature < int(Database.loc[0,["MAX2"]])) and \
                (Patient.Temperature > int(Database.loc[0,["MAX1"]])):
            DiagnosisReport += "Temp :" + Database.loc[0, ["MAX1_COND"]].values

        elif (Patient.Temperature < int(Database.loc[0,["MIN1"]])) and Patient.Temperature > int(Database.loc[0,["MIN2"]]) :
            DiagnosisReport +=  "Temp :" +Database.loc[0,["MIN2_COND"]].values
        else :
            DiagnosisReport += "Temp :" + Database.loc[0, ["MIN1_COND"]].values

        DiagnosisReport += "__"

        if (Patient.HeartRate > int(Database.loc[1,["MAX2"]])):
            DiagnosisReport += " HeartRate :" + Database.loc[1, ["MAX2_COND"]].values

        elif  (Patient.HeartRate < int(Database.loc[1,["MAX2"]])) and \
                (Patient.HeartRate > int(Database.loc[1,["MAX1"]])):
            DiagnosisReport += "HeartRate :" + Database.loc[1, ["MAX1_COND"]].values

        elif (Patient.HeartRate < int(Database.loc[1,["MIN1"]])) and Patient.HeartRate > int(Database.loc[1,["MIN2"]]) :
            DiagnosisReport +=  "HeartRate :" +Database.loc[1,["MIN2_COND"]].values
        else :
            DiagnosisReport += "HeartRate :" + Database.loc[1, ["MIN1_COND"]].values

        DiagnosisReport += "__"
        if (Patient.SPO2Level > int(Database.loc[2,["MAX2"]])):
            DiagnosisReport += " SPO2Level :" + Database.loc[2, ["MAX2_COND"]].values

        elif  (Patient.SPO2Level < int(Database.loc[2,["MAX2"]])) and \
                (Patient.SPO2Level > int(Database.loc[2,["MAX1"]])):
            DiagnosisReport += "SPO2Level :" + Database.loc[2, ["MAX1_COND"]].values

        elif (Patient.SPO2Level < int(Database.loc[2,["MIN1"]])) and Patient.SPO2Level > int(Database.loc[2,["MIN2"]]) :
            DiagnosisReport +=  "SPO2Level :" +Database.loc[2,["MIN2_COND"]].values
        else :
            DiagnosisReport += "SPO2Level :" + Database.loc[2, ["MIN1_COND"]].values

        DiagnosisReport += "__"
        if (Patient.BloodPreassure > int(Database.loc[3,["MAX2"]])):
            DiagnosisReport += " BloodPreassure :" + Database.loc[3, ["MAX2_COND"]].values

        elif  (Patient.BloodPreassure < int(Database.loc[3,["MAX2"]])) and \
                (Patient.BloodPreassure > int(Database.loc[3,["MAX1"]])):
            DiagnosisReport += "BloodPreassure :" + Database.loc[3, ["MAX1_COND"]].values

        elif (Patient.BloodPreassure < int(Database.loc[3,["MIN1"]])) and Patient.BloodPreassure > int(Database.loc[3,["MIN2"]]) :
            DiagnosisReport +=  "BloodPreassure :" +Database.loc[3,["MIN2_COND"]].values
        else :
            DiagnosisReport += "BloodPreassure :" + Database.loc[3, ["MIN1_COND"]].values

        DiagnosisReport += "__"
        if (Patient.BloodGlucose > int(Database.loc[4,["MAX2"]])):
            DiagnosisReport += " BloodGlucose :" + Database.loc[4, ["MAX2_COND"]].values

        elif  (Patient.BloodGlucose < int(Database.loc[4,["MAX2"]])) and \
                (Patient.BloodGlucose > int(Database.loc[4,["MAX1"]])):
            DiagnosisReport += "BloodGlucose :" + Database.loc[4, ["MAX1_COND"]].values

        elif (Patient.BloodGlucose < int(Database.loc[4,["MIN1"]])) and Patient.BloodGlucose > int(Database.loc[4,["MIN2"]]) :
            DiagnosisReport +=  "BloodGlucose :" +Database.loc[4,["MIN2_COND"]].values
        else :
            DiagnosisReport += "BloodGlucose :" + Database.loc[4, ["MIN1_COND"]].values


        UpdateDiagnosisAnalaysis(ExecutionTime,DiagnosisReport)


    DaySimulated = 0
    def UpdateDiagnosisAnalaysis(ExecutionTime,DiagnosisReport):
        global DaySimulated

        LogTable.setItem(DaySimulated,0 ,QTableWidgetItem(str(Patient.Temperature)) )
        LogTable.setItem(DaySimulated,1 ,QTableWidgetItem(str(Patient.HeartRate)) )
        LogTable.setItem(DaySimulated,2 ,QTableWidgetItem(str(Patient.SPO2Level)) )
        LogTable.setItem(DaySimulated,3 ,QTableWidgetItem(str(Patient.BloodPreassure)) )
        LogTable.setItem(DaySimulated,4 ,QTableWidgetItem(str(Patient.BloodGlucose)) )
        LogTable.setItem(DaySimulated,5 ,QTableWidgetItem(str(DiagnosisReport)) )
        LogTable.setItem(DaySimulated,6 ,QTableWidgetItem(str(format(ExecutionTime, ".5f"))) )

        LogTable.update()


        DaySimulated +=1




    SimulateDay = QPushButton("Simulate Patient's Day" , MainWindowGUI)
    SimulateDay.setFixedSize(200,40)
    SimulateDay.setStyleSheet("QPushButton {border: 1px blue;border-radius: 5px;  background-color: #075691; color : white;}""QPushButton::hover"
            "{"
            "background-color : green;"
            "}")
    SimulateDay.move(50,300)
    SimulateDay.clicked.connect(SimulateDays)

    PatientDiagnosisRuleFile = QPushButton("Browse DataBase..", MainWindowGUI)
    PatientDiagnosisRuleFile.setFixedSize(150, 40)
    PatientDiagnosisRuleFile.setStyleSheet(
        "QPushButton {border: 1px blue;border-radius: 5px;  background-color: #075691; color : white;}""QPushButton::hover"
        "{"
        "background-color : #1a85b4;"
        "}")
    PatientDiagnosisRuleFile.move(300, 300)
    PatientDiagnosisRuleFile.clicked.connect(ReadPatientDatabase)



    def SaveConfiguration():
        global PatientName,PatientName ,WeightPAtient

        PatientName =PatientName_inp.text().strip()
        PatientAge =PatientAge_inp.text().strip()
        WeightPAtient = PatientWeight_inp.text()
        DialogueBox.close()


    DialogueBox = QDialog(MainWindowGUI)
    DialogueBox.setFixedSize(300, 170)
    DialogueBox.setStyleSheet("background-color: 	white" "")
    DialogueBox.setWindowTitle("Registration")
    formGroupBox = QGroupBox("Patient Details")
    layout = QFormLayout()
    PatientName_inp = QLineEdit()
    PatientAge_inp = QLineEdit()
    PatientWeight_inp = QLineEdit()
    layout.addRow(QLabel("Patient Name"), PatientName_inp)
    layout.addRow(QLabel("Patient Age"), PatientAge_inp)
    layout.addRow(QLabel("Patient Weight"), PatientWeight_inp)
    formGroupBox.setLayout(layout)

    buttonBox = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(SaveConfiguration)
    buttonBox.rejected.connect(DialogueBox.close)

    mainLayout = QVBoxLayout()

    mainLayout.addWidget(formGroupBox)
    mainLayout.addWidget(buttonBox)
    DialogueBox.setLayout(mainLayout)

    def SystemSettings():
        PatientName_inp.setText(PatientName)
        PatientAge_inp.setText(PatientAge)
        PatientWeight_inp.setText(WeightPAtient)
        DialogueBox.exec_()


    toolbar = QToolBar(MainWindowGUI)
    toolbar.move(0,0)

    toolButton = QToolButton()
    toolButton.setText("Settings")
    toolButton.setIcon(QIcon(":/resources/ConfigIcon.JPG"))
    toolButton.clicked.connect(SystemSettings)

    MainWindowGUI.show()
    sys.exit(Aplication.exec_())