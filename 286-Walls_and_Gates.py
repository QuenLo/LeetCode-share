class Solution:
    def wallsAndGates(self, room: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        WALL = -1
        GATE= 0
        
        # if there is no room
        room_l = len(room)
        if room_l < 1: return
        
        room_w = len(room[0])
        
        queue = []
        for l in range(room_l):
            for w in range(room_w):
                if room[l][w] == GATE:
                    queue.append( [l,w] )
                    
        def count_pass( room, l_move, w_move, queue ):
            if (l_move >= room_l) or (w_move >= room_w)\
            or (l_move < 0) or (w_move <0)\
            or room[l_move][w_move] != EMPTY:
                return
            room[l_move][w_move] = room[l][w] + 1
            queue.append( [l_move, w_move] )
            
        
        while queue:
            point = queue.pop(0)
            l = point[0]
            w = point[1]
            
            # down
            l_move, w_move = l + 1, w
            count_pass( room, l_move, w_move, queue )
            
            # up
            l_move, w_move = l - 1, w
            count_pass( room, l_move, w_move, queue )
            
            # right
            l_move, w_move = l, w + 1
            count_pass( room, l_move, w_move, queue )
            
            # left
            l_move, w_move = l, w - 1
            count_pass( room, l_move, w_move, queue )
            
        
        
