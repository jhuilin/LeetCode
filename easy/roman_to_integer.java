class Solution {
    public int romanToInt(String s) {
		int index = 0;
		int total = 0;
		while(s.length()-1 >= index) {
			if(s.charAt(index) == 'I')
				total += 1;
			if(s.charAt(index) == 'V') {
				if(index != 0 && s.charAt(index-1) == 'I')
					total = total + 5 - 2;
				else
					total += 5;
			}
			if(s.charAt(index) == 'X') {
				if(index != 0 && s.charAt(index-1) == 'I')
					total = total + 10 - 2;
				else
					total += 10;
			}
			if(s.charAt(index) == 'L'){
				if(index != 0 && s.charAt(index-1) == 'X')
					total = total + 50 - 20;
				else
					total += 50;
			}
			if(s.charAt(index) == 'C'){
				if(index != 0 && s.charAt(index-1) == 'X')
					total = total + 100 - 20;
				else
					total += 100;
			}
			if(s.charAt(index) == 'D'){
				if(index != 0 && s.charAt(index-1) == 'C')
					total = total + 500 - 200;
				else
					total += 500;
			}
			if(s.charAt(index) == 'M'){
				if(index != 0 && s.charAt(index-1) == 'C')
					total = total + 1000 - 200;
				else
					total += 1000;
			}
			++index;
		}
		return total;
	}
}