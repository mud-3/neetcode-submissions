class Solution:
#solution using ascii value
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return " "
            
        return ";".join(
            ",".join(str(ord(char)) for char in string) for string in strs
        )

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []

        decoded = []
        for asciis in s.split(';'):
            asciis = asciis.split(',')
            expanded = []
            for char in asciis:
                if char == "":
                    expanded.append("")
                else:
                    expanded.append(chr(int(char)))

            decoded.append("".join(expanded))
        return decoded