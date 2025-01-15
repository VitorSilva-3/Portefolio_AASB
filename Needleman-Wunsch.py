from typing import List, Tuple
from Blosum import Blosum62

## @package alinhamento_sequencias
#  @brief Módulo para alinhamento de sequências utilizando a matriz de substituição Blosum62.
#
#  Este módulo oferece funcionalidades para alinhar duas sequências utilizando a matriz
#  de substituição Blosum62 e uma penalização por gaps. Inclui funções para calcular pontuações
#  de alinhamento, reconstruir alinhamentos e visualizar a matriz de alinhamento.

def alinhar(seq1: str, seq2: str, gap: int = -8) -> Tuple[List[List[int]], List[List[str]]]:
    """!
    @brief Alinha duas sequências utilizando a matriz de substituição Blosum62 e uma penalização por gaps.
    
    @param seq1: Primeira sequência a alinhar.
    @param seq2: Segunda sequência a alinhar.
    @param gap: Penalização por gap (valor predefinido: -8).
    
    @return Tuplo contendo:
            - List[List[int]]: Matriz de pontuação.
            - List[List[str]]: Matriz de traceback.
    
    @exception ValueError Se as sequências de entrada forem vazias.
    
    @details A função utiliza programação dinâmica para calcular o alinhamento global
             ideal entre duas sequências. Cria uma matriz de pontuação e uma matriz de traceback
             para armazenar o caminho do alinhamento.
    """
    if not seq1 or not seq2:
        raise ValueError("As sequências de entrada não podem ser vazias")
        
    subst = Blosum62().substituicao
    
    pontuacao: List[List[int]] = [[0 for _ in range(len(seq1) + 1)] for _ in range(len(seq2) + 1)]
    traceback: List[List[str]] = [[' ' for _ in range(len(seq1) + 1)] for _ in range(len(seq2) + 1)]
    
    for p in range(len(seq1)):
        pontuacao[0][p + 1] = pontuacao[0][p] + gap
        traceback[0][p + 1] = 'E'
    
    for p in range(len(seq2)):
        pontuacao[p + 1][0] = pontuacao[p][0] + gap
        traceback[p + 1][0] = 'C'
    
    for p1, x1 in enumerate(seq1):
        for p2, x2 in enumerate(seq2):
            diagonal = pontuacao[p2][p1] + subst(x1, x2)
            acima = pontuacao[p2][p1 + 1] + gap
            esquerda = pontuacao[p2 + 1][p1] + gap
            
            pontuacao[p2 + 1][p1 + 1] = max(diagonal, acima, esquerda)
            
            if pontuacao[p2 + 1][p1 + 1] == diagonal:
                traceback[p2 + 1][p1 + 1] = 'D'
            elif pontuacao[p2 + 1][p1 + 1] == acima:
                traceback[p2 + 1][p1 + 1] = 'C'
            else:
                traceback[p2 + 1][p1 + 1] = 'E'
    
    return pontuacao, traceback

def imprimir_matriz(matriz: List[List[int]]) -> None:
    """!
    @brief Imprime uma matriz de pontuação de forma formatada.
    
    @param matriz Matriz de pontuação a ser impressa.
    """
    for linha in matriz:
        print(' '.join(f"{x:3d}" for x in linha))

def imprimir_traceback(matriz: List[List[str]]) -> None:
    """!
    @brief Imprime uma matriz de traceback.
    
    @param matriz Matriz de traceback a ser impressa.
    """
    for linha in matriz:
        print(' '.join(linha))

def obter_pontuacao_alinhamento(seq1: str, seq2: str, gap: int = -8) -> int:
    """!
    @brief Calcula a pontuação final de alinhamento entre duas sequências.
    
    @param seq1 Primeira sequência.
    @param seq2 Segunda sequência.
    @param gap Penalização por gaps (valor predefinido: -8).
    
    @return Pontuação final de alinhamento.
    """
    return alinhar(seq1, seq2, gap)[0][-1][-1]

def reconstruir_alinhamento(seq1: str, seq2: str, traceback: List[List[str]]) -> Tuple[str, str]:
    """!
    @brief Reconstrói o alinhamento a partir da matriz de traceback.
    
    @param seq1 Primeira sequência.
    @param seq2 Segunda sequência.
    @param traceback Matriz de traceback.
    
    @return Tuplo contendo as sequências alinhadas (aligned_seq1, aligned_seq2).
    
    @exception ValueError Se a matriz de traceback contiver direções inválidas.
    """
    C, L = len(seq1), len(seq2)
    alinhada_seq1, alinhada_seq2 = '', ''
    
    while C > 0 or L > 0:
        if traceback[L][C] == 'D':
            L -= 1
            C -= 1
            alinhada_seq1 = seq1[C] + alinhada_seq1
            alinhada_seq2 = seq2[L] + alinhada_seq2
        elif traceback[L][C] == 'E':
            C -= 1
            alinhada_seq1 = seq1[C] + alinhada_seq1
            alinhada_seq2 = '-' + alinhada_seq2
        elif traceback[L][C] == 'C':
            L -= 1
            alinhada_seq1 = '-' + alinhada_seq1
            alinhada_seq2 = seq2[L] + alinhada_seq2
        else:
            raise ValueError(f"Direção inválida '{traceback[L][C]}' na matriz de traceback")
    
    return alinhada_seq1, alinhada_seq2

if __name__ == "__main__":
    seq1, seq2 = "HGWAG", "PHSWG"
    matriz_pontuacao, matriz_traceback = alinhar(seq1, seq2)
    print("Matriz de Pontuação:")
    imprimir_matriz(matriz_pontuacao)
    print("\nMatriz de Traceback:")
    imprimir_traceback(matriz_traceback)
    alinhada_seq1, alinhada_seq2 = reconstruir_alinhamento(seq1, seq2, matriz_traceback)
    print("\nAlinhamento:")
    print(alinhada_seq1)
    print(alinhada_seq2)
