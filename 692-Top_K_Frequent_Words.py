class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = collections.Counter(words)
        count_i = collections.defaultdict(list)
        
        for c in count:
            count_i[count[c]].append(c)
            
        large = list( sorted(count_i.keys()) )
        # print(large, count_i)
        
        total = 0
        ans = []
        for l in large[::-1]:
            total += len(count_i[l])
            
            if total <= k:
                ans.extend( sorted(count_i[l]) )
            elif total > k:
                ans.extend( sorted(count_i[l])[:k-total] )
                break
        
        return ans
  
class SolutionII:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = collections.Counter(words)
        res = sorted(count, key=lambda x: (-count[x], x))
        return res[:k]
