import java.util.*;

public class Solution {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int m = input.nextInt();
    int n = input.nextInt();
    BitSet[] B = {new BitSet(m), new BitSet(m)};

    for (int i = 0; i < n; i++) {
      String op = input.next();
      int param1 = input.nextInt();
      int param2 = input.nextInt();

      switch (op) {
        case "AND":
          B[param1-1].and(B[param2-1]);
          break;
        case "OR":
          B[param1-1].or(B[param2-1]);
          break;
        case "XOR":
          B[param1-1].xor(B[param2-1]);
          break;
        case "SET":
          B[param1-1].set(param2);
          break;
        case "FLIP":
          B[param1-1].flip(param2);
      }
      System.out.println(B[0].cardinality() + " " + B[1].cardinality());
    }
  }
}
