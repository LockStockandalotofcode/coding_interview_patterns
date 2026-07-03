class TrieNode:
    def __init__(self):
        # hashmap of all children
        # trie expected to have multiple stems
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        # Root node at base of Trie (Prefix Tree)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # look for prefix
        # when prefix not found, make new nodes
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] # anyways we move onto next node, child node of char c 
        # mark the end 
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        # search for prefix, if not return False
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        # return true only if is_word flag: True
        return node.is_word

    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        # search for prefix, if not return False
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True