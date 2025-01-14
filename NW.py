"""!
@package sequence_alignment
@brief Module for sequence alignment using Blosum62 substitution matrix.

This module provides functionality for aligning two sequences using the Blosum62
substitution matrix and a gap penalty. It includes functions for calculating
alignment scores, reconstructing alignments, and visualizing the alignment matrix.
"""

from typing import List, Tuple, Union
from blosum import Blosum62
from pprint import pprint

def align(s1: str, s2: str, g: int = -8) -> Tuple[List[List[int]], List[List[str]]]:
    """!
    @brief Aligns two sequences using Blosum62 substitution matrix and gap penalty.
    
    @param s1: First sequence to align
    @param s2: Second sequence to align
    @param g: Gap penalty (default: -8)
    
    @return Tuple containing:
            - List[List[int]]: Score matrix
            - List[List[str]]: Traceback matrix
    
    @exception ValueError If input sequences are empty
    
    @details The function uses dynamic programming to compute the optimal global
             alignment between two sequences. It builds a score matrix and a
             traceback matrix to store the alignment path.
    """
    if not s1 or not s2:
        raise ValueError("Input sequences cannot be empty")
        
    subst = Blosum62().subst
    
    # Initialize score and trace matrices
    score: List[List[int]] = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    trace: List[List[str]] = [[' ' for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    
    # Initialize first row
    for p in range(len(s1)):
        score[0][p + 1] = score[0][p] + g
        trace[0][p + 1] = 'E'
    
    # Initialize first column
    for p in range(len(s2)):
        score[p + 1][0] = score[p][0] + g
        trace[p + 1][0] = 'C'
    
    # Fill matrices
    for p1, x1 in enumerate(s1):
        for p2, x2 in enumerate(s2):
            diagonal = score[p2][p1] + subst(x1, x2)
            up = score[p2][p1 + 1] + g
            left = score[p2 + 1][p1] + g
            
            score[p2 + 1][p1 + 1] = max(diagonal, up, left)
            
            if score[p2 + 1][p1 + 1] == diagonal:
                trace[p2 + 1][p1 + 1] = 'D'
            elif score[p2 + 1][p1 + 1] == up:
                trace[p2 + 1][p1 + 1] = 'C'
            else:
                trace[p2 + 1][p1 + 1] = 'E'
    
    return score, trace

def print_matrix(mat: List[List[int]]) -> None:
    """!
    @brief Prints a score matrix in a formatted way.
    
    @param mat Score matrix to print
    """
    for row in mat:
        print(' '.join(f"{x:3d}" for x in row))

def print_trace(mat: List[List[str]]) -> None:
    """!
    @brief Prints a traceback matrix.
    
    @param mat Traceback matrix to print
    """
    for row in mat:
        print(' '.join(row))

def get_alignment_score(s1: str, s2: str, g: int = -8) -> int:
    """!
    @brief Calculates the final alignment score between two sequences.
    
    @param s1 First sequence
    @param s2 Second sequence
    @param g Gap penalty (default: -8)
    
    @return Final alignment score
    """
    return align(s1, s2, g)[0][-1][-1]

def reconstruct_alignment(s1: str, s2: str, trace: List[List[str]]) -> Tuple[str, str]:
    """!
    @brief Reconstructs the alignment from the traceback matrix.
    
    @param s1 First sequence
    @param s2 Second sequence
    @param trace Traceback matrix
    
    @return Tuple containing aligned sequences (aligned_s1, aligned_s2)
    
    @exception ValueError If traceback matrix contains invalid direction
    """
    C, L = len(s1), len(s2)
    aligned_s1, aligned_s2 = '', ''
    
    while C > 0 or L > 0:
        if trace[L][C] == 'D':
            L -= 1
            C -= 1
            aligned_s1 = s1[C] + aligned_s1
            aligned_s2 = s2[L] + aligned_s2
        elif trace[L][C] == 'E':
            C -= 1
            aligned_s1 = s1[C] + aligned_s1
            aligned_s2 = '-' + aligned_s2
        elif trace[L][C] == 'C':
            L -= 1
            aligned_s1 = '-' + aligned_s1
            aligned_s2 = s2[L] + aligned_s2
        else:
            raise ValueError(f"Invalid direction '{trace[L][C]}' in traceback matrix")
    
    return aligned_s1, aligned_s2

if __name__ == "__main__":
    # Example usage
    s1, s2 = "HGWAG", "PHSWG"
    score_matrix, trace_matrix = align(s1, s2)
    print("Score matrix:")
    print_matrix(score_matrix)
    print("\nTrace matrix:")
    print_trace(trace_matrix)
    aligned_s1, aligned_s2 = reconstruct_alignment(s1, s2, trace_matrix)
    print("\nAlignment:")
    print(aligned_s1)
    print(aligned_s2)
