int countPrimeSetBits(int left, int right) {
    int i = left;
    int count = 0;
    int set = 0;
    while(i <= right){
        set = __builtin_popcount(i);
        if(set == 2 || set ==3 || set ==5|| set ==7||set == 11||set ==13 ||set == 17|| set == 19){
            count += 1;
        }
        i += 1;
    }
    return count;
}