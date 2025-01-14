"""!
@package dna_processing
@brief Module for DNA sequence processing and protein extraction.

This module provides functionality for DNA sequence manipulation, including:
- Reverse complement calculation
- Codon extraction
- Amino acid translation
- Protein identification from DNA sequences
- Open Reading Frame (ORF) analysis
"""

from typing import List, Set, Dict
from table import table  # Import codon to amino acid translation table

def revcomp(dna: str) -> str:
    """!
    @brief Calculate the reverse complement of a DNA sequence.
    
    @param dna DNA sequence string (should contain only ACGT characters)
    @return The reverse complement sequence
    
    @exception KeyError If DNA sequence contains invalid characters
    
    @details Reverses the DNA sequence and replaces each nucleotide with its
             complementary base (A↔T, C↔G)
    """
    if not dna:
        return ""
        
    if not all(base in "ACGT" for base in dna):
        raise ValueError("DNA sequence should only contain A, C, G, T characters")
        
    reverse = "".join(reversed(dna))
    return "".join(complementary_character(base) for base in reverse)

def complementary_character(base: str) -> str:
    """!
    @brief Get the complementary base for a DNA nucleotide.
    
    @param base Single character representing a DNA base (A, C, G, or T)
    @return Complementary base character
    
    @exception KeyError If input is not a valid DNA base
    """
    translation: Dict[str, str] = dict(zip("ACGT", "TGCA"))
    try:
        return translation[base]
    except KeyError:
        raise ValueError(f"Invalid DNA base: {base}")

def get_codons(dna: str) -> List[str]:
    """!
    @brief Split DNA sequence into codons (triplets).
    
    @param dna DNA sequence string
    @return List of complete codons (triplets)
    
    @details Incomplete codons at the end of the sequence are discarded
    """
    return [dna[i:i+3] for i in range(0, len(dna), 3) if len(dna[i:i+3]) == 3]

def codon_to_amino(codons: List[str]) -> str:
    """!
    @brief Translate a list of codons to amino acid sequence.
    
    @param codons List of DNA codons
    @return String of corresponding amino acids
    
    @exception KeyError If an invalid codon is encountered
    """
    try:
        return ''.join(table[codon] for codon in codons)
    except KeyError as e:
        raise ValueError(f"Invalid codon encountered: {e}")

def get_prots(amino: str) -> List[str]:
    """!
    @brief Extract all proteins from an amino acid sequence.
    
    @param amino Amino acid sequence string
    @return List of protein sequences (starting with M and ending with _)
    
    @details Proteins are identified as sequences that:
             - Start with Methionine (M)
             - End with a stop codon (_)
             - May overlap with other proteins
    """
    prots: List[str] = []
    inside_prot: bool = False
    current_prot: str = ''

    for aa in amino:
        if aa == 'M':
            inside_prot = True
            if current_prot:  # Handle nested proteins
                prots.append(current_prot + '_')
            current_prot = 'M'
        elif aa == '_':
            if inside_prot:
                prots.append(current_prot + '_')
            inside_prot = False
            current_prot = ''
        elif inside_prot:
            current_prot += aa
            
    return prots

def get_orfs(dna: str) -> List[List[str]]:
    """!
    @brief Calculate all 6 possible Open Reading Frames (ORFs) of a DNA sequence.
    
    @param dna DNA sequence string
    @return List of 6 ORFs (3 from forward strand, 3 from reverse complement)
    
    @details Each ORF is represented as a list of codons
    """
    def three_orfs(seq: str) -> List[List[str]]:
        """Generate 3 ORFs from a single strand."""
        return [get_codons(seq[p:]) for p in range(3)]
    
    return three_orfs(dna) + three_orfs(revcomp(dna))

def get_all_prots(dna: str) -> List[str]:
    """!
    @brief Extract all possible proteins from a DNA sequence.
    
    @param dna DNA sequence string
    @return List of unique proteins sorted by length (descending) and sequence
    
    @exception ValueError If DNA sequence contains invalid characters
    
    @details Analyzes all 6 reading frames and returns unique proteins
    """
    try:
        # Get amino acid sequences for all ORFs
        orfs: List[str] = [codon_to_amino(orf) for orf in get_orfs(dna)]
        # Extract proteins from each ORF
        prot_orfs: List[List[str]] = [get_prots(orf) for orf in orfs]
        # Create set of unique proteins
        unique_prots: Set[str] = {prot for prot_list in prot_orfs for prot in prot_list}
        # Sort by length (descending) and sequence
        return sorted(unique_prots, key=lambda p: (-len(p), p))
    except ValueError as e:
        raise ValueError(f"Error processing DNA sequence: {e}")

if __name__ == '__main__':
    test_dna = 'TGTGGGGAGGTCATAGGTACTGGCCC'
    try:
        proteins = get_all_prots(test_dna)
        print(f"DNA sequence: {test_dna}")
        print("Extracted proteins:")
        for protein in proteins:
            print(protein)
    except ValueError as e:
        print(f"Error: {e}")
