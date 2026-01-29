function solution(left, right) {
  let answer = 0;

  for (let i = 1; i <= right; i++) {
    if (Number.isInteger(Math.sqrt(i))) answer -= i;
    else answer += i;
  }

  return answer;
}