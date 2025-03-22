function solution(number) {
  return Array.from(number).reduce((acc, v) => acc + Number(v), 0) % 9;
}