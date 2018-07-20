#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import os

class PolishDataBaseSuplementer:
    def addPolishNameToFamilyAndUpperTaxons(self, p_speciesList, p_outputDirName):
        l_polishNamesDataBase = self.__readPolishDataBase()
        
        l_singleLine = re.split("\n", l_polishNamesDataBase)
        
        l_x = re.split("\t", l_singleLine[0]) 
        print l_x[1]

    def __readPolishDataBase(self):
        l_polishNamesDataBasePath = "BazaPolskichRodzinWGore_unicode.txt"
        
        l_fileHandler = open(l_polishNamesDataBasePath, "r")
        l_polishDataBaseAsString = l_fileHandler.read()
        l_fileHandler.close()

        print l_polishNamesDataBasePath + " reading succeeded."
        
        return l_polishDataBaseAsString 


