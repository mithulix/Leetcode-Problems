int jump(int* nums, int numsSize){
    int l = 0;
    int r = numsSize -1 ;
    int jumps = 0;

    while(r>0) {
        if(l+nums[l] >= r) {
            r = l;
            jumps++;
            l = 0;
        } else {
            l++;
        }
    }
    return jumps;
}