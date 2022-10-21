class Solution:
 
    def rotate_with_pointers(self, matrix: list[list[int]]) -> None:
            
            # set up left/right boundaries 
            l = 0
            r = len(matrix) - 1
            
            # OUTER WHILE LOOP TRAVERSES EACH "SQUARE/RING" OF THE BOX FROM OUTERMOST TO INNERMOST 
            while l < r:
                for i in range(r - l):     # NUMBER OF INNER ROTATIONS IN EACH SQUARE.  E.G - 4X4 WILL HAVE 3, 3X3 WILL HAVE 2
            
                    top, bottom = l, r
                    
                    # GO THROUGH SQUARE CCW TO MOVE THINGS CW
                    
                    # save topLeft variable for last step 
                    topLeft = matrix[top][l + i]
                    
                    # move bottomLeft into topLeft               
                    matrix[top][l + i] = matrix[bottom - i][l]    
                    
                    # move bottomRight into bottomLeft 
                    matrix[bottom - i][l] = matrix[bottom][r -i]   
                    
                    # move topRight into bottomRight 
                    matrix[bottom][r -i] = matrix[top + i][r]
                    
                    # move topLeft into topRight 
                    matrix[top + i][r] = topLeft

                    
                # OUTER LOOP - SHIFT THE ENTIRE BOX INWARDS           
                r -= 1   # decrement right pointer
                l += 1   # increment left pointer


    def rotate_with_loops(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        
        for i in range(n):
            for j in range(i):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        
        
matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix2 = [[5, 1, 9, 11],
           [2, 4, 8, 10],
           [13, 3, 6, 7],
           [15,14,12,16]]

matrix3 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix4 = [[5, 1, 9, 11],
           [2, 4, 8, 10],
           [13, 3, 6, 7],
           [15,14,12,16]]

print(matrix1)
Solution().rotate_with_pointers(matrix1)
print(matrix1)

print(matrix2)
Solution().rotate_with_pointers(matrix2)
print(matrix2)
        
print(matrix3)
Solution().rotate_with_loops(matrix3)
print(matrix3)

print(matrix4)
Solution().rotate_with_loops(matrix4)
print(matrix4)
                