#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

class SingleRecordDataExtractor:
    def getValueOfGivenFieldFromSpeciesRecord(self, p_speciesRecord, p_fieldType):
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
 
