/**
 * @file pointer_practice.c
 * @author caleb eioluwa (caleberioluwa@gmail.com)
 * @brief sample code on pointer usage from the c programming book 
 * @version 0.1
 * @date 2021-12-19
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#include <stdio.h>


#define ALLOCSIZE 10000 /* size oof available space */
static char allocbuf[ALLOCSIZE]; /* stoorage for alloc */
static char* allocp = allocbuf; /* pointer to next free position */

char* alloc(int n)
{
    if(allocbuf+ALLOCSIZE-allocp>=n){
        allocp+=n; 
        return allocp-n;
    }else{
        return 0;
    }
}
void afree(char* p){
    if(p>=allocbuf && p< allocbuf+ALLOCSIZE)
        allocp=p;
}