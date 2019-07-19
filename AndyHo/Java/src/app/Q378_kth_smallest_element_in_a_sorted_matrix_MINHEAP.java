// ref. https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code

package app;

import java.util.*;

class Q378_kth_smallest_element_in_a_sorted_matrix_MINHEAP
{
    class Tuple
    {
        int val = 0;
        int i = 0, j = 0;
        public Tuple( int val, int i, int j )
        {
            this.val = val;
            this.i = i;
            this.j = j;
        }
    }

    public int kthSmallest(int[][] matrix, int k)
    {
        PriorityQueue<Tuple> minHeap = new PriorityQueue<Tuple>( new Comparator<Tuple>()
        {
            public int compare( Tuple x, Tuple y )
            {
                return x.val - y.val;
            }
        });
        for( int j = 0; j < matrix.length; j++ )
            minHeap.offer( new Tuple( matrix[0][j], 0, j ) );
        // traverse at most k-1 since the matrix is already sorted!!
        for( int j = 0; j < k-1; j++ )
        {
            Tuple t = minHeap.poll();
            if( t.i == matrix.length-1 ) continue;
            minHeap.offer( new Tuple( matrix[t.i+1][t.j], t.i+1, t.j ) );
        }
        return minHeap.poll().val;
    }
}