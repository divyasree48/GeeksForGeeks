//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
 

// } Driver Code Ends
/*You are required to complete this method*/

class Solution
{
    public:
    int dp[1000][1000];
    int mod=1000000007;
    int fun(string s,string t,int i,int j,int n,int m)
    {
        if(j>=m)return 1;
        if(i>=n)return 0;
        if(dp[i][j]!=-1)return dp[i][j]%mod;
        int c=0;
        if(s[i]==t[j])c+=fun(s,t,i+1,j+1,n,m);
        c+=fun(s,t,i+1,j,n,m);
        dp[i][j]=c%mod;
        return dp[i][j];
    }
    int subsequenceCount(string s, string t)
    {
        memset(dp,-1,sizeof(dp));
      return fun(s,t,0,0,s.size(),t.size());
    }
};
 


//{ Driver Code Starts. 

//  Driver code to check above method
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		string tt;
		cin>>s;
		cin>>tt;
		
		Solution ob;
		cout<<ob.subsequenceCount(s,tt)<<endl;
		
		
	}
  
}
// } Driver Code Ends