#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        l=[]
        for i in arr:
            a=i.value/i.weight
            l.append([i.value,i.weight,a])
        l=sorted(l,key=lambda x:x[2])[::-1]
        c=0.0
        #print(l)
        for i in range(n):
            if l[i][1]<=w:
                w-=l[i][1]
                c+=l[i][0]
            else:
                
                c+=(l[i][0]*w)/l[i][1]
                break
            #print(c,w)
        return c
                
        
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends