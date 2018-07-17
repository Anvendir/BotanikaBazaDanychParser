#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from SingleRecordDataExtractor import SingleRecordDataExtractor

class ExcelDataBaseBuilder:
    def buildDataBase(self, p_formatedSpeciesList, p_outputDirName):
        l_outputFileName = p_outputDirName + "/excelDataBaseForImport.csv" 

        l_outputFile = open(l_outputFileName, "w")

        l_header = self.__prepareHeader()
        l_outputFile.write(l_header) 
        l_outputFile.write("\n")

        for l_speciesRecord in p_formatedSpeciesList:
            l_singleCommand = self.__prepareSingleExcelDataBaseRecordForSingleSpeciesRecord(l_speciesRecord)
            l_outputFile.write(l_singleCommand)
            l_outputFile.write(";")
            l_outputFile.write("\n")
        
        l_outputFile.close()

        print "File " + l_outputFileName + " saved."
        print "When you import this file to MS Excel remember about coding type: \"65001 : Unicode (UTF-8)\"."
       
    def __prepareHeader(self):
        l_header = "Nazwa łacinska;" + \
                   "Nazwa polska;" + \
                   "Nazwa łacinska + autorzy;" + \
                   "Autor gatunku;" + \
                   "Autor podgatunku;" + \
                   "Synantropizacja;" + \
                   "Podgatunek łacińska;" + \
                   "Podgatunek polska;" + \
                   "Gatunek łacińska;" + \
                   "Gatunek polska;" + \
                   "Rodzaj łacińska;" + \
                   "Rodzaj polska;" + \
                   "Rodzina łacińska;" + \
                   "Rodzina polska;" + \
                   "Rząd łacińska;" + \
                   "Rząd polska;" + \
                   "Nadrząd łacińska;" + \
                   "Nadrząd polska;" + \
                   "Podklasa łacińska;" + \
                   "Podklasa polska;" + \
                   "Klasa łacińska;" + \
                   "Klasa polska;" + \
                   "Podgromada łacińska;" + \
                   "Podgromada polska;" + \
                   "Gromada łacińska;" + \
                   "Gromada polska;" + \
                   "Królestwo łacińska;" + \
                   "Królestwo polska;"
        return l_header;

    def __prepareSingleExcelDataBaseRecordForSingleSpeciesRecord(self, p_speciesRecord):
        l_dataExtractor = SingleRecordDataExtractor() 

        l_latinName = l_dataExtractor.getLatinName(p_speciesRecord)
        l_polishName = l_dataExtractor.getPolishName(p_speciesRecord)
        l_latinNamePlusAuthor = l_dataExtractor.getLatinNameWithAuthor(p_speciesRecord)
        l_author = l_dataExtractor.getSpeciesAuthor(p_speciesRecord)
        l_authorSubsp = l_dataExtractor.getSubspeciesAuthor(p_speciesRecord)
        l_synantrop = l_dataExtractor.getSynantrop(p_speciesRecord)

        l_systemathicHierarchy = self.__prepareSystematicHierarchy(p_speciesRecord)

        l_valuesFromAllFields = l_latinName + ";" + \
                                l_polishName + ";" + \
                                l_latinNamePlusAuthor + ";" + \
                                l_author + ";" + \
                                l_authorSubsp + ";" + \
                                l_synantrop + ";" + \
                                l_systemathicHierarchy

        return l_valuesFromAllFields 

    def __prepareSystematicHierarchy(self, p_speciesRecord):
        l_dataExtractor = SingleRecordDataExtractor() 

        l_subSpeciesLatin = l_dataExtractor.getLatinSubspeciesName(p_speciesRecord)
        l_subSpeciesPolish = l_dataExtractor.getPolishSubspeciesName(p_speciesRecord)
        l_speciesLatin = l_dataExtractor.getLatinSpeciesName(p_speciesRecord)
        l_speciesPolish = l_dataExtractor.getPolishSpeciesName(p_speciesRecord)
        l_genusLatin = l_dataExtractor.getLatinGenusName(p_speciesRecord)
        l_genusPolish = l_dataExtractor.getPolishGenusName(p_speciesRecord)
        l_family = l_dataExtractor.getLatinFamilyName(p_speciesRecord)
        l_familyPolish = ""
        l_order = l_dataExtractor.getLatinOrderName(p_speciesRecord)
        l_orderPolish = ""
        l_superorder = l_dataExtractor.getLatinSuperorderName(p_speciesRecord)
        l_superorderPolish = "" 
        l_subclass = l_dataExtractor.getLatinSubclassName(p_speciesRecord)
        l_subclassPolish = ""
        l_class_ = l_dataExtractor.getLatinClassName(p_speciesRecord)
        l_classPolish = ""
        l_subdivision = l_dataExtractor.getLatinSubdivisionName(p_speciesRecord)
        l_subdivisionPolish = ""
        l_division = l_dataExtractor.getLatinDivisionName(p_speciesRecord)
        l_divisionPolish = ""
        l_realm = ""
        l_realmPolish = ""

        l_systemathicHierarchy = l_subSpeciesLatin + ";" + \
                                 l_subSpeciesPolish + ";" + \
                                 l_speciesLatin + ";" + \
                                 l_speciesPolish + ";" + \
                                 l_genusLatin + ";" + \
                                 l_genusPolish + ";" + \
                                 l_family + ";" + \
                                 l_familyPolish + ";" + \
                                 l_order + ";" + \
                                 l_orderPolish + ";" + \
                                 l_superorder + ";" + \
                                 l_superorderPolish + ";" + \
                                 l_subclass + ";" + \
                                 l_subclassPolish + ";" + \
                                 l_class_ + ";" + \
                                 l_classPolish + ";" + \
                                 l_subdivision + ";" + \
                                 l_subdivisionPolish + ";" + \
                                 l_division + ";" + \
                                 l_divisionPolish + ";" + \
                                 l_realm + ";" + \
                                 l_realmPolish

        return l_systemathicHierarchy 

