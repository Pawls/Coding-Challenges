public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0) return "";

        StringBuilder s = new StringBuilder(strs[0]);
        foreach (string word in strs)
        {
            if (word.Length == 0) return "";
            for (int i = 0; i < s.Length; i++)
            {
                if (word[i] != s[i])
                {
                    s.Remove(i, s.Length - i);
                    break;
                }
                else if (i == word.Length - 1 && i < s.Length - 1)
                {
                    s.Remove(i + 1, s.Length - i - 1);
                    break;
                }
            }
        }
        return s.ToString();
    }
}