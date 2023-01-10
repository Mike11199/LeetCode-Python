class Solution:
    def searchMatrix_BF(self, matrix, target):
        """
        Brute Force = O(M x N) or O(N)
        """
        if not matrix:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
    
    def searchMatrix_Binary_Search(self, matrix, target):
        """
        Binary Search:  O( log N)
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        # perform binary search to find the correct row where the target should exist.
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # if we created an invalid condition - none of the rows can contain the target value, return false.
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        l = 0
        r = COLS - 1

        # perform binary search within the row where target should exist.  return true if target found, or return false.
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m -1
            else:
                return True
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
target_2 = 4

answer = Solution()
print(answer.searchMatrix_Binary_Search(matrix,target)) # s/b True
print(answer.searchMatrix_Binary_Search(matrix,target_2)) # s/b False
