public class Solution {
    
    public int MinimumDeletions(string s) {
        int[] b_left = new int[s.Length];
        int[] a_right = new int[s.Length];
        int min_del = s.Length;
        
        // Bs to the left
        int counter = 0;
        for (int i = 0; i < s.Length; ++i) {
            b_left[i] = counter;
            if (s[i] == 'b') {
                counter++;
            }
        }

        // As to the right
        counter = 0;
        for (int i = s.Length-1; i >= 0; --i) {
            a_right[i] = counter;
            min_del = Math.Min(min_del, b_left[i] + a_right[i]);
            if (s[i] == 'a') {
                counter++;
            }
        }
            
        return min_del;
    }
}