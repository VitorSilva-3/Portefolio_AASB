class TestesAlinhamentoSequencias(unittest.TestCase):
    """!
    @brief Classe de testes unitários para as funções de alinhamento de sequências.
    """
    
    def test_alinhamento_sequencias_simples(self):
        """!
        @brief Testa o alinhamento de sequências simples.
        """
        seq1: str = "ACT"
        seq2: str = "ACGT"
        seq1_alinhada, seq2_alinhada = alinhamento(seq1, seq2)
        self.assertEqual(seq1_alinhada, "AC-T")
        self.assertEqual(seq2_alinhada, "ACGT")

    def test_alinhamento_sequencias_vazias(self):
        """!
        @brief Testa o alinhamento com sequências vazias.
        """
        with self.assertRaises(ValueError):
            alinhamento("", "ACT")

    def test_consenso_sequencias_diferentes_tamanhos(self):
        """!
        @brief Testa o consenso com sequências de tamanhos diferentes.
        """
        with self.assertRaises(ValueError):
            consenso("ACT", "ACGT")

    def test_consenso_sequencias_iguais(self):
        """!
        @brief Testa o consenso com sequências idênticas.
        """
        resultado: str = consenso("ACGT", "ACGT")
        self.assertEqual(resultado, "ACGT")

    def test_alinhamento_progressivo_vazio(self):
        """!
        @brief Testa o alinhamento progressivo com lista vazia.
        """
        with self.assertRaises(ValueError):
            alinhamento_progressivo([])

    def test_alinhamento_progressivo_uma_sequencia(self):
        """!
        @brief Testa o alinhamento progressivo com uma única sequência.
        """
        sequencias: List[str] = ["ACGT"]
        resultado: List[str] = alinhamento_progressivo(sequencias)
        self.assertEqual(resultado, sequencias)

    def test_alinhamento_progressivo_multiplas_sequencias(self):
        """!
        @brief Testa o alinhamento progressivo com múltiplas sequências.
        """
        sequencias: List[str] = ["ACTG", "ACG", "ACT"]
        resultado: List[str] = alinhamento_progressivo(sequencias)
        self.assertEqual(len(resultado), 3)
        self.assertEqual(len(resultado[0]), len(resultado[1]))
        self.assertEqual(len(resultado[1]), len(resultado[2]))

if __name__ == "__main__":
    unittest.main()
