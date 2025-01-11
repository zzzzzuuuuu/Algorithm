function solution(str1, str2) {
  let string = '';
  for (let i=0; i<str1.length; i++) {
    string += str1[i];
    string += str2[i];
  }
  return string;
}