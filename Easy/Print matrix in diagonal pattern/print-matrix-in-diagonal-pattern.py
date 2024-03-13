# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        i=0
        j=0
        k=1
        ans=[]
        n=len(mat)
        while(len(ans)<n*n):
            if k&1:#down to up
                while(i>=0 and j<n):
                    ans.append(mat[i][j])
                    i-=1
                    j+=1
                if i<0 and j<n:
                    i=0
                if j==n:
                    j-=1
                    i+=2
            else:#up to down
                while(i<n and j>=0):
                    ans.append(mat[i][j])
                    i+=1
                    j-=1
                if i<n and j<0:
                    j=0
                if i==n:
                    i-=1
                    j+=2
            k+=1
        return ans
            
                
                
                


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends