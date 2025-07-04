function solution(my_strings, parts) {
  return parts.map(([s, e], i) => my_strings.slice(s, e+1)).join('');
}