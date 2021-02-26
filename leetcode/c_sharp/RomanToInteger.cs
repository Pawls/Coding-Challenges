public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> roman = new Dictionary<char, int> {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        
        int result = 0;
        for (int i = s.Length-1; i >= 0; i--) {
            result += roman[s[i]];
            // If there is a char to the left, we need to check
            // if it will change our current number.
            if (i > 0){
                switch (s[i]) {
                    case 'V':
                    case 'X':
                        if (s[i-1] == 'I'){
                            result -= 1;
                            i--; // Skip the next character
                        }
                        break;
                    case 'L':
                    case 'C':
                        if (s[i-1] == 'X'){
                            result -= 10;
                            i--;
                        }
                        break;
                    case 'D':
                    case 'M':
                        if (s[i-1] == 'C'){
                            result -= 100;
                            i--;
                        }
                        break;

                }
            }
        }
        return result;
    }
}