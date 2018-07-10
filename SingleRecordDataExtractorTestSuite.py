#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import unittest

from SingleRecordDataExtractor import SingleRecordDataExtractor 

g_abiesCephalonica_correctRecord = '''"nr_kol": 2,"rodz_id": 607,"rodzaj": "Abies","nzw_gat": "cephalonica","gatunek": "Abies cephalonica","autor_gat": "Loudon","n_lacinska": "Abies cephalonica Loudon","n_polska": "Jodła grecka","synantrop": "U","rodzina": "Pinaceae","rzad": "Pinales","nadrzad": "","podklasa": "","klasa": "Coniferopsida","podgromada": "Gymnospermae","gromada": "Spermatophyta"'''

class SingleRecordDataExtractorTestSuite(unittest.TestCase):
    def testIfSingleRecordDataExtractorIsCreatedProperly(self):
        m_sut = SingleRecordDataExtractor()
   
    def testIfExtractingValueOfLatinNameFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinName(g_abiesCephalonica_correctRecord)
        assert l_result == "Abies cephalonica", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_abiesCephalonica_correctRecord)
        assert l_result == "Jodła grecka", "Actual value: " + l_result

    def testIfExtractingValueOfLatinNamePlusAuthorFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinNameWithAuthor(g_abiesCephalonica_correctRecord)
        assert l_result == "Abies cephalonica Loudon", "Actual value: " + l_result

    def testIfExtractingValueOfAuthorFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getSpeciesAuthor(g_abiesCephalonica_correctRecord)
        assert l_result == "Loudon", "Actual value: " + l_result

    def testIfExtractingValueOfAuthorSubspFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getSubspeciesAuthor(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSynantropFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getSynantrop(g_abiesCephalonica_correctRecord)
        assert l_result == "U", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubspeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSubspeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSpeciesInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSpeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "cephalonica", "Actual value: " + l_result

    def testIfExtractingValueOfSpeciesInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSpeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "grecka", "Actual value: " + l_result

    def testIfExtractingValueOfGenusInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinGenusName(g_abiesCephalonica_correctRecord)
        assert l_result == "Abies", "Actual value: " + l_result

    def testIfExtractingValueOfGenusInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishGenusName(g_abiesCephalonica_correctRecord)
        assert l_result == "Jodła", "Actual value: " + l_result

    def testIfExtractingValueOfFamilyInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinFamilyName(g_abiesCephalonica_correctRecord)
        assert l_result == "Pinaceae", "Actual value: " + l_result

    def testIfExtractingValueOfOrderInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinOrderName(g_abiesCephalonica_correctRecord)
        assert l_result == "Pinales", "Actual value: " + l_result

    def testIfExtractingValueOfSuperorderInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSuperorderName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubclassInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubclassName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfClassInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinClassName(g_abiesCephalonica_correctRecord)
        assert l_result == "Coniferopsida", "Actual value: " + l_result

    def testIfExtractingValueOfSubdivisionInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubdivisionName(g_abiesCephalonica_correctRecord)
        assert l_result == "Gymnospermae", "Actual value: " + l_result

    def testIfExtractingValueOfDivisionInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinDivisionName(g_abiesCephalonica_correctRecord)
        assert l_result == "Spermatophyta", "Actual value: " + l_result

if __name__ == "__main__":
    unittest.main()
