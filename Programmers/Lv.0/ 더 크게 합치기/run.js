function solution(a, b) {
  let answer1 = String(a) + String(b);
  let answer2 = String(b) + String(a);
  return (answer1 > answer2 ? Number(answer1) : Number(answer2));
}