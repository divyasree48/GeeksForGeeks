#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        l=[0]
        ans=[0]
        vis=[0]*10001
        vis[0]=1
        while(len(l)):
            x=l[0]
            l.pop(0)
            #print(x)
            for i in adj[x]:
                if vis[i]==0:
                    l.append(i)
                    ans.append(i)
                    vis[i]=1
            
        return ans
            
        


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends