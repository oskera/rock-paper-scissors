class Trie:

    root = None

    def __init__(self):
        self.root = Node()

class Node:

    children = {}
    frequency = 0

    def __init__(self):
        pass
