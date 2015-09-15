__author__ = 'galaxy'
#Given a Fastq file, splits the Fastq file into a Fasta file and a QUAL file.

from Bio import SeqIO
import sys

input_filename = sys.argv[1]
input_type = "fastq"

output_filename = "out.qual"

output1 = SeqIO.convert(input_filename, "fastq", output_filename, "qual")

