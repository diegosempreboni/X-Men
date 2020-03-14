import os
import fileinput
import ntpath
import subprocess
import sys
import glob
import shutil

import warnings

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

ntpath.basename("a/b/c")

def openFile():
    global fname

    fname =  askopenfilename(initialdir = os.path.abspath(__file__),title = "Select file",filetypes = (("TAMARIN files","*.spthy"),("all files","*.*")))

    if fname:

        jname, ext = os.path.splitext(path_leaf(fname))

        print('\nPlease use the file '+jname+ext+' with the X-Men tool\n')

        splitFile(fname)

        subprocess.call(['java', '-jar', 'Tool/X-Men_2.0.jar'])

        merge()
    else:
        print("\nNo file has been chosen \n")

def excise(filename, fnn, start, end):
    with open(filename) as infile, open(fnn, "w") as outfile:
        for line in infile:
            if line.strip() == start:
                break
            outfile.write(line)
        for line in infile:
            if line.strip() == end:
                break
        for line in infile:
            outfile.write(line)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def splitFile(fname):
    global directory,justname, extension,preamble,postamble
    shutil.copy2(fname, fname+"_tmp")
    directory = os.path.dirname(fname) + "/"
    justname, extension = os.path.splitext(path_leaf(fname))
    #create the files with just the functions, channels and so on.
    preamble = directory + justname+"_pre"+extension
    excise(fname, preamble, "/****RULES****/", "/****ENDOFMODEL****/")
    #create the files with just the axioms and the restrictions
    postamble = directory + justname+"_post"+extension
    excise(fname, postamble, "/****MODEL****/", "/****ENDOFRULES****/")
    #create the files with just the rules
    path_new_file = directory + justname+"_tmp"+extension
    excise(fname, path_new_file, "/****MODEL****/", "/****RULES****/")
    excise(path_new_file, fname, "/****ENDOFRULES****/", "/****ENDOFMODEL****/")
    os.remove(path_new_file)
    with open(fname, "a") as myfile:
        myfile.write("end")

def merge():
    val = 0

    if glob.glob(directory+"*.m"):
        os.mkdir("mutated_models")

    for file in glob.glob(directory+"*.m"):
        filenames = [preamble, file, postamble]
        nfile = directory+justname+"_M"+str(val)+extension
        with open(nfile, 'w') as outfile:
            for nfname in filenames:
                with open(nfname) as infile:
                    for line in infile:
                        outfile.write(line)
        shutil.move(nfile,os.path.dirname(os.path.abspath(__file__))+"/mutated_models/")
        val = val + 1
    for file in glob.glob(directory+"*.m"):
        os.remove(file)



   
    os.rename(fname+"_tmp", fname)
    os.remove(preamble)
    os.remove(postamble)

if __name__ == '__main__':

    openFile()

    



