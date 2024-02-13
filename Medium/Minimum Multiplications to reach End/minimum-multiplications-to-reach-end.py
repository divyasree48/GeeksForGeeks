#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        mod=100000
        l=[[start,0]]
        vis=[0]*100001
        vis[start]=1
        while(len(l)):
            x=l[0]
            a=x[0]
            b=x[1]
            l.pop(0)
            if a==end:
                return b
            for i in arr:
                
                y=(a*i)%mod
                if y==end:
                    return b+1
                if vis[y]!=1:
                    vis[y]=1
                    l.append([y,b+1])
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends