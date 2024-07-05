class TrieNode:
    def __init__(self, char):
        self.val = char
        self.edges={}
        self.word_end=False
