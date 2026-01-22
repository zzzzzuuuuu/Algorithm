function solution(x) {
  const number = String(x).split('');
  return +x % number.reduce((a, b) => (a + +b), 0) === 0;
}