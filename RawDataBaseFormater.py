#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

class RawDataBaseFormater:
    def formatRawDataBase(self, p_dataBase):
        l_speciesList = self.__makeSingleSpeciesSingleListRecord(p_dataBase)

        for i in range(len(l_speciesList)):
            l_speciesList[i] = self.__removeNewLineFromSingleSpeciesRecord(l_speciesList[i])
            l_speciesList[i] = self.__removeAllTabulatorFromSingleSpeicesRecord(l_speciesList[i]) 
            l_speciesList[i] = self.__removeAllSpacesBeforeFieldsInSingeSpeciesRecord(l_speciesList[i])
            l_speciesList[i] = self.__removeSynonymsFieldFromSingleSpeciesRecord(l_speciesList[i])
            l_speciesList[i] = self.__removeBranchLabelFromSingleSpeciesRecord(l_speciesList[i])  
            l_speciesList[i] = self.__addBackslashToApostropheInSingleSpeciesRecord(l_speciesList[i])

        self.__removingEmptyRecordsFromList(l_speciesList)
        print "Formating species list finished."
        return l_speciesList

    def __removingEmptyRecordsFromList(self, p_formatedList):
        print "Removing empty elements from formated species list."
        print("List length before: " + str(len(p_formatedList)) + ".")
        p_formatedList.remove("")
        print("List length after: " + str(len(p_formatedList)) + ".")

    def __makeSingleSpeciesSingleListRecord(self, p_dataBase):
        return re.split("}{", p_dataBase); 

    def __removeNewLineFromSingleSpeciesRecord(self, p_speciesRecord):
        return re.split("\n", p_speciesRecord)

    def __removeAllTabulatorFromSingleSpeicesRecord(self, p_speciesRecord):
        return re.sub("\t", "", ''.join(p_speciesRecord)) 

    def __removeAllSpacesBeforeFieldsInSingeSpeciesRecord(self, p_speciesRecord):
        return re.sub(", ", ",", ''.join(p_speciesRecord)) 

    def __removeSynonymsFieldFromSingleSpeciesRecord(self, p_speciesRecord):
        return re.sub("\"synonyms\".*\],", "", ''.join(p_speciesRecord), 1)

    def __removeBranchLabelFromSingleSpeciesRecord(self, p_speciesRecord):
        l_speciesRecord = re.sub("\"branch\": {", "", ''.join(p_speciesRecord))
        return re.sub("}", "", ''.join(l_speciesRecord), 1)

    def __addBackslashToApostropheInSingleSpeciesRecord(self, p_speciesRecord):
        return re.sub("'", "\\'", ''.join(p_speciesRecord))

