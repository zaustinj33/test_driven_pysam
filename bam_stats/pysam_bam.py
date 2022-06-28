import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pysam

#%%

class bam_stats:
    def __init__(self, cutoff, input_file):
        self.cutoff = cutoff
        self.input_file = input_file
        print(self.input_file)
        self.read_bamfile = pysam.AlignmentFile(input_file, "r", check_sq=False)
        self.Passed_cutoff_reads = pysam.AlignmentFile(self.input_file.strip('.bam')+"Ccutoff.bam",
                                                       "wb", template=self.read_bamfile)

    def total_reads(self):
        total_read_count = 0
        for read in self.read_bamfile.fetch():
            total_read_count += 1
        return total_read_count

    # check each read for C content, write to new file if passed filter
    def Count_Cs_per_chrom(self):
        self.chr_dict = {}
        total_read_count = 0
        for read in self.read_bamfile.fetch():

            # Init removed read count
            if read.reference_name in self.chr_dict:
                removed_read_count = self.chr_dict[read.reference_name]
            else:
                self.chr_dict[read.reference_name] = {'converted':0,'total':0}

            # Check n C's
            total_read_count +=1
            self.chr_dict[read.reference_name]['total'] += 1
            sequence = read.query_sequence.upper()
            C = float(sequence.count('C'))

            if C <= int(self.cutoff):
                self.Passed_cutoff_reads.write(read)
                #print("read has more than X Cs")
            else:
                self.chr_dict[read.reference_name]['converted'] += 1

        self.read_bamfile.close()
        self.Passed_cutoff_reads.close()

        #print(sum(x['total'] for x in chr_dict if x))
        return self.chr_dict

    def plot_chr_dist(self):
        plot_dict = pd.DataFrame(self.Count_Cs_per_chrom()).transpose()
        melt_plot = pd.melt(plot_dict.reset_index(), id_vars='index', value_vars = ['converted','total'])

        plt.figure(figsize = (8,8))
        p = sns.barplot(data=melt_plot, x='index', y='value', hue='variable')
        p.set_xticklabels(p.get_xticklabels(),rotation = 30)
        plt.savefig("test_bam.png",bbox_inches='tight', dpi=400, transparent=True)

        return p

test = bam_stats(3, "test_bam.bam")
test.plot_chr_dist()