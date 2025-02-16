function solution(arr) {
  let result = [];
  arr.forEach(n => {
    for (let i = 0; i < n; i++) result.push(n);
  })
  return result;
}