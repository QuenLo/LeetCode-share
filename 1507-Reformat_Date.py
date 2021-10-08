class Solution:
    def reformatDate(self, date: str) -> str:
        
        date_s = date.split(" ")
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        month = date_s[1]
        day = date_s[0]
        year = date_s[2]
        
        return '{}-{:02}-{:0>2}'.format(year, Month.index(month) + 1, day[:-2])
