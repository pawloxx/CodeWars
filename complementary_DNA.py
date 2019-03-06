# A-> T
# T-> A
# G -> C
# C -> G

def DNA_strand(dna):
    dna_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    x = ""
    for i in dna:
        for k, v in dna_dict.items():
            if i == k:
                x += ''.join(v)
    return x


print(DNA_strand("TGCA"))