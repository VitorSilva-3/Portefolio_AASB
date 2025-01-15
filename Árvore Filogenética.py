from typing import List, Dict, Tuple


def calcular_distancia(s1: str, s2: str) -> int:
    """
    @brief Calcula a distância de edição entre duas sequências.
    @param s1 Primeira sequência.
    @param s2 Segunda sequência.
    @return Distância de edição entre s1 e s2.
    """
    mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        mat[i][0] = i
    for j in range(len(s2) + 1):
        mat[0][j] = j

    for i, char_s1 in enumerate(s1, 1):
        for j, char_s2 in enumerate(s2, 1):
            custo = 0 if char_s1 == char_s2 else 1
            mat[i][j] = min(
                mat[i - 1][j] + 1,  # Remoção
                mat[i][j - 1] + 1,  # Inserção
                mat[i - 1][j - 1] + custo  # Substituição
            )

    return mat[-1][-1]


def gerar_matriz_distancias(sequencias: List[str]) -> Dict[str, Dict[str, int]]:
    """
    @brief Gera uma matriz de distâncias para um conjunto de sequências.
    @param sequencias Lista de sequências.
    @return Matriz de distâncias entre todas as sequências.
    """
    distancias = {}
    for s1 in sequencias:
        distancias[s1] = {}
        for s2 in sequencias:
            if s1 != s2:
                distancia = calcular_distancia(s1, s2)
                distancias[s1][s2] = distancia
                distancias.setdefault(s2, {})[s1] = distancia
    return distancias


def encontrar_par_minimo(matriz_distancias: Dict[str, Dict[str, int]]) -> Tuple[Tuple[str, str], int]:
    """
    @brief Encontra o par de sequências com a menor distância na matriz.
    @param matriz_distancias Matriz de distâncias.
    @return Par de sequências com a menor distância e o valor da distância.
    """
    menor_distancia = float('inf')
    menor_par = None

    for s1, distancias in matriz_distancias.items():
        for s2, valor in distancias.items():
            if valor < menor_distancia:
                menor_distancia = valor
                menor_par = (s1, s2)

    return menor_par, menor_distancia


def atualizar_distancias(
    matriz_distancias: Dict[str, Dict[str, float]], par: Tuple[str, str]
) -> Dict[str, Dict[str, float]]:
    """
    @brief Atualiza a matriz de distâncias ao fundir dois clusters.
    @param matriz_distancias Matriz de distâncias.
    @param par Par de sequências a fundir.
    @return Matriz de distâncias atualizada.
    """
    s1, s2 = par
    novo_cluster = f"({s1},{s2})"
    matriz_distancias[novo_cluster] = {}

    for seq in list(matriz_distancias.keys()):
        if seq not in par:
            if seq in matriz_distancias[s1] and seq in matriz_distancias[s2]:
                nova_distancia = (matriz_distancias[s1][seq] + matriz_distancias[s2][seq]) / 2
                matriz_distancias[novo_cluster][seq] = nova_distancia
                matriz_distancias[seq][novo_cluster] = nova_distancia

    for seq in par:
        matriz_distancias.pop(seq, None)
        for valores in matriz_distancias.values():
            valores.pop(seq, None)

    return matriz_distancias


def construir_arvore(sequencias: List[str]) -> str:
    """
    @brief Constrói uma árvore filogenética a partir de um conjunto de sequências.
    @param sequencias Lista de sequências.
    @return Árvore filogenética representada como um cluster hierárquico.
    """
    matriz_distancias = gerar_matriz_distancias(sequencias)

    while len(matriz_distancias) > 1:
        par_minimo, _ = encontrar_par_minimo(matriz_distancias)
        matriz_distancias = atualizar_distancias(matriz_distancias, par_minimo)

    return list(matriz_distancias.keys())[0]


if __name__ == '__main__':
    from pprint import pprint

    sequencias = ["CCG", "GT", "GTA", "AAT", "AT", "ACG", "ACGT"]

    # Gerar a matriz de distâncias
    matriz_distancias = gerar_matriz_distancias(sequencias)
    pprint(matriz_distancias)

    # Construir a árvore filogenética
    arvore = construir_arvore(sequencias)
    print("Árvore Filogenética:", arvore)
