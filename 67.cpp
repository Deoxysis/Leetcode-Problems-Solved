class Solution {
public:
    string addBinary(string a, string b) {
        int a_ptr = a.length() - 1;
        int b_ptr = b.length() - 1;
        int diff = a_ptr - b_ptr;
        if(diff > 0){
            int k = 0;
            while(k < diff){
                b = "0" + b;
                k += 1;
            }
        }
        else{
            diff = diff * -1;
            int k = 0;
            while(k < diff){
                a = "0" + a;
                k += 1;
            }
        }
        a_ptr = max(a_ptr, b_ptr);
        string res = "";
        bool carry = 0;
        while(a_ptr >= 0){
            if(a[a_ptr] == '1' && b[a_ptr] == '1'){
                if(carry){
                    res = "1" + res;
                }
                else{
                    res = "0" + res;
                    carry = 1;
                }
            }
            else if(a[a_ptr] == '1' || b[a_ptr] == '1'){ //either of them is 1
                if(carry){
                    res = "0" + res;
                    carry = 1;
                }
                else{
                    res = "1" + res;
                }
            }
            else{ //both zero
                if(carry){
                    res = "1" + res;
                    carry = 0;
                }
                else{
                    res = "0" + res;
                }
            }
            a_ptr -= 1;
        }
        if(carry) res = "1" + res;
        return res;
    }
};