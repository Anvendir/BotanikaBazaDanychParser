#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

class SingleRecordDataExtractor:
    def getLatinName(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gatunek")

    def getPolishName(self, p_speciesRecord):
        l_rawPolishName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "n_polska")
        return self.__removeAdditionalNameInBracketsIfNeeded(l_rawPolishName)

    def getLatinNameWithAuthor(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "n_lacinska")

    def getSpeciesAuthor(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "autor_gat")

    def getSubspeciesAuthor(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "autor_pgat")

    def getSynantrop(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "synantrop")

    def getLatinSubspeciesName(self, p_speciesRecord):
        l_latinSubspieciesNameWithPrefix = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgatunek")
        return re.sub("subsp. ", "", l_latinSubspieciesNameWithPrefix)

    def getPolishSubspeciesName(self, p_speciesRecord):
        if "" == self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgatunek"):
            return ""

        l_polishFullName = self.getPolishName(p_speciesRecord)
        return self.__getSubspeciesName(l_polishFullName)
   
    def getLatinSpeciesName(self, p_speciesRecord):
        return self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "nzw_gat")

    def getPolishSpeciesName(self, p_speciesRecord):
        l_polishFullName = self.getPolishName(p_speciesRecord)
        return self.__getSpeciesName(l_polishFullName)

    def getLatinGenusName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gatunek")
        return self.__getGenusName(l_latinFullName)

    def getPolishGenusName(self, p_speciesRecord):
        l_polishFullName = self.getPolishName(p_speciesRecord)
        return self.__getGenusName(l_polishFullName)

    def getLatinFamilyName(self, p_speciesRecord):
        l_latinFamily = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rodzina")
        return l_latinFamily

    def getPolishFamilyName(self, p_speciesRecord):
        l_latinFamilyName = self.getLatinFamilyName(p_speciesRecord)
        l_polishDataBase = self.__readPolishDataBase()

        l_listWhereSingleLineIsSingleListElement = self.__getFileAsListSingleLineAsSingleListElement(l_polishDataBase) 
        
        for l_singleLine in l_listWhereSingleLineIsSingleListElement:
            l_lineSplitedByRecords = re.split("\t", l_singleLine)
            if self.__getLatinFamilyNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords) == l_latinFamilyName:
                return self.__getPolishFamilyNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords)

        return ""

    def getLatinOrderName(self, p_speciesRecord):
        l_latinOrderName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rzad")
        return l_latinOrderName

    def getPolishOrderName(self, p_speciesRecord):
        l_latinOrderName = self.getLatinOrderName(p_speciesRecord)
        l_polishDataBase = self.__readPolishDataBase()

        l_listWhereSingleLineIsSingleListElement = self.__getFileAsListSingleLineAsSingleListElement(l_polishDataBase) 
        
        for l_singleLine in l_listWhereSingleLineIsSingleListElement:
            l_lineSplitedByRecords = re.split("\t", l_singleLine)
            if self.__getLatinOrderNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords) == l_latinOrderName:
                return self.__getPolishOrderNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords)

        return ""

    def getLatinSuperorderName(self, p_speciesRecord):
        l_latinSuperorderName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "nadrzad")
        return l_latinSuperorderName

    def getLatinSubclassName(self, p_speciesRecord):
        l_subClassFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podklasa")
        return l_subClassFullName

    def getLatinClassName(self, p_speciesRecord):
        l_latinClassName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "klasa")
        return l_latinClassName

    def getPolishClassName(self, p_speciesRecord):
        l_latinClassName = self.getLatinClassName(p_speciesRecord)
        l_polishDataBase = self.__readPolishDataBase()

        l_listWhereSingleLineIsSingleListElement = self.__getFileAsListSingleLineAsSingleListElement(l_polishDataBase) 
        
        for l_singleLine in l_listWhereSingleLineIsSingleListElement:
            l_lineSplitedByRecords = re.split("\t", l_singleLine)
            if self.__getLatinClassNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords) == l_latinClassName:
                return self.__getPolishClassNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords)

        return ""

    def getLatinSubdivisionName(self, p_speciesRecord):
        l_latinSubdivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgromada")
        return l_latinSubdivisionName

    def getLatinDivisionName(self, p_speciesRecord):
        l_latinDivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")
        return l_latinDivisionName

    def getPolishDivisionName(self, p_speciesRecord):
        l_latinDivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")
        l_polishDataBase = self.__readPolishDataBase()

        l_listWhereSingleLineIsSingleListElement = self.__getFileAsListSingleLineAsSingleListElement(l_polishDataBase) 
        
        for l_singleLine in l_listWhereSingleLineIsSingleListElement:
            l_lineSplitedByRecords = re.split("\t", l_singleLine)
            if self.__getLatinDivisionNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords) == l_latinDivisionName:
                return self.__getPolishDivisionNameFromSinglePolishDataBaseLine(l_lineSplitedByRecords)

        return ""

    def __getLatinFamilyNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[1]

    def __getPolishFamilyNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[0]

    def __getLatinOrderNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[3]

    def __getPolishOrderNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[2]

    def __getLatinClassNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[9]

    def __getPolishClassNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[8]

    def __getLatinDivisionNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[13]

    def __getPolishDivisionNameFromSinglePolishDataBaseLine(self, p_polishDataBaseLineSplitedByRecords):
        return p_polishDataBaseLineSplitedByRecords[12]

    def __getFileAsListSingleLineAsSingleListElement(self, p_polishNameDataBase):
        return re.split("\n", p_polishNameDataBase) 

    def __readPolishDataBase(self):
        l_polishNamesDataBasePath = "BazaPolskichRodzinWGore_unicode.txt"

        l_fileHandler = open(l_polishNamesDataBasePath, "r")
        l_polishDataBaseAsString = l_fileHandler.read().decode('utf-16le').encode('utf-8')
        l_fileHandler.close()
        
        return l_polishDataBaseAsString 

    def __getValueOfGivenFieldFromSpeciesRecord(self, p_speciesRecord, p_fieldType):
        l_fieldsFromRecordAsList = self.__splitRecordByFields(p_speciesRecord)
        l_searchedField = self.__findFieldWithItsValueForGivenType(l_fieldsFromRecordAsList, p_fieldType)

        return self.__getValueFromParFieldTypeAndValue(p_fieldType, l_searchedField)

    def __replFunctionForRemoveNotSeparatorCommas(self, p_matchObject):
        if p_matchObject.group(0) == ',\"':
            return ',\"'
        else:
            return ' '

    def __changeCommaWhichAreNotFieldsSeparatorsWithSpace(self, p_speciesRecord):
        return re.sub(',.', self.__replFunctionForRemoveNotSeparatorCommas, p_speciesRecord)

    def __splitRecordByFields(self, p_speciesRecord):
        l_preprocessedSpeciesRecord = self.__changeCommaWhichAreNotFieldsSeparatorsWithSpace(p_speciesRecord)
        return re.split(',', l_preprocessedSpeciesRecord) 

    def __findFieldWithItsValueForGivenType(self, p_fieldsFromRecordAsList, p_fieldType):
        l_searchedField = ""
        for l_field in p_fieldsFromRecordAsList:
            if re.search("\"" + p_fieldType + "\": ", l_field):
                l_searchedField = l_field 
                break

        return l_searchedField

    def __getValueFromParFieldTypeAndValue(self, p_fieldType, p_fieldTypeAndValuePar):
        l_valueOfFieldWithQuotes = re.sub("\"" + p_fieldType + "\": ", "", p_fieldTypeAndValuePar)
        return self.__removeQuotesFromValue(l_valueOfFieldWithQuotes)

    def __removeQuotesFromValue(self, p_fieldWithQuotes):
        return re.sub("\"", "", p_fieldWithQuotes)

    def __getSubspeciesName(self, p_fullName):
        l_nameAsListFirstElementGenusSecondSpeciesThirdSubSpecies = re.split(" ", p_fullName)

        if 3 <= len(l_nameAsListFirstElementGenusSecondSpeciesThirdSubSpecies):
            return l_nameAsListFirstElementGenusSecondSpeciesThirdSubSpecies[2]
        else:
            return ""
 
    def __getSpeciesName(self, p_fullName):
        l_nameAsListFirstElementGenusSecondSpecies = re.split(" ", p_fullName)

        if 2 <= len(l_nameAsListFirstElementGenusSecondSpecies):
            return l_nameAsListFirstElementGenusSecondSpecies[1]
        else:
            return ""

    def __getGenusName(self, p_fullName):
        l_nameAsListFirstElementGenusSecondSpecies = re.split(" ", p_fullName)
        
        if 1 <= len(l_nameAsListFirstElementGenusSecondSpecies):
            return l_nameAsListFirstElementGenusSecondSpecies[0]
        else:
            return ""

    def __removeAdditionalNameInBracketsIfNeeded(self, p_rawPolishName):
        l_doubleBacketWithSpaceBeforeRegex = r' \(.*\(.*\).*\)'
        l_preprocessed = re.sub(l_doubleBacketWithSpaceBeforeRegex, "", p_rawPolishName)

        l_doubleBacketWithSpaceAfterRegex = r'\(.*\(.*\).*\) '
        l_preprocessed = re.sub(l_doubleBacketWithSpaceAfterRegex, "", l_preprocessed)

        l_bracketsWithSpaceAfterRegex = r'\(.*\) '
        l_preprocessed = re.sub(l_bracketsWithSpaceAfterRegex, "", l_preprocessed)

        l_bracketWithSpaceBeforeRegex = r' \(.*\)'
        return re.sub(l_bracketWithSpaceBeforeRegex, "", l_preprocessed)

    
