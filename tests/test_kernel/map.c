#include "data_gen.h"
#include <stdlib.h>
#include <stdio.h>

void map(double* dst, double* src, double d, int size){
    for (int i = 0; i < size; ++i) {
        dst[i] = src[i] + d;
    }
}

int main(int argc, const char** argv){
    int size = 512;
    if (argc > 1){
        size = atoi(argv[1]);
    }
    double* arr = rand_double_arr(size);
    double* res = (double*) malloc(size * sizeof(double));

    map(res, arr, 5.0, size);

    for (int i = 0; i < size; ++i) {
        printf("%lf=>%lf ", arr[i], res[i]);
    }

    return 0;
}