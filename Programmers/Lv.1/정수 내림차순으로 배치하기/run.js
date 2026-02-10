function solution(n) {
  var answer = 0;
  return +String(n).split('').sort().reverse().join('');
}