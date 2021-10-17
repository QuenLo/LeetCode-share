class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        max_pos = max( [x]+forbidden ) + a + b
        jump = [0] + [float('inf')]*(max_pos+1)
        
        for f in forbidden: jump[f] = -1
        
        dq = deque([0])
        
        while dq:
            pos = dq.popleft()
            if pos+a <= max_pos and jump[pos+a] > jump[pos] + 1:
                jump[pos+a] = jump[pos] + 1
                dq.append( pos+a )
            if pos-b > 0 and jump[pos-b] > jump[pos] + 1:
                jump[pos-b] = jump[pos] + 1
                if post-b+a <= max_pos and jump[pos+a-b] > jump[pos] + 2:
                    jump[ pos+a-b ] = jump[pos] + 2
                    dq.append( pos+a-b )
        
        return jump[x] if jump[x]<float('inf') else -1
