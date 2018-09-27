class Solution(object):
    def frequencySort(self, s):
        
        #unique key
        sSet = set(s)
        sTable = []
        
        #count letter -> sTable( Count, key*Count )
        for key in sSet:
            Count = s.count(key)
            sTable.append( ( Count,  key*Count ) )
        
        #sort in descending
        sTable.sort(key = lambda table: table[0], reverse = True)
        
        return ''.join( map( lambda table: table[1], sTable) )
