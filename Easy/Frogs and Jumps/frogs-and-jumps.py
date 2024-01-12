#User function Template for python3

class Solution:
    def unvisitedLeaves(self, n, leaves, frogs):
        # code here
        l=[0]*(leaves+1)
        l[0]=1
        frogs.sort()
        if frogs[0]==1:
            return 0
        cnt=0
        for i in frogs:
            if i<=leaves and l[i]==0:
                for j in range(i,leaves+1,i):
                    l[j]=1
                    
        
            
        
        return l.count(0)
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends