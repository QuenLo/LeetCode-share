// ref. https://leetcode.com/problems/top-k-frequent-words/discuss/108346/my-simple-java-solution-using-hashmap-priorityqueue-onlogk-time-on-space/110558

package app;

import java.util.*;

class Q692_top_k_frequent_words
{
    public List<String> topKFrequent(String[] words, int k)
    {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for( String s : words )
            map.put( s, map.getOrDefault( s, 0 ) + 1 );
        System.out.print( map );
        
        // if the count of two words is same then insert based on string compare of the keys
        PriorityQueue<Map.Entry<String, Integer>> maxHeap = new PriorityQueue<Map.Entry<String, Integer>>
        (
            // sort out those words by their frequencies
            (a, b) ->
                a.getValue() == b.getValue() ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue()
        );

        // insert to heap
        List<String> ans = new ArrayList<String>();
        for( Map.Entry<String, Integer> n : map.entrySet() ) maxHeap.add( n );

        while( k-- > 0 ) ans.add( maxHeap.poll().getKey() );
        return ans;
    }
}