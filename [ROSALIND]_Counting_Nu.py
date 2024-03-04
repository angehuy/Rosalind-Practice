### Rosalind Problems
#############################################################################

# Problem: Given string of DNA, return 4 integars separated by space of the counts of each nucleotide

string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Initialize a dictionary to store counts for each symbol
symbol_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Iterate through each letter in the string
for letter in string:
    # Increment the corresponding counter in the dictionary
    if letter in symbol_counts: # checks if key name exists in dict
        symbol_counts[letter] += 1 # accesses the key and increments the value

string = ""

for symbol, count in symbol_counts.items():
    # .items() returns each key:value pair as tuple
    string += str(count) + " "
print(string)