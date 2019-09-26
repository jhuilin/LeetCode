class Solution {
    public int lengthOfLongestSubstring(String s){
        if(s.length() == 0) return 0;
        ArrayList<String> l1 = new ArrayList<String>();
        int length = 0;
        boolean isContain = false;
        int i = 0;
        while(i < s.length()){
            String letter = String.valueOf(s.charAt(i));
            if(l1.contains(letter)){
                isContain = true;
            	if(l1.size() > length)
            		length = l1.size();
            	int position = l1.indexOf(letter);
            	remove(position,l1);
            	l1.add(letter);
            }else{
            	l1.add(letter);
            }
            ++i;
        }
        if(isContain == false)  return i;
        if(l1.size() > length)	return l1.size();
        return length;
    }
    public static void remove(int position, ArrayList<String> list) {
    	while(position >= 0) {
    		list.remove(position);
    		--position;
        }
    }
}