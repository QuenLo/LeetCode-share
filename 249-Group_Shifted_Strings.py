class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        
        for s in strings:
            k = ()
            for ch in range(len(s)-1):
                diff = 26 + ord(s[ch+1]) - ord(s[ch])
                k += (diff % 26,)
                
            hashmap[k].append(s)
            
        return [ list(hashmap[k]) for k in hashmap ]
