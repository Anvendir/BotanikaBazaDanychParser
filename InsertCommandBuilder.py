#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

class InsertCommandBuilder:
    def prepareInsertCommandsForSpeciesList(self, p_formatedSpeciesList):
        l_outputFileName = "insertCommandsForAllSpeciesList.txt" 
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
                " `synantrop`," \
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
        l_latinName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gatunek")
        l_polishName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "n_polska")
        l_latinNamePlusAuthor = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "n_lacinska")
        l_author = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "autor_gat") 
        l_synantrop = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "synantrop")

        l_systemathicHierarchy = self.__prepareSystematicHierarchy(p_speciesRecord, l_latinName, l_polishName)

        l_valuesFromAllFields = l_latinName + ", " + \
                                l_polishName + ", " + \
                                l_latinNamePlusAuthor + ", " + \
                                l_author + ", " + \
                                l_synantrop + ", " + \
                                l_systemathicHierarchy

        return l_valuesFromAllFields 

    def __prepareSystematicHierarchy(self, p_speciesRecord, p_latinName, p_polishName):
        l_speciesLatin = self.__getSpeciesNameFromName(p_latinName)
        l_speciesPolish = self.__getSpeciesNameFromName(p_polishName)
        l_genusLatin = self.__getGenusNameFromName(p_latinName)
        l_genusPolish = self.__getGenusNameFromName(p_polishName)
        l_family = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rodzina")
        l_order = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rzad")
        l_superorder = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "nadrzad")
        l_subclass = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podklasa")
        l_class_ = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "klasa")
        l_subdivision = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgromada")
        l_division = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")

        l_systemathicHierarchy = l_speciesLatin + ", " + \
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

    def __getSpeciesNameFromName(self, p_name):
        l_nameAsListFirstElementGenusSecondSpecies = re.split(" ", p_name)

        if 2 == len(l_nameAsListFirstElementGenusSecondSpecies):
            return "'" + l_nameAsListFirstElementGenusSecondSpecies[1]
        else:
            return "''"

    def __getGenusNameFromName(self, p_name):
        l_nameAsListFirstElementGenusSecondSpecies = re.split(" ", p_name)
        
        if 2 == len(l_nameAsListFirstElementGenusSecondSpecies):
            return l_nameAsListFirstElementGenusSecondSpecies[0] + "'"
        else:
            return "''"

    def __formatFieldValueForInsertCommand(self, p_fieldValue):
        formatedValue = "'" + p_fieldValue + "'"
        return formatedValue

    def __getValueOfGivenFieldFromSpeciesRecord(self, p_speciesRecord, p_fieldType):
        l_fieldsFromSingleSpiecesRecordsList = re.split(',', p_speciesRecord)
        
        l_searchedField = ""
        for l_field in l_fieldsFromSingleSpiecesRecordsList:
            if re.search("\"" + p_fieldType + "\": ", l_field):
                l_searchedField = l_field 
                break

        l_valueOfFieldWithQuotes = re.sub("\"" + p_fieldType + "\": ", "", l_searchedField)
        l_valueOfField = re.sub("\"", "", l_valueOfFieldWithQuotes)
        return self.__formatFieldValueForInsertCommand(l_valueOfField)

