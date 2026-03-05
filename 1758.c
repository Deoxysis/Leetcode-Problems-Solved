int minOperations(char* s) {
    int start0 = 0, start1 = 0;

    for(int i = 0; s[i]; i++) {
        if(s[i] != (i % 2 ? '1' : '0')) start0++;
        if(s[i] != (i % 2 ? '0' : '1')) start1++;
    }

    return start0 < start1 ? start0 : start1;
}