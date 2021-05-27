public class Solution {
    
    public bool BuddyStrings(string a, string b) {
        if (a.Length != b.Length) return false;
        
        HashSet<char> set_a = new HashSet<char>(a.ToCharArray());
        HashSet<char> set_b = new HashSet<char>(b.ToCharArray());
        
        // If the strings are the same, there must be at least one duplicate character
        // for a swap to be possible.
        if (a == b){            
            return set_a.Count != a.Length;
        }
        
        // If the strings do not contain the same characters, return false
        set_a.SymmetricExceptWith(set_b);
        if (set_a.Count != 0) {
            return false;
        }
        
        // If mismatched positions exceeds 2, then a single swap cannot resolve the strings
        List<int> mismatched = new List<int>();
        for (int i = 0; i < a.Length; ++i) {
            if (a[i] != b[i]) {
                mismatched.Add(i);
            }
            if (mismatched.Count > 2) {
                return false;
            }
        }
        return a[mismatched[0]] == b[mismatched[1]] && a[mismatched[1]] == b[mismatched[0]];
    }
}