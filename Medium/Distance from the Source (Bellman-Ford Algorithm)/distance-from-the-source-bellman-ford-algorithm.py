#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, v, edges, s):
        #code here
        dis=[100000000]*v
        dis[s]=0
        for i in range(v-1):
            for j in edges:
                u=j[0]
                v=j[1]
                wt=j[2]
                if dis[u]!=100000000 and dis[u]+wt<dis[v]:
                    dis[v]=dis[u]+wt
        a=dis.copy()
        #print(dis)
        for j in edges:
            u=j[0]
            v=j[1]
            wt=j[2]
            if a[u]!=100000000 and a[u]+wt<a[v]:
                a[v]=a[u]+wt
        #print(a)
        #print(dis)
        if a!=dis:
            #print(1)
            return [-1]
        return a
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends