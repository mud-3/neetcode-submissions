class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0

        for char in s:
            window = s[left:right]
            print(window)

            if char in window:
                for c in window:
                    left = left + 1
                    if c == char:
                        break
                
            
            right += 1

            length = right - left

            if length > max_length:
                max_length = length
            
        
        return max_length
        