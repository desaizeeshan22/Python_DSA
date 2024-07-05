from Tries.TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.edges:
                curr.edges[char] = TrieNode(char)
            curr = curr.edges[char]
        curr.word_end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return curr.word_end

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.edges:
                return False
            curr = curr.edges[char]
        return True


t = Trie()
word1 = "CANADA"
word2 = "CANARY"
word3 = "CANDLE"
t.insert(word1)
t.insert(word2)
t.insert(word3)
print(t.search(word1))
