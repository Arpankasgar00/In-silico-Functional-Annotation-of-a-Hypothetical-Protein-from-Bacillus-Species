from Bio import SeqIO
from collections import Counter

record = SeqIO.read("data/hypothetical_protein.fasta", "fasta")
sequence = record.seq

aa_count = Counter(sequence)

print("Amino acid composition:")
for aa, count in aa_count.items():
    print(f"{aa}: {count}")
