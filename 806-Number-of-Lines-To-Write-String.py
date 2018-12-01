class Solution(object):
    def numberOfLines(self, widths, S):
        total,raw = 0, 1
        Ord_a = ord('a')
        for s in S:
            total += widths[ord(s)-Ord_a]
            if(total > 100):
                total = widths[ord(s)-Ord_a]
                raw +=1
        if total == 100:
            raw += 1
            total = 0
        return [raw, total]
