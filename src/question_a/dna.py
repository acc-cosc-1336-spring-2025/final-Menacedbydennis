# 1. FUNCTION IMPLEMENTATION (goes at the top)
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            yield i + 1  # Return positions as separate values