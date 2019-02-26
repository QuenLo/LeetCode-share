class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique = set()
        
        for email in emails:
            [localname, domainname] = email.split("@")
            localname = "".join(localname.split("+")[0].split("."))

            unique.add(localname+domainname)
        
        return len(unique)
        
# solution 2
class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        return len( set( map( self.process_email, emails ) ) )
    
    def process_email( self, email ):
        [localname, domainname] = email.split("@")
        localname = "".join(localname.split("+")[0].split("."))
        
        return (localname+"@"+domainname)
