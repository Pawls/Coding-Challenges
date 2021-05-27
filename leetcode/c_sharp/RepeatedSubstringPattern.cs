public class Solution {
    
    public static int[] GetFactors(int num) {
        List<int> res = new List<int>();
        for (int i = num/2; i > 0; i--) {
            if (num % i == 0) {
                res.Add(i);
            }
        }
        return res.ToArray();
    }
    
    public bool RepeatedSubstringPattern(string s) {
        if (s.Length <= 1) return false;
        
        var factors = GetFactors(s.Length);
        foreach (int num in factors) {
            string substring = s.Substring(0, num);
            for (int i = num; i <= s.Length - num; i += num) {
                if (s.Substring(i, num) != substring) {
                    break;
                }
                if (i == s.Length - num) {
                    return true;
                }
            }
        }
        return false;
    }
}