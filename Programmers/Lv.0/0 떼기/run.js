
function solution(n_str) {
  return n_str.substring(n_str.split('').findIndex(v => v !== '0'));
}