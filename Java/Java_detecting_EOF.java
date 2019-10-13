import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	/*
	 * At end of stream:
	 * read() returns -1.
	 * read(byte[]) returns -1.
	 * read(byte[], int, int) returns -1.
	 * readLine() returns null.
	 * readXXX() for any other X throws EOFException.
	 * Scanner.hasNextLine() returns false.
	 * Scanner.nextLine() throws NoSuchElementException.
	 * Unless you've encountered one of these, your program hasn't encountered end of stream. 
	 * NB \u001a is a Ctrl/z. Not EOF. EOF is not a character value
	*/

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 1;
        while(sc.hasNext()){
            String s = sc.nextLine();
            System.out.printf("%d %s%n", i, s);
            i++;
        }
    }
}