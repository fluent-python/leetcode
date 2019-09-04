#include <bits/stdc++.h> 

class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        vector<int> ans;
        int sub = accumulate(A.begin(), A.end(), 0) - accumulate(B.begin(), B.end(), 0);
        printf("sub: %d", sub);
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                if ((A[i] - B[j])*2 == sub) {
                    ans.push_back(A[i]);
                    ans.push_back(B[j]);
                    return ans;
                }
            }
        }
        return ans;
    }
};
