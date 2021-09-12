/* 
    Time: O(minlen(A[i])*A.size())
    Space: O(1)
    Tag: Strings manipualtion
    Difficulty: E
    Logic: Keep cutting the common character from start of all the strings
*/

string Solution::longestCommonPrefix(vector<string> &A) {
    int n=A.size();
    int minLen=INT_MAX;
    for(int i=0;i<n;i++){
        minLen=min(minLen, (int)A[i].length());
    }
    string res="";
    for(int i=0;i<minLen;i++){
        for(int j=1;j<n;j++){
            if(A[j][i]!=A[j-1][i]) return res;
        }
        res+=A[0][i];
    }
    return res;
}

