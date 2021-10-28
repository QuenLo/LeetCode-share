class Solution:
    def simplifyPath(self, path: str) -> str:
        
        seps = path.split("/")
        queue = []
        
        for sep in seps[1:]:
            if len(sep) < 1:
                continue
            if sep == "..":
                if queue:
                    queue.pop()
            elif sep == ".":
                continue
            else:
                queue.append(sep)
        
        return "/"+"/".join(queue)
