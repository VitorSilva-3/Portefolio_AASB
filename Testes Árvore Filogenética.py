import unittest

class TesteAlgoritmoDNA(unittest.TestCase):
    def test_calcular_distancia(self):
        """
        @brief Testa a função calcular_distancia para diferentes casos.
        """
        self.assertEqual(calcular_distancia("AGT", "ACT"), 1)  # Apenas uma substituição
        self.assertEqual(calcular_distancia("CGTAC", "CGTGC"), 1)  # Substituição no meio
        self.assertEqual(calcular_distancia("A", "G"), 1)  # Substituição de um único carácter
        self.assertEqual(calcular_distancia("TACG", "TACG"), 0)  # Sequências idênticas
        self.assertEqual(calcular_distancia("", "ATCG"), 4)  # Inserções necessárias

    def test_gerar_matriz_distancias(self):
        """
        @brief Testa a função gerar_matriz_distancias para diferentes conjuntos de sequências.
        """
        sequencias = ["A", "AG", "AGT"]
        esperado = {
            "A": {"AG": 1, "AGT": 2},
            "AG": {"A": 1, "AGT": 1},
            "AGT": {"A": 2, "AG": 1}
        }
        self.assertEqual(gerar_matriz_distancias(sequencias), esperado)

    def test_encontrar_par_minimo(self):
        """
        @brief Testa a função encontrar_par_minimo para diferentes matrizes de distâncias.
        """
        matriz_distancias = {
            "AG": {"CT": 3, "GTA": 4},
            "CT": {"AG": 3, "GTA": 2},
            "GTA": {"AG": 4, "CT": 2}
        }
        self.assertEqual(encontrar_par_minimo(matriz_distancias), (("CT", "GTA"), 2))

    def test_atualizar_distancias(self):
        """
        @brief Testa a função atualizar_distancias para verificar a fusão de clusters.
        """
        matriz_distancias = {
            "AG": {"CT": 3, "GTA": 4},
            "CT": {"AG": 3, "GTA": 2},
            "GTA": {"AG": 4, "CT": 2}
        }
        esperado = {
            "(AG,CT)": {"GTA": 3.0},
            "GTA": {"(AG,CT)": 3.0}
        }
        self.assertEqual(atualizar_distancias(matriz_distancias, ("AG", "CT")), esperado)

    def test_construir_arvore(self):
        """
        @brief Testa a função construir_arvore para verificar a construção de uma árvore filogenética.
        """
        sequencias = ["AGT", "ACT", "GCT", "GTT"]
        arvore = construir_arvore(sequencias)
        self.assertTrue(isinstance(arvore, str))  # A árvore é representada como uma string.

if __name__ == '__main__':
    unittest.main()
