class WordDictionary(object):

    def __init__(self):
        
        # Initialize a collection to store words
        self.word_store = collections.defaultdict(list)
        

    def addWord(self, word):

        # Adds a word into word_store
        # Classified by how long is the word
        self.word_store[len(word)].append(word)
        

    def search(self, word):
        
        word_len = len(word)

        if '.' not in word:
            return word in self.word_store[len(word)]
        else:
            for item in self.word_store[word_len]:
                # Comparison character one by one
                for alpha in range(0,word_len):
                    #print alpha
                    if word[alpha] != "." and word[alpha] != item[alpha]:
                        break
                    if alpha == (word_len-1) :
                        return True
                    
            return False
