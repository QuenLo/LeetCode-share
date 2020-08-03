class SolutionI:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(x for x in s if x.isalpha() or x.isdigit()).lower()
        return s == s[::-1]
        
class SolutionII:
    def isPalindrome(self, s: str) -> bool:
        
        gap = ord('a') - ord('A')
        news = []
        
        for sr in s:
            sr = ord(sr)
            if sr < 123 and sr > 96:
                news.append(chr(sr - gap))
            elif sr> 64 and sr < 91:
                news.append(chr(sr))
            elif sr > 47 and sr < 58:
                news.append(chr(sr))
        
        head = 0
        tail = len(news) - 1
        while head < tail:
            if news[head] != news[tail]:
                return False
            head += 1
            tail -= 1
        

        return True
