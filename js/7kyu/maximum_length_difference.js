// https://www.codewars.com/kata/5663f5305102699bad000056/train/javascript

function mxdiflg(a1, a2) {

  let max_len = 0;

  if (a1.length === 0 || a2.length === 0) {
    return -1;
  }

  a1.forEach(w1 => {
    a2.forEach(w2 => {
      let diff = Math.abs(w1.length - w2.length);
      if (diff > max_len) {
        max_len = diff;
      }
    })
  });

  return max_len;

}



var s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"];
var s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];

mxdiflg(s1, s2)