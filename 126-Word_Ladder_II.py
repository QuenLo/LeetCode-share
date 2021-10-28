class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        tree, words, len_w = collections.defaultdict(set), set( wordList ), len(beginWord)
        if endWord not in words:
            return []
        
        found, q, nextq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                # a -> z
                for char in string.ascii_lowercase:
                    for i in range(len_w):
                        test = x[:i] + char + x[i+1:] 
                        if test == endWord:
                            found = True
                            tree[x].add(test)
                        elif test in words:
                            nextq.add(test)
                            tree[x].add(test)
            q, nextq = nextq, set()
        
        def back(x):
            if x == endWord:
                return [[x]]
            else:
                ans = []
                for test in tree[x]:
                    for y in back(test):
                        ans.append( [x] + y ) 
                return ans
            
        # [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
            
        return back(beginWord)
