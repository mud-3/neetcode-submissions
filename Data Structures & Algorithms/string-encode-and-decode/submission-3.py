class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += word
            ans += "/"
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        word = ""
        for string in s:
            if string != "/":
                word += string
            else:
                ans.append(word)
                word = ""
        return ans

