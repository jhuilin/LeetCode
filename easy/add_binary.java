class Solution {
    public String addBinary(String a, String b) {
        int la = a.length() - 1;
        int lb = b.length() - 1;
        String result = "";
        int carry = 0;
        while(la >= 0 && lb >= 0 ){
            if(a.charAt(la) == '1' && b.charAt(lb) == '1'){
                if(carry == 0){
                    result = "0" + result;
                    carry = 1;
                }
                else{
                    result = "1" + result;
                    carry = 1;
                }
            }
            else if(a.charAt(la) == '0' && b.charAt(lb) == '0'){
               if(carry == 0)
                    result = "0" + result;
               else{
                   result = "1" + result;
                   carry = 0;
               }
            }
           else{
               if(carry == 0)
                   result = "1" + result;
               else{
                   result = "0" + result;
                   carry = 1;
               }
           }
            --la;
            --lb;
        }
        if(la > lb){
            while(la>=0){
                if(a.charAt(la) == '1'){
                    if(carry == 1){
                        result = "0" + result;
                        carry = 1;
                    }
                    else{
                        result = "1" + result;
                        carry = 0;
                    }
                }
                if(a.charAt(la) == '0')
                {
                    if(carry == 1){
                        result = "1"+ result;
                        carry = 0;
                    }
                    else{
                        result = "0" + result;
                    }
                }
                --la;
            }
        }
        if(lb > la){
            while(lb>=0){
                if(b.charAt(lb) == '1'){
                    if(carry == 1){
                        result = "0" + result;
                        carry = 1;
                    }
                    else{
                        result = "1" + result;
                        carry = 0;
                    }
                }
                if(b.charAt(lb) == '0'){
                    if(carry == 1){
                        result = "1" + result;
                        carry = 0;
                    }
                    else{
                        result = "0" + result;
                    }
                }
                --lb;
            }
        }
        if(carry == 1)
            result = "1" + result;
        return result;
    }
}