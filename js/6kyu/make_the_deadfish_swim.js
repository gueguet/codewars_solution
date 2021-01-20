// https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/javascript

function parse( data )
{
  
  let res = new Array();
  let val = 0;

  // could use
  // data.split('').reduce(...)
  // and switch(...)
  Array.from(data).forEach((char) => {
  
    if (char === "o") {
      res.push(val);
    }

    if (char === "i") {
      val += 1;
    }

    if (char === "d") {
      val -= 1;
    }

    if (char === "s") {
      val = val * val;
    }
  
  });

  return res;

}

parse("iiisdoso")