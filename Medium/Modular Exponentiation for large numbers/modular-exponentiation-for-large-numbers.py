#User function Template for python3

class Solution:
	def PowMod(self,a,b,m):
		# Code here
		res=1
		while(b):
    		if b&1:
    		    b-=1
    		    res=(res*a)%m
    		else:
    		    b//=2
    		    a=(a*a)%m
		return res%m
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends*m)*(a%m)