class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size();
        int mid, result;

        while (l <= r) {
            mid = (l + r) / 2;
            result = nums[mid];

            if (result == target) {
                return mid;
            } else if (result > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return -1;
    }
};
