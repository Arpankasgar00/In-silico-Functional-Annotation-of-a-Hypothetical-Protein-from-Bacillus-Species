from Bio.Blast import NCBIXML

with open("results/blast_result.xml") as handle:
    blast_record = next(NCBIXML.parse(handle))


organisms = set()

for alignment in blast_record.alignments[:10]:
    title = alignment.title

    if "[" in title and "]" in title:
        organism = title.split("[")[-1].split("]")[0]
        organisms.add(organism)

print("Organisms represented among top hits:")
for org in organisms:
    print("-", org)
