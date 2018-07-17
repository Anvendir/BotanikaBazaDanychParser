#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import os
from InsertCommandBuilder import InsertCommandBuilder
from RawDataBaseFormater import RawDataBaseFormater
from ExcelDataBaseBuilder import ExcelDataBaseBuilder

def readDataBase():
    l_fileHandler = open("bazaCalosc.txt", "r")
    dataBaseAsString = l_fileHandler.read()
    l_fileHandler.close()
    print "Raw list reading succeeded."
    return dataBaseAsString 

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

def readInsertCommandsForAllSpecies(p_outputDirName):
    l_fileHandler = open(p_outputDirName + "/insertCommandsForAllSpeciesList.txt", "r")
    l_rawFileContent = l_fileHandler.read()
    l_fileHandler.close()
    return re.split('\n', l_rawFileContent)

def divideInsertCommandFileBy1000Records(p_outputDirName):
    l_allInsertCommands = readInsertCommandsForAllSpecies(p_outputDirName)

    l_outPutFileNamePrefix = p_outputDirName + "/insertCommandsFor_" 
    l_outputFileName = l_outPutFileNamePrefix + str(0) + "_" + str(1000) + ".txt" 
    l_outputFile = open(l_outputFileName, "w")

    for l_iterator in range(len(l_allInsertCommands)):
        if not (l_iterator % 1000) and l_iterator:
            l_outputFile.close();
            print "File " + l_outputFileName + " saved."

            l_outputFileName = l_outPutFileNamePrefix + str(l_iterator) + "_" + str(l_iterator + 1000) + ".txt" 
            l_outputFile = open(l_outputFileName, "w")

        l_outputFile.write(l_allInsertCommands[l_iterator])
        l_outputFile.write("\n")

        if l_iterator == len(l_allInsertCommands) - 1:
            l_outputFile.close();
            print "File " + l_outputFileName + " saved."

#main program section
print "\033[94m" + "Program started." + "\033[0m"

l_outputDirName = "./outputFiles"
createOutputDirIfNeeded(l_outputDirName)

l_dataBase = readDataBase()
l_formatedSpeciesList = RawDataBaseFormater().formatRawDataBase(l_dataBase)
saveIndirectOutputToFile(l_formatedSpeciesList, l_outputDirName)

InsertCommandBuilder().prepareInsertCommandsForSpeciesList(l_formatedSpeciesList, l_outputDirName)
divideInsertCommandFileBy1000Records(l_outputDirName)

ExcelDataBaseBuilder().buildDataBase(l_formatedSpeciesList, l_outputDirName)

print "\033[92m" + "Program finished successfully!" + "\033[0m"
