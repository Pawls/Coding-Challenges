public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.Length == 1 && nums2.Length == 0) return (double)nums1[0];
        if (nums2.Length == 1 && nums1.Length == 0) return (double)nums2[0];

        int mid = (nums1.Length + nums2.Length) / 2;

        // If either list is empty, we may find the median directly
        if (nums1.Length == 0) {
            return (nums2.Length % 2 == 0) ? ((nums2[mid - 1] + nums2[mid]) / 2.0) : (double)nums2[mid];
        }
        if (nums2.Length == 0) {
            return (nums1.Length % 2 == 0) ? ((nums1[mid - 1] + nums1[mid]) / 2.0) : (double)nums1[mid];
        }

        // If either list starts after the other finishes, then merging is not necessary
        int first = 0;
        int second = 0;
        if (nums2[0] > nums1[nums1.Length - 1]) {
            first = ((mid - 1) > (nums1.Length - 1)) ? nums2[(mid - 1) - nums1.Length] : nums1[mid - 1];
            second = (mid > (nums1.Length - 1)) ? nums2[mid - nums1.Length] : nums1[mid];
            return ((nums1.Length + nums2.Length) % 2 == 0) ? (first + second) / 2.0 : (double)second;
        }
        if (nums1[0] > nums2[nums2.Length - 1]) {
            first = ((mid - 1) > (nums2.Length - 1)) ? nums1[(mid - 1) - nums2.Length] : nums2[mid - 1];
            second = (mid > (nums2.Length - 1)) ? nums1[mid - nums2.Length] : nums2[mid];
            return ((nums1.Length + nums2.Length) % 2 == 0) ? (first + second) / 2.0 : (double)second;
        }

        // If we've made it this far, the lists must be merged
        for (int i = 0, j = 0, count = 0; count <= mid; count++) {
            first = second;
            if (i >= nums1.Length) {
                second = nums2[j++];
            } else if (j >= nums2.Length) {
                second = nums1[i++];
            } else if (nums1[i] <= nums2[j]) {
                second = nums1[i++];
            } else {
                second = nums2[j++];
            }
        }

        return ((nums1.Length + nums2.Length) % 2 == 0) ? ((first + second) / 2.0) : (double)second;
    }
}