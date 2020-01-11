# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 2020
Script to move the *.nef Files to another folder, with same folder structure
Userful to backup the NEF files.
referece: deleteRAWWithoutJPG.py from Tim Wruetz
@author: Weifeng Shu
"""

import tkinter
from tkinter import filedialog
import os
import shutil

def main(testmode=0):    
    found_files = 0
    if(testmode):
        source_folder = "D:/Personal/github/WeshuGit/JpgRawUtils/test_folder/src"
    else:
        #Create and Hide window for directory search
        root = tkinter.Tk()
        root.withdraw()
        #Set current directory as start point
        currdir = os.getcwd()
        #Select the directory, which should be cleaned
        source_folder      = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')  
    source_folder = source_folder.replace('/','\\')
    print("Source directory: ", source_folder)
    if len(source_folder) > 0:
        #Try to create a directory named delDir which contains raws without a jpg
        #partner after script execution.
        destination_folder = source_folder+"\\..\\RawDir"
        try:
            os.mkdir(destination_folder)
            print("Destination directory: " , destination_folder ,  " Created ") 
        except FileExistsError:
            print("Destination directory: " , destination_folder ,  " already exists") 
        
    #If directory creation was successfull sort by jpg and orf    
    if len(source_folder) > 0:
        ##FIND NEF FILES
        for dirName, subdirList, fileList in os.walk(source_folder):
            # generate list of files in directory with desired extension
            for fname in fileList:
                if fname.lower().endswith('.nef'):
                    found_files = found_files + 1
                    print('#%04d -- '%(found_files), dirName, fname)
                    dest_folder = dirName.replace(source_folder,destination_folder)
                    print('         ',dest_folder+'\\'+fname)
                    if not os.path.isdir(dest_folder):
                        os.mkdir(dest_folder)
                    if testmode:
                        shutil.copy(dirName+'\\'+fname,dest_folder+'\\'+fname)
                    else:
                        shutil.move(dirName+'\\'+fname,dest_folder+'\\'+fname)
if __name__ == "__main__":
    if 1:
        main()
    else:
        main(1) # test mode