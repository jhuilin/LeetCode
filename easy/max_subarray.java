class Solution {
    public int maxSubArray(int[] nums) {
        int current = nums[0], global = nums[0];
        for(int i = 1; i< nums.length; ++i){
            current = max(nums[i],nums[i]+current);
            if(current > global)
                global = current;
        }
        return global;
    }
    public static int max(int a, int b)
    {
        if(a>b) return a;
        else    return b;
    }
}