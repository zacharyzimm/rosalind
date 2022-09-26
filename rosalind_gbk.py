from Bio import Entrez

def get_count_of_entries(genus, first_date, second_date):
    """
    Given a genus name, followed by two dates in YYYY/MM/DD format
    Returns the number of Nucleotide GenBank Entries for the given genus published between the specified dates
    
    """
    Entrez.email = 'zacharyzimmerman@berkeley.edu'
    handle = Entrez.esearch(db='nucleotide', term=f'"{genus}"[Organism] AND ("{first_date}"[Publication Date]:"{second_date}"[Publication Date])')
    record = Entrez.read(handle)
    handle.close()
    return record['Count']

if __name__=="__main__":
    with open('rosalind_gbk.txt', 'r') as f:
        genus = f.readline().strip()
        first_date = f.readline().strip()
        second_date = f.readline().strip()
    count = get_count_of_entries(genus, first_date, second_date)
    print(count)
