class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = []
        output = []
        for string in strs:
            sort = sorted(string)
            if sort not in hashMap:
                hashMap.append(sort)
                output.append([string])
            else:
                output[hashMap.index(sort)].append(string)

        return output