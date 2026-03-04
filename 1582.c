int numSpecial(int** mat, int matSize, int* matColSize) {
    //assuming we are given rows, columns
    int *one_count_row = (int*)malloc(sizeof(int)*matSize);
    for(int i= 0; i < matSize; i+= 1)
        one_count_row[i] = 0;
    int *one_count_col = (int*)malloc(sizeof(int)* *matColSize);
    for(int i= 0; i < *matColSize; i+= 1)
        one_count_col[i] = 0;
    //first we create maps
    for(int i = 0; i < matSize; i+= 1){
        for(int j = 0; j < *matColSize; j += 1){
            if (mat[i][j] == 1){
                one_count_row[i] += 1;
                one_count_col[j] += 1;
            }
        }
    }
    //simply check for each 1
    int special_count = 0;
    for(int i = 0; i < matSize; i += 1){
        for(int j = 0; j < *matColSize; j += 1){
            if (mat[i][j] == 1 && one_count_row[i] == 1 && one_count_col[j] == 1){
                special_count += 1;
            }
        }
    }

    return special_count;
}