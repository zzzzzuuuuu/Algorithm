function solution(rank, att) {
  return rank
    .map((r, i) => [i, r])
    .filter(([i, _]) => att[i])
    .sort((a, b) => a[1] - b[1])
    .slice(0, 3)
    .reduce((acc, [i], idx) => acc + i * [10000, 100, 1][idx], 0);
}