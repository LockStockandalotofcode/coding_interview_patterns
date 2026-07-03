class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class InsertAndSearchWordsWithWildcards:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # traverse through word
        # skip through prefix, then make new nodes if left
        for c in word:
            if c not in node.children:
                # make node
                node.children[c] = TrieNode()
            # increment
            node = node.children[c]

        node.is_word = True

    def search_helper(self, word: str, word_index: str, node: TrieNode) -> bool:
        for i in range(word_index, len(word)):
            c = word[i]
            # 3 possibilities
            # wildcard, valid next character, not valid
            if c == '.':
                # recursively call over all child nodes, to search for remaining word
                for child in node.children.values(): # .values a dict method 
                    if self.search_helper(word, i+1, child):
                        return True
                return False
            elif c in node.children:
                # increment node to children
                node = node.children[c]
            else:
                return False

        # return only if a word ends 
        return node.is_word

    def search(self, word: str) -> bool:
        # using helper function, because we emply recursion 
        node = self.root
        return self.search_helper(word, 0, node)

