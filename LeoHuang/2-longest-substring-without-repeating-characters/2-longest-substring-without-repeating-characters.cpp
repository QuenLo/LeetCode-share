class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    if(s.length() == 1) return 1;
    string subStr;
    int maxLength = 0;
    int i = 0;
    while(i < s.length()) {
      subStr = "";
      for(int j = i; j < s.length(); j++) {
        if(subStr.find(s[j]) != string::npos) {
          if(subStr.length() > maxLength) maxLength = subStr.length();
          i++;
          break;
        } else {
          subStr += s[j];
        }
        if(j == s.length() - 1) i = s.length();
      }
    }
    if(subStr.length() > maxLength) return subStr.length();
    return maxLength;
  }
};