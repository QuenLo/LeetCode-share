class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # step 0: unique letters
        reverse_adj_list = { c: [] for word in words for c in word }
        
        # step 1: edges
        for first_w, second_w in zip(words, words[1:]):
            for f, s in zip( first_w, second_w ):
                if f!= s:
                    reverse_adj_list[s].append(f)
                    break
            else:
                # second word isn't a prefix of first word
                if len(first_w) > len(second_w):
                    return ""
                
        # step 2: DFS
        seen = {}
        output = []
        def visist(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for next_node in reverse_adj_list[node]:
                result = visist(next_node)
                if not result:
                    return False
            seen[node] = True
            output.append(node)
            return True
        
        if not all( visist(node) for node in reverse_adj_list ):
            return ""
        
        return "".join(output)
