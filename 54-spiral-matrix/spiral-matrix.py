class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        result=[]

        while top<=bottom and left<=right:
            for col in range(left,right+1):
                result.append(matrix[top][col])
            top+=1
            for col in range(top,bottom+1):
                result.append(matrix[col][right])
            right-=1
            if top<=bottom:
                for col in range(right,left-1,-1):
                    result.append(matrix[bottom][col])

                bottom-=1
            
            if left<=right:
                for col in range(bottom,top-1,-1):
                    result.append(matrix[col][left])
                left+=1
        return result
                
                