import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        if (k > s.length()) return null;
        if (k == s.length()) return s + "\n" + s;
        
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        for (int i = 1; i < s.length()-k+1; i++){
            String sub = s.substring(i, i + k);            
            smallest = smallest.compareTo(sub) > 0 ? sub : smallest;
            largest = largest.compareTo(sub) < 0 ? sub : largest;
        }
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}