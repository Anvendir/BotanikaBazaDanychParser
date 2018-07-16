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
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rodzina")
        return self.__getGenusName(l_latinFullName)

    def getLatinOrderName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "rzad")
        return self.__getGenusName(l_latinFullName)

    def getLatinSuperorderName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "nadrzad")
        return self.__getGenusName(l_latinFullName)

    def getLatinSubclassName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podklasa")
        return self.__getGenusName(l_latinFullName)

    def getLatinClassName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "klasa")
        return self.__getGenusName(l_latinFullName)

    def getLatinSubdivisionName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "podgromada")
        return self.__getGenusName(l_latinFullName)

    def getLatinDivisionName(self, p_speciesRecord):
        l_latinFullName = self.__getValueOfGivenFieldFromSpeciesRecord(p_speciesRecord, "gromada")
        return self.__getGenusName(l_latinFullName)

    def __getValueOfGivenFieldFromSpeciesRecord(self, p_speciesRecord, p_fieldType):
        l_fieldsFromRecordAsList = self.__splitRecordByFields(p_speciesRecord)
        l_searchedField = self.__findFieldWithItsValueForGivenType(l_fieldsFromRecordAsList, p_fieldType)

        return self.__getValueFromParFieldTypeAndValue(p_fieldType, l_searchedField)

    def __splitRecordByFields(self, p_speciesRecord):
        return re.split(',', p_speciesRecord) 

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
        l_temp = re.sub("\(.*\)\ ", "", p_rawPolishName)
        return re.sub("\ \(.*\)", "", l_temp)


