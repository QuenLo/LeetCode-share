// ref. https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80147/Simple-Java-solution-using-a-stack-with-explanation

package app;

import java.util.*;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer>
{
    Stack<NestedInteger> stack = new Stack<>();

    public NestedIterator(List<NestedInteger> nestedList)
    {
        for( int i = nestedList.size() - 1; i >= 0; i-- )
            stack.push( nestedList.get( i ) );
    }

    @Override
    public Integer next()
    {
        return stack.pop().getInteger();
    }

    @Override
    public boolean hasNext()
    {
        while( !stack.isEmpty() )
        {
            NestedInteger t = stack.peek();
            if( t.isInteger() ) return true;
            stack.pop();
            for( int i = t.getList().size() - 1; i >= 0; i-- )
                stack.push( t.getList().get( i ) );
        }
        return false;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */