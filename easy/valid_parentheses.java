class Solution {
	public boolean isValid(String s) {
        if(s.isEmpty()) return true;
	    if(s.length()%2 == 1) return false;
	    Stack<Character> stacks = new Stack<Character>();
	    HashMap<Character,Character> tokens = new HashMap<Character,Character>();
	    tokens.put(')', '(');
	    tokens.put('}', '{');
	    tokens.put(']', '[');
	    int index = 0;
	    char currentToken = s.charAt(index); 
	    if(currentToken == ']' || currentToken == '}' || currentToken == ')')
	        return false;
	    stacks.push(currentToken);
	    ++index;
	    while(s.length()-1 >= index){
	    	currentToken = s.charAt(index);
	        if(currentToken == '(' || currentToken == '{' || currentToken == '['){
                stacks.push(currentToken);
            }
	        else{
	        	if(stacks.peek() == tokens.get(currentToken))
	        		stacks.pop();
	        	else
	        		return false;
	        }
	        ++index;
	    }
	    return stacks.isEmpty();
	}
}