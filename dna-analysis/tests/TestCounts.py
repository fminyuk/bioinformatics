import unittest
import Counts


class TestCounts(unittest.TestCase):
    def test_pattern_to_number(self):
        n = Counts.pattern_to_number('GT')

        self.assertEqual(11, n)

    def test_number_to_pattern(self):
        p = Counts.number_to_pattern(11, 2)

        self.assertEqual('GT', p)

    def test_compute_frequencies(self):
        r = Counts.compute_frequencies('ACGCGGCTCTGAAA', 2)

        self.assertEqual('2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0', ' '.join(map(str, r)))

    def test_faster_frequent_words(self):
        r = Counts.faster_frequent_words('ACGCGGCTCTGAAA', 2)

        self.assertEqual('AA CG CT GC', ' '.join(map(str, r)))

    def test_finding_frequent_words_by_sorting(self):
        r = Counts.finding_frequent_words_by_sorting('AAGCAAAGGTGGG', 2)

        self.assertEqual('AA GG', ' '.join(map(str, r)))
