from question_a.dna import get_most_likely_ancestor_consensus

def main():
    while True:
        dna1 = input("Enter DNA string (9-16 letters): ").upper()
        if not (9 <= len(dna1) <= 16) or not dna1.isalpha():
            print("Invalid DNA string.")
            continue

        dna2 = input("Enter DNA substring (4 letters): ").upper()
        if len(dna2) != 4 or not dna2.isalpha():
            print("Invalid DNA substring.")
            continue

        # 3. CALL THE FUNCTION AND UNPACK THE RESULTS
        result = list(get_most_likely_ancestor_consensus(dna1, dna2))
        if result:
            print("Substring found at positions:", *result)
        else:
            print("Substring not found.")

        if input("Try again? (yes/no): ").lower() != 'yes':
            break
