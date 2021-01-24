function isPowerOfTwo(n){
  if (n==0) {
    return false;
  }
  while(n!=1) {
    if (n%2 == 0) {
      n = n/2;
    }
    else {
      return false;
    }
  }
  return true;
}


// we could have usef log 
// return Number.isInteger(Math.log2(n));