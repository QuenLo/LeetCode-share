// ref. https://leetcode.com/problems/top-k-frequent-elements/discuss/81733/*Java*-straightforward-O(N-%2B-(N-k)lg-k)-solution
// ref. https://www.geeksforgeeks.org/priority-queue-class-in-java-2/

package app;

import java.util.*;

class Q347_top_k_frequent_elements
{
    public List<Integer> topKFrequent(int[] nums, int k)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for( int i = 0; i < nums.length; i++ )
            map.put( nums[ i ], map.getOrDefault( nums[ i ], 0 ) + 1 );

        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>( (a, b) -> map.get( b ) - map.get( a ) );
        /* (a, b) -> map.get( b ) - map.get( a ) equals to the following:
               Comparator<String> comparator = (s1, s2) -> {
                   return b - a;
               };
         */

        // insert to heap
        List<Integer> ans = new ArrayList<Integer>();
        for( int n : map.keySet() )
        {
            maxHeap.add( n );
            // k in ans, (n-k) in maxHeap
            if( maxHeap.size() > map.size() - k ) ans.add( maxHeap.poll() );
        }
        return ans;
    }
}