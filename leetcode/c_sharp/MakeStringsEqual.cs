public class Solution {
    public int MinimumSwap(string s1, string s2) {
        if (s1.Length != s2.Length) return -1;
        if (s1 == s2) return 0;
        
        int xy = 0;
        int yx = 0;
        for (int i = 0; i < s1.Length; ++i) {
            if (s1[i] == 'x' && s2[i] == 'y') {
                xy++;
            } else if (s1[i] == 'y' && s2[i] == 'x') {
                yx++;
            }
        }
        
        if ((xy % 2 + yx % 2) % 2 != 0) {
            return -1;
        }
        return (xy / 2) + (yx / 2) + (xy % 2) + (yx % 2);
    }
}