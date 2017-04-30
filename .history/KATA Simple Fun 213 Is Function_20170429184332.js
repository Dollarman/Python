function isFunction(pairs) {
  var mypairs = pairs;
  mypairs.sort(function(a,b){
    return a[0] - b[0];
  });
  for (i in mypairs) {
    if (i + 1 == mypairs.length) {break;}
    if (mypairs[i + 1][0] == mypairs[i][0]) {
      if (mypairs[i + 1][1] != mypairs[i][1]) {
        return false;
      }
    }
  }
  return true;
}

console.log(isFunction( [[0.5,1.5],[2.5,3.5]] ));