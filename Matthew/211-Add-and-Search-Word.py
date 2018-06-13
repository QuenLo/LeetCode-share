class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_leaf = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        print (curr)
        for char in word:
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word):
        return self.helper(word, self.root)
        
    def helper(self, word, node):
        if len(word) == 0:
            return node.is_leaf
        first = word[0]
        if first == ".":
            for key in node.children:
                # return true if any was true
                if self.helper(word[1:], node.children[key]):
                    return True
        else:
            if first not in node.children:
                return False
            return self.helper(word[1:], node.children[first])
        return False
