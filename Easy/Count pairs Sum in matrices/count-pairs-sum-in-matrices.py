#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		def binary_search(n,l):
		    i=0
		    j=len(l)-1
		    while(i<=j):
		        m=(i+j)//2
		        if l[m]==n:
		            return 1
		        elif l[m]>n:
		            j=m-1
		        else:
		            i=m+1
		    return 0
		list1=[]
		list2=[]
		for i in mat1:
		    list1.extend(i)
		for i in mat2:
		    list2.extend(i)
		ans=0
		for i in list1:
		    if i<x:
    		    if binary_search(x-i,list2):
    		        ans+=1
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends