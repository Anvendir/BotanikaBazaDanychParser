#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import os
from InsertCommandBuilder import InsertCommandBuilder
from RawDataBaseFormater import RawDataBaseFormater
from ExcelDataBaseBuilder import ExcelDataBaseBuilder
from InsertCommandFileDivider import InsertCommandFileDivider
from PolishDataBaseSuplementer import PolishDataBaseSuplementer

def readDataBase():
    l_fileHandler = open("bazaCalosc.txt", "r")
    l_dataBaseAsString = l_fileHandler.read()
    l_fileHandler.close()
    print "Raw list reading succeeded."
    return l_dataBaseAsString 

def createOutputDirIfNeeded(p_outputDirName):
    if not os.path.exists(p_outputDirName):
        os.makedirs(p_outputDirName)

def saveIndirectOutputToFile(p_speciesList, p_outputDirName):
    l_outputFileName = p_outputDirName + "/indirectOutputFile.txt"
    l_indirectOutputFile = open(l_outputFileName, "w")

    for l_singleSpeciesRecord in p_speciesList:
        l_indirectOutputFile.write(l_singleSpeciesRecord)
        l_indirectOutputFile.write("\n")
        
    l_indirectOutputFile.close()
    print "File " + l_outputFileName + " saved." 

#main program section
print "\033[94m" + "Program started." + "\033[0m"

l_outputDirName = "./outputFiles"
createOutputDirIfNeeded(l_outputDirName)

l_dataBase = readDataBase()
l_formatedSpeciesList = RawDataBaseFormater().formatRawDataBase(l_dataBase)
saveIndirectOutputToFile(l_formatedSpeciesList, l_outputDirName)

l_suplementer = PolishDataBaseSuplementer()
l_suplementer.addPolishNameToFamilyAndUpperTaxons(l_formatedSpeciesList, l_outputDirName)

l_insertCommandBuilder = InsertCommandBuilder() 
l_outputFileName = l_insertCommandBuilder.buildInsertCommandsForSpeciesList(l_formatedSpeciesList, l_outputDirName)

l_insertCommandDivider = InsertCommandFileDivider()
l_insertCommandDivider.divideInsertCommandFileBy1000Records(l_outputFileName, l_outputDirName)

ExcelDataBaseBuilder().buildDataBase(l_formatedSpeciesList, l_outputDirName)

print "\033[92m" + "Program finished successfully!" + "\033[0m"
