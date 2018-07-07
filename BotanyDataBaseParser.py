#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from InsertCommandBuilder import InsertCommandBuilder
from RawDataBaseFormater import RawDataBaseFormater

def readDataBase():
    l_fileHandler = open("bazaCalosc.txt", "r")
    dataBaseAsString = l_fileHandler.read()
    l_fileHandler.close()
    print "Raw list reading succeeded."
    return dataBaseAsString 

def saveIndirectOutputToFile(p_speciesList):
    l_outputFileName = "indirectOutputFile.txt"
    l_indirectOutputFile = open(l_outputFileName, "w")

    for l_singleSpeciesRecord in p_speciesList:
        l_indirectOutputFile.write(l_singleSpeciesRecord)
        l_indirectOutputFile.write("\n")
        
    l_indirectOutputFile.close()
    print "File " + l_outputFileName + " saved." 

def readInsertCommandsForAllSpecies():
    l_fileHandler = open("insertCommandsForAllSpeciesList.txt", "r")
    l_rawFileContent = l_fileHandler.read()
    l_fileHandler.close()
    return re.split('\n', l_rawFileContent)

def divideInsertCommandFileBy1000Records():
    l_allInsertCommands = readInsertCommandsForAllSpecies()

    l_outputFileName = "insertCommandsFor_" + str(0) + "_" + str(1000) + ".txt" 
    l_outputFile = open(l_outputFileName, "w")

    for l_iterator in range(len(l_allInsertCommands)):
        if not (l_iterator % 1000) and l_iterator:
            l_outputFile.close();
            print "File " + l_outputFileName + " saved."

            l_outputFileName = "insertCommandsFor_" + str(l_iterator) + "_" + str(l_iterator + 1000) + ".txt" 
            l_outputFile = open(l_outputFileName, "w")

        l_outputFile.write(l_allInsertCommands[l_iterator])
        l_outputFile.write("\n")

        if l_iterator == len(l_allInsertCommands) - 1:
            l_outputFile.close();
            print "File " + l_outputFileName + " saved."

#main program section
print "\033[94m" + "Program started." + "\033[0m" 
l_dataBase = readDataBase()
l_formatedSpeciesList = RawDataBaseFormater().formatRawDataBase(l_dataBase)
saveIndirectOutputToFile(l_formatedSpeciesList)
InsertCommandBuilder().prepareInsertCommandsForSpeciesList(l_formatedSpeciesList)
divideInsertCommandFileBy1000Records()
print "\033[92m" + "Program finished successfully!" + "\033[0m"
