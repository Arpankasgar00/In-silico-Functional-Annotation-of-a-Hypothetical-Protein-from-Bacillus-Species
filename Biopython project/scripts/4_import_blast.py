from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("data/hypothetical_protein.fasta", "fasta")

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
)

with open("results/blast_result.xml", "w") as out_put:
    out_put.write(result_handle.read())

print("BLAST search completed and saved.")
