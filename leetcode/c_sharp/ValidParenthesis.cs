public class Solution
{
    public bool IsValid(string s)
    {
        // Return false if Length is odd
        if (s.Length % 2 == 1) return false;

        Stack<char> stack = new Stack<char>();
        char popped;
        foreach (char c in s)
        {
            switch (c)
            {
                case '(':
                case '{':
                case '[':
                    stack.Push(c);
                    break;
                case ')':
                    if (stack.TryPop(out popped))
                    {
                        if (popped != '(')
                            return false;
                        break;
                    }
                    return false;
                case '}':
                    if (stack.TryPop(out popped))
                    {
                        if (popped != '{')
                            return false;
                        break;
                    }
                    return false;
                case ']':
                    if (stack.TryPop(out popped))
                    {
                        if (popped != '[')
                            return false;
                        break;
                    }
                    return false;
                default:
                    return false;
            }
        }

        return stack.Count == 0;
    }
}