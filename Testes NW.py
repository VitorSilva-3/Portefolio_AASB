"""!
@brief Unit tests for sequence alignment module.
"""

import unittest
from sequence_alignment import align, get_alignment_score, reconstruct_alignment

class TestSequenceAlignment(unittest.TestCase):
    """!
    @brief Test cases for sequence alignment functions.
    """
    
    def setUp(self):
        """!
        @brief Set up test cases.
        """
        self.s1 = "HGWAG"
        self.s2 = "PHSWG"
        self.empty = ""
        
    def test_align_basic(self):
        """!
        @brief Test basic alignment functionality.
        """
        score, trace = align(self.s1, self.s2)
        self.assertIsInstance(score, list)
        self.assertIsInstance(trace, list)
        self.assertEqual(len(score), len(self.s2) + 1)
        self.assertEqual(len(score[0]), len(self.s1) + 1)
        
    def test_align_empty_sequence(self):
        """!
        @brief Test alignment with empty sequences.
        """
        with self.assertRaises(ValueError):
            align(self.empty, self.s2)
        with self.assertRaises(ValueError):
            align(self.s1, self.empty)
            
    def test_alignment_score(self):
        """!
        @brief Test alignment score calculation.
        """
        # Test with known sequences
        score = get_alignment_score("HG", "HG")
        self.assertGreater(score, 0)  # Match should give positive score
        
        score1 = get_alignment_score("HG", "PG")
        score2 = get_alignment_score("HG", "HH")
        self.assertNotEqual(score1, score2)  # Different mismatches should give different scores
        
    def test_reconstruct_alignment(self):
        """!
        @brief Test alignment reconstruction.
        """
        score, trace = align(self.s1, self.s2)
        aligned_s1, aligned_s2 = reconstruct_alignment(self.s1, self.s2, trace)
        
        # Check alignment properties
        self.assertEqual(len(aligned_s1), len(aligned_s2))
        self.assertTrue('-' in aligned_s1 or '-' in aligned_s2)
        
        # Remove gaps and check if original sequences are recovered
        self.assertEqual(aligned_s1.replace('-', ''), self.s1)
        self.assertEqual(aligned_s2.replace('-', ''), self.s2)
        
    def test_invalid_traceback(self):
        """!
        @brief Test reconstruction with invalid traceback matrix.
        """
        invalid_trace = [['X' for _ in range(len(self.s1) + 1)] 
                        for _ in range(len(self.s2) + 1)]
        with self.assertRaises(ValueError):
            reconstruct_alignment(self.s1, self.s2, invalid_trace)
            
    def test_different_gap_penalties(self):
        """!
        @brief Test alignment with different gap penalties.
        """
        score1 = get_alignment_score(self.s1, self.s2, g=-8)
        score2 = get_alignment_score(self.s1, self.s2, g=-4)
        self.assertNotEqual(score1, score2)

if __name__ == '__main__':
    unittest.main()
