class Solution {
public:
    bool checkDivisibility(int n) {
        int t = n;
        int sums = 0;
        int prods = 1;
                while(t != 0){

                    sums += t%10;
                    prods *= t%10;
                    t /= 10;
        }
        return n%(sums+prods)==0;
    }
};