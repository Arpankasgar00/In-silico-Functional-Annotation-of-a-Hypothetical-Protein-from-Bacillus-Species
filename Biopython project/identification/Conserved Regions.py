from Bio.Blast import NCBIXML

with open("results/blast_result.xml") as handle:
    blast_record = next(NCBIXML.parse(handle))

print("Closest homologs:\n")
for alignment in blast_record.alignments[:1]:  # best hit
    hsp = alignment.hsps[0]

    print("Query alignment:")
    print(hsp.query[:100])

    print("\nMatch alignment:")
    print(hsp.match[:100])

    print("\nSubject alignment:")
    print(hsp.sbjct[:100])
