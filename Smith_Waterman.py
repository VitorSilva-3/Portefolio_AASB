import numpy as np
from typing import Tuple

def smith_waterman(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -2) -> Tuple[int, str, str]:
    """
    @brief Implements the Smith-Waterman algorithm for local sequence alignment.

    @param seq1 The first sequence (string) to be aligned.
    @param seq2 The second sequence (string) to be aligned.
    @param match The score for character matches (integer, default is 2).
    @param mismatch The penalty for character mismatches (integer, default is -1).
    @param gap The penalty for introducing gaps (integer, default is -2).

    @return A tuple containing:
        - The maximum alignment score (int).
        - The aligned sequence derived from seq1 (str).
        - The aligned sequence derived from seq2 (str).

    @details This algorithm builds a scoring matrix and uses backtracking to find the optimal local alignment
    between the two input sequences.
    """
    m, n = len(seq1), len(seq2)
    matriz = np.zeros((m+1, n+1), dtype=int)
    score_max = 0
    max_pos = None

    # Build the scoring matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            match_score = match if seq1[i-1] == seq2[j-1] else mismatch
            matriz[i, j] = max(
                0,
                matriz[i-1, j-1] + match_score,  # Diagonal (match/mismatch)
                matriz[i-1, j] + gap,           # Gap in seq2
                matriz[i, j-1] + gap            # Gap in seq1
            )
            if matriz[i, j] > score_max:
                score_max = matriz[i, j]
                max_pos = (i, j)

    # Backtracking to reconstruct the alignment
    seq1_aligned = []
    seq2_aligned = []
    i, j = max_pos

    while matriz[i, j] > 0:
        if matriz[i, j] == matriz[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            seq1_aligned.append(seq1[i-1])
            seq2_aligned.append(seq2[j-1])
            i -= 1
            j -= 1
        elif matriz[i, j] == matriz[i-1, j] + gap:  # Gap in seq2
            seq1_aligned.append(seq1[i-1])
            seq2_aligned.append('-')
            i -= 1
        elif matriz[i, j] == matriz[i, j-1] + gap:  # Gap in seq1
            seq1_aligned.append('-')
            seq2_aligned.append(seq2[j-1])
            j -= 1

    seq1_aligned = "".join(reversed(seq1_aligned))
    seq2_aligned = "".join(reversed(seq2_aligned))

    return score_max, seq1_aligned, seq2_aligned
