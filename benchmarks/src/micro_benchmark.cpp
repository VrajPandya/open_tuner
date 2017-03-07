#include<iostream>
#include<cstdint>
#include<stdlib.h>

#define KILO 1024
#define MEGA KILO * KILO

using namespace std;

int main(int argc, const char** argv){
	int * block = (int*)malloc(8 * MEGA);
	int L;
	int s;
	for (L = 4 * KILO; L <= 8 * MEGA; L *= 2){
		for(s = 0; s <= L/2; s *= 2){
			__builtin_prefetch((const void*)(&block[s]),0,0);
		}
	
	}

}
