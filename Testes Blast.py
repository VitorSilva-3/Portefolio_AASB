import unittest
from sequence_analysis import query_map, get_all_positions, hits, extend_hit_direction

class TestSequenceAnalysis(unittest.TestCase):
    def test_query_map(self):
        seq = "AATATAT"
        result = query_map(seq, 3)
        expected = {"AAT": [0, 4], "ATA": [1, 5], "TAT": [2, 6]}
        self.assertEqual(dict(result), expected)

    def test_get_all_positions(self):
        subseq = "ATA"
        seq = "AATATAT"
        result = get_all_positions(subseq, seq)
        expected = [1, 5]
        self.assertEqual(result, expected)

    def test_hits(self):
        query = "AATATAT"
        seq = "AATATGTTATATAATAATATTT"
        qm = query_map(query, 3)
        result = hits(qm, seq)
        expected = [(0, 0), (0, 12), (1, 1), (1, 13), (4, 16), (5, 17), (6, 18)]
        self.assertEqual(result, expected)

    def test_extend_hit_direction(self):
        query = "AATATAT"
        seq = "AATATGTTATATAATAATATTT"
        hit = (0, 0)
        result = extend_hit_direction(query, seq, hit, 3, 1)
        expected = (0, 0, 5, 5)  
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
