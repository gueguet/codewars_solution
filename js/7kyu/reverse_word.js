// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/javascript

function reverSingleWord(wrd) {
    res = ''
    for (let index = wrd.length-1; index >= 0; index--) {
        res += wrd[index];
    }
    return res
}   


function reverseWords(str) {
    res = ''
    str.split(' ').forEach(element => {
        console.log(element);
        res += reverSingleWord(element) + ' ';
    });
    return res.substring(0, res.length - 1);
}   


reverseWords('The quick brown fox jumps over the lazy dog.')



/*

* clever

function reverseWords(str) {
  return str.split(' ').map(function(word){
    return word.split('').reverse().join('');  // * use split to be able to use reverse on an array 
  }).join(' '); // * goog guess to use join
}

*/
