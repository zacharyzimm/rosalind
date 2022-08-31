import re
import io
#translate genetic code into protein

# codon table creation from
# from https://scipython.com/static/media/examples/E5/codon_lookup.py
# codon_lookup.py
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

#original code onwards

with open('rosalind_prot.txt') as file:
    f = file.read()
    codons = [f[i:i+3] for i in range(0, len(f), 3)]
    translated = []
    for codon in codons:
        if codon_table[codon] == '*':
            break
        translated.append(codon_table[codon])
    print(''.join(translated))