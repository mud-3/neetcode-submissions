class Solution:
#solution using non ascii delimiter
    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return " "
        encoded = "€".join(strs)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == " ":
            return [""]
        decoded = s.split('€')
        print(decoded)
        return decoded