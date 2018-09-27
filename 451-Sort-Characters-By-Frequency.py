class Solution(object):
    def frequencySort(self, s):
        
        #unique key
        sSet = set(s)
        sTable = []
        
        #count letter -> sTable( 'key', num )
        for key in sSet:
            sTable.append( ( key, s.count(key) ) )
        
        #sort in descending
        sTable.sort(key = lambda table: table[1], reverse = True)
        
        return ''.join( map( lambda table: table[0]*table[1], sTable) )
