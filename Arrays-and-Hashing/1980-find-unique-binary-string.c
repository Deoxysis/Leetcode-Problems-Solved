char* findDifferentBinaryString(char** nums, int numsSize) {
    char *ans = (char*)malloc(sizeof(char) * (1 + numsSize));
    for(int i = 0; i < numsSize; i += 1){
        ans[i] = nums[i][i] ^ 1;
    }
    ans[numsSize] = '\0';
    return ans;
}