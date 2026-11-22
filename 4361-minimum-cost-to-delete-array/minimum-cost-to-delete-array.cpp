class Solution {
public:
    long long minCost(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin()+1, nums.begin()+n-1);

        long long curr = 0, ans = 0;

        for(int i=2; i<n-1; i+=2){
            curr += nums[i] + nums[i-1];
            ans = min(ans, curr);
        }

        return ans + nums[0] + nums[n-1];
    }
};