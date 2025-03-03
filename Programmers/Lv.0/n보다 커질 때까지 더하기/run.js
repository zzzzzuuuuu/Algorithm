function solution(numbers, n) {
  let sum = 0;
  for (let v of numbers) {
    sum += v;
    if (sum > n) return sum;
  }
  return sum;
}