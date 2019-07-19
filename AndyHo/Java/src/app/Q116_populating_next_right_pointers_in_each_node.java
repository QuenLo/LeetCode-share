// ref. https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37472/A-simple-accepted-solution

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
class Q116_populating_next_right_pointers_in_each_node
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
        if( root == null ) return root;
        Node pre = root;
        Node cur = null;
        while( pre.left != null )
        {
            cur = pre;
            while( cur != null )
            {
                cur.left.next = cur.right;
                // change to right sub-tree
                if( cur.next != null ) cur.right.next = cur.next.left;
                cur = cur.next;
            }
            pre = pre.left;
        }
        return root;
    }
}