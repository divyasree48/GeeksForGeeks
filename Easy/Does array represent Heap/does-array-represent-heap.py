
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here 
        for i in range(0,n):
            a=(2*i)+1
            b=(2*i)+2
            if a>=n:
                break
            else:
                if arr[a]>arr[i]:
                    return 0
                if b>=n:
                    break
                else:
                    if arr[b]>arr[i]:
                        return 0
        return 1
                



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends