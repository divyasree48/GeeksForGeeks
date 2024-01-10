#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) : 
        #Complete the function
        if K==1:
            return n
        a=[]
        a.append(arr[0]%K)
        for i in range(1,n):
            a.append((a[i-1]+arr[i])%K)
        #print(a)
        d={}
        maxi=-999
        for i in range(n):
            if a[i]==0:
                maxi=max(maxi,i+1)
            elif a[i] not in d.keys():
                d[a[i]]=i
            else:
                
                if i-d[a[i]]>maxi:
                    maxi=i-d[a[i]]
        if(maxi==-999):
            return 0
        return maxi
            







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends