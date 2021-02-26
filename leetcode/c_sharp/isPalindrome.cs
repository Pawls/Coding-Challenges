public class Solution
{
    public bool IsPalindrome(int x)
    {
        string str = x.ToString();
        int end = str.Length;
        for (int i = 0; i < end / 2; i++)
        {
            if (str[i] != str[end - i - 1])
            {
                return false;
            }
        }
        return true;
    }
}