import unittest

class TestSmithWaterman(unittest.TestCase):
    def test_basic_alignment(self):
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        match = 2
        mismatch = -1
        gap = -2

        expected_score = 2
        expected_seq1 = "G"
        expected_seq2 = "G"

        score, aligned_seq1, aligned_seq2 = smith_waterman(seq1, seq2, match, mismatch, gap)
        
        self.assertEqual(score, expected_score)
        self.assertEqual(aligned_seq1, expected_seq1)
        self.assertEqual(aligned_seq2, expected_seq2)

    def test_full_alignment(self):
        seq1 = "ACACACTA"
        seq2 = "AGCACACA"
        match = 2
        mismatch = -1
        gap = -2

        expected_score = 10
        expected_seq1 = "ACACACTA"
        expected_seq2 = "A-CACACA"

        score, aligned_seq1, aligned_seq2 = smith_waterman(seq1, seq2, match, mismatch, gap)
        
        self.assertEqual(score, expected_score)
        self.assertEqual(aligned_seq1, expected_seq1)
        self.assertEqual(aligned_seq2, expected_seq2)

if __name__ == "__main__":
    unittest.main()
