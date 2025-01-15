"""
@brief Testes unitários para o módulo de alinhamento de sequências.
"""

import unittest
from alinhamento_sequencias import alinhar, obter_pontuacao_alinhamento, reconstruir_alinhamento

class TestAlinhamentoSequencias(unittest.TestCase):
    """
    @brief Casos de teste para as funções de alinhamento de sequências.
    """

    def setUp(self):
        """
        @brief Configuração inicial dos casos de teste.
        """
        self.seq1 = "HGWAG"
        self.seq2 = "PHSWG"
        self.sequencia_vazia = ""

    def test_alinhar_basico(self):
        """
        @brief Testa a funcionalidade básica do alinhamento.
        """
        pontuacao, traceback = alinhar(self.seq1, self.seq2)
        self.assertIsInstance(pontuacao, list)
        self.assertIsInstance(traceback, list)
        self.assertEqual(len(pontuacao), len(self.seq2) + 1)
        self.assertEqual(len(pontuacao[0]), len(self.seq1) + 1)

    def test_alinhar_sequencia_vazia(self):
        """
        @brief Testa o alinhamento com sequências vazias.
        """
        with self.assertRaises(ValueError):
            alinhar(self.sequencia_vazia, self.seq2)
        with self.assertRaises(ValueError):
            alinhar(self.seq1, self.sequencia_vazia)

    def test_pontuacao_alinhamento(self):
        """
        @brief Testa o cálculo da pontuação final de alinhamento.
        """
        pontuacao_igual = obter_pontuacao_alinhamento("HG", "HG")
        self.assertGreater(pontuacao_igual, 0)  

        pontuacao_diferente = obter_pontuacao_alinhamento("HG", "PG")
        self.assertLess(pontuacao_diferente, pontuacao_igual)  

    def test_reconstruir_alinhamento(self):
        """
        @brief Testa a reconstrução do alinhamento a partir da matriz de traceback.
        """
        pontuacao, traceback = alinhar(self.seq1, self.seq2)
        alinhada_seq1, alinhada_seq2 = reconstruir_alinhamento(self.seq1, self.seq2, traceback)

        self.assertEqual(len(alinhada_seq1), len(alinhada_seq2))
        self.assertTrue("-" in alinhada_seq1 or "-" in alinhada_seq2)
        self.assertEqual(alinhada_seq1.replace("-", ""), self.seq1)
        self.assertEqual(alinhada_seq2.replace("-", ""), self.seq2)

    def test_traceback_invalido(self):
        """
        @brief Testa a reconstrução com uma matriz de traceback inválida.
        """
        traceback_invalido = [['X' for _ in range(len(self.seq1) + 1)] for _ in range(len(self.seq2) + 1)]
        with self.assertRaises(ValueError):
            reconstruir_alinhamento(self.seq1, self.seq2, traceback_invalido)

    def test_diferentes_penalizacoes_gap(self):
        """
        @brief Testa o alinhamento utilizando diferentes penalizações por gaps.
        """
        pontuacao_gap_alto = obter_pontuacao_alinhamento(self.seq1, self.seq2, gap=-10)
        pontuacao_gap_baixo = obter_pontuacao_alinhamento(self.seq1, self.seq2, gap=-4)
        self.assertNotEqual(pontuacao_gap_alto, pontuacao_gap_baixo)  

if __name__ == "__main__":
    unittest.main()
