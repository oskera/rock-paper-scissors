"""Main module"""

from logic.trie import Trie

trie = Trie()
trie.insert("RPS")
trie.insert("RP")
trie.insert("PS")

print(trie.search("R"))
print(trie.search("RP"))
print(trie.search("RPS"))
print(trie.search("P"))
