function solution(my_string) {
  const result = [];
  for (let i = 0; i < my_string.length; i++) {
    result.push(my_string.substring(i));
  }
  return result.sort();
}