class Solution {
public:

    long int sum(string val){
        long int s = 0;
        for(int i = 0; i<val.size(); i+=1){
            s += (val[i] - '0');
        }
        return s;
    }
    string digitSum(string s, int k) {
        
        while(s.size() > k){
            string temp = "";
            int t = 0;
            int rounds = s.size()/k;
            while(rounds){
                string slice = s.substr(t,k);
                t += k;
                // long num = stoll(slice);
                long num = sum(slice);
                temp += to_string(num);
                rounds -= 1;
            }
            string slice = s.substr(t);
            t += k;
            if(slice.size()>0){
            // long num = stoll(slice);
            long num = sum(slice);
            temp += to_string(num);
            }
            s = temp;
        }
        return s;
    }
};
