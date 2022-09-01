import re

def count_transitions(s1, s2):
    """
    counts the number of A->G and C->T (and vice versa)
    transitions between two sequences of equal length
    """
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    return sum([1 if ((s1[i:i+1] != s2[i:i+1]) and 
                ((s1[i:i+1] in purines and s2[i:i+1] in purines) or
                (s1[i:i+1] in pyrimidines and s2[i:i+1] in pyrimidines)))
                else 0 
                for i in range(len(s1))])

def count_transversions(s1, s2):
    """
    counts the number of transversions between two strings of equal length.
    transversions are where a purine is substituted for a pyrimidine or vice-versa
    """
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    
    return sum([1 if ((s1[i:i+1] != s2[i:i+1]) and 
                ((s1[i:i+1] in purines and s2[i:i+1] in pyrimidines) or
                (s1[i:i+1] in pyrimidines and s2[i:i+1] in purines)))
                else 0 
                for i in range(len(s1))])

def trans_ratio(filepath):
    """
    given two DNA strings of equal length in FASTA format,
    returns their transition/transversion ratio
    """
    with open(filepath, 'r') as f:
        file = f.read()
        sequences = list(map(lambda x: x.replace('\n', ''), re.split(r'>.*\n', file)))
        sequences.pop(0) #the way i parse the file causes the first entry to be an empty string
        s = sequences[0]
        t = sequences[1]
        return count_transitions(s,t)/count_transversions(s,t)

trans_ratio('rosalind_tran.txt')

