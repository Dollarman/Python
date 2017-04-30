function isFunction(pairs) {
  var mypairs = pairs;
  mypairs.sort(function(a,b){
    return a[0] - b[0];
  });
  for (i in mypairs) {
    if (i + 1 > mypairs.length) {break;}
    if (mypairs[i + 1][0] = mypairs[i][0]) {
      if (mypairs[i + 1] != mypairs[i]) {
        return false;
      }
    }
  }
}