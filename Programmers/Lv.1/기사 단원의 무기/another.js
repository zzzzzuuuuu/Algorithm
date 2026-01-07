function solution(number, limit, power) {
  let answer = 0;

  for (let i = 1; i <= number; i++) {
    let count = 0;
    for (let j = 1; j * j <= i; j++) {
      if (j*j === i) count += 1;
      else if (i % j === 0) count += 2;
    }
    answer += count > limit ? power : count;
  }

  return answer;
}