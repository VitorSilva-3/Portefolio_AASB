from typing import List, Tuple
import unittest

def alinhamento(seq1: str, seq2: str) -> Tuple[str, str]:
    """!
    @brief Alinha duas sequências utilizando o algoritmo Needleman-Wunsch.
    
    Esta função implementa o algoritmo de Needleman-Wunsch para alinhar duas sequências.
    
    @param seq1: Primeira sequência a ser alinhada.
    @param seq2: Segunda sequência a ser alinhada.
    @return: Um tuplo contendo as duas sequências alinhadas.
    @throws ValueError: Se alguma das sequências estiver vazia.
    """
    if not seq1 or not seq2:
        raise ValueError("As sequências não podem estar vazias")

    # Inicialização de parâmetros
    correspondencia: int = 1
    nao_correspondencia: int = -1
    penalizacao_lacuna: int = -1

    # Criação da matriz de pontuação
    n: int = len(seq1) + 1
    m: int = len(seq2) + 1
    matriz_pontuacao: List[List[int]] = [[0] * m for _ in range(n)]

    # Inicialização das bordas
    for i in range(n):
        matriz_pontuacao[i][0] = i * penalizacao_lacuna
    for j in range(m):
        matriz_pontuacao[0][j] = j * penalizacao_lacuna

    # Preenchimento da matriz
    for i in range(1, n):
        for j in range(1, m):
            pontuacao_correspondencia: int = correspondencia if seq1[i - 1] == seq2[j - 1] else nao_correspondencia
            matriz_pontuacao[i][j] = max(
                matriz_pontuacao[i - 1][j - 1] + pontuacao_correspondencia,
                matriz_pontuacao[i - 1][j] + penalizacao_lacuna,
                matriz_pontuacao[i][j - 1] + penalizacao_lacuna,
            )

    # Traçado de volta para obter alinhamento
    seq1_alinhada: str = ""
    seq2_alinhada: str = ""
    i, j = len(seq1), len(seq2)

    while i > 0 or j > 0:
        if i > 0 and j > 0 and matriz_pontuacao[i][j] == matriz_pontuacao[i - 1][j - 1] + (
            correspondencia if seq1[i - 1] == seq2[j - 1] else nao_correspondencia
        ):
            seq1_alinhada = seq1[i - 1] + seq1_alinhada
            seq2_alinhada = seq2[j - 1] + seq2_alinhada
            i -= 1
            j -= 1
        elif i > 0 and matriz_pontuacao[i][j] == matriz_pontuacao[i - 1][j] + penalizacao_lacuna:
            seq1_alinhada = seq1[i - 1] + seq1_alinhada
            seq2_alinhada = "-" + seq2_alinhada
            i -= 1
        else:
            seq1_alinhada = "-" + seq1_alinhada
            seq2_alinhada = seq2[j - 1] + seq2_alinhada
            j -= 1

    return seq1_alinhada, seq2_alinhada

def consenso(seq1: str, seq2: str) -> str:
    """!
    @brief Gera a sequência de consenso de duas sequências alinhadas.
    
    @param seq1: Primeira sequência alinhada.
    @param seq2: Segunda sequência alinhada.
    @return: Sequência de consenso.
    @throws ValueError: Se as sequências tiverem comprimentos diferentes.
    """
    if len(seq1) != len(seq2):
        raise ValueError("As sequências devem ter o mesmo comprimento")

    consenso_lista: List[str] = []
    for a, b in zip(seq1, seq2):
        if a == b:
            consenso_lista.append(a)
        elif a == "-" or b == "-":
            consenso_lista.append("-")
        else:
            consenso_lista.append("N")  # Representa conflito
    return "".join(consenso_lista)

def alinhamento_progressivo(sequencias: List[str]) -> List[str]:
    """!
    @brief Realiza alinhamento progressivo de uma lista de sequências.
    
    @param sequencias: Lista de sequências a serem alinhadas.
    @return: Lista de sequências alinhadas progressivamente.
    @throws ValueError: Se a lista de sequências estiver vazia.
    """
    if not sequencias:
        raise ValueError("A lista de sequências não pode estar vazia")
    if len(sequencias) < 2:
        return sequencias

    # Alinhar as duas primeiras sequências
    seq1_alinhada, seq2_alinhada = alinhamento(sequencias[0], sequencias[1])
    alinhamento_multiplo: List[str] = [seq1_alinhada, seq2_alinhada]

    # Alinhar progressivamente as sequências restantes
    for i in range(2, len(sequencias)):
        # Calcular o consenso atual
        consenso_atual: str = consenso(alinhamento_multiplo[0], alinhamento_multiplo[1])
        for seq in alinhamento_multiplo[2:]:
            consenso_atual = consenso(consenso_atual, seq)

        # Alinhar o consenso com a nova sequência
        consenso_alinhado, nova_seq_alinhada = alinhamento(consenso_atual, sequencias[i])

        # Atualizar o alinhamento múltiplo
        for j in range(len(alinhamento_multiplo)):
            seq_atualizada: str = ""
            seq_alinhada: str = alinhamento_multiplo[j]
            indice_consenso: int = 0

            for caractere in consenso_alinhado:
                if caractere == "-":
                    seq_atualizada += "-"
                else:
                    seq_atualizada += seq_alinhada[indice_consenso]
                    indice_consenso += 1

            alinhamento_multiplo[j] = seq_atualizada

        # Adicionar a nova sequência alinhada
        alinhamento_multiplo.append(nova_seq_alinhada)

    return alinhamento_multiplo
