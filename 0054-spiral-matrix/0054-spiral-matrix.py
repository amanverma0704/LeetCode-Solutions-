class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])

        total = n*m
        ans = []
        c = 0

        columnstart = 0
        rowstart = 0
        columnend = m-1
        rowend = n-1

        while c<total:
            # rowstart, columnstart -> columnend
            for i in range(columnstart,columnend+1):
                ans.append(matrix[rowstart][i])
                c += 1
            rowstart += 1
            if c == total:
                break
            
            #columnend, rowstart -> rowend
            for i in range(rowstart, rowend+1):
                ans.append(matrix[i][columnend])
                c += 1
            columnend -= 1
            if c == total:
                break
            
            # rowend, columnend -> columnstart
            for i in range(columnend, columnstart-1,-1):
                ans.append(matrix[rowend][i])
                c += 1
            rowend -= 1
            if c == total:
                break
            
            # columnstart, rowend -> rowstart
            for i in range(rowend, rowstart-1,-1):
                ans.append(matrix[i][columnstart])
                c += 1
            columnstart += 1
        
        return ans


        