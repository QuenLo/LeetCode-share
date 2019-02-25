class WordDictionary(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.dictionary = {}

  def addWord(self, word):
    """
    Adds a word into the data structure.
    :type word: str
    :rtype: void
    """
    if len(word) in self.dictionary:
      self.dictionary[len(word)].append(word)
    else:
      self.dictionary[len(word)] = [word]

  def search(self, word):
    """
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    :type word: str
    :rtype: bool
    """
    if len(word) not in self.dictionary:
        return False 
    if '.' in word:
      for item in self.dictionary[len(word)]:
        if re.match(re.compile(word), item) is not None:
          return True
      return False
    else:
      if word not in self.dictionary[len(word)]:
        return False
    return True
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
