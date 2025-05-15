import unittest
from src.question_a.dna import get_most_likely_ancestor_consensus
class TestDNAFunctions(unittest.TestCase):
    def test_get_most_likely_ancestor_consensus(self):
        # Convert generator to list for comparison
        result = list(get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT"))
        expected = [2, 4, 10]
        self.assertEqual(result, expected)

