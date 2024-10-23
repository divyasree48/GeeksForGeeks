#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        ind = [0] * V
        for i in range(V):
            for j in adj[i]:
                ind[j] += 1
        q = deque([])
        for i in range(V):
            if ind[i] == 0:
                q.append(i)
        nodes = 0
        while q:
            node = q.popleft()
            nodes += 1
            for it in adj[node]:
                ind[it] -= 1
                if ind[it] == 0:
                    q.append(it)
        return not nodes == V


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends