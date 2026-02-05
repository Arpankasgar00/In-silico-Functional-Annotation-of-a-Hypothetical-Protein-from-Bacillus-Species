import requests

def fetch_uniprot_annotation(accession):
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    protein_name = data["proteinDescription"]["recommendedName"]["fullName"]["value"]

    functions = []
    if "comments" in data:
        for comment in data["comments"]:
            if comment["commentType"] == "FUNCTION":
                for text in comment["texts"]:
                    functions.append(text["value"])

    organism = data["organism"]["scientificName"]

    return protein_name, organism, functions



blast_accessions = [" WP_070145234","HHT7239960" ]

for acc in blast_accessions:
    result = fetch_uniprot_annotation(acc)

    if result:
        protein, organism, functions = result
        print("Accession:", acc)
        print("Protein:", protein)
        print("Organism:", organism)
        print("Function:")
        for f in functions:
            print("-", f)
        print("=" * 70)
