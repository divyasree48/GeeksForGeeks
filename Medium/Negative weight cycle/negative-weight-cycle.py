#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dis=[100000000]*n
		k=0
		for i in range(n-1):
		    for j in edges:
		        if k==0:
		            dis[j[0]]=0
		            k=1
		        u=j[0]
		        v=j[1]
		        wt=j[2]
		        if dis[u]!=100000000 and dis[u]+wt<dis[v]:
		            dis[v]=dis[u]+wt
		a=dis.copy()
		#print(dis)
		for i in edges:
		    u=i[0]
		    v=i[1]
		    wt=i[2]
		    if a[u]!=100000000 and a[u]+wt<a[v]:
		        a[v]=a[u]+wt
		#print(a)
		if a==dis:
		    return 0
		return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends