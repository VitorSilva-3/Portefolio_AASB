import unittest

class TestSmithWaterman(unittest.TestCase):

    def setUp(self):
        self.scoring_matrix = [
            [2, -1, -1, -1],
            [-1, 2, -1, -1],
            [-1, -1, 2, -1],
            [-1, -1, -1, 2]
        ]
        self.g = -2

    def test_SW(self):
        seq1 = "AGT"
        seq2 = "AGT"
        score, trace = SW(seq1, seq2, self.scoring_matrix, self.g)
        self.assertEqual(score[1][1], 2)
        self.assertEqual(score[2][2], 4)
        self.assertEqual(trace[1][1], 'D')
        self.assertEqual(trace[2][2], 'D')

    def test_score_SW(self):
        seq1 = "AGT"
        seq2 = "AGT"
        score, _ = SW(seq1, seq2, self.scoring_matrix, self.g)
        max_score = score_SW(score)
        self.assertEqual(max_score, 4)

    def test_reconstruct_SW(self):
        seq1 = "AGT"
        seq2 = "AGT"
        score, trace = SW(seq1, seq2, self.scoring_matrix, self.g)
        alinhamento_seq1, alinhamento_seq2 = reconstruct_SW(seq1, seq2, score, trace)
        self.assertEqual(alinhamento_seq1, "AGT")
        self.assertEqual(alinhamento_seq2, "AGT")

if __name__ == '__main__':
    unittest.main()

