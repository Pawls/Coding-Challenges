import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;
        int[] primes = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};
        int hash_a = 1;
        int hash_b = 1;
        for (int i = 0; i < a.length(); i++) {
            int c1 = (((int) a.charAt(i)) & ~32) - 65;
            int c2 = (((int) b.charAt(i)) & ~32) - 65;
            hash_a *= primes[c1];
            hash_b *= primes[c2];
        }
        return hash_a == hash_b;
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
