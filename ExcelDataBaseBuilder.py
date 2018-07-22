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
            l_outputFile.write("\n")
        
        l_outputFile.close()

        print "File " + l_outputFileName + " saved."
        print "When you import this file to MS Excel remember about coding type: \"65001 : Unicode (UTF-8)\"."
       
    def __prepareHeader(self):
        l_header = "Nazwa polska (1);" + \
                   "Nazwa łacinska (2);" + \
                   "Nazwa łacinska + autorzy (3);" + \
                   "Autor gatunku (4);" + \
                   "Autor podgatunku (5);" + \
                   "Synantropizacja (6);" + \
                   "Podgatunek polska (7);" + \
                   "Podgatunek łacińska (8);" + \
                   "Gatunek polska (9);" + \
                   "Gatunek łacińska (10);" + \
                   "Rodzaj polska (11);" + \
                   "Rodzaj łacińska (12);" + \
                   "Rodzina polska (13);" + \
                   "Rodzina łacińska (14);" + \
                   "Rząd polska (15);" + \
                   "Rząd łacińska (16);" + \
                   "Nadrząd polska (17);" + \
                   "Nadrząd łacińska (18);" + \
                   "Podklasa polska (19);" + \
                   "Podklasa łacińska (20);" + \
                   "Klasa polska (21);" + \
                   "Klasa łacińska (22);" + \
                   "Podgromada polska (23);" + \
                   "Podgromada łacińska (24);" + \
                   "Gromada polska (25);" + \
                   "Gromada łacińska (26);" + \
                   "Królestwo polska (27);" + \
                   "Królestwo łacińska (28);"
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

        l_valuesFromAllFields = l_polishName + ";" + \
                                l_latinName + ";" + \
                                l_latinNamePlusAuthor + ";" + \
                                l_author + ";" + \
                                l_authorSubsp + ";" + \
                                l_synantrop + ";" + \
                                l_systemathicHierarchy

        return l_valuesFromAllFields 

    def __prepareSystematicHierarchy(self, p_speciesRecord):
        l_dataExtractor = SingleRecordDataExtractor() 

        l_subSpeciesPolish = l_dataExtractor.getPolishSubspeciesName(p_speciesRecord)
        l_subSpeciesLatin = l_dataExtractor.getLatinSubspeciesName(p_speciesRecord)

        l_speciesPolish = l_dataExtractor.getPolishSpeciesName(p_speciesRecord)
        l_speciesLatin = l_dataExtractor.getLatinSpeciesName(p_speciesRecord)

        l_genusPolish = l_dataExtractor.getPolishGenusName(p_speciesRecord)
        l_genusLatin = l_dataExtractor.getLatinGenusName(p_speciesRecord)

        l_familyPolish = l_dataExtractor.getPolishFamilyName(p_speciesRecord) 
        l_family = l_dataExtractor.getLatinFamilyName(p_speciesRecord)

        l_orderPolish = l_dataExtractor.getPolishOrderName(p_speciesRecord)
        l_order = l_dataExtractor.getLatinOrderName(p_speciesRecord)

        l_superorderPolish = l_dataExtractor.getPolishSuperorderName(p_speciesRecord)
        l_superorder = l_dataExtractor.getLatinSuperorderName(p_speciesRecord)

        l_subclassPolish = l_dataExtractor.getPolishSubclassName(p_speciesRecord)
        l_subclass = l_dataExtractor.getLatinSubclassName(p_speciesRecord)

        l_classPolish = l_dataExtractor.getPolishClassName(p_speciesRecord)
        l_class_ = l_dataExtractor.getLatinClassName(p_speciesRecord)

        l_subdivisionPolish = l_dataExtractor.getPolishSubdivisionName(p_speciesRecord)
        l_subdivision = l_dataExtractor.getLatinSubdivisionName(p_speciesRecord)

        l_divisionPolish = l_dataExtractor.getPolishDivisionName(p_speciesRecord)
        l_division = l_dataExtractor.getLatinDivisionName(p_speciesRecord)

        l_realmPolish = l_dataExtractor.getPolishRealmName(p_speciesRecord)
        l_realm = l_dataExtractor.getLatinRealmName(p_speciesRecord)

        l_systemathicHierarchy = l_subSpeciesPolish + ";" + \
                                 l_subSpeciesLatin + ";" + \
                                 l_speciesPolish + ";" + \
                                 l_speciesLatin + ";" + \
                                 l_genusPolish + ";" + \
                                 l_genusLatin + ";" + \
                                 l_familyPolish + ";" + \
                                 l_family + ";" + \
                                 l_orderPolish + ";" + \
                                 l_order + ";" + \
                                 l_superorderPolish + ";" + \
                                 l_superorder + ";" + \
                                 l_subclassPolish + ";" + \
                                 l_subclass + ";" + \
                                 l_classPolish + ";" + \
                                 l_class_ + ";" + \
                                 l_subdivisionPolish + ";" + \
                                 l_subdivision + ";" + \
                                 l_divisionPolish + ";" + \
                                 l_division + ";" + \
                                 l_realmPolish + ";" + \
                                 l_realm + ";"

        return l_systemathicHierarchy 

