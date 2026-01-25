function solution(s) {
  const number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9};
  let result = '';
  let temp = '';

  for (const c of s) {
    if (!isNaN(c)) result += c;
    else {
      temp += c;
      if (temp in number) {
        result += number[temp];
        temp = '';
      }
    }
  }

  return +result;
}