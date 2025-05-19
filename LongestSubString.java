import java.util.*;

public class LongestSubString {
    public static int movingWindow(String s){
        Set<Character> uniqueChars = new HashSet<>();
        int n=s.length();
        int left=0;
        int maxLength=0;
        for(int right=0; right<n; right++){
            while(uniqueChars.contains(s.charAt(right))){
                uniqueChars.remove(s.charAt(left));
                left++;
            }
            uniqueChars.add(s.charAt(right));
            maxLength=Math.max(maxLength,right-left+1);
        }
        return maxLength;
    }
    public static boolean isStringWithUniqueChars(String s){
        Set<Character> uniqueChar = new HashSet<>();
        for(char c:s.toCharArray()){
            uniqueChar.add(c);
        }
        return uniqueChar.size() == s.length();
    }
    public static int lengthOfLongestSubString(String s){
        String result="";
        String tempString="";
        for(int i=0;i<s.length();i++){
            for(int j=i+1;j<s.length();j++){
                tempString=s.substring(i,j);
                if (isStringWithUniqueChars(tempString) & tempString.length()>result.length()) {
                    result=tempString;
                }
            }
        }
        System.out.println(result);
        return result.length();
    }
    public static void main(String[] args){
        System.out.println(lengthOfLongestSubString("pwwwkew"));
        System.out.println(movingWindow("pwwkew"));
    }
}
