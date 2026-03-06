bool checkOnesSegment(char* s) {
    bool seen = 0;
    int i = 1;
    while(s[i]){
        if(s[i] == '0'){
            seen = 1;
        }
        if( s[i] == '1' && seen){
            return 0;
        }
        i += 1;
    }
    return 1;
}