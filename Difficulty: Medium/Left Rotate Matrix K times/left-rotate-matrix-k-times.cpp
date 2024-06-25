//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    void rev(vector<int>&v, int i, int j){
        while(i < j){
            swap(v[j--],v[i++]);
        }
    }
    vector<vector<int>> rotateMatrix(int k, vector<vector<int>> mat) {
        for(auto &it : mat){
            int n = it.size();
            k = k % n;
            rev(it, 0, n-1);
            rev(it, 0, n-k-1);
            rev(it, n-k, n-1);
        }
        return mat;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;
        vector<vector<int>> mat(n, vector<int>(m));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> mat[i][j];
        Solution ob;
        vector<vector<int>> ans = ob.rotateMatrix(k, mat);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                cout << ans[i][j] << " ";
            cout << "\n";
        }
    }
}

// } Driver Code Ends