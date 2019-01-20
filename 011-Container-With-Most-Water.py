class Solution:
    # O(n)
    def maxArea(self, height):
        max_container = 0
        pos_left, pos_right = 0, len(height) - 1
        
        while( pos_left < pos_right ):
            if( height[pos_left] > height[pos_right] ):
                max_container = max( max_container, ( pos_right - pos_left )*height[pos_right] )
                pos_right -= 1
            else:
                max_container = max( max_container, ( pos_right - pos_left )*height[pos_left] )
                pos_left += 1
        return max_container
    
    '''
    # O(n^2)
    def maxArea(self, height):
    temp_max = 0
    length = len(height)
    current_left_height = 0
    current_right_height = 0

    for pos_left in range(0,length-1):
        if (current_left_height < height[pos_left]):
            current_left_height = height[pos_left]
            for pos_right in range(length-1, pos_left, -1):
                if(current_right_height < height[pos_right]):
                    current_right_height = height[pos_right]
                    container = (pos_right - pos_left) * min(height[pos_right], height[pos_left])
                    temp_max = max(container,temp_max)
            current_right_height = 0
    return temp_max
    '''
        
