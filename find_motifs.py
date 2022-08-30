#Finding a motif in DNA
#Given two strings of DNA s and t,
#Find all locations of t as a substring of s

s = 'GATATATGCATATACTT'
t = 'ATAT'

subsections = {i: s[i:i+len(t)] 
               for i in range(0, len(s)) 
               if len(s[i:i+len(t)]) == len(t)}

[k + 1 for k, v in subsections.items() if v == t] #Question calls for 1-indexed strings