
 # @brief Calcula a distância de edição entre duas sequências.
 # @param s1 Primeira sequência.
 # @param s2 Segunda sequência.
 # @return int Distância de edição entre s1 e s2.
 
def calcular_distancia(s1: str, s2: str) -> int:
    # Criar a matriz de distâncias
    mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Inicializar as margens da matriz
    for i in range(len(s1) + 1):
        mat[i][0] = i
    for j in range(len(s2) + 1):
        mat[0][j] = j

    # Preencher a matriz utilizando a fórmula da distância
    for i, char_s1 in enumerate(s1, 1):
        for j, char_s2 in enumerate(s2, 1):
            custo = 0 if char_s1 == char_s2 else 1
            mat[i][j] = min(
                mat[i - 1][j] + 1,  # Remoção
                mat[i][j - 1] + 1,  # Inserção
                mat[i - 1][j - 1] + custo  # Substituição
            )

    return mat[-1][-1]


 # @brief Gera uma matriz de distâncias para um conjunto de sequências.
 # @param sequencias Lista de sequências.
 # @return dict Matriz de distâncias entre todas as sequências.
 
def gerar_matriz_distancias(sequencias: list[str]) -> dict[str, dict[str, int]]:
    # Criar um dicionário para armazenar as distâncias
    distancias = {}
    for s1 in sequencias:
        distancias[s1] = {}
        for s2 in sequencias:
            if s1 != s2 and s2 not in distancias:
                distancia = calcular_distancia(s1, s2)
                distancias[s1][s2] = distancia
                distancias.setdefault(s2, {})[s1] = distancia

    return distancias


 # @brief Encontra o par de sequências com a menor distância na matriz.
 # @param matriz_distancias Matriz de distâncias.
 # @return tuple Par de sequências com a menor distância e o valor da distância.
 
def encontrar_par_minimo(matriz_distancias: dict[str, dict[str, int]]) -> tuple[tuple[str, str], int]:
    # Encontrar o par com a menor distância
    menor_distancia = float('inf')
    menor_par = None

    for s1, distancias in matriz_distancias.items():
        for s2, valor in distancias.items():
            if valor < menor_distancia:
                menor_distancia = valor
                menor_par = (s1, s2)

    return menor_par, menor_distancia


 # @brief Atualiza a matriz de distâncias ao fundir dois clusters.
 # @param matriz_distancias Matriz de distâncias.
 # @param par Par de sequências a fundir.
 # @return dict Matriz de distâncias atualizada.
 
def atualizar_distancias(matriz_distancias: dict[str, dict[str, float]], par: tuple[str, str]) -> dict[str, dict[str, float]]:
    s1, s2 = par

    # Criar um novo cluster a partir de s1 e s2
    novo_cluster = (s1, s2)
    matriz_distancias[novo_cluster] = {}

    for seq, dist in list(matriz_distancias.items()):
        if seq not in par:
            nova_distancia = (matriz_distancias[s1][seq] + matriz_distancias[s2][seq]) / 2
            matriz_distancias[novo_cluster][seq] = nova_distancia
            matriz_distancias[seq][novo_cluster] = nova_distancia

    # Remover s1 e s2 da matriz
    for seq in par:
        matriz_distancias.pop(seq, None)
        for valores in matriz_distancias.values():
            valores.pop(seq, None)

    return matriz_distancias


 # @brief Constrói uma árvore filogenética a partir de um conjunto de sequências.
 # @param sequencias Lista de sequências.
 # @return tuple Árvore filogenética representada como um cluster hierárquico.
 
def construir_arvore(sequencias: list[str]) -> tuple:
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
