public class Solution {
    public bool CloseStrings(string a, string b) {
        if (a.Length != b.Length) return false;
        if (a == b) return true;
        
        // First, each string must use the same letters
        HashSet<char> set_a = new HashSet<char>(a.ToCharArray());
        HashSet<char> set_b = new HashSet<char>(b.ToCharArray());
        if (!set_a.SetEquals(set_b)) {
            return false;
        }
        
        // Count the occurences of each letter
        int[] l1 = new int[26];
        int[] l2 = new int[26];
        foreach (char c in a) {
            l1[c-'a']++;
        }
        foreach (char c in b) {
            l2[c-'a']++;
        }
        
        // Finally, ensure that both strings char counts have the same pattern of digits 
        Array.Sort(l1);
        Array.Sort(l2);
        return Enumerable.SequenceEqual(l1, l2);
    }
}