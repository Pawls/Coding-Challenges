public class Solution {
    
    public int RepeatedStringMatch(string a, string b) {
        for (int i = 0; i < a.Length; i++) {
            if (a[i] == b[0]) {
                for (int j = i; j-i < b.Length && a[j % a.Length] == b[j-i]; j++) {
                    if ((j-i+1) == b.Length) {
                        return (int)Math.Ceiling(((double)(i + b.Length) / a.Length));
                    }
                }
            }
        }
        return -1;
    }
}