class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
#         ans = []
        
#         for i in range(1,n+1):
#             if i%15 == 0:
#                 ans.append( "FizzBuzz" )
#             elif i%5 == 0:
#                 ans.append( "Buzz" )
#             elif i%3 == 0:
#                 ans.append( "Fizz" )
#             else:
#                 ans.append( str(i) )
                
#         return ans
        return ['Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or str(i) for i in range(1,n+1)]
