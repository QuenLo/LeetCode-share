class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        names = {}
        adj_list = collections.defaultdict(set)
        
        for account in accounts:
            for email in account[1:]:
                names[email] = account[0]
                adj_list[email].add(account[1])
                adj_list[account[1]].add(email)
                
                
        seen = set()
        
        def bfs(nn):
            result = []
            q = [nn]
            
            while q:
                email = q.pop(0)
                seen.add(email)
                result.append(email)
                
                for neigh in adj_list[email]:
                    if neigh not in seen:
                        seen.add(neigh)
                        q.append(neigh)
            
            return sorted(result)
        
        total = []
        for email in adj_list.keys():
            if email not in seen:
                temp = [names[email]] + bfs(email)
                total.append(temp)
                
        return total
        
        


## Disjoint Set Union
# N is the number of accounts and K is the maximum length of an account.
# Time complexity: O(NK⋅logNK+NK⋅α(N))
# Space complexity: O(NK)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        union_find = {}
        email_to_name = {}
        
        def find(x):
            if x not in union_find:
                union_find[x] = x
            if union_find[x] != x:
                union_find[x] = find(union_find[x])
            return union_find[x]
        
        def union(x, y):
            union_find[find(x)] = find(y)
            
        for name, *emails in accounts:
            
            if len(emails) == 1:
                find(emails[0])
                
            for e1, e2 in itertools.combinations(emails, 2):
                union(e1, e2)
                
            for email in emails:
                if email not in email_to_name:
                    email_to_name[email] = name
                    
        group_root = collections.defaultdict(list)
        for email in union_find:
            group_root[find(email)].append(email)
        
        
        return [ [email_to_name[root]] + sorted(emails) for root, emails in group_root.items() ]
