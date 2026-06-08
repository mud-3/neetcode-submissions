#include <algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> solutions;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            int target = nums[i];

            if (target > 0) {
                break;
            }
            if (i > 0 && target == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int sum = nums[left] + nums[right] + target;
                if (sum == 0) {
                    solutions.push_back({nums[left], nums[right], target});
                    left++;
                    right--;
                    while (nums[left] == nums[left - 1] && left < right) {
                        left++;
                    }
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return solutions;
    }
};
