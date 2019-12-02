# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:47:46 2019
Skript to delete/sort RAW Files not having a specific JPG patner
So you only delete the jpg, and the specific raw files get deleted,too
@author: Tim Wruetz
"""

import tkinter
from tkinter import filedialog
import os
import shutil

def main():    
    
    #Create and Hide window for directory search
    root = tkinter.Tk()
    root.withdraw()
    #Set current directory as start point
    currdir = os.getcwd()
    #Select the directory, which should be cleaned
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')  
    destination_folder = tempdir+"/delDir"

    #Try to create a directory named delDir which contains raws without a jpg
    #partner after script execution.
    try:
        os.mkdir(destination_folder)
        print("Directory " , destination_folder ,  " Created ") 
    except FileExistsError:
        print("Directory " , destination_folder ,  " already exists") 
        
    #If directory creation was successfull sort by jpg and orf    
    if len(tempdir) > 0:
        path = tempdir

        JPGfiles = []
        RAWfiles = []
        
        files = os.listdir(path) 
        
        for ii in range(len(files)):           
            if ".JPG" in files[ii]:
                JPGfiles.append(files[ii].split(".")[0])
            if ".jpg" in files[ii]:
                JPGfiles.append(files[ii].split(".")[0])
            if ".ORF" in files[ii]:
                RAWfiles.append(files[ii].split(".")[0])
            if ".orf" in files[ii]:
                RAWfiles.append(files[ii].split(".")[0])
                
        #Move Raws without jpg partner            
        for kk in range(len(RAWfiles)):        
            if not RAWfiles[kk] in JPGfiles:
                shutil.move(tempdir+"/"+RAWfiles[kk]+".ORF", destination_folder+"/"+RAWfiles[kk]+".ORF")     
     

if __name__ == "__main__":
    main()
    

