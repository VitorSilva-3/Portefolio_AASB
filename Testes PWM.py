"""!
@brief Unit tests for DNA processing module.
"""

import unittest
from dna_processing import (
    revcomp,
    complementary_character,
    get_codons,
    codon_to_amino,
    get_prots,
    get_orfs,
    get_all_prots
)

class TestDNAProcessing(unittest.TestCase):
    """!
    @brief Test cases for DNA processing functions.
    """
    
    def setUp(self):
        """!
        @brief Set up test cases.
        """
        self.dna = "TGTGGGGAGGTCATAGGTACTGGCCC"
        self.invalid_dna = "ATGCX"
        
    def test_revcomp(self):
        """!
        @brief Test reverse complement calculation.
        """
        # Test basic reverse complement
        self.assertEqual(revcomp("ATGC"), "GCAT")
        # Test empty sequence
        self.assertEqual(revcomp(""), "")
        # Test palindrome
        self.assertEqual(revcomp("ATAT"), "ATAT")
        # Test invalid sequence
        with self.assertRaises(ValueError):
            revcomp(self.invalid_dna)
            
    def test_complementary_character(self):
        """!
        @brief Test complementary base calculation.
        """
        self.assertEqual(complementary_character("A"), "T")
        self.assertEqual(complementary_character("C"), "G")
        self.assertEqual(complementary_character("G"), "C")
        self.assertEqual(complementary_character("T"), "A")
        with self.assertRaises(ValueError):
            complementary_character("X")
            
    def test_get_codons(self):
        """!
        @brief Test codon extraction.
        """
        # Test perfect triplets
        self.assertEqual(get_codons("ATGCGA"), ["ATG", "CGA"])
        # Test incomplete codon at end
        self.assertEqual(get_codons("ATGCG"), ["ATG"])
        # Test empty sequence
        self.assertEqual(get_codons(""), [])
        
    def test_codon_to_amino(self):
        """!
        @brief Test codon to amino acid translation.
        """
        # Test start codon
        self.assertEqual(codon_to_amino(["ATG"]), "M")
        # Test stop codon
        self.assertEqual(codon_to_amino(["TAA"]), "_")
        # Test multiple codons
        self.assertEqual(codon_to_amino(["ATG", "TAA"]), "M_")
        # Test invalid codon
        with self.assertRaises(ValueError):
            codon_to_amino(["XYZ"])
            
    def test_get_prots(self):
        """!
        @brief Test protein extraction from amino acid sequence.
        """
        # Test basic protein
        self.assertEqual(get_prots("M_"), ["M_"])
        # Test no protein
        self.assertEqual(get_prots("ABC"), [])
        # Test multiple proteins
        self.assertEqual(get_prots("M_M_"), ["M_", "M_"])
        # Test nested proteins
        self.assertEqual(get_prots("MM_"), ["M_", "M_"])
        
    def test_get_orfs(self):
        """!
        @brief Test ORF calculation.
        """
        orfs = get_orfs("ATGCGA")
        # Should have 6 ORFs
        self.assertEqual(len(orfs), 6)
        # Each ORF should be a list of codons
        for orf in orfs:
            self.assertTrue(all(len(codon) == 3 for codon in orf))
            
    def test_get_all_prots(self):
        """!
        @brief Test protein extraction from DNA sequence.
        """
        # Test with known sequence
        prots = get_all_prots(self.dna)
        self.assertIsInstance(prots, list)
        # Test ordering
        if len(prots) > 1:
            self.assertGreaterEqual(len(prots[0]), len(prots[-1]))
        # Test invalid sequence
        with self.assertRaises(ValueError):
            get_all_prots(self.invalid_dna)

if __name__ == '__main__':
    unittest.main()
