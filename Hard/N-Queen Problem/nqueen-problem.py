#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        grid=[[0]*n for _ in range(n)]
        ans=[]
        def valid(i,j,n,grid):
            x=i
            y=j
            while(x>=0):
                if grid[x][y]:
                    return 0
                x-=1
            x=i
            y=j
            while(x>=0 and y>=0):
                if grid[x][y]:
                    return 0
                x-=1
                y-=1
            x=i
            y=j
            while(x>=0 and y<n):
                if grid[x][y]:
                    return 0
                x-=1
                y+=1
            return 1
        def fun(i,n,grid):
            if i==n:
                v=[]
                for k in range(n):
                    c=0
                    for j in range(n):
                        c+=1
                        if grid[k][j]==1:
                            v.append(c)
                            break
                        
                ans.append(v)
                return
            for j in range(n):
                if valid(i,j,n,grid):
                    grid[i][j]=1
                    fun(i+1,n,grid)
                    grid[i][j]=0
        fun(0,n,grid)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends