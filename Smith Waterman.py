from typing import List, Tuple

def SW(seq1: str, seq2: str, scoring_matrix: List[List[int]], g: int) -> Tuple[List[List[int]], List[List[str]]]:
    """
    @brief Implementa o algoritmo Smith-Waterman para alinhamento local.
    
    @param seq1 A primeira sequência a ser alinhada.
    @param seq2 A segunda sequência a ser alinhada.
    @param scoring_matrix Matriz de pontuação para alinhamento de bases.
    @param g A penalidade de gap.

    @return Uma tupla contendo duas matrizes:
        - A matriz de pontuação (score), que contém os valores de pontuação de cada célula.
        - A matriz de rastreamento (trace), que indica a direção do melhor caminho para reconstrução do alinhamento.
    
    @details O algoritmo Smith-Waterman realiza o alinhamento local entre duas sequências com base em uma matriz de pontuação e penalidade de gap. A matriz de rastreamento é usada para reconstruir o alinhamento após o cálculo das pontuações.
    """
    # Adição de gap ao início da sequência
    seq1 = "-" + seq1
    seq2 = "-" + seq2
    
    # Definir número de linhas e colunas em nossa matriz 
    n_lins = len(seq1)
    n_cols = len(seq2)

    # Construção das matrizes score e trace de tamanho (n_lins x n_cols)
    score = [[0] * (n_cols) for _ in range(n_lins)]
    trace = [[''] * (n_cols) for _ in range(n_lins)]

    # Preenchimento da matriz score
    for L in range(1, n_lins):
        for C in range(1, n_cols):
            # Cálculo dos scores diagonal, esquerda, e ascendente
            D = score[L - 1][C - 1] + subst(scoring_matrix, seq1[C], seq2[L])  # Diagonal
            E = score[L][C - 1] + g                                            # Esquerda == gap em seq1
            A = score[L - 1][C] + g                                            # Ascendente == gap em seq2

            # Escolha do melhor score e preenchimento da matriz score
            direcao_final = max(D, E, A, 0)     # 0 impede valores negativos
            score[L][C] = direcao_final

            # Preenchimento da matriz trace
            if direcao_final == D:
                trace[L][C] = "D"
            elif direcao_final == E:
                trace[L][C] = "E"
            elif direcao_final == A:
                trace[L][C] = "A"
            elif direcao_final == 0:
                trace[L][C] = ""
            else:
                raise ValueError(f"Unexpected trace value at L={L}, C={C}: {trace[L][C]}")  # Handle unexpected cases

    return score, trace

def score_SW(score: List[List[int]]) -> int:
    """
    @brief Retorna o valor de score máximo da matriz Smith-Waterman.
    
    @param score A matriz de pontuação gerada pelo algoritmo Smith-Waterman.

    @return O valor máximo encontrado na matriz de pontuação.
    
    @details A função percorre toda a matriz de pontuação e retorna o valor máximo, que corresponde ao alinhamento local mais forte entre as duas sequências.
    """
    max_value = max(max(row) for row in score)
    return max_value

def reconstruct_SW(seq1: str, seq2: str, score: List[List[int]], trace: List[List[str]]) -> Tuple[str, str]:
    """
    @brief Reconstrói os alinhamentos baseando-se nas matrizes geradas pelo algoritmo Smith-Waterman.
    
    @param seq1 A primeira sequência a ser alinhada.
    @param seq2 A segunda sequência a ser alinhada.
    @param score A matriz de pontuação gerada pelo algoritmo.
    @param trace A matriz de rastreamento gerada pelo algoritmo.

    @return Um tupla contendo as duas sequências alinhadas.
    
    @details A função realiza o backtracking na matriz de rastreamento para reconstruir o alinhamento local ótimo entre as duas sequências.
    """
    indices = []
    maximo = score_SW(score)             
    for i in range(len(score)):
        for j in range(len(score[i])):
            if score[i][j] == maximo:
                indices.append((i, j))
    
    # Associa a posição inicial para reconstrução ao/s máximo/s da matriz
    alinhamento_seq1 = ''
    alinhamento_seq2 = ''
    
    for pos_max in indices:
        L, C = pos_max

        # Reconstrução do alinhamento
        while C > 0 or L > 0:
            if trace[L][C] == 'D':
                L -= 1
                C -= 1
                alinhamento_seq1 = seq1[C] + alinhamento_seq1
                alinhamento_seq2 = seq2[L] + alinhamento_seq2
            elif trace[L][C] == 'E':
                C -= 1
                alinhamento_seq1 = seq1[C] + alinhamento_seq1
                alinhamento_seq2 = '-' + alinhamento_seq2
            elif trace[L][C] == 'A':
                L -= 1
                alinhamento_seq1 = '-' + alinhamento_seq1
                alinhamento_seq2 = seq2[L] + alinhamento_seq2
            elif trace[L][C] == '':    # Garante que a reconstrução termina em 0
                break

    return alinhamento_seq1, alinhamento_seq2
