function solution(my_string, s, e) {
  const str = my_string.substring(s, e+1);
  return my_string.replace(str, str.split('').reverse().join(''));
}

// 반례) s부터 e까지의 부분 이전에 동일한 문자열이 있다면 거기가 바뀌는 문제 발생