from Bio.SeqIO.QualityIO import FastqGeneralIterator
import sys

input_file = sys.argv[1]
output_file = input_file.replace('.fq', '_formatted.fq')

with open(input_file) as in_handle:
    with open(output_file, "w") as out_handle:
        for title, seq, qual in FastqGeneralIterator(in_handle):
            title = title.replace(' ', '_'+title[-8:]+' ')
            out_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
#%%

#import pysam

