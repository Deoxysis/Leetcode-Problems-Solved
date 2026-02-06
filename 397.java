class Solution {
    public int integerReplacement(int n) {
        long m = n;
        int steps = 0;
        while (m != 1) {
            if (m == 3)
                return steps+2;
            steps++;
            if (m % 2 == 0) {
                m /= 2;
            } else {

                String s1 = Long.toBinaryString(m - 1);
                String s2 = Long.toBinaryString(m + 1);

                int count1 = 0;
                int count2 = 0;

                for (int i = s1.length() - 2; i >= 0; i--) {
                    char c = s1.charAt(i);
                    if (c == '0') {
                        count1 += 1;
                    } else
                        break;
                }
                for (int i = s2.length() - 2; i >= 0; i--) {
                    char c = s2.charAt(i);
                    if (c == '0') {
                        count2 += 1;
                    } else
                        break;
                }
                if (count1 >= count2) {
                    m--;
                } else {
                    m++;
                }
            }

            // System.out.println(n);
        }
        return steps;
    }
    // public static int reduce(int n, int steps){
    //     if (n == 1){
    //         return steps
    //     }
    //     if (n % 2 == 0){
    //         return 
    //     }
    // }
}