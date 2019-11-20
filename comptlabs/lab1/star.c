#include<stdio.h>
void star(int n);
void main(){
	
	star(5);
}

void star(int n){
	
	for(int j=1;j<n;j++){
		for(int i=1;i<n-j;i++){
			printf(" ");
		}
		for(int k=0;k<2*j-1;k++){
		printf("*");}
		printf("\n");
	}
}
