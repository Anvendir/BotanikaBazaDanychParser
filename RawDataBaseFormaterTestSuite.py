#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
        print g_readedDataBaseRecord 

    def testThereWillBeTwoRecordsOnFormatedList(self):
        m_sut = RawDataBaseFormater()
        l_output = m_sut.formatRawDataBase(g_readedDataBaseRecord)
        assert 2 == len(l_output), "BlaBla"

if __name__ == "__main__":
    unittest.main()
