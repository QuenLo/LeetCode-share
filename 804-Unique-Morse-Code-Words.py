class Solution(object):
    def uniqueMorseRepresentations(self, words):
        
        # define Morse Code
        MorseCodeDic = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",\
                     'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",\
                     'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        
        # MorseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",\
        #             ".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # create set 
        AnserSet = set()
        
        for word in words:
            word2morse = ""
            for alphabet in word:
                word2morse += MorseCodeDic[alphabet]
                
                # this is slower
                # word2morse += MorseList[ord(alphabet)-97]
                
            AnserSet.add(word2morse)
                
        return len(AnserSet)
