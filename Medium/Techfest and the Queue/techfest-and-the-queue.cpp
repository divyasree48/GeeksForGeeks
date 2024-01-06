//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
	int sumOfPowers(int a, int b){
	    // Code here
	    
	    vector<int> v(b+1,1);
	    int c=0;
	    for(int i=2;i<b+1;i++){
	        if(v[i]==1){
	            if(i>=a and i<=b)
	            c++;
	            int j=i*2;
	            while(j<=b){
	                if(j>=a and j<=b){
	                    int temp=j;
	                    while(temp!=1 and temp%i==0){
	                        temp/=i;
	                        c++;
	                    }
	                }
	                v[j]=0;
	                j+=i;
	            }
	        }
	    }
	    return c;
	}
	
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int a, b;
		cin >>  a >> b;
		Solution obj;
		int ans = obj.sumOfPowers(a, b);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends