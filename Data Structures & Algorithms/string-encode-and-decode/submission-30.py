class Solution:
#solution using ascii value
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return " "
        encoded = []
        for string in strs:
            ascii_values = [str(ord(char)) for char in string]
            encoded.append(", ".join(ascii_values))
        return "; ".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []
        ss = s.split('; ')
        decoded = []
        for values in ss:
            values = values.split(', ')
            expanded = []
            for char in values:
                if char == "":
                    expanded.append("")
                else:
                    expanded.append(chr(int(char)))
                    
            decoded.append("".join(expanded))
        return decoded