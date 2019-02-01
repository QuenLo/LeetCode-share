class Solution(object):
    def fullJustify(self, words, maxWidth):
        
        current_string = ""
        Ans_list, current_list = [], []

        for word in words:
            if len(current_string) + len(word) + len(current_list) > maxWidth:
                if len(current_list) == 1:
                    Ans_list.append( current_list[0] + " "*(maxWidth - len(current_list[0])) )
                else:
                    rest_space = maxWidth - len(current_string)
                    split_space, begin_space = divmod( rest_space, len(current_list) - 1 )
                    current_string = (" "*(split_space+1)).join(current_list[:begin_space+1])
                    current_string += " "*(split_space)
                    current_string += (" "*(split_space)).join(current_list[begin_space+1:])
                    Ans_list.append(current_string)
                # clear all
                current_string = ""
                del current_list[:]
            # add new word
            current_list.append(word)
            current_string += word

        Ans_list.append( ' '.join(current_list) + ' '*(maxWidth - len(current_string) - len(current_list) + 1) )
        
        return Ans_list
