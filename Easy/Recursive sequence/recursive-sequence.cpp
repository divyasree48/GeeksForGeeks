//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    long long sequence(int n){
        // code here
        long long mod=1e9+7;
        long long y=1;
        long long ans=0;
        for(long long i=1;i<=n;i++)
        {
            long long j=i,p=1;
            while(j)
            {
                p*=y%mod;
                p=p%mod;
                y+=1;
                j-=1;
            }
          //  cout<<p<<" ";
            ans+=p%mod;
        }
        return ans%mod;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        cout<<ob.sequence(N)<<endl;
    }
    return 0;
}
// } Driver Code Ends