// ref. https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37473/My-recursive-solution(Java)

package app;

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val,Node _left,Node _right,Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Q116_populating_next_right_pointers_in_each_node_RECURSIVE
{
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;
    
        public Node() {}
    
        public Node(int _val,Node _left,Node _right,Node _next) {
            val = _val;
            left = _left;
            right = _right;
            next = _next;
        }
    }
    
    public Node connect(Node root)
    {
        helper( root );
        return root;
    }
    
    private void helper( Node root )
    {
        if( root == null ) return;
        
        if( root.left != null )
        {
            root.left.next = root.right;
            if( root.next != null )
                root.right.next = root.next.left;
        }
        
        helper( root.left );
        helper( root.right );
    }
}