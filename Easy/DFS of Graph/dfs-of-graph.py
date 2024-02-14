#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, v, adj):
        # code here
        vis=[0]*v
        l=[]
        def fun(i,v,adj):
            if i==v:
                return 
            if vis[i]==0:
                l.append(i)
                vis[i]=1
            for j in adj[i]:
                if vis[j]==0:
                    l.append(j)
                    vis[j]=1
                    fun(j,v,adj)
        fun(0,v,adj)
        return l


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends