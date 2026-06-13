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
            tail = head

            while s[tail] != ':':
                tail += 1
                
            length = int(s[head: tail])

            decoded.append(s[tail + 1: tail + length + 1])

            tail = head = tail + length + 1
        return decoded