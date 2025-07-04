function solution(my_strings, parts) {
  return my_strings.map((str, i) => {
    const [s, e] = parts[i];
    return str.substring(s, e+1);
  }).join('');
}