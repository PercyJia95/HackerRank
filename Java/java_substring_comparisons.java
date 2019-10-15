import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "A";
        for(int i=0; i<k; i++){
            smallest = smallest + "z";
            largest = largest + "A";
        }
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        int i = 0;
        int len = s.length();
        for(String cur; i+k<=len; i=i+1){
            if(i+3<len){
                cur = s.substring(i,i+k);
            }else{
                cur = s.substring(i);
            }
            if(smallest.compareTo(cur)>0){
                smallest = cur;
            }
            if(largest.compareTo(cur)<0){
                largest = cur;
            }
        }
        return smallest + "\n" + largest;
    }

/* NOTE for this:
 *
 * We define the following terms:
 *
 * Lexicographical Order, also known as alphabetic or dictionary order, 
 * orders characters as follows:
 * For example, ball < cat, dog < dorm, Happy < happy, Zoo < ball.
 *
 * A substring of a string is a contiguous block of characters in the string. 
 * For example, the substrings of abc are a, b, c, ab, bc, and abc.
 *
 */