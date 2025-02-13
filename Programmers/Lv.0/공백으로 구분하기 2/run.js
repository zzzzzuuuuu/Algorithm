function solution(my_string) {
  return my_string.split(' ').filter(Boolean);
  // return my_string.split(' ').filter(v => v);
}