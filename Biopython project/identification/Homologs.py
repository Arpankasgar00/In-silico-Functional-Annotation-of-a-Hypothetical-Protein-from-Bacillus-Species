from Bio.Blast import NCBIXML

with open("results/blast_result.xml") as handle:
    blast_record = next(NCBIXML.parse(handle))


for alignment in blast_record.alignments[:5]:
    hsp = alignment.hsps[0]

    identity = (hsp.identities / hsp.align_length) * 100

    print("Protein:", alignment.title)
    print("Accession:", alignment.accession)
    print("Identity (%):", round(identity, 2))
    print("Alignment length:", hsp.align_length)
    print("E-value:", hsp.expect)
    print("-" * 60)
