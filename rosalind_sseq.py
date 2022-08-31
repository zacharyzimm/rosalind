def read_fasta(filepath):
    """
    Reads a FASTA file as provided by rosalind
    """
    with open(filepath, 'r') as f:
        file = f.read()
        sequences = list(map(lambda x: x.replace('\n', ''), re.split(r'>.*\n', file)))
        sequences.pop(0)
        return sequences

def find_subseq(s, t):
    subseq = [*t]
    result = []
    n = 0
    for char in subseq:
        n = s.find(char, n)
        result.append(n)
        n+=1
    for item in result:
        print(item + 1, end=' ') #rosalind uses 1-notation for strings
    return result

seqs = read_fasta('rosalind_sseq.txt')
result = find_subseq(seqs[0], seqs[1])