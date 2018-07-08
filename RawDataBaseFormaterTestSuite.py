#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import unittest
from RawDataBaseFormater import RawDataBaseFormater 

g_readedDataBaseRecord = """
}{
	"nr_kol": 2, "rodz_id": 607, "rodzaj": "Abies",
	"nzw_gat": "cephalonica", "gatunek": "Abies cephalonica", "autor_gat": "Loudon",
	"n_lacinska": "Abies cephalonica Loudon", "n_polska": "Jodła grecka",
	"synantrop": "U",
	"synonyms": [
	],
	"branch": {
		"rodzina": "Pinaceae",
		"rzad": "Pinales",
		"nadrzad": "",
		"podklasa": "",
		"klasa": "Coniferopsida",
		"podgromada": "Gymnospermae",
		"gromada": "Spermatophyta"
	}
}{
	"nr_kol": 3, "rodz_id": 607, "rodzaj": "Abies",
	"nzw_gat": "concolor", "gatunek": "Abies concolor", "autor_gat": "(Gordon) Lindl. ex Hildebr.",
	"n_lacinska": "Abies concolor (Gordon) Lindl. ex Hildebr.", "n_polska": "Jodła jednobarwna (J. kalifornijska)",
	"synantrop": "U",
	"synonyms": [
	],
	"branch": {
		"rodzina": "Pinaceae",
		"rzad": "Pinales",
		"nadrzad": "",
		"podklasa": "",
		"klasa": "Coniferopsida",
		"podgromada": "Gymnospermae",
		"gromada": "Spermatophyta"
	}
}{
"""

class RawDataBaseFormaterTestuite(unittest.TestCase):
    def testRawDataBaseFormaterCreatesProperly(self):
        m_sut = RawDataBaseFormater()

    def testThereWillBeTwoRecordsInFormatedList(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        assert 2 == len(l_output), "Too many elements of fromatedDataList! Actual size: " + str(len(l_output))

    def testThereWillBeNoNewLinesInSingleSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        assert not re.search("\n", l_output[0]), "The are some new lines in single species record"

    def testThereWillBeNoTabulatorsInSingleSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        assert not re.search("\t", l_output[0]), "The are some tabulators in single species record"

    def testThereWillBeNoSpacesBetweenFieldsInSingelSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        l_noSpacesVetweenFieldsCondition = not re.search(", ", l_output[0]) and not re.search(" ,", l_output[0])
        assert l_noSpacesVetweenFieldsCondition, "The are some spaces between records in single species record"

    def testThereWillBeNoBracketsInSingelSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        l_noBracketsCondition = not re.search("{", l_output[0]) and not re.search("}", l_output[0])
        assert l_noBracketsCondition, "The are some brackets { or } in single species record"

    def testThereIsNoSynonymsInSingleSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        l_noSynonymsCondition = not re.search("synonyms", l_output[0])
        assert l_noSynonymsCondition, "The are synonyms in single species record"

    def testThereIsNoBranchInSingleSpeciesRecord(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        l_noBranchCondition = not re.search("\"branch\"", l_output[0])
        assert l_noBranchCondition, "The are some branch in single species record"

if __name__ == "__main__":
    unittest.main()
