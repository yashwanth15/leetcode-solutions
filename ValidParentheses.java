import java.util.Map;
import java.util.ArrayDeque;
import java.util.Deque;

public class ValidParentheses {
    public static boolean isValid(String s){
        int typeA=0;
        int typeB=0;
        int typeC=0;
        for(int i=0;i<s.length();i++){
            char character = s.charAt(i);
            if(character=='(')
                typeA++;
            else if(character==')')
                typeA--;
            else if(character=='[') 
                typeB++;
            else if(character==']')
                typeB--;
            else if(character=='{')
                typeC++;
            else if(character=='}')
                typeC--;
            else
                return false;

        }
        return typeA==0 && typeB==0 && typeC==0;
    }

    public static boolean isValidUsingStack(String s){
        Map<Character,Character> parentheses = Map.of(
            ')','(',
            ']','[',
            '}','{'
            );
        Deque<Character> stack = new ArrayDeque<>();
        for(char element: s.toCharArray()){
            if(parentheses.containsKey(element)){
                char top = stack.isEmpty()?'#': stack.pop();
                if(top!=parentheses.get(element)){
                    return false;
                }
            }else {
                stack.push(element);
            }
        }
        return stack.isEmpty();

    }

    public static void main(String[] args){
        String s = "({})";
        System.out.println(isValid(s));
        System.err.println(isValidUsingStack(s));
    }
}