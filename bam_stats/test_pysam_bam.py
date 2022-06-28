import unittest
import pysam_bam


class Testbam_stats(unittest.TestCase):

    def setUp(self):
        self.counts = pysam_bam.bam_stats(3, 'test_bam.bam')

    def test_chrom(self):
        """25 chromosomes"""
        self.assertEqual(len(self.counts.Count_Cs_per_chrom()), 25, "incorrect chromosomes")

    def test_read_count(self):
        """all reads accounted for"""
        #read_counts = sum(x['total'] for x in self.counts.Count_Cs_per_chrom() if x)
        #self.assertEqual(self.counts.line_count, self.counts.total_reads()+1, "read count unequal")

    def test_seq_match(self):
        """if target sequence is present at returned index of read, return true"""

if __name__ == '__main__':
    unittest.main()