import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
	public static void main (String[] args)
	 {
	 //code
	     Scanner s = new Scanner(System.in);
	    int t = s.nextInt();
	    while(t--!=0){
	        int n = s.nextInt();
	        
	        int[] arr = new int[n+1];
	        for(int i=0; i<=n; i++)
	        arr[i] = Math.max(arr[i/2] + arr[i/3] + arr[i/4],i);
	        
	        System.out.println(arr[n]);
	    }
	 }
}