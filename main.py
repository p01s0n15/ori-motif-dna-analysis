import re
from Bio import Entrez, SeqIO

Entrez.email = "meow@gmail.com"

ori_pattern = r"(?i)[TA]TTTAT[AG]TTT[TA]"

chromosome_ids = [
    "NC_001133.9", "NC_001134.8", "NC_001135.5", "NC_001136.10",
    "NC_001137.3", "NC_001138.5", "NC_001139.9", "NC_001140.6",
    "NC_001141.2", "NC_001142.9", "NC_001143.9", "NC_001144.5",
    "NC_001145.3", "NC_001146.8", "NC_001147.6", "NC_001148.4"
]

for chromosome_id in chromosome_ids:
    fetch_handle = Entrez.efetch(db="nucleotide", id=chromosome_id, rettype="fasta", retmode="text")
    seq_record = SeqIO.read(fetch_handle, "fasta")
    fetch_handle.close()

    filename = f"{chromosome_id}.fasta"
    with open(filename, "w") as output_handle:
        SeqIO.write(seq_record, output_handle, "fasta")

    chromosome_sequence = seq_record.seq
    ori_positions = [(match.start(), match.end()) for match in re.finditer(ori_pattern, str(chromosome_sequence))]

    print(f"Chromosome {chromosome_id} - Potential ORI positions:")
    for start_pos, end_pos in ori_positions:
        print(f"Start: {start_pos}, End: {end_pos}")

    print(f"Sequence saved to {filename}")
