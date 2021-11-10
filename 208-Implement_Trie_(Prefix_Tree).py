class TrieNode:
    def __init__(self, ch=""):
        self.val = ch
        self.is_word = False
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                next_node = TrieNode(ch=ch)
                node.children[ch] = next_node
                node = next_node
        node.is_word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
