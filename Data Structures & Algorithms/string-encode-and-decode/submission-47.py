class Solution:
    #solution using optimal method
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(f"{str(len(string))}:{string}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        head = tail = 0
        while tail < len(s):
            while s[tail] != ':':
                tail += 1
            num = int(s[head: tail])
            if tail < len(s) - 1:
                tail += 1
            decoded.append(s[tail:tail + num])
            head = tail = tail + num
            tail += 1
        return decoded