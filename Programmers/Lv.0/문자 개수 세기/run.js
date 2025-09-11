function solution(my_string) {
  let result = new Array(52).fill(0);

  for (let i = 0; i < my_string.length; i++) {
    let c = my_string.charCodeAt(i);
    if (c >= 65 && c <= 90) result[c - 65]++;
    else if (c >= 91 && c <= 122) result[c - 71]++; // c - 97 + 26
  }

  return result;
}