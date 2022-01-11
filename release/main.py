#!/usr/bin/env python3

'''
M7L
use camera ov9281 mipi

Date :  28/12/2021

'''


import time
import sys
import os
import csv
sys.path.append('/usr/local/python/cv2/python3')
import cv2 as cv
import glob
import numpy as np
from PIL import Image
from tifffile import imsave

import ctypes 

from ctypes import *

import RPi.GPIO as GPIO
import time

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

#from PyQt5 import QtCore, QtGui, QtWidgets 
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel , QPushButton , QHBoxLayout, QVBoxLayout, QSpinBox, QGraphicsScene, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap , QImage 
 
# This is our window from QtCreator
import gui_auto



val  = []  
acqimage = {}
calibacqimage = {}
label = ['x1' , 'y1', 'x2' , 'y2' , 'ss' , 'gain', 'calibration']   


pinRED = 37
pinGREEN_ON = 12
pinGREEN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinGREEN, GPIO.OUT)


so_file1 = '/lib/arm-linux-gnueabihf/libudev.so.1.6.13'
so_file2 = '/home/pi/utility/EFW/EFW_linux_mac_SDK_V1.7/lib/armv7/libEFWFilter.so'

efw = ctypes.CDLL(so_file1, ctypes.RTLD_GLOBAL)
efw = ctypes.CDLL(so_file2, ctypes.RTLD_GLOBAL)


class EFW_INFO(ctypes.Structure):
       _fields_ = [
                  ("ID", ctypes.c_int),
                  ("Name", ctypes.c_char *64),   
                  ("slotNum", ctypes.c_int)
                  ] 

 
# create class for our Raspberry Pi GUI
class GUI(QMainWindow, gui_auto.Ui_MainWindow):
    # access variables inside of the UI's file
    
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file    
        
        self.btn_exit.clicked.connect(self.exitProgram)
        self.btn_start_loop.clicked.connect(self.acquisitionStart)
        self.buttonSaveParameters.clicked.connect(self.saveParameters)   
          
        self.readfileparameter()
        self.initCamera()

    # legge parametri da file
    def readfileparameter(self):  
        if val:
           for i in range(6):
               val.pop()
               
        #read in the csv file
        csvfile = csv.reader(open('param.v1.csv'))   

        for row in csvfile:
            val.extend([row[1]])   
        

        print  ("x1  = " + val[0] + " y1  = " + val[1] + " - x2  = " + val[2] + " y2  = " + val[3])
        print  ("shutter = " +  val[4] )
        print  ("gain = " +  val[5] )  
        print  ("flag calibration = " +  val[6] )    

        self.spinBoxX1.setValue (int(val[0])) 
        self.spinBoxY1.setValue (int(val[1])) 
        self.spinBoxX2.setValue (int(val[2])) 
        self.spinBoxY2.setValue (int(val[3])) 	
        		 
        self.spinBoxShutter.setValue (int(val[4]))   #shutter
        self.spinBoxGain.setValue (int(val[5]))      #gain
        
        if int(val[6]) == 1 : 
           self.checkBoxCalibration.setChecked(True)
        else :
           self.checkBoxCalibration.setChecked(False)
        



    # read parameter dell' interfaccia
    def readparameter(self): 
					
       val[0] = str(self.spinBoxX1.value() ) 
       val[1] = str(self.spinBoxY1.value() ) 
       val[2] = str(self.spinBoxX2.value() )
       val[3] = str(self.spinBoxY2.value() ) 	

       print  ("x1  = " + val[0] + " y1  = " + val[1] + " - x2  = " + val[2] + " y2  = " + val[3])		 

       val[4] = str(self.spinBoxShutter.value()) 
       print  ("shutter = " +  val[4] )
       
       val[5] = str(self.spinBoxGain.value()) 
       print  ("gain = " +  val[5] )      
             
       if  self.checkBoxCalibration.isChecked() : #flag calibration
           val[6] = 1 
       else :
           val[6] = 0
           
       #print  ("flag calibration = " +  val[6])    
           
           
    #collegato al tasto save config
    def saveParameters (self) :
	    
       self.readparameter()    
       f = open ('param.v1.csv','w')  

       wr = csv.writer(f)  
       wr.writerow([label[0] ,val[0]])
       wr.writerow([label[1] ,val[1]])
       wr.writerow([label[2] ,val[2]])
       wr.writerow([label[3] ,val[3]])
       wr.writerow([label[4] ,val[4]])
       wr.writerow([label[5] ,val[5]])
       wr.writerow([label[6] ,val[6]])


       print  ("Configuration parameters saved")
       self.Message ("Configuration parameters saved")
       
       self.initCamera()
       
       self.readparameter()
       self.showCalibArea()


    def Message (self,message) :
       self.labelMsg.setText  (message) 

    '''''''''''''''''''''''''''''''''''''''''''''
    calibration_area
    view calibration area
    area value in configuration file
    '''''''''''''''''''''''''''''''''''''''''''''

    #def calibration_area():
    
 
    '''''''''''''''''''''''''''''''''''''''''''''
    radiometric_calibration
    parameter: 
                  numcamera
                  image 
               
    '''''''''''''''''''''''''''''''''''''''''''''            

    
    def radiometricCalibration (self,numcamera,singleimage):
    
      #calibfile = []
   
      #calibfile.append  ('img/vignetting/IMG_CV_B.tiff' )
      #calibfile.append  ('img/vignetting/IMG_CV_G.tiff' )  
      #calibfile.append  ('img/vignetting/IMG_CV_R.tiff' )
      #calibfile.append  ('img/vignetting/IMG_CV_N.tiff' )

      # immagine da calibrare
      print ("singleimage type = ",type (singleimage))
      nparray =  singleimage
            
            
      #nparray = np.array (singleimage)
      #print ("nparray type = ",type (nparray))


      
      #legge i dati di Vignettatura corrispondenti all'immagine numcamera
      #imV = cv.imread(calibfile[numcamera]) 
      #arrayVIGN = np.array (imV)

      #print ("arrayIMG",  type (arrayIMG))
      #print ("arrayVIGN", type (arrayVIGN)) 
   
      # Corregge con la matrice della vignettatura i dati dell'immagine  ---- DA INSERIRE
      ### resultarray =  arrayIMG * arrayVIGN
   
      # [x1:x2, y1:y2] area della mattonella (calcola valore medio)      
      resultarraysubReg = nparray[int(val[0]):int(val[2]), int(val[1]):int(val[3])]   
      tileValue = np.mean(resultarraysubReg)
      print("mean =  ", tileValue)
      resultarray = np.divide (nparray,tileValue)
      print ("resultarray = ",resultarray)
      
      #resultarray = resultarray * 255
      #print ("resultarray = ",resultarray)
   
      return resultarray   

    '''''''''''''''''''''''''''''''''''''''''''''
    moveFilter
    parameter: 
               Target               
    Move Filter to Target and acquire img

    '''''''''''''''''''''''''''''''''''''''''''''

    def moveFilter(self,filterWheelID, info, Target ):
    
       #info = EFW_INFO()
       p0 = pointer(info)
       #print("ID =  ", info.ID)
       #print("index Name =  ", info.Name)
       #print("ID =  ", info.slotNum)
       #pID = pointer(info.ID)
      

       #efw.EFWGetID(filterWheelID, pointer(info.ID))
    
       # OPEN
       err = efw.EFWOpen(filterWheelID)
       if err != 0 :
          print("Filter wheel open error" , err)
          self.Message ("Filter wheel open error")
          sys.exit(0)
       else :
          print("Filter wheel open OK" , err)
          self.Message ("Filter wheel open OK")

       # EFWGetProperty è necessaria
       efw.EFWGetProperty(filterWheelID, p0)
       #print("index letto = ",info.ID ) 
       #print("index Name =  ", info.Name) 
       #print("ID =  ", info.slotNum) 
    
       #targetSlot 0,1,2,3

       print("Request to move to position =", Target)
       time.sleep (2) 
 
       err = 99
       #print ("GREENON ON")
       GPIO.output(pinGREEN, GPIO.HIGH)
       err = efw.EFWSetPosition(c_int(filterWheelID), c_int(Target))
       if err == 0 :
         message =  "Filter wheel moving to position " + str(Target)
         print (message)
         self.Message (message)
         QtCore.QCoreApplication.processEvents()
         time.sleep (2) 
         self.still_capture(Target) 
       else :               
         print("Moving Error = ",err )
         message = "Moving Error = " + err
         self.Message (message) 
         time.sleep (3)   
       # pinGREEN off
       GPIO.output(pinGREEN, GPIO.LOW)
    
       #Close      
       err = efw.EFWClose(filterWheelID)
       print("Close Filterwheel", err)


    def still_capture(self,slot): 
        name = 'img/img' + str(slot) + '.raw'
        #cmd1 = "v4l2-ctl --set-fmt-video=width=1280,height=800,pixelformat=Y10 --stream-mmap --stream-count=1 --stream-to=" + name + " --verbose"
        cmd1 = "v4l2-ctl --set-fmt-video=width=1280,height=800,pixelformat=Y10 --stream-mmap --stream-count=1 --stream-to=" + name 
        print(cmd1) 
        #self.Message (cmd1)         
        os.system(cmd1)

  
    def initCamera(self): 
        cmd1 = "v4l2-ctl --set-ctrl=exposure=" + val[4] +",gain=" + val[5]
        os.system(cmd1) 
        print(cmd1) 
        #self.Message (cmd1)                  


    '''''''''''''''''''''''''''''''''''''''''''''
    showImage
    parameter: 
               slot               
    
    Save image
    Show Calibration ROI
    if required call Radiometric Calibration
    Show image
    
    '''''''''''''''''''''''''''''''''''''''''''''

    def showImage(self,slot ):
        
        name            = 'img/img' + str(slot) + '.raw'
        name_tif        = 'img/img' + str(slot) + '.tif'  
        name_calib_tif  = 'img/img' + str(slot) + 'calib.tiff'    
          
        # width and height sono invertite per trasformare il file da raw a tiff
        # numpy array that can be directly manipulated
        # read
        width  = 800
        height = 1280
        fd  = open(name, 'rb')
        f   = np.fromfile(fd, dtype=np.uint8,count=width*height)
        img = f.reshape((width, height)) 
        fd.close()
        #save tiff
        imgPIL = Image.fromarray(img)
        imgPIL.save(name_tif, format='TIFF') 
        
        

        
        #se selezionata chiama la calibrazione
        #nessuna calibrazione          
        if int (val[6]) == 0:
           acqimage[slot] = img
           frame = img
           size = frame.shape
           height, width = frame.shape[:2]	
           
        #calibrazione
        else :
           #image = Image.open(name_tif)
           #frame = np.asarray(image)
           frame = np.asarray(imgPIL)
           calibnparray = self.radiometricCalibration (slot,frame)  
           calibimg = Image.fromarray(calibnparray)
                
           #Save file tiff calibrato
           calibimg.save(name_calib_tif, format='TIFF') 
           
           #https://stackoverflow.com/questions/24124458/how-to-change-numpy-array-into-grayscale-opencv-image
           cv_img = np.array(calibnparray*255).astype('uint8')
           # l'operazione successiva sembra zoomare l'img
           #cv_gray = cv.cvtColor(cv_img, cv.COLOR_GRAY2RGB)
           frame = cv_img
           
           
        #NDVI
        if slot == 3 and  acqimage :
              self.NDVI()
            
        # draw a rectangle around the region of interest                     
        #                     start point , end point , bianco  , 2
        cv.rectangle(frame, (int(val[0]),int(val[1])),
                            (int(val[2]),int(val[3])), (255, 255, 255), 2)   
         
        resized = cv.resize( frame, (408, 255), interpolation = cv.INTER_AREA)
        size = resized.shape
        step = resized.size / size[0]
        #The image is stored using 8-bit indexes into a colormap.
        qformat = QImage.Format_Indexed8

        '''
        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        '''
        
        img = QImage(resized, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        
        # BLU    window 0
        if slot == 0:			
            self.labelBlue.setPixmap(QPixmap.fromImage(img))

        # GREEN  window 1  
        elif slot == 1 :
            self.labelGreen.setPixmap(QPixmap.fromImage(img))

        # RED    window 2 
        elif slot == 2 :
            self.labelRed.setPixmap(QPixmap.fromImage(img)) 
            
        # NIR    window 3          
        elif slot == 3 :
            self.labelNIR.setPixmap(QPixmap.fromImage(img)) 
        QtCore.QCoreApplication.processEvents()

 
    def showCalibArea(self):
        # DA Fare 
        #    non cancella i rettangoli già disegnati
        #    gli estremi del rettangolo in bianco non sono visibili
		
        if not acqimage:
            frame = cv.imread('img/black.tif')
        else :    
            frame = acqimage[2] 
            size = frame.shape
            height, width = frame.shape[:2]
 
   					        
        # draw a rectangle around the region of interest                     
        #                     start point , end point , bianco  , 2
        cv.rectangle(frame, (int(val[0]),int(val[1])),
                            (int(val[2]),int(val[3])), (255, 255, 255), 4)   
         
        resized = cv.resize( frame, (408, 255), interpolation = cv.INTER_AREA)
        size = resized.shape
        step = resized.size / size[0]
        #The image is stored using 8-bit indexes into a colormap.
        qformat = QImage.Format_Indexed8

        img = QImage(resized, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
			
        self.labelRed.setPixmap(QPixmap.fromImage(img))

        QtCore.QCoreApplication.processEvents()
 
 
    def NDVI(self): 
        red = acqimage[2] 
        red = red.astype('f4')
        infrared =  acqimage[3] 
        infrared = infrared.astype('f4')
        green = acqimage[1] 
        green = green.astype('f4')
        blue = acqimage[0] 
        blue = blue.astype('f4')
        non_zero_div_term = 0.000000000000000001 #term to avoid division / 0

        # NDVI= (nir-r)/(nir+r)
        den = infrared + red + non_zero_div_term
        num= infrared - red
        img_ndvi = (num/den)
        
        arr_ndvi = np.asarray(img_ndvi)
        print ("min ", arr_ndvi.min)
        print ("max ", arr_ndvi.max)

        #Save NDVI image as TIF
        imsave('img/ndvi.tif',img_ndvi) 
        print("NDVI",img_ndvi) 
 
 
    # func. collegata al tasto Exit
    def exitProgram (self):  
        print('Exit from program')
        sys.exit(1) 
 
    # func. collegata al tasto START
    def acquisitionStart (self): 

        self.Message ("Start Acquisition")
        QtCore.QCoreApplication.processEvents()
        for i in range(4):
            self.moveFilter(filterWheelID,info, i )
            #self.showImage (0,False,False,True)
            self.showImage (i)	
        self.Message ("End Acquisition")    	
						
 
# python bit to figure how who started This
if __name__ == "__main__":


     # Check if Filter wheel exists
     # Refresh device list if EFW is connected or disconnected  
     EFW_count = efw.EFWGetNum()  
     if EFW_count <= 0 :
         print ('No filter wheel connected')
         #GUI.Message ("No filter wheel connected")
         sys.exit(0)
     else :
         print ("Number of attached filter wheel = ",  EFW_count)
         #GUI.Message ("Filter wheel connected")
    
     # Initialize structure
     info = EFW_INFO()
     filterWheelID = 0
    
     #read_parameter()


	 # a new app instance
     app = QApplication(sys.argv)

     form = GUI()

     form.show()
	 # without this, the script exits immediately.
     sys.exit(app.exec_())




