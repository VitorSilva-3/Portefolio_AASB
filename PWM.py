"""!
@package sequence_matrix
@brief Module for sequence matrix analysis and position weight calculations.

This module provides functionality for:
- Counting nucleotides/amino acids in sequence alignments
- Position Weight Matrix (PWM) calculation
- Position-Specific Scoring Matrix (PSSM) calculation
- Sequence probability calculations
"""

from typing import List, Dict, Union, Set
import math
import re
from collections import Counter

Number = Union[int, float]
Matrix = List[Dict[str, Number]]

def count_table(seqs: List[str], alphabet: str = "ACGT", pseudocount: float = 0.0) -> Matrix:
    """!
    @brief Calculate count table for each column in a sequence alignment.
    
    @param seqs List of aligned sequences
    @param alphabet Set of allowed characters (default: "ACGT" for DNA)
    @param pseudocount Value to add to each count to avoid zeros
    
    @return List of dictionaries with character counts for each position
    
    @exception AssertionError If sequences have different lengths
    """
    if not seqs:
        return []
        
    if not all(len(seqs[0]) == len(s) for s in seqs):
        raise ValueError("All sequences must have the same length")
        
    counts: Matrix = []
    for column in zip(*seqs):
        column_counts = {base: column.count(base) + pseudocount for base in alphabet}
        counts.append(column_counts)
    
    return counts

def calculate_pwm(seqs: List[str], seq_type: str = "DNA", pseudocount: float = 0.0) -> Matrix:
    """!
    @brief Calculate Position Weight Matrix (PWM).
    
    @param seqs List of aligned sequences
    @param seq_type "DNA" or "PROTEIN" to define alphabet
    @param pseudocount Value to add to counts to avoid zeros
    
    @return List of dictionaries with normalized frequencies
    
    @exception ValueError If seq_type is invalid or sequences have different lengths
    """
    if not seqs:
        return []
    
    seq_type = seq_type.upper()
    if seq_type not in ["DNA", "PROTEIN"]:
        raise ValueError(f"Invalid sequence type: {seq_type}")
        
    alphabet = "ACGT" if seq_type == "DNA" else "ARNDCQEGHILKMFPSTWYVBZX_"
    counts = count_table(seqs, alphabet=alphabet, pseudocount=pseudocount)
    
    seq_length = len(seqs)
    alphabet_size = len(alphabet)
    normalization_factor = seq_length + alphabet_size * pseudocount
    
    pwm: Matrix = [
        {k: v / normalization_factor for k, v in pos.items()}
        for pos in counts
    ]
    
    return pwm

def round_matrix(matrix: Matrix, decimals: int = 2) -> Matrix:
    """!
    @brief Round values in a position matrix to specified decimal places.
    
    @param matrix Position matrix (PWM or PSSM)
    @param decimals Number of decimal places
    
    @return Matrix with rounded values
    """
    return [
        {k: round(v, decimals) for k, v in pos.items()}
        for pos in matrix
    ]

def sequence_probability(seq: str, pwm: Matrix) -> float:
    """!
    @brief Calculate probability of generating a sequence given a PWM.
    
    @param seq Sequence to calculate probability for
    @param pwm Position Weight Matrix
    
    @return Probability of generating the sequence
    
    @exception ValueError If sequence length doesn't match PWM length
    """
    if len(seq) != len(pwm):
        raise ValueError("Sequence length must match PWM length")
    
    prob = 1.0
    for base, column in zip(seq, pwm):
        try:
            prob *= column[base]
        except KeyError:
            raise ValueError(f"Invalid character in sequence: {base}")
    
    return prob

def find_most_probable(seq: str, pwm: Matrix) -> List[str]:
    """!
    @brief Find most probable subsequence(s) in a larger sequence using PWM.
    
    @param seq Larger sequence to search in
    @param pwm Position Weight Matrix
    
    @return Sorted list of most probable subsequences
    
    @exception ValueError If sequence is shorter than PWM length
    """
    motif_length = len(pwm)
    if len(seq) < motif_length:
        raise ValueError("Sequence must be at least as long as PWM")
    
    probabilities: Dict[str, float] = {}
    pattern = '.' * motif_length
    
    for match in re.finditer(f'(?=({pattern}))', seq):
        subseq = match.group(1)
        probabilities[subseq] = sequence_probability(subseq, pwm)
    
    if not probabilities:
        return []
        
    max_prob = max(probabilities.values())
    return sorted(set(k for k, v in proba
