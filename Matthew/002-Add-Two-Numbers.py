class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        z = 0
        return self.add(l1, l2, ans, z)
    def add(self, l1, l2, ans, z):
        if l1.next == None and l2.next == None:
            n = l1.val + l2.val + z
            ans.append(n%10)
            if n//10 > 0:
                ans.append(n//10)
            return ans
        elif l1.next == None:
            n = l1.val + l2.val + z
            l1.val = 0
            ans.append(n%10)
            return self.add(l1, l2.next, ans, n//10)
        elif l2.next == None:
            n = l1.val + l2.val + z
            l2.val = 0
            ans.append(n%10)
            return self.add(l1.next, l2, ans, n//10)
        else:
            n = l1.val + l2.val + z
            ans.append(n%10)
            return self.add(l1.next, l2.next, ans, n//10)
