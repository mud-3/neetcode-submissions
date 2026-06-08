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

        l, r, t = 0, len(matrix), len(matrix[0])

        while l <= r:
            m = l + ((r - l) // 2)

            if m >= len(matrix):
                return False

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][t - 1] < target:
                l = m + 1
            else:
                return BinarySearch(matrix[m], target)
        
        return False