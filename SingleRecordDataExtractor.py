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
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinFamilyName, "FAMILY")

    def getLatinOrderName(self, p_speciesRecord):
        l_latinOrderName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rzad")
        return l_latinOrderName

    def getPolishOrderName(self, p_speciesRecord):
        l_latinOrderName = self.getLatinOrderName(p_speciesRecord)
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinOrderName, "ORDER")

    def getLatinSuperorderName(self, p_speciesRecord):
        l_latinSuperorderName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "nadrzad")
        return l_latinSuperorderName

    def getPolishSuperorderName(self, p_speciesRecord):
        l_latinSuperorderName = self.getLatinSubclassName(p_speciesRecord)
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinSuperorderName, "SUPERORDER")

    def getLatinSubclassName(self, p_speciesRecord):
        l_subClassFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podklasa")
        return l_subClassFullName

    def getPolishSubclassName(self, p_speciesRecord):
        l_latinSubclassName = self.getLatinSubclassName(p_speciesRecord)
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinSubclassName, "SUBCLASS")

    def getLatinClassName(self, p_speciesRecord):
        l_latinClassName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "klasa")
        return l_latinClassName

    def getPolishClassName(self, p_speciesRecord):
        l_latinClassName = self.getLatinClassName(p_speciesRecord)
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinClassName, "CLASS")

    def getLatinSubdivisionName(self, p_speciesRecord):
        l_latinSubdivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgromada")
        return l_latinSubdivisionName

    def getPolishSubdivisionName(self, p_speciesRecord):
        l_latinSubdivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgromada")
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinSubdivisionName, "SUBDIVISION")

    def getLatinDivisionName(self, p_speciesRecord):
        l_latinDivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")
        return l_latinDivisionName

    def getPolishDivisionName(self, p_speciesRecord):
        l_latinDivisionName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinDivisionName, "DIVISION")

    def getLatinRealmName(self, p_speciesRecord):
        l_polishDataBase = self.__readPolishDataBase()
        l_listWhereSingleLineIsSingleListElement = self.__splitFileByLines(l_polishDataBase)
        
        l_exampleDataRecord = l_listWhereSingleLineIsSingleListElement[1]
        l_lineSplitedByRecords = self.__splitLineByRecords(l_exampleDataRecord)
        return self.__getValueFromPolishDatabaseSingleLine(l_lineSplitedByRecords, self.__RECORD_INDEX["REALM_LATIN"])

    def getPolishRealmName(self, p_speciesRecord):
        l_latinRealmName = self.getLatinRealmName(p_speciesRecord)
        return self.__getValueOfGivenFieldFromPolishDataBase(l_latinRealmName, "REALM")

    __RECORD_INDEX = {'FAMILY_PL': 0, 'FAMILY_LATIN': 1, \
               'ORDER_PL': 2, 'ORDER_LATIN': 3, \
               'SUPERORDER_PL': 4, 'SUPERORDER_LATIN': 5, \
               'SUBCLASS_PL': 6, 'SUBCLASS_LATIN': 7, \
               'CLASS_PL': 8, 'CLASS_LATIN': 9, \
               'SUBDIVISION_PL': 10, 'SUBDIVISION_LATIN': 11, \
               'DIVISION_PL': 12, 'DIVISION_LATIN': 13, \
               'REALM_PL': 14, 'REALM_LATIN': 15, \
              }

    def __getValueOfGivenFieldFromPolishDataBase(self, p_latinName, p_recordType):
        l_rawPolishDataBase = self.__readPolishDataBase()
        l_singleLineAsSingleListElement = self.__splitFileByLines(l_rawPolishDataBase) 
        
        l_polishRecordIndex = self.__RECORD_INDEX[p_recordType + "_PL"]
        l_latinRecordIndex = self.__RECORD_INDEX[p_recordType + "_LATIN"]

        for l_singleLine in l_singleLineAsSingleListElement:
            l_lineSplitedByRecords = self.__splitLineByRecords(l_singleLine)

            if self.__getValueFromPolishDatabaseSingleLine(l_lineSplitedByRecords, l_latinRecordIndex) == p_latinName:
                return self.__getValueFromPolishDatabaseSingleLine(l_lineSplitedByRecords, l_polishRecordIndex)

        return ""

    def __getValueFromPolishDatabaseSingleLine(self, p_lineSplitedByRecords, p_index):
        return p_lineSplitedByRecords[p_index]

    def __removeWindowsEndLineCharacters(self, p_polishNameDataBaseAsString):
        return re.sub("\r", "", p_polishNameDataBaseAsString)

    def __splitLineByRecords(self, p_singleLineFromPolishDataBase):
        return re.split("\t", p_singleLineFromPolishDataBase)

    def __splitFileByLines(self, p_polishNameDataBaseAsString):
        l_preprocessedDataBase = self.__removeWindowsEndLineCharacters(p_polishNameDataBaseAsString)
        l_splitedList = re.split("\n", l_preprocessedDataBase)
        l_splitedList.pop()
        return l_splitedList

    def __readPolishDataBase(self):
        l_polishNamesDataBasePath = "BazaPolskichRodzinWGore_unicode.txt"

        l_fileHandler = open(l_polishNamesDataBasePath, "r")
        l_polishDataBaseAsString = l_fileHandler.read().decode('utf-16le').encode('utf-8')
        l_fileHandler.close()
        
        return l_polishDataBaseAsString 

    def __removeBrackleBracketsFromRecord(self, p_speciesRecord):
        l_openBrackleBracketRemoved = re.sub("{", "", p_speciesRecord)
        l_closeBrackleBracketRemoved = re.sub("}", "", l_openBrackleBracketRemoved)
        return l_closeBrackleBracketRemoved 

    def __getValueOfGivenFieldFromSpeciesRecord(self, p_speciesRecord, p_fieldType):
        l_preprocessedSpeciesRecord = self.__removeBrackleBracketsFromRecord(p_speciesRecord)
        l_fieldsFromRecordAsList = self.__splitRecordByFields(l_preprocessedSpeciesRecord)
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

    
