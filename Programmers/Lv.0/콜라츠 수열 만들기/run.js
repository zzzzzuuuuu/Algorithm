function solution(n) {
  const answer = [];

  while (1) {
    answer.push(n);
    if (n === 1) break;
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
  }

  return answer;
}