f = open('rosalind_splc.txt', 'r')
file = f.read()
sequences = list(map(lambda x: x.replace('\n', ''), re.split(r'>.*\n', file)))
sequences.pop(0) #parser was creating an empty entry

main_seq = sequences.pop(0)
for s in sequences:
    main_seq = main_seq.replace(s,'')
translate_to_protein(main_seq)