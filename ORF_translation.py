import io
import re

def reverse_complement(seq):
    """
    Generates the reverse complement of a DNA sequence
    """
    return seq[::-1].translate(str.maketrans('ATCG','TAGC'))
    
def generate_reading_frames(seq):
    """
    Takes a sequence and generates all open reading frames
    returns a list of strings, each being an open reading frame
    """
    pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
    return set(pattern.findall(seq)+pattern.findall(reverse_complement(seq)))
    
def translate_to_protein(seq):
    """
    translates a single DNA sequence into its corresponding protein sequence
    """
    ####
    #from https://scipython.com/static/media/examples/E5/codon_lookup.py
    bases = ['T', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    ####
    grouped = [seq[i:i+3] for i in range(0, len(seq), 3) if len(seq[i:i+3])==3]
    translated = [codon_table[item] for item in grouped]
    return ''.join(translated)
    
def translate_dna_sequence(filepath):
    """
    Takes a single DNA sequence, generates the ORFs, and then translates
    them to protein. Prints out the translated proteins for the formatted answer to the question in rosalind
    
    for flexibility (and just practice), can take either a .txt file or a direct sequence as input
    built to be able to handle expanded use cases in the future if necessary
    """
    if filepath.endswith('.txt') or filepath.endswith('.fasta'):
        with open(filepath) as f:
            lines = f.readlines()
            header = lines.pop(0) #pops off the header of the FASTA file
            seq = ''
            for line in lines:
                seq += line.strip('\n')
    else:
        seq = filepath
    orfs = generate_reading_frames(seq)
    translated = list(map(translate_to_protein, orfs))
    for protein in translated:
        print(protein)
    return translated

#test case
seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
translate_dna_sequence(seq)

#Solution
translate_dna_sequence('rosalind_orf.txt')