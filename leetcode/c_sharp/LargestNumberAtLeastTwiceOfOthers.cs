public class Solution {
    public int DominantIndex(int[] nums) {
        // For each int in nums, if this number is greater than the current biggest, it must be twice as big
        // to change the result to true, else, if this num is greater than half the largest, result becomes false.
        if (nums.Length == 1) return 0;

        int largest = nums[0];
        int index = 0;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] >= largest * 2) {
                largest = nums[i];
                index = i;
            } else if (nums[i] > (largest / 2) && nums[i] != largest) {
                index = -1;
            }
        }
        return index;
    }
}