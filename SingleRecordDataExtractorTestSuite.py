#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import unittest

from SingleRecordDataExtractor import SingleRecordDataExtractor 

g_abiesCephalonica_correctRecord = '''"nr_kol": 2,"rodz_id": 607,"rodzaj": "Abies","nzw_gat": "cephalonica","gatunek": "Abies cephalonica","autor_gat": "Loudon","n_lacinska": "Abies cephalonica Loudon","n_polska": "Jodła grecka","synantrop": "U","rodzina": "Pinaceae","rzad": "Pinales","nadrzad": "","podklasa": "","klasa": "Coniferopsida","podgromada": "Gymnospermae","gromada": "Spermatophyta"'''

g_acenaMacrostemon_correctRecord = '''"nr_kol": 7,"rodz_id": 26,"rodzaj": "Acaena","nzw_gat": "macrostemon","gatunek": "Acaena macrostemon","autor_gat": "Hook. f.","n_lacinska": "Acaena macrostemon Hook. f.","synantrop": "E","rodzina": "Rosaceae","rzad": "Rosales","nadrzad": "Rosiflorae","podklasa": "Rosidae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_aconitumTauricum_correctRecord = '''"nr_kol": 43,"rodz_id": 511,"rodzaj": "Aconitum","nzw_gat": "tauricum","gatunek": "Aconitum tauricum","autor_gat": "Wulfen","podgatunek": "subsp. nanum","autor_pgat": "(Baumg.) Goly","n_lacinska": "Aconitum tauricum Wulfen subsp. nanum (Baumg.) Goly","n_polska": "Tojad tauryjski","chroniony": "s","rodzina": "Ranunculaceae","rzad": "Ranunculales","nadrzad": "","podklasa": "Polycarpicae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_ballotaNigraFoetida_correctRecord = '''"nr_kol": 458,"rodz_id": 53,"rodzaj": "Ballota","nzw_gat": "nigra","gatunek": "Ballota nigra","autor_gat": "L.","podgatunek": "subsp. foetida","autor_pgat": "Hayek","n_lacinska": "Ballota nigra L. subsp. foetida Hayek","n_polska": "Mierznica czarna cuchnąca","synantrop": "A","rodzina": "Lamiaceae","rzad": "Lamiales","nadrzad": "Tubiflorae","podklasa": "Asteridae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_begniaHortensis_correctRecord = '''"nr_kol": 478,"rodz_id": 542,"rodzaj": "Begonia","nzw_gat": "x hortensis","gatunek": "Begonia x hortensis","autor_gat": "Graf & Zwicky","n_lacinska": "Begonia x hortensis Graf & Zwicky","n_polska": "Begonia (Ukośnica) stale kwitnąca","synantrop": "U","rodzina": "Begoniaceae","rzad": "Begoniales","nadrzad": "Cistiflorae","podklasa": "Dilleniidae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_ageratumHoustonianum_correctRecord = '''"nr_kol": 68,"rodz_id": 718,"rodzaj": "Ageratum","nzw_gat": "houstonianum","gatunek": "Ageratum houstonianum","autor_gat": "Mill.","n_lacinska": "Ageratum houstonianum Mill.","n_polska": "Żeniszek (Ageratum) meksykański","synantrop": "U","rodzina": "Asteraceae","rzad": "Asterales","nadrzad": "Campanulatae","podklasa": "Asteridae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_ageratumHoustonianum_withModifiedSubspeciesRecord = '''"nr_kol": 68,"rodz_id": 718,"rodzaj": "Ageratum","nzw_gat": "houstonianum","gatunek": "Ageratum houstonianum","autor_gat": "Mill.","podgatunek": "subsp. houstonianum","n_lacinska": "Ageratum houstonianum Mill.","n_polska": "Żeniszek (Ageratum) meksykański typowy","synantrop": "U","rodzina": "Asteraceae","rzad": "Asterales","nadrzad": "Campanulatae","podklasa": "Asteridae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_ageratumHoustonianum_withModifiedGenusRecord = '''"nr_kol": 68,"rodz_id": 718,"rodzaj": "Ageratum","nzw_gat": "houstonianum","gatunek": "Ageratum houstonianum","autor_gat": "Mill.","podgatunek": "subsp. houstonianum","n_lacinska": "Ageratum houstonianum Mill.","n_polska": "(Ageratum) Żeniszek meksykański typowy","synantrop": "U","rodzina": "Asteraceae","rzad": "Asterales","nadrzad": "Campanulatae","podklasa": "Asteridae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_abiesConcolor_correctRecord = '''"nr_kol": 3,"rodz_id": 607,"rodzaj": "Abies","nzw_gat": "concolor","gatunek": "Abies concolor","autor_gat": "(Gordon) Lindl. ex Hildebr.","n_lacinska": "Abies concolor (Gordon) Lindl. ex Hildebr.","n_polska": "Jodła jednobarwna (J. kalifornijska)","synantrop": "U","rodzina": "Pinaceae","rzad": "Pinales","nadrzad": "","podklasa": "","klasa": "Coniferopsida","podgromada": "Gymnospermae","gromada": "Spermatophyta"'''

g_ammobiumAlatum_correctRecord = '''"nr_kol": 239,"rodz_id": 279,"rodzaj": "Ammobium","nzw_gat": "alatum","gatunek": "Ammobium alatum","autor_gat": "R. Br.","n_lacinska": "Ammobium alatum R. Br.","n_polska": "Wiekuistka rozgałęziona (Złociszek oskrzydlony,Susz)","synantrop": "U","rodzina": "Asteraceae","rzad": "Asterales","nadrzad": "Campanulatae","podklasa": "Asteridae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

g_arabisGlabra_correctRecord = '''"nr_kol": 319,"rodz_id": 765,"rodzaj": "Arabis","nzw_gat": "glabra","gatunek": "Arabis glabra","autor_gat": "(L.) Bernh.","n_lacinska": "Arabis glabra (L.) Bernh.","n_polska": "Gęsiówka wieżyczkowata (Wieżyczka (Wieżycznik) gładka)","rodzina": "Brassicaceae","rzad": "Capparales","nadrzad": "Cistiflorae","podklasa": "Dilleniidae","klasa": "Dicotyledoneae","podgromada": "Angiospermae","gromada": "Spermatophyta"'''

class SingleRecordDataExtractorTestSuite(unittest.TestCase):
    def testIfSingleRecordDataExtractorIsCreatedProperly(self):
        m_sut = SingleRecordDataExtractor()
   

    def testIfExtractingValueOfLatinNameFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinName(g_abiesCephalonica_correctRecord)
        assert l_result == "Abies cephalonica", "Actual value: " + l_result

    def testIfExtractingValueOfLatinNameFieldWorksForHybridWithXCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinName(g_begniaHortensis_correctRecord)
        assert l_result == "Begonia x hortensis", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_abiesCephalonica_correctRecord)
        assert l_result == "Jodła grecka", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForCaseWhereThereIsBracketCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_begniaHortensis_correctRecord)
        assert l_result == "Begonia stale kwitnąca", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForCaseWhereThereIsBracketAdditionalCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_abiesConcolor_correctRecord)
        assert l_result == "Jodła jednobarwna", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForCaseWhereThereIsBracketOneMoreCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_ammobiumAlatum_correctRecord)
        assert l_result == "Wiekuistka rozgałęziona", "Actual value: " + l_result

    def testIfExtractingValueOfPolishNameFieldWorksForCaseWhereThereIsDoubleBracketCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishName(g_arabisGlabra_correctRecord)
        assert l_result == "Gęsiówka wieżyczkowata", "Actual value: " + l_result


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

    def testIfExtractingValueOfAuthorSubspFieldWorksForFilledSubspCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getSubspeciesAuthor(g_aconitumTauricum_correctRecord)
        assert l_result == "(Baumg.) Goly", "Actual value: " + l_result


    def testIfExtractingValueOfSynantropFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getSynantrop(g_abiesCephalonica_correctRecord)
        assert l_result == "U", "Actual value: " + l_result


    def testIfExtractingValueOfSubspeciesInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubspeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInLatinFieldWorksForFilledSubspeciesCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubspeciesName(g_aconitumTauricum_correctRecord)
        assert l_result == "nanum", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSubspeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInPolishFieldWorksForFilledSubspeciesCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSubspeciesName(g_ballotaNigraFoetida_correctRecord)
        assert l_result == "cuchnąca", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInPolishFieldWorksForTwoWordSpeciesNameAndNoSubspeciesCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSubspeciesName(g_begniaHortensis_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubspeciesInPolishFieldWorksForBracketCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSubspeciesName(g_ageratumHoustonianum_withModifiedSubspeciesRecord)
        assert l_result == "typowy", "Actual value: " + l_result


    def testIfExtractingValueOfSpeciesInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSpeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "cephalonica", "Actual value: " + l_result

    def testIfExtractingValueOfSpeciesInLatinFieldWorksForHybridWithXCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSpeciesName(g_begniaHortensis_correctRecord)
        assert l_result == "x hortensis", "Actual value: " + l_result

    def testIfExtractingValueOfSpeciesInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSpeciesName(g_abiesCephalonica_correctRecord)
        assert l_result == "grecka", "Actual value: " + l_result

    def testIfExtractingValueOfSpeciesInPolishFieldWorksForBracketCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishSpeciesName(g_ageratumHoustonianum_correctRecord)
        assert l_result == "meksykański", "Actual value: " + l_result


    def testIfExtractingValueOfGenusInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinGenusName(g_abiesCephalonica_correctRecord)
        assert l_result == "Abies", "Actual value: " + l_result

    def testIfExtractingValueOfGenusInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishGenusName(g_abiesCephalonica_correctRecord)
        assert l_result == "Jodła", "Actual value: " + l_result

    def testIfExtractingValueOfGenusInPolishFieldWorksForBracketCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishGenusName(g_ageratumHoustonianum_withModifiedGenusRecord)
        assert l_result == "Żeniszek", "Actual value: " + l_result


    def testIfExtractingValueOfFamilyInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinFamilyName(g_abiesCephalonica_correctRecord)
        assert l_result == "Pinaceae", "Actual value: " + l_result

    def testIfExtractingValueOfFamilyInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishFamilyName(g_abiesCephalonica_correctRecord)
        assert l_result == "Sosnowate", "Actual value: " + l_result
    
    def testIfExtractingValueOfFamilyInPolishFieldWorksForSecondSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishFamilyName(g_acenaMacrostemon_correctRecord)
        assert l_result == "Różowate", "Actual value: " + l_result


    def testIfExtractingValueOfOrderInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinOrderName(g_abiesCephalonica_correctRecord)
        assert l_result == "Pinales", "Actual value: " + l_result

    def testIfExtractingValueOfOrderInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishOrderName(g_abiesCephalonica_correctRecord)
        assert l_result == "Sosnowce", "Actual value: " + l_result


    def testIfExtractingValueOfSuperorderInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSuperorderName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSuperorderInLatinFieldWorksForFilledSuperorderCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSuperorderName(g_acenaMacrostemon_correctRecord)
        assert l_result == "Rosiflorae", "Actual value: " + l_result


    def testIfExtractingValueOfSubclassInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubclassName(g_abiesCephalonica_correctRecord)
        assert l_result == "", "Actual value: " + l_result

    def testIfExtractingValueOfSubclassInLatinFieldWorksForFilledSubclassCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubclassName(g_acenaMacrostemon_correctRecord)
        assert l_result == "Rosidae", "Actual value: " + l_result


    def testIfExtractingValueOfClassInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinClassName(g_abiesCephalonica_correctRecord)
        assert l_result == "Coniferopsida", "Actual value: " + l_result

    def testIfExtractingValueOfClassInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishClassName(g_abiesCephalonica_correctRecord)
        assert l_result == "Szpilkowe", "Actual value: " + l_result


    def testIfExtractingValueOfSubdivisionInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinSubdivisionName(g_abiesCephalonica_correctRecord)
        assert l_result == "Gymnospermae", "Actual value: " + l_result


    def testIfExtractingValueOfDivisionInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinDivisionName(g_abiesCephalonica_correctRecord)
        assert l_result == "Spermatophyta", "Actual value: " + l_result

    def testIfExtractingValueOfDivisionInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishDivisionName(g_abiesCephalonica_correctRecord)
        assert l_result == "Rośliny nasienne", "Actual value: " + l_result


    def testIfExtractingValueOfRealmInLatinFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getLatinRealmName(g_abiesCephalonica_correctRecord)
        assert l_result == "Plantae", "Actual value: " + l_result

    def testIfExtractingValueOfRealmInPolishFieldWorksForSimpleCase(self):
        m_sut = SingleRecordDataExtractor()
        l_result = m_sut.getPolishRealmName(g_abiesCephalonica_correctRecord)
        assert l_result == "Rośliny", "Actual value: " + l_result

if __name__ == "__main__":
    unittest.main()
