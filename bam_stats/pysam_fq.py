import pysam, sys
import numpy as np

class Fq_stats:

    def __init__(self, qual, length, input_fq, seq):
        self.qual = qual
        self.length = length
        self.fq_file = input_fq
        self.output_fq = input_fq.strip('.fq') +"fq_out.fq"
        self.removed_reads = 0
        self.seq = seq

    def length_filter(self):
        with pysam.FastxFile(self.fq_file) as fh:
            for entry in fh:
                #print(entry.name)
                len(entry.sequence)
                if len(entry.sequence) > self.length:
                    self.removed_reads += 1
                #print(entry.comment)
                #print(entry.quality)
        return self.removed_reads

    def qual_filter(self):
        self.qualities = []
        with pysam.FastxFile(self.fq_file) as fh:
            for entry in fh:
                self.qualities.append(np.mean(entry.get_quality_array()))
        return self.qualities

    def seq_finder(self):
        self.match_reads = {}
        with pysam.FastxFile(self.fq_file) as fh:
            for entry in fh:
                for i in range(len(entry.sequence) - len(self.seq)):
                    if entry.sequence[i:i+len(self.seq)] == self.seq:
                        if entry.name in self.match_reads.keys():
                            self.match_reads[entry.name].append(i)
                        else:
                            self.match_reads[entry.name] = []
                            self.match_reads[entry.name].append(i)

        return self.match_reads

test = Fq_stats(30,30,"test_1.fq", 'ATAC')
print(test.seq_finder())



#with pysam.FastxFile(filename) as fin, open(out_filename, mode='w') as fout:
#    for entry in fin:
#        fout.write(str(entry) + '\n')

# calculate stats from fq file

# visualize stats
