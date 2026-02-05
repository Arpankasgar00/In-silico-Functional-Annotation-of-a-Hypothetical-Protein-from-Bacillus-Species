from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

record = SeqIO.read("data/hypothetical_protein.fasta", "fasta")
sequence = str(record.seq)

analysis = ProteinAnalysis(sequence)

print("Molecular Weight:", analysis.molecular_weight())
print("Isoelectric Point (pI):", analysis.isoelectric_point())
print("Aromaticity:", analysis.aromaticity())
print("Instability Index:", analysis.instability_index())
print("GRAVY:", analysis.gravy())
