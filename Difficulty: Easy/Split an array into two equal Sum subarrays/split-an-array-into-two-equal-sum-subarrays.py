class Solution:
    def canSplit(self, arr):
        #code here
        summ=sum(arr)
        a=0
        for i in arr:
            a+=i
            b=summ-a
            if a==b:
                return 1
        return 0
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends