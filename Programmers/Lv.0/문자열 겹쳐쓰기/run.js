function solution(my_string, overwrite_string, s) {
  str1 = my_string.slice(0, s);
  str2 = my_string.slice(s + overwrite_string.length);
  return (str1 + overwrite_string + str2);
}