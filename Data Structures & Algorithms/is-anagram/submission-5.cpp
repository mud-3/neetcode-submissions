class Solution {
public:
    bool isAnagram(string s, string t) {
        for (char c : s) {
            auto pos = t.find(c);
            if (pos != std::string::npos) {
                t.erase(pos, 1);
            } else {
                return false;
            }
        }
        return t.empty();
    }
};
