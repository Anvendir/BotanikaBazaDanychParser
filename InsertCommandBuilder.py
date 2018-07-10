#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
from SingleRecordDataExtractor import SingleRecordDataExtractor

class InsertCommandBuilder:
    def prepareInsertCommandsForSpeciesList(self, p_formatedSpeciesList, p_outputDirName):
        l_outputFileName = p_outputDirName + "/insertCommandsForAllSpeciesList.txt" 
        l_outputFile = open(l_outputFileName, "w")

        for l_speciesRecord in p_formatedSpeciesList:
            l_singleCommand = self.__prepareInsertCommandForSingleSpeciesRecord(l_speciesRecord)
            l_outputFile.write(l_singleCommand)
            l_outputFile.write(";")
            l_outputFile.write("\n")
        
        l_outputFile.close()

        print "File " + l_outputFileName + " saved."

    def __prepareInsertCommandForSingleSpeciesRecord(self, p_speciesRecord):
        l_insertCommandName = "INSERT INTO"
        l_tableSystematykaName = "`systematyka`"
        l_tableSystematykaFieldsNames = self.__prepareTableSystematykaFieldsName() 
        l_valuesPartInInsertCommand = self.__prepareValuesPartInInsertCommand(p_speciesRecord)

        l_insertCommandForSingleSpecies = l_insertCommandName + " " + \
                                          l_tableSystematykaName + " " + \
                                          l_tableSystematykaFieldsNames + " " + \
                                          l_valuesPartInInsertCommand 

        return l_insertCommandForSingleSpecies 

    def __prepareValuesPartInInsertCommand(self, p_speciesRecord):
        l_valuesFromAllFields = self.__prepareValuesFromAllFields(p_speciesRecord)
        l_valuesPartInInsertCommand = "VALUES (NULL, " + l_valuesFromAllFields + ")"
        return l_valuesPartInInsertCommand 

    def __prepareTableSystematykaFieldsName(self):
        return "(`id`," + \
               " `nazwa lacinska`," + \
               " `nazwa polska`," \
               " `nazwa lacinska + autor`," \
               " `autor`," \
               " `autor podgatunku`," \
               " `synantrop`," \
               " `podgatunek`," \
               " `podgatunek_pl`," \
               " `gatunek`," \
               " `gatunek_pl`," \
               " `rodzaj`," \
               " `rodzaj_pl`," \
               " `rodzina`," \
               " `rzad`," \
               " `nadrzad`," \
               " `podklasa`," \
               " `klasa`," \
               " `podgromada`," \
               " `gromada`)"

    def __prepareValuesFromAllFields(self, p_speciesRecord):
        l_dataExtractor = SingleRecordDataExtractor() 

        l_latinName = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinName(p_speciesRecord))
        l_polishName = self.__formatFieldValueForInsertCommand(l_dataExtractor.getPolishName(p_speciesRecord))
        l_latinNamePlusAuthor = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinNameWithAuthor(p_speciesRecord))
        l_author = self.__formatFieldValueForInsertCommand(l_dataExtractor.getSpeciesAuthor(p_speciesRecord))
        l_authorSubsp = self.__formatFieldValueForInsertCommand(l_dataExtractor.getSubspeciesAuthor(p_speciesRecord)) 
        l_synantrop = self.__formatFieldValueForInsertCommand(l_dataExtractor.getSynantrop(p_speciesRecord))

        l_systemathicHierarchy = self.__prepareSystematicHierarchy(p_speciesRecord)

        l_valuesFromAllFields = l_latinName + ", " + \
                                l_polishName + ", " + \
                                l_latinNamePlusAuthor + ", " + \
                                l_author + ", " + \
                                l_authorSubsp + ", " + \
                                l_synantrop + ", " + \
                                l_systemathicHierarchy

        return l_valuesFromAllFields 

    def __prepareSystematicHierarchy(self, p_speciesRecord):
        l_dataExtractor = SingleRecordDataExtractor() 

        l_subSpeciesLatin = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinSubspeciesName(p_speciesRecord))
        l_subSpeciesPolish = self.__formatFieldValueForInsertCommand(l_dataExtractor.getPolishSubspeciesName(p_speciesRecord))
        l_speciesLatin = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinSpeciesName(p_speciesRecord))
        l_speciesPolish = self.__formatFieldValueForInsertCommand(l_dataExtractor.getPolishSpeciesName(p_speciesRecord))
        l_genusLatin = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinGenusName(p_speciesRecord))
        l_genusPolish = self.__formatFieldValueForInsertCommand(l_dataExtractor.getPolishGenusName(p_speciesRecord))
        l_family = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinFamilyName(p_speciesRecord))
        l_order = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinOrderName(p_speciesRecord))
        l_superorder = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinSuperorderName(p_speciesRecord))
        l_subclass = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinSubclassName(p_speciesRecord))
        l_class_ = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinClassName(p_speciesRecord))
        l_subdivision = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinSubdivisionName(p_speciesRecord))
        l_division = self.__formatFieldValueForInsertCommand(l_dataExtractor.getLatinDivisionName(p_speciesRecord))

        l_systemathicHierarchy = l_subSpeciesLatin + ", " + \
                                 l_subSpeciesPolish + ", " + \
                                 l_speciesLatin + ", " + \
                                 l_speciesPolish + ", " + \
                                 l_genusLatin + ", " + \
                                 l_genusPolish + ", " + \
                                 l_family + ", " + \
                                 l_order + ", " + \
                                 l_superorder + ", " + \
                                 l_subclass + ", " + \
                                 l_class_ + ", " + \
                                 l_subdivision + ", " + \
                                 l_division

        return l_systemathicHierarchy 

    def __formatFieldValueForInsertCommand(self, p_fieldValue):
        formatedValue = "'" + p_fieldValue + "'"
        return formatedValue

