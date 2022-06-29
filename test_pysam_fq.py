import unittest
import pysam_fq

class TestFq_stats(unittest.TestCase):

    def setUp(self):
        self.counts = pysam_fq.Fq_stats(30,30,"test_1.fq",'ATAC')

    def test_length_filter(self):
        self.assertGreater(self.counts.length_filter(), 0, "no reads in file")

if __name__ == '__main__':
    unittest.main()