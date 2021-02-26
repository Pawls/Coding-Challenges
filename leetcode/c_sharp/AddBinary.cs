public class Solution
{
    public string AddBinary(string a, string b)
    {
        StringBuilder result = new StringBuilder();
        int i = a.Length - 1;
        int j = b.Length - 1;
        int sum = 0;
        int carry = 0;
        while (i >= 0 && j >= 0)
        {
            sum = (a[i] - '0') + (b[j] - '0') + carry;
            carry = 0;
            if (sum > 1)
            {
                carry = 1;
            }
            sum %= 2;
            result.Insert(0, sum.ToString());
            i--;
            j--;
        }

        while (i >= 0)
        {
            sum = (a[i] - '0') + carry;
            carry = 0;
            if (sum > 1)
            {
                carry = 1;
            }
            sum %= 2;
            result.Insert(0, sum.ToString());
            i--;
        }

        while (j >= 0)
        {
            sum = (b[j] - '0') + carry;
            carry = 0;
            if (sum > 1)
            {
                carry = 1;
            }
            sum %= 2;
            result.Insert(0, sum.ToString());
            j--;
        }

        if (carry > 0)
        {
            result.Insert(0, carry.ToString());
        }

        return result.ToString();
    }
}