// 재귀함수로 풀어보기...
function solution(num, count = 0) {
  if (count > 500) return -1;
  if (num === 1) return count;

  const next = num % 2 === 0 ? num / 2 : num * 3 + 1;
  return solution(next, count + 1;)
}