class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for ch in s:
            if output and output[-1] == ch:
                output.pop()
            else:
                output.append(ch)
                
        return "".join(output)
