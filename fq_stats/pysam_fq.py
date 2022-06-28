import pysam, sys

filename = sys.argv[1]
out_filename = filename.strip('.fq') +"fq_out.fq"
with pysam.FastxFile(filename) as fh:
    for entry in fh:
        print(entry.name)
        print(entry.sequence)
        print(entry.comment)
        print(entry.quality)

with pysam.FastxFile(filename) as fin, open(out_filename, mode='w') as fout:
    for entry in fin:
        fout.write(str(entry) + '\n')