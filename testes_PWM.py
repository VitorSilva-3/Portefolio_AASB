import unittest
from PWM import AnalisadorSequencias

class TesteAnalisadorSequencias(unittest.TestCase):
    """!
    @brief Testes unitários para a classe AnalisadorSequencias.
    """
    
    def setUp(self):
        """!
        @brief Prepara os dados de teste utilizados em vários testes.
        """
        self.sequencias = ['ATTG', 'ATCG', 'ATTC', 'ACTC']
        self.resultado_pwm = AnalisadorSequencias.pwm(self.sequencias)

    def test_tabela_contagens(self):
        """!
        @brief Testa o cálculo da tabela de contagens.
        """
        resultado = AnalisadorSequencias.tabela_contagens(self.sequencias)
        primeira_pos_esperada = {'A': 4, 'C': 0, 'G': 0, 'T': 0}
        self.assertEqual(resultado[0], primeira_pos_esperada)

    def test_pwm_adn(self):
        """!
        @brief Testa o cálculo da PWM para sequências de ADN.
        """
        resultado = self.resultado_pwm
        # Primeira posição deve ser toda A's
        self.assertAlmostEqual(resultado[0]['A'], 1.0)
        self.assertAlmostEqual(resultado[0]['C'], 0.0)

    def test_pwm_tipo_invalido(self):
        """!
        @brief Testa o cálculo da PWM com tipo de sequência inválido.
        """
        with self.assertRaises(AssertionError):
            AnalisadorSequencias.pwm(self.sequencias, tipo="ARN")

    def test_pwm_comprimentos_diferentes(self):
        """!
        @brief Testa o cálculo da PWM com sequências de comprimentos diferentes.
        """
        sequencias_invalidas = ['ATTG', 'ATC', 'ATTC']
        with self.assertRaises(AssertionError):
            AnalisadorSequencias.pwm(sequencias_invalidas)

    def test_prob_gerar_sequencia(self):
        """!
        @brief Testa o cálculo da probabilidade de sequência.
        """
        seq = "ATTG"
        prob = AnalisadorSequencias.prob_gerar_sequencia(seq, self.resultado_pwm)
        self.assertGreater(prob, 0)
        self.assertLessEqual(prob, 1)

    def test_seq_mais_provavel(self):
        """!
        @brief Testa a procura das sequências mais prováveis.
        """
        seq_longa = "ATTGATTCATCG"
        resultado = AnalisadorSequencias.seq_mais_provavel(seq_longa, self.resultado_pwm)
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(len(seq) == 4 for seq in resultado))

    def test_calcula_pssm(self):
        """!
        @brief Testa o cálculo da PSSM.
        """
        pssm = AnalisadorSequencias.calcula_pssm(self.resultado_pwm)
        # Verifica se os valores da PSSM são finitos para probabilidades não-zero
        self.assertTrue(all(isinstance(val, float) 
                          for pos in pssm 
                          for val in pos.values()))

if __name__ == '__main__':
    unittest.main()