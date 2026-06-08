class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        i = 0
        for string in strs:
            sort = str(sorted(string))
            if sort not in hashMap:
                hashMap[sort] = i
                output.append([])
                output[i] = [string]
                i += 1
            else:
                output[hashMap[sort]].append(string)

        return output