class Solution:
    def compress(self, chars: List[str]) -> int:
        
        length = len(chars)
        if length < 2: return length
        
        writer = 0
        anchor = 0
        
        for i,v in enumerate( chars ):
            if (i + 1 == length or chars[i+1] != v):
                chars[writer] = v
                writer += 1
                
                if i > anchor:
                    numbers = i - anchor +1

                    for n in str(numbers):
                        chars[writer] = n
                        writer += 1

                anchor = i+1
        
        return writer
