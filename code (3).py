def subArraySum(self,arr, n, s): 
        #subarray with given sum
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
               