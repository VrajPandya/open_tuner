#include "data_gen.h"
#include <stdlib.h>
#include <stdio.h>

double map(double* src, int size){
    double d = 0.0;
    for (int i = 0; i < size; ++i) {
        d += src[i];
    }
    return d;
}

int main(int argc, const char** argv){
    int size = 512;
    if (argc > 1){
        size = atoi(argv[1]);
    }
    double* arr = rand_double_arr(size);

    double res = (res, arr, 5.0, size);

    for (int i = 0; i < size; ++i) {
        printf("%lf ", arr[i]);
    }

    printf("reduce: %lf", res);

    return 0;
}