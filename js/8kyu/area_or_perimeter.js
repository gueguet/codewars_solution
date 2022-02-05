// https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/javascript

const areaOrPerimeter = (l, w) => {
  if (l === w) {
    return l ** 2;
  }
  return 2 * l + 2 * w;
};

areaOrPerimeter(2, 2);

/*
* clever
const areaOrPerimeter = (l , w) => l === w ? l*w : 2*(l+w);
*/
