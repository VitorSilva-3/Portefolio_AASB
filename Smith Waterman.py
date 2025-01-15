import numpy as np
from typing import Tuple

def smith_waterman(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -2) -> Tuple[int, str, str]:
    """
    @brief Implementa o algoritmo Smith-Waterman para o alinhamento local de sequências.

    @param seq1 Primeira sequência (string) a alinhar.
    @param seq2 Segunda sequência (string) a alinhar.
    @param match Pontuação para correspondência de caracteres (valor inteiro, padrão 2).
    @param mismatch Penalidade para caracteres diferentes (valor inteiro, padrão -1).
    @param gap Penalidade para introdução de gaps (valor inteiro, padrão -2).

    @return Uma tupla contendo:
        - A pontuação máxima do alinhamento local (int).
        - A sequência alinhada derivada de seq1 (str).
        - A sequência alinhada derivada de seq2 (str).

    @details Este algoritmo constrói uma matriz de pontuação e utiliza backtracking para encontrar o alinhamento local ótimo entre as duas sequências fornecidas.
    """
    m, n = len(seq1), len(seq2)
    matriz = np.zeros((m+1, n+1), dtype=int)
    score_maximo = 0
    max_pos = None

    for i in range(1, m+1):
        for j in range(1, n+1):
            match_score = match if seq1[i-1] == seq2[j-1] else mismatch
            matriz[i, j] = max(
                0,
                matriz[i-1, j-1] + match_score,  
                matriz[i-1, j] + gap,           
                matriz[i, j-1] + gap            
            )
            if matriz[i, j] > score_maximo:
                score_maximo = matriz[i, j]
                max_pos = (i, j)

    seq1_alinhada = []
    seq2_alinhada = []
    i, j = max_pos

    while matriz[i, j] > 0:
        if matriz[i, j] == matriz[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            seq1_alinhada.append(seq1[i-1])
            seq2_alinhada.append(seq2[j-1])
            i -= 1
            j -= 1
        elif matriz[i, j] == matriz[i-1, j] + gap:  
            seq1_alinhada.append(seq1[i-1])
            seq2_alinhada.append('-')
            i -= 1
        elif matriz[i, j] == matriz[i, j-1] + gap:  
            seq1_alinhada.append('-')
            seq2_alinhada.append(seq2[j-1])
            j -= 1

    seq1_alinhada = "".join(reversed(seq1_alinhada))
    seq2_alinhada = "".join(reversed(seq2_alinhada))

    return score_maximo, seq1_alinhada, seq2_alinhada
