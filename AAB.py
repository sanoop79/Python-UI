# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:23:51 2019

@author: Achutha.P
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *


import pandas as pd
import re


from storeString1 import storeString1
from storeString2 import storeString2
# =============================================================================
# from storeStrings import storeStrings
# =============================================================================


# ## importing files as file and dict

# In[129]:




class Form(QWidget):
    
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
	  
      group1 = QGroupBox('File to be processed')		
      layout1 = QHBoxLayout()
      
      
      self.b1 = QPushButton("Open")
      self.b1.setCheckable(True)
      self.b1.resize(80,80)
      self.b1.setMaximumSize(QSize(80,80))
      self.b1.toggle()
      self.b1.clicked.connect(self.populatetext)
      self.b1.clicked.connect(self.onButtonClicked1)
      #file_name = self.b1.clicked.connect(self.populatetext)
      #self.b1.clicked.connect(self.pop)
      #print (file_name)
      self.secbut1 = QPushButton("Add")
      self.secbut1.setCheckable(True)
      self.secbut1.setMaximumSize(QSize(80,80))
      
      layout1.addWidget(self.b1)
      
      
       
      
      
      self.textbox_1 = QLineEdit(self)
      self.textbox_1.setMaximumSize(QSize(400, 400*0.1))
      
      layout1.addWidget(self.textbox_1)
      #layout1.addWidget(self.secbut1)
      layout1.setAlignment(Qt.AlignCenter)
      group1.setLayout(layout1)
      
      
      group2 = QGroupBox('Dictionaries')
      layout2 = QHBoxLayout()
      
      self.b2 = QPushButton("Open")
      self.b2.setCheckable(True)
      self.b2.resize(80,80)
      self.b2.setMaximumSize(QSize(80,80))
      self.b2.toggle()
      self.b2.clicked.connect(self.populatetext2)
      self.b2.clicked.connect(self.onButtonClicked2)
      #self.b2.clicked.connect(self.btnstate)
      layout2.addWidget(self.b2)
      layout2.setAlignment(Qt.AlignCenter)
      
      
      self.textbox_2 = QLineEdit(self)
      self.textbox_2.setMaximumSize(QSize(400, 400*0.1))

      layout2.addWidget(self.textbox_2)
      group2.setLayout(layout2)
      
      
      group3 = QGroupBox('Inferences')
      layoutlab = QVBoxLayout()
      self.label1 = QLabel()
      self.label2 = QLabel()
      self.label3 = QLabel()
      layoutlab.addWidget(self.label1)
      layoutlab.addWidget(self.label2)
      layoutlab.addWidget(self.label3)
      layoutlab.setAlignment(Qt.AlignLeft)
      group3.setLayout(layoutlab)
      
      
      
      add_layout = QVBoxLayout()     
      
      add_layout.addWidget(group1)
      add_layout.addWidget(group2)
      add_layout.addWidget(group3)
      add_layout.setAlignment(Qt.AlignCenter)
      add_layout.addStretch
      
      run_layout = QHBoxLayout()
      
      self.runb = QPushButton("Run")
      self.runb.setCheckable(True)
      self.runb.resize(80,80)
      self.runb.toggle()
      self.runb.clicked.connect(self.btnstate)
# =============================================================================
#       self.runb.clicked.connect(self.saveFile)
# =============================================================================
      
      self.runb.clicked.connect(self.runClick)
      self.runb.clicked.connect(self.populateLabel)
      
      
      run_layout.addWidget(self.runb)
      run_layout.setAlignment(Qt.AlignCenter)
      
      refresh_layout=QHBoxLayout()
      self.refresh=QPushButton("Refresh")
      self.refresh.resize(80,80)
      self.refresh.toggle()
      #self.refresh.clicked.connect(self.refreshed)
      refresh_layout.addWidget(self.refresh)
      refresh_layout.setAlignment(Qt.AlignCenter)
      
      fin_layout = QVBoxLayout()
      
      
      fin_layout.addLayout(add_layout)
      fin_layout.addLayout(run_layout)
      fin_layout.addLayout(refresh_layout)
      
      
      
 
      self.setLayout(fin_layout)    
      
		
      self.setWindowTitle("Masking App")
      
   def pop(self):
       text_1 = OpenClick(self)
       textbox_1.setText(str(text_1))

   def btnstate(self,):
      if self.runb.isChecked():
         self.runb.setText('Finished')
      else:
         self.runb.setText('Processing')

   def populatetext(self):
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
       
       if fileName:
           self.textbox_1.setText(fileName)
       
       #self.refreshed()
           

           #print (fileName)
   def populatetext2(self):
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
       
       if fileName:
           self.textbox_2.setText(fileName)
         
           #print (fileName)
# =============================================================================
#    def saveFile(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Excel Files (*.xlsx);;Text Files (*.txt)", options=options)
#        fileName = fileName+'.xlsx'
#        if fileName:
#            storeStrings(fileName)
# =============================================================================
            
            
   def OpenClick(self):
      clkopen.App()
      
   def runClick(self):
       import sbsprocessing as proc
       #proc
       
   
   def onButtonClicked1(self):
       storeString1(self.textbox_1.text())


   def onButtonClicked2(self):
       storeString2(self.textbox_2.text())
       
       
   def populateLabel(self):
       from sbsprocessing import numqty,emailqty,nameqty
       self.label1.setText(nameqty)
       self.label2.setText(numqty)
       self.label3.setText(emailqty)
       
   #def refreshed(self):
     
       
       
   #def onButtonClickeds(self):
       

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.setGeometry(200,200,1000,500)
   #data = Form.populatetext.
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
   
   
   
# =============================================================================
# def run  
# file = pd.read_excel('data_file')
# dict1 = pd.read_excel('dict_file',names=['Name'])
# 
# 
# # #code for appending dicts need to be added here
# 
# # ## Define Functions
# 
# # In[169]:
# 
# 
# def dict_process(df):
#     df = df['Name'].tolist()
#     low_dict = [x.lower() for x in df]
#     
#     return low_dict
# 
# 
# # In[182]:
# 
# 
# def file_process(df):
#     processed_body = []
#     for i in range (len(df)):
#         data = df['Body'][i]
#         data = data.replace('\n','').replace('\r','').replace(' | ',' ').replace(',',' ')
#         data = data.lower()
#         #data = list(data.split())
#         processed_body.append(data)
#     df['Processed_body'] = processed_body
#     return df       
#     
# 
# 
# # In[249]:
# 
# 
# def masking(file, dictionary):
#     masked_body = []
#     #dictionary = dictionary['Name']
#     for i in range (len(file)):
#         data = file['Processed_body'][i]
#         data = list(data.split())
#         
#         sent = []
#         for j in range (len(data)):
#             word = data[j]
#             if word in dictionary :
#                 word = list(word)
#                 for y in range (len(word)):
#                     word[y] = 'X'
#                 word = convert(word)
#             else:
#                 word = word
#             sent.append(word)
#         
#         
#         data = convert_fin(sent)
#         masked_body.append(data)
#         
#     file['Masked'] = masked_body
#     file = file.drop(['Body','Processed_body'],axis=1)
#     file = file[['Subject', 'Masked', 'From_name', 'From address', 'From(type)', 'to name',
#        'category', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9' ]]
#     
#     return file
#         
#         
# 
# 
# # In[234]:
# 
# 
# def convert(s): 
#   
#     # initialization of string to "" 
#     new = "" 
#   
#     # traverse in the string  
#     for x in s: 
#         new += x
#         #new += " "
#   
#     # return string  
#     return new 
# 
# 
# 
# 
# 
# def convert_fin(s): 
#   
#     # initialization of string to "" 
#     new = "" 
#   
#     # traverse in the string  
#     for x in s: 
#         new += x
#         new += " "
#   
#     # return string  
#     return new 
# 
# 
# 
# 
# 
# dictionary = dict_process(dict1)
# 
# 
# processed_data = file_process(file)
# 
# file = masking(processed_data,dictionary)
# #C:/Users/Achutha.P/Desktop/Docs/datafile1.xlsx
# 
# file.to_excel('C:/Users/Achutha.P/Desktop/Masked.xlsx')
# =============================================================================
