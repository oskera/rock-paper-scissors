class Trie:

    root = None

    def __init__(self):
        self.root = Node()

    def insert(self, sequence):
        current = self.root
        for c in sequence:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
            current.frequency += 1

class Node:

    children = None
    frequency = 0

    def __init__(self):
        self.children = {}
        self.frequency = 1
