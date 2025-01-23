function solution(num_list) {
  // Array.reduce(acc, cur, idx, src) => { return acc + cur; }, initialValue);
  let sum = num_list.reduce((a, b) => a + b, 0);
  let mul = num_list.reduce((a, b) => a * b, 1);

  return mul < sum ** 2 ? 1 : 0;
}