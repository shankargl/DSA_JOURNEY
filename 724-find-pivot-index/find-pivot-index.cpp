class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total=0;
        for (auto i : nums){
            total+=i;
        }
        int pre=0;
        int n=nums.size();
        for (int i = 0; i<n; i++){
            int now=total-pre-nums[i];
            if (now==pre){
                return i;
            }
            pre=pre+nums[i];
        }
        return -1;
    }
};