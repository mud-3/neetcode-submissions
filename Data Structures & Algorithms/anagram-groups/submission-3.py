class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        for string in strs:
            sort = str(sorted(string))
            if sort not in hashMap:
                hashMap[sort] = [string]
            else:
                hashMap[sort].append(string)

        for key in hashMap:
            output.append(hashMap[key])

        return output