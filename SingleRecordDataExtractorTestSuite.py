#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import unittest

from SingleRecordDataExtractor import SingleRecordDataExtractor 

g_abiesCephalonica_correctRecord = '''"nr_kol": 2,"rodz_id": 607,"rodzaj": "Abies","nzw_gat": "cephalonica","gatunek": "Abies cephalonica","autor_gat": "Loudon","n_lacinska": "Abies cephalonica Loudon","n_polska": "Jodła grecka","synantrop": "U","rodzina": "Pinaceae","rzad": "Pinales","nadrzad": "","podklasa": "","klasa": "Coniferopsida","podgromada": "Gymnospermae","gromada": "Spermatophyta"'''

class SingleRecordDataExtractorTestSuite(unittest.TestCase):
    def testIfSingleRecordDataExtractorIsCreatedProperly(self):
        m_sut = SingleRecordDataExtractor()
    
    def testIfExtractingValueOfGenusInLatinFieldWorksForSimmpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getValueOfGivenFieldFromSpeciesRecord(g_abiesCephalonica_correctRecord, "rodzaj")
        assert l_result == "Abies", "Actual value: " + l_result

if __name__ == "__main__":
    unittest.main()
