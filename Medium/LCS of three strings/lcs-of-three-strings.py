#User function Template for python3

class Solution:

    def LCSof3(self,a,b,c,n1,n2,n3):
        # code here
        dp=[[[-1]*(len(c)+1)for _ in range(len(b)+1)]for _ in range(len(a)+1)]
        def fun(i,j,k,a,b,c,n1,n2,n3):
            if i>=n1 or j>=n2 or k>=n3:
                return 0
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            if a[i]==b[j] and b[j]==c[k]:
                dp[i][j][k]=fun(i+1,j+1,k+1,a,b,c,n1,n2,n3)+1
                return dp[i][j][k]
            
            
            
            dp[i][j][k]=max(fun(i+1,j,k,a,b,c,n1,n2,n3),fun(i,j+1,k,a,b,c,n1,n2,n3),fun(i,j,k+1,a,b,c,n1,n2,n3))
            return dp[i][j][k]
            
        return fun(0,0,0,a,b,c,n1,n2,n3)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends