class Solution {
public:
    string removeOuterParentheses(string S) {
        string out;
        int count = 0;
        for (char s : S){
            if(s == '(' && count++ > 0 ) out += s;
            if(s == ')' && count-- > 1 ) out += s;
        }
        return out;
    }
};
