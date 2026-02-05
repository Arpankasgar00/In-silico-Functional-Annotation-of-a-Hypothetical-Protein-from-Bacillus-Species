from Bio import SeqIO

fasta_file = "data/hypothetical_protein.fasta"

record = SeqIO.read(fasta_file, "fasta")

print("ID:", record.id)
print("Description:", record.description)
print("Sequence length:", len(record.seq))
print("First 50 amino acids:", record.seq[:50])
