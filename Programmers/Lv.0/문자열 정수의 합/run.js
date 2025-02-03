function solution(num_str) {
  let sum = 0;
  num_str.split('').forEach(n => sum += Number(n));

  return sum;
}