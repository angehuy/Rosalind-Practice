''' Rosalind Problems
Problem: Transcribing DNA into RNA (replace all instances of U with T)
'''

def transcribe(string):
    print(string.replace('T','U'))

if __name__ == "__main__" :
    l1 = open("./rosalind_rna.txt", "r")
    l2 = l1.readline().strip() # remove all the white/tab space
    transcribe(l2)