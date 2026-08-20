class Solution {
public:
    int minPartitions(string n) {
        int32_t i = n.length() - 1;
        uint8_t max = 1;
        while(i >= 0){
            uint16_t c = n[i] - '0';
            max = max > c ? max : c;
            if (max == 9) return 9;
            i -= 1;
        }
        return  max;
    }
};