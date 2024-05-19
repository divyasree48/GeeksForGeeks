#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        
       #Write your code here
        a=[]
        k=0
        c=0
        j=0
        for i in range(n):
            c+=arr[i]
            if c>=s:
                while(j<i+1 and c>=s):
                    if c==s:
                        a.append(j+1)
                        a.append(i+1)
                        return a
                    elif c>s:
                        c-=arr[j]
                    j+=1
        a.append(-1)
        return a
               








#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends