#include"data_gen.h"
#include <time.h>
#include <stdlib.h>

double* rand_double_arr(int size){
    double* res = (double*) malloc(size * sizeof(double));
    srand((unsigned)time(NULL));
    for (int i = 0; i < size; ++i) {
        res[i] = (double)rand()/RAND_MAX;
    }
    return res;
}

int* rand_int_arr(int size){
    int* res = (int*) malloc(size * sizeof(int));
    srand((unsigned)time(NULL));
    for (int i = 0; i < size; ++i) {
        res[i] = (int)rand();
    }
    return res;
}

char* rand_char_arr(int size){
    char* res = (char*) malloc(size * sizeof(char));
    srand((unsigned)time(NULL));
    for (int i = 0; i < size; ++i) {
        res[i] = (char)rand();
    }
    return res;
}

float* rand_float_arr(int size){
    float* res = (float*) malloc(size * sizeof(float));
    srand((unsigned)time(NULL));
    for (int i = 0; i < size; ++i) {
        res[i] = (float)rand();
    }
    return res;
}

