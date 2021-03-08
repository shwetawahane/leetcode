//Merging 2 Packages
//Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

//Analyze the time and space complexities of your solution.

//Example:

//input:  arr = [4, 6, 10, 15, 16],  lim = 21

//output: [3, 1] # since these are the indices of the
  //             # weights 6 and 15 whose sum equals to 21
//Constraints:

//[time limit] 5000ms

//[input] array.integer arr

//0 ≤ arr.length ≤ 100
//[input] integer limit

//[output] array.integer







import java.io.*;
import java.util.*;

class Solution {

  static int[] getIndicesOfItemWeights(int[] arr, int limit) {
    
   // List original = Arrays.asList(arr);
    if(arr.length==0 || arr.length==1){
      return new int[0];
    }
    else{
      int[] ans = new int[2];
      for(int i=arr.length-1; i>0;i--){
        for(int j=i-1;j>=0;j--){
          if(arr[i]+arr[j]==limit){
            ans[0]=i;
            ans[1]=j;
            return ans;
        }
      }
    }
    return new int[0];
    }
    
  }

  public static void main(String[] args) {

  }

}