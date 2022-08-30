import io
from itertools import combinations

#Given a DNA sequence of at most 1kbp
#return the position and length of every reverse palindrome
#with length between 4 and 12

def reverse_complement(seq):
    """
    Generates the reverse complement of a DNA sequence
    """
    complement = str.maketrans({'A':'T', 'G':'C', 'T':'A', 'C':'G'})
    return seq[::-1].translate(complement)

def is_palindrome(seq):
    """
    checks if a DNA sequence is a palindrome,
    if it equals its reverse complement
    """
    return seq == reverse_complement(seq)

def find_restriction_sites(seq, smallest_motif, largest_motif):
    """
    Finds the position and length of all reverse palindromes in a sequence
    with length between smallest_motif and largest_motif
    """
    result = []
    for i in range(smallest_motif, largest_motif + 1):
        subsections = ({q: seq[q: q+i] 
                           for q in range(0, len(seq))
                           if len(seq[q:q+i]) == i })
        for k, v in subsections.items():
            if is_palindrome(v):
                result.append((k + 1, len(v))) #question calls for 1 indexed string
    return result

with open('rosalind_revp.txt') as f:
    next(f)
    fasta = f.readlines()
    seq = ''
    for line in fasta:
        seq = seq + line.strip('\n')
    answer = find_restriction_sites(seq, 4, 12)
    for item in answer:
        print(item[0],item[1])


    