function solution(arr) {
  let result = [];
  arr.forEach(v => {
    if (v >= 50 && v % 2 === 0) result.push(v/2);
    else if (v < 50 && v % 2 === 1) result.push(v*2);
    else result.push(v);
  })
  return result;
}