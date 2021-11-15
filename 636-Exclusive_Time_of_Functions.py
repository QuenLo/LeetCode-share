class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        ftimes = [0]*n
        stack = []
        pre_start_time = 0
        
        for log in logs:
            f_id, which, f_time = log.split(":")
            f_id, f_time = int(f_id), int(f_time)
            
            if which == "start":
                if stack:
                    ftimes[stack[-1]] += f_time - pre_start_time
                    
                stack.append(f_id)
                pre_start_time = f_time
            
            else:
                ftimes[stack.pop()] += f_time - pre_start_time + 1
                pre_start_time = f_time + 1
                
        return ftimes
