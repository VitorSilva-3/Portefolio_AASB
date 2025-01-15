# Testes Unitários para sequências de DNA
import unittest

class TesteAlgoritmoDNA(unittest.TestCase):
    def test_calcular_distancia(self):
        # Testes com sequências de DNA
        self.assertEqual(calculate_distance("AGT", "ACT"), 1)  # Apenas uma substituição
        self.assertEqual(calculate_distance("CGTAC", "CGTGC"), 1)  # Substituição no meio
        self.assertEqual(calculate_distance("A", "G"), 1)  # Substituição de um único carácter
        self.assertEqual(calculate_distance("TACG", "TACG"), 0)  # Sequências idênticas
        self.assertEqual(calculate_distance("", "ATCG"), 4)  # Inserções necessárias

    def test_gerar_matriz_de_distancias(self):
        # Testar a geração da matriz de distâncias com sequências de DNA
        sequencias = ["A", "AG", "AGT"]
        esperado = {
            "A": {"AG": 1, "AGT": 2},
            "AG": {"A": 1, "AGT": 1},
            "AGT": {"A": 2, "AG": 1}
        }
        self.assertEqual(generate_distance_matrix(sequencias), esperado)

    def test_encontrar_par_minimo(self):
        # Testar encontrar o par com a menor distância
        matriz_distancias = {
            "AG": {"CT": 3, "GTA": 4},
            "CT": {"AG": 3, "GTA": 2},
            "GTA": {"AG": 4, "CT": 2}
        }
        self.assertEqual(find_minimum_pair(matriz_distancias), (("CT", "GTA"), 2))

    def test_atualizar_distancias(self):
        # Testar a atualização da matriz de distâncias
        matriz_distancias = {
            "AG": {"CT": 3, "GTA": 4},
            "CT": {"AG": 3, "GTA": 2},
            "GTA": {"AG": 4, "CT": 2}
        }
        esperado = {
            ("AG", "CT"): {"GTA": 3.0},
            "GTA": {("AG", "CT"): 3.0}
        }
        self.assertEqual(update_distances(matriz_distancias, ("AG", "CT")), esperado)

    def test_construir_arvore(self):
        # Testar a construção de uma árvore filogenética
        sequencias = ["AGT", "ACT", "GCT", "GTT"]
        arvore = build_tree(sequencias)
        self.assertTrue(isinstance(arvore, tuple))

if __name__ == '__main__':
    unittest.main()
