#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dic):
        def fun(n,s,dic):
            if len(s)==0:
                return 1
            for i in dic:
                x=s[:len(i):]
                if x==i:
                    if fun(n,s[len(i)::],dic):
                        return 1
            return 0
        return fun(n,s,dic)
                    
                
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends