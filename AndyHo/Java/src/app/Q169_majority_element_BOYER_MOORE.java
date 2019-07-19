package app;

class Q169_majority_element_BOYER_MOORE {
    public int majorityElement(int[] nums)
    {
        int count = 0, major = nums[ 0 ];
        for( int e : nums )
        {
            if( e != major )
                count--;
            if( e == major )
                count++;
            if( count == 0 )
            {
                major = e;
                count++;
            }
        }
        return major;
    }
}