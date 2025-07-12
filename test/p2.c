#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,m,a[10][10],b[10][10],i,j,s[10][10];
    scanf("%d %d",&n,&m);
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        scanf("%d",&a[i][j]);
    }
}
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        scanf("%d",&b[i][j]);
    }
}
printf("First Matrix: \n");
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        printf("%d ",a[i][j]);
    }
    printf("\n");
}
printf("Second Matrix: \n");
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        printf("%d ",b[i][j]);
    }
    printf("\n");
}
printf("Sum of the two matrices is:\n");
for(i=0;i<n;i++){
    for(j=0;j<m;j++){
        s[i][j]=a[i][j]+b[i][j];
        printf("%d ",s[i][j]);
    }
    printf("\n");
}

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
