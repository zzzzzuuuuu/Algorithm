function solution(d, budget) {
  let count = 0;
  d.sort((a, b) => a - b);

  for (const v of d) {
    if ((budget - v) < 0) break;
    budget -= v;
    count++;
  }

  return count;
}