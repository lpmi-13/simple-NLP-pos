import unittest
from simple_nlp.utils import find_total_nouns
from simple_nlp.utils import find_total_verbs
from simple_nlp.utils import find_total_adjectives
DATA_SOURCE = './data/sample.txt'

class ComputeAllStats(unittest.TestCase):

    def test_total_nouns(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_total_nouns = 19
        result = find_total_nouns(data)
        self.assertEqual(expected_total_nouns, result)

    def test_total_verbs(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_total_verbs = 14
        result = find_total_verbs(data)
        self.assertEqual(expected_total_verbs, result)        

    def test_total_adjectives(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_total_adjectives = 2
        result = find_total_adjectives(data)
        self.assertEqual(expected_total_adjectives, result)
