''' Rosalind Problems
Problem: Get the reverse complement. The two strands of DNA double helix are reverse
# complements of each other

# I have two versions (trial + error)
'''

def reverse_complement(string):
    complement_dict = {"A": "T", "T":"A", "G":"C", "C":"G"}
    reverse_complement = ""
    for letter in string:
        reverse_complement += complement_dict[letter]
    print(reverse_complement[::-1]) # use splicing to reverse the string



if __name__ == "__main__" :
    l1 = open("./rosalind_revc.txt", "r")
    l2 = l1.readline().strip() # remove all the white/tab space
    reverse_complement(l2)



def reverse_complement2(string):
    complement_dict = {"A": "T", "T":"A", "G":"C", "C":"G"}
    reverse_complement = ""
    for letter in string:
        ##letter.replace(letter, complement_dict[letter])
        ##reverse_complement += letter 
        # ^doesn't work because you're getting the original letter, not the letter with the replacement
        # because replace creates a copy of the string
        reverse_complement += letter.replace(letter, complement_dict[letter])
        # ^ this works

    print(reverse_complement[::-1]) # use splicing to reverse the string

# reverse_complement2("AAAACCCGGT")

