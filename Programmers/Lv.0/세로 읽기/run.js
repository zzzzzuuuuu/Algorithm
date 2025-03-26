function solution(my_string, m, c) {
  let result = [];
  for (let i = 0; i < my_string.length; i+=m) {
    result.push(my_string.substring(i, i+m));
  }
  return result.map(l => l[c-1]).join('');
}