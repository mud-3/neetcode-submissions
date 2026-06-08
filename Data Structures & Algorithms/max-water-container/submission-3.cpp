class Solution {
public:
    int min(int a, int b) {
        if (a < b) {
            return a;
        }
        return b;
    }

    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int maxWater = 0;

        while (left < right) {
            int water = min(heights[left], heights[right]) * (right - left);

            if (water > maxWater) {
                maxWater = water;
            }

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
            
        }

        return maxWater;
    }
};
