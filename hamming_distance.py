def hamming_distance(s, t):
    """
    Assuming two strings of equal length s and t,
    calculates the Hamming distance between them,
    defined as the number of mismatched symbols at corresponding locations
    in each string
    """
    if len(s) != len(t):
        raise Exception("Error! S and T must be of equal length")
        
    return sum([0 if s[i:i+1] == t[i:i+1] else 1 for i in range(len(s))])

filename = 'rosalind_hamm.txt'
with open(filename) as f:
    strings = f.readlines()
    s = strings[0]
    t = strings[1]
    print(hamming_distance(s, t))