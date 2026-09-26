class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLUMNS=len(matrix),len(matrix[0])
        t,b=0,ROWS-1
        while t<=b:
            row=(t+b) // 2
            # print(row)
            if target>matrix[row][-1]:
                t=row+1
            elif target<matrix[row][0]:
                b=row-1
            else:
                break
        if not (t<=b):
            return False
            
        l,r=0,COLUMNS-1
        row=(t+b) // 2
        while l<=r:
            col=(l+r) // 2
            if matrix[row][col] < target:
                l=col+1
            elif matrix[row][col] > target:
                r=col-1
            else:
                return True
        return False
       
       
        