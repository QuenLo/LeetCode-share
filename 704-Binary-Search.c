int search(int* nums, int numsSize, int target){
    return binery( nums, numsSize, target, 0 );

}
int binery(int* nums, int numsSize, int target, int piv){
    int mid = numsSize / 2;
    
    if ( target == *(nums+mid) ) return piv + mid;
    if (mid <= 0) return -1;
    if ( target < *(nums+mid) ) return binery( nums, mid, target, piv );
    else return binery( nums+mid, numsSize-mid, target, mid+piv);
}

int search2(int* nums, int numsSize, int target){
    int l=0, r=numsSize, mid = r/2;
    while (l<r){
        mid = (l+r)/2;
        if( target == *(nums+mid) ) return mid;
        else if( target < *(nums+mid) ) r = mid;
        else l = mid+1;
    }
    return -1;
}

