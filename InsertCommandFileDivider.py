#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import re

class InsertCommandFileDivider:
    def divideInsertCommandFileBy1000Records(self, p_outputFileName, p_outputDirName):
        l_allInsertCommands = self.__readInsertCommandsForAllSpecies(p_outputFileName, p_outputDirName)

        l_outPutFileNamePrefix = p_outputDirName + "/insertCommandsFor_"
        self.__divideFileBy1000Records(l_allInsertCommands, l_outPutFileNamePrefix)
   
    def __divideFileBy1000Records(self, p_allInsertCommands, p_outputFileNamePrefix):
        l_outputFileName = self.__getOutputFileName(p_outputFileNamePrefix, 0) 
        l_outputFile = open(l_outputFileName, "w")

        for l_iterator in range(len(p_allInsertCommands)):
            if self.__shouldSaveFile(l_iterator):
                l_outputFile.close();
                print "File " + l_outputFileName + " saved."

                l_outputFileName = self.__getOutputFileName(p_outputFileNamePrefix, l_iterator)
                l_outputFile = open(l_outputFileName, "w")

            l_outputFile.write(p_allInsertCommands[l_iterator])
            l_outputFile.write("\n")

            if self.__isLastRecordToSave(l_iterator, len(p_allInsertCommands)):
                l_outputFile.close();
                print "File " + l_outputFileName + " saved."

    def __isLastRecordToSave(self, p_iterator, p_listLenght):
        return p_iterator == (p_listLenght - 1) 

    def __getOutputFileName(self, p_filePrefix, p_iterator):
        return p_filePrefix + str(p_iterator) + "_" + str(p_iterator + 1000) + ".txt" 

    def __shouldSaveFile(self, p_iterator):
        return self.__isThousandRecord(p_iterator) and self.__isNotFirstRecord(p_iterator)

    def __isNotFirstRecord(self, p_iterator):
        return p_iterator != 0

    def __isThousandRecord(self, p_iterator):
        return not (p_iterator % 1000) 

    def __readInsertCommandsForAllSpecies(self, p_outputFileName, p_outputDirName):
        l_fileHandler = open(p_outputDirName + "/" + p_outputFileName, "r")
        l_rawFileContent = l_fileHandler.read()
        l_fileHandler.close()
        return re.split('\n', l_rawFileContent)

