class Solution(object):
    def fullJustify(self, words, maxWidth):
        words_len, current_string = len(words), ""
        Ans_list, current_list, current_words = [], [], 0
        i = 0
        while i < words_len:
            if len(current_string) + len(words[i]) + 1 > maxWidth:
                if current_words == 1:
                    current_string += " "*(maxWidth - len(current_string))
                elif current_string == "":
                    current_string = words[i]
                    current_string += " "*(maxWidth - len(current_string))
                    i += 1
                else :
                    rest_space = maxWidth - len(current_string)
                    if not rest_space % (current_words - 1):
                        split_space = int(rest_space / (current_words - 1)) + 1
                        current_string = (" "*split_space).join(current_list)
                    else:
                        split_space = int( rest_space // (current_words - 1) ) + 1
                        begin_space = rest_space % (current_words - 1)
                        current_string = (" "*(split_space+1)).join(current_list[:begin_space+1])
                        current_string += " "*(split_space)
                        current_string += (" "*(split_space)).join(current_list[begin_space+1:])

                Ans_list.append(current_string)    
                current_string = ""
                current_words = 0
                del current_list[:]
            elif i == words_len -1 :
                current_list.append(words[i])
                current_string = " ".join(current_list)
                current_string += " "*(maxWidth - len(current_string))
                Ans_list.append(current_string)
                break
            else:
                current_list.append(words[i])
                current_string = " ".join(current_list)
                current_words += 1
                i += 1
        
        return Ans_list
        
