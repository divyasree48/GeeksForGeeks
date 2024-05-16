
from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        
        adj=[[]for i in range(n+1)]
        for i in edges:
            a=i[0]
            b=i[1]
            adj[b].append(a)
            adj[a].append(b)
        #print(adj)
        def fun(node,par,res):
            c=0
            for i in adj[node]:
                if i!=par:
                    x=fun(i,node,res)
                    if x&1:
                        c+=1
                    else:
                        res[0]+=1
                        #print(i)
            return c+1
        res=[0]
        fun(1,-1,res)
        return res[0]
        '''def fun(node,cnt):
            if len(adj[node])>0:
                for i in adj[node]:
                    cnt[0]+=1
                    #print(adj)
                    fun(i,cnt)
            return
        c=d=0
        for i in adj[1]:
            a=[1]
            fun(i,a)
            print(i,a)
            if a[0]&1:
                c+=1
            else:
                d+=1
        return d'''



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends