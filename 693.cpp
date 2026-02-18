class Solution {
public:
    bool hasAlternatingBits(int n) {
        bool bit = n & 1;
        while(n != 0){
            if ((n & 1) != bit){
                return false;
            }
            bit = !bit ;
            n >>= 1;
        }
        return true;
    }
};