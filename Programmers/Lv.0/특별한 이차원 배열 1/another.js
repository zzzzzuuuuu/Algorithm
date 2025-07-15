function solution(n) {
  const answer = Array.from(Array(n), () => Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    answer[i][i] = 1;
  }

  return answer;
}

function solution2(n) {
  return Array.from({length: n}, (_, i) =>
    Array.from({length: n}, (_, j) => (i === j ? 1 : 0))
  );
}