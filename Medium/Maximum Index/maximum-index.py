#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        mx=[a[-1]]
        mn=[a[0]]
        for i in range(1,n):
            mn.append(min(mn[-1],a[i]))
        for i in range(n-2,-1,-1):
            mx.append(max(mx[-1],a[i]))
        i=j=maxi=0
        mx=mx[::-1]
        #print(mx,mn)
        
        while(i<n and j<n):
            if mx[i]>=mn[j]:
                
                #if i<n and j<n:
                   # print(j,i)
                maxi=max(maxi,abs(j-i))
                i+=1
            else:
                j+=1
        return maxi
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends