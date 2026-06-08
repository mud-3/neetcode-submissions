class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def BinarySearch(array, target):
            l, r = 0, len(array) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                result = array[m]

                if result == target:
                    return True
                elif result > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][len(matrix[0]) - 1] < target:
                l = m + 1
            else:
                return BinarySearch(matrix[m], target)
        
        return False