import unittest
from logic.trie import Trie

class TestAI(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert(self):
        trie = Trie()
        trie.insert("RPP")
        self.assertEqual(1, trie.search("RPP"))

    def test_insert_multiple(self):
        trie = Trie()
        trie.insert("RPP")
        trie.insert("RPP")
        trie.insert("RPP")
        self.assertEqual(3, trie.search("RPP"))

    def test_insert_many(self):
        trie = Trie()
        trie.insert("RPP")
        trie.insert("RP")
        trie.insert("RPP")
        trie.insert("RPP")
        trie.insert("RPPS")
        self.assertEqual(4, trie.search("RPP"))
