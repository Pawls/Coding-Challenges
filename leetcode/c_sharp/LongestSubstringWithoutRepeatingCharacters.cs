public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if (s.Length < 2) {
            return s.Length;
        }
        int left = 0;
        int right = 0;
        int longest = 0;
        Dictionary<char, int> seen = new Dictionary<char, int>();
        while (right < s.Length) {
            if (seen.ContainsKey(s[right])) {
                if (seen[s[right]] >= left) {
                    longest = Math.Max(longest, right - left);
                    left = seen[s[right]] + 1;
                    if (s.Length - longest <= left) {
                        break;
                    }
                }
                seen[s[right]] = right;
            } else {
                seen.Add(s[right], right);
            }
            right++;
        }
        return longest >= (right - left) ? longest : (right - left);
    }
}