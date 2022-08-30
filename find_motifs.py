import io

#Finding a motif in DNA
#Given two strings of DNA s and t,
#Find all locations of t as a substring of s

f = open('rosalind_subs.txt')
lines = f.readlines()
s = lines[0].strip('\n')
t = lines[1].strip('\n')
subsections = {i: s[i:i+len(t)] 
               for i in range(0, len(s)) 
               if len(s[i:i+len(t)]) == len(t)}

result = [k + 1 for k, v in subsections.items() if v == t]

for item in result:
    print(item,end=' ')
