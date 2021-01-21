import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static boolean flag;
    public static Scanner input;
    public static int B;
    public static int H;
    
    static {
        Scanner input = new Scanner(System.in);
        B = input.nextInt();
        H = input.nextInt();
        try {
            if (B <= 0 || H <= 0){
                throw new Exception("Breadth and height must be positive");
            } else {
                flag = true;
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }


public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

