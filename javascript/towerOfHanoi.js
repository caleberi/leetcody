function towerOfHanoi(source,destination,intermediate,n){
    if(n<=0)
        return
    towerOfHanoi(source,intermediate,destination,n-1);
    console.log("Move Disk-%d FROM %s TO %s",n,source,destination);
    towerOfHanoi(intermediate,destination,source,n-1);
}


towerOfHanoi("Source","Destination","Intermediate",3)