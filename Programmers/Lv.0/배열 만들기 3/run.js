function solution(arr, intervals) {
  let result = [];
  intervals.map(([s, e]) => {
    result = result.concat(arr.slice(s, e+1));
  })
  return result;
}