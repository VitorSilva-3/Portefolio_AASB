from collections import defaultdict
from typing import List, Dict, Tuple

DEBUG: bool = False  

## @package sequence_analysis
#  Módulo para análise de sequências biológicas.
#  Este módulo inclui funções para mapear substrings em uma sequência,
#  encontrar hits entre sequências e estender alinhamentos.

def query_map(seq: str, window_size: int) -> Dict[str, List[int]]:
    """
    @brief Cria um mapa de substrings e suas posições na sequência.

    @param seq Sequência de entrada.
    @param window_size Tamanho da janela para substrings.
    @return Dicionário com substrings como chaves e listas de posições como valores.
    """
    res = defaultdict(list)
    size = len(seq)
    for position in range(size - window_size + 1):
        subseq = seq[position:position + window_size]
        res[subseq].append(position)
        if DEBUG:
            print(f"Substring encontrada: {subseq} na posição {position}")
    if DEBUG:
        print("Mapa de substrings criado:", dict(res))
    return res

def get_all_positions(subseq: str, seq: str) -> List[int]:
    """
    @brief Encontra todas as posições de uma substring em uma sequência.

    @param subseq Substring a ser encontrada.
    @param seq Sequência onde buscar.
    @return Lista de posições onde a substring ocorre.
    """
    return [i for i in range(len(seq) - len(subseq) + 1) if seq[i:i + len(subseq)] == subseq]

def hits(qm: Dict[str, List[int]], seq: str) -> List[Tuple[int, int]]:
    """
    @brief Identifica hits entre duas sequências.

    @param qm Mapa de substrings gerado pela função query_map.
    @param seq Sequência para comparação.
    @return Lista de tuplas (posição na query, posição na sequência).
    """
    res = []
    for subseq, positions_query in qm.items():
        for pos_query in positions_query:
            for pos_seq in get_all_positions(subseq, seq):
                res.append((pos_query, pos_seq))
    return res

def extend_hit_direction(query: str, seq: str, hit: Tuple[int, int], window_size: int, direction: int) -> Tuple[int, int, int, int]:
    """
    @brief Estende um alinhamento em uma direção.

    @param query Sequência de query.
    @param seq Sequência de referência.
    @param hit Tupla com posições iniciais (query, sequência).
    @param window_size Tamanho da janela inicial.
    @param direction Direção da extensão (+1 para frente, -1 para trás).
    @return Tupla com posição inicial na query, posição inicial na sequência,
            tamanho do alinhamento e número de caracteres iguais.
    """
    pos_query, pos_seq = hit
    match_size = window_size
    equal_chars = window_size

    while 0 <= pos_query + direction < len(query) and 0 <= pos_seq + direction < len(seq):
        pos_query += direction
        pos_seq += direction
        if query[pos_query] == seq[pos_seq]:
            equal_chars += 1
        else:
            if equal_chars < (match_size + 1) // 2:
                break
        match_size += 1

    start_query = pos_query - (match_size - 1) * direction
    start_seq = pos_seq - (match_size - 1) * direction
    return start_query, start_seq, match_size, equal_chars

if __name__ == "__main__":
    query = "AATATAT"
    seq = "AATATGTTATATAATAATATTT"

    window_size = 3
    qm = query_map(query, window_size)

    hits_result = hits(qm, seq)
    print("Hits encontrados:", hits_result)

    for hit in hits_result:
        result = extend_hit_direction(query, seq, hit, window_size, direction=1)
        print("Extensão do hit:", hit, "->", result)
