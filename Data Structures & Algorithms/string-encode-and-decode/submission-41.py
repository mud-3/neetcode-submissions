class Solution:
#solution using ascii value
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "[]"
            
        return ";".join(
            ",".join(str(ord(char)) for char in string) for string in strs
        )

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []

        decoded = []
        for asciis in s.split(';'):
            if asciis == "":
                decoded.append("")
            else:
                decoded.append(
                    "".join(chr(int(char_code)) for char_code in asciis.split(","))
                )
        return decoded