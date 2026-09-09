class Solution {
public:
    long long countCommas(long long n) {
        long long count=0;
        long long p=1000;
        while (p<=n){
            count=count+(n-p+1);
            p=p*1000;
        }
        return count;
        
    }
};