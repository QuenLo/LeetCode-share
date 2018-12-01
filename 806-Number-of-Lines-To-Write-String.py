class Solution(object):
    def numberOfLines(self, widths, S):
        total,raw = 0, 1
        for s in S:
            total += widths[ord(s)-ord('a')]
            if(total == 100):
                total = 0
                raw += 1
            elif(total > 100):
                total = widths[ord(s)-ord('a')]
                raw +=1
        return [raw, total]
