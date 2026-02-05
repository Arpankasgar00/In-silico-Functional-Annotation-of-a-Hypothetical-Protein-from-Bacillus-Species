from Bio.Blast import NCBIXML

blast_xml = "results/blast_result.xml"

accessions = []

with open(blast_xml) as handle:
    blast_records = NCBIXML.parse(handle)
    blast_record = next(blast_records)

for alignment in blast_record.alignments[:10]:
    accession = alignment.accession
    title = alignment.title
    evalue = alignment.hsps[0].expect

    accessions.append(accession)

    print("Accession:", accession)
    print("Title:", title)
    print("E-value:", evalue)
    print("-" *5 )

print("Top BLAST accessions:", accessions)
